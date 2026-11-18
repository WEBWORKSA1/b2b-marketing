#!/usr/bin/env python3
"""Auto-refresh: pulls RSS headlines + YouTube uploads into data/*.json, then rebuilds the site.
Runs in GitHub Actions (see .github/workflows/refresh.yml). Standard library only."""
import json, os, re, sys, html, datetime, subprocess, urllib.request
import xml.etree.ElementTree as ET
from email.utils import parsedate_to_datetime

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "content"))
from data import NEWS_SOURCES, YOUTUBE_HANDLES

UA = {"User-Agent": "Mozilla/5.0 (compatible; B2BMarketingBot/1.0; +https://b2b.marketing)"}
NS = {"atom": "http://www.w3.org/2005/Atom", "media": "http://search.yahoo.com/mrss/", "yt": "http://www.youtube.com/xml/schemas/2015"}

def get(url, timeout=20):
    req = urllib.request.Request(url, headers=UA)
    with urllib.request.urlopen(req, timeout=timeout) as r:
        return r.read()

def clean(t, n=220):
    t = html.unescape(re.sub(r"<[^>]+>", " ", t or ""))
    t = re.sub(r"\s+", " ", t).strip()
    return (t[: n - 1].rsplit(" ", 1)[0] + "…") if len(t) > n else t

def iso(d):
    if not d: return None
    try: return parsedate_to_datetime(d).astimezone(datetime.timezone.utc).isoformat()
    except Exception: pass
    try: return datetime.datetime.fromisoformat(d.replace("Z", "+00:00")).astimezone(datetime.timezone.utc).isoformat()
    except Exception: return None

def news():
    items = []
    for name, url in NEWS_SOURCES:
        try:
            root = ET.fromstring(get(url))
        except Exception as e:
            print("news fail", name, e); continue
        entries = root.findall(".//item") or root.findall(".//atom:entry", NS)
        for it in entries[:8]:
            title = it.findtext("title") or it.findtext("atom:title", namespaces=NS)
            link = it.findtext("link")
            if not link:
                l = it.find("atom:link", NS); link = l.get("href") if l is not None else None
            date = it.findtext("pubDate") or it.findtext("atom:published", namespaces=NS) or it.findtext("atom:updated", namespaces=NS)
            summ = it.findtext("description") or it.findtext("atom:summary", namespaces=NS) or ""
            if title and link and link.startswith("http"):
                items.append({"title": clean(title, 160), "link": link.strip(), "source": name, "date": iso(date), "summary": clean(summ, 200)})
        print("news ok", name)
    items.sort(key=lambda x: x["date"] or "", reverse=True)
    return items[:150]

def channel_id(handle):
    page = get(f"https://www.youtube.com/@{handle}").decode("utf-8", "ignore")
    m = re.search(r'"(?:channelId|externalId)":"(UC[\w-]{22})"', page) or re.search(r'channel/(UC[\w-]{22})', page)
    return m.group(1) if m else None

def videos():
    items = []
    for h in YOUTUBE_HANDLES:
        try:
            cid = channel_id(h)
            if not cid: print("yt no id", h); continue
            root = ET.fromstring(get(f"https://www.youtube.com/feeds/videos.xml?channel_id={cid}"))
            ch = root.findtext("atom:title", namespaces=NS) or h
            for e in root.findall("atom:entry", NS)[:5]:
                vid = e.findtext("yt:videoId", namespaces=NS)
                if vid and re.fullmatch(r"[\w-]{11}", vid):
                    items.append({"id": vid, "title": clean(e.findtext("atom:title", namespaces=NS), 140), "channel": ch, "date": iso(e.findtext("atom:published", namespaces=NS))})
            print("yt ok", h)
        except Exception as ex:
            print("yt fail", h, ex)
    items.sort(key=lambda x: x["date"] or "", reverse=True)
    return items[:60]

def save(fn, items):
    p = os.path.join(ROOT, "data", fn)
    if not items and os.path.exists(p):
        print("keeping previous", fn); return
    with open(p, "w") as f:
        json.dump({"updated": datetime.datetime.now(datetime.timezone.utc).isoformat(), "items": items}, f, indent=1)

if __name__ == "__main__":
    save("news.json", news())
    save("videos.json", videos())
    subprocess.run([sys.executable, os.path.join(ROOT, "scripts", "build.py")], check=True)
