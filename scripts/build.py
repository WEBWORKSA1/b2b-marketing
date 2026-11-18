#!/usr/bin/env python3
"""Static site generator for B2B.Marketing. Run: python3 scripts/build.py"""
import html, json, os, re, sys, datetime
ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "content"))
from guides import GUIDES
from tools import TOOLS
from data import GLOSSARY, STACK, TEMPLATES

SITE = "https://b2b.marketing"
NAME = "B2B.Marketing"
TODAY = datetime.date.today().isoformat()
YEAR = datetime.date.today().year
ADSENSE = '<script async src="https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=ca-pub-6620975821265271" crossorigin="anonymous"></script>'
PAGES = []  # (path, title, desc) for sitemap + search
BASE404 = """<script>document.write('<base href="'+(location.pathname.indexOf('/b2b-marketing/')===0?'/b2b-marketing/':'/')+'">')</script>"""
E = html.escape

def slugify(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")

def inline(t):
    t = E(t, quote=False)
    t = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", t)
    return t

def md(text):
    out, para, lst, ltype = [], [], [], None
    def flush():
        nonlocal para, lst, ltype
        if para:
            out.append("<p>" + inline(" ".join(para)) + "</p>"); para = []
        if lst:
            out.append(f"<{ltype}>" + "".join(f"<li>{inline(i)}</li>" for i in lst) + f"</{ltype}>"); lst = []; ltype = None
    toc = []
    for line in text.strip().split("\n"):
        s = line.strip()
        if not s:
            flush(); continue
        if s.startswith("### "):
            flush(); out.append(f"<h3>{inline(s[4:])}</h3>")
        elif s.startswith("## "):
            flush(); h = s[3:]; i = slugify(h); toc.append((i, h)); out.append(f'<h2 id="{i}">{inline(h)}</h2>')
        elif s.startswith("- "):
            if para: flush()
            if ltype not in (None, "ul"): flush()
            ltype = "ul"; lst.append(s[2:])
        elif re.match(r"^\d+\. ", s):
            if para: flush()
            if ltype not in (None, "ol"): flush()
            ltype = "ol"; lst.append(re.sub(r"^\d+\. ", "", s))
        else:
            if lst: flush()
            para.append(s)
    flush()
    return "\n".join(out), toc

NAV = [("Playbooks", "guides/"), ("Tools", "tools/"), ("Martech Stack", "stack/"), ("Templates", "templates/"), ("News", "news/"), ("Videos", "videos/"), ("Glossary", "glossary/")]

def page(path, title, desc, body, *, jsonld=None, extra_js="", crumbs=None, ptype="website", index=True, noads=False):
    depth = path.count("/") if path.endswith("/") else path.count("/")
    r = "../" * depth if path not in ("", "index.html") else ""
    if path.endswith(".html") and "/" not in path: r = ""
    url = SITE + "/" + (path if path != "index.html" else "")
    full_title = title if title.startswith(NAME) else f"{title} | {NAME}"
    ld = [{"@context": "https://schema.org", "@type": "Organization", "name": NAME, "url": SITE + "/", "logo": SITE + "/assets/img/logo.svg"}]
    if crumbs:
        items = [{"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"}]
        for i, (n, u) in enumerate(crumbs, 2):
            items.append({"@type": "ListItem", "position": i, "name": n, "item": SITE + "/" + u})
        ld.append({"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": items})
    if jsonld: ld += jsonld if isinstance(jsonld, list) else [jsonld]
    nav = "".join(f'<li><a href="{r}{u}"{" aria-current=page" if path.startswith(u) else ""}>{n}</a></li>' for n, u in NAV)
    crumb_html = ""
    if crumbs:
        crumb_html = '<nav class="crumbs container" aria-label="Breadcrumb"><a href="' + (r or "./") + '">Home</a>' + "".join(
            f' <span>›</span> <a href="{r}{u}">{E(n)}</a>' if k < len(crumbs) - 1 else f' <span>›</span> <span aria-current="page">{E(n)}</span>'
            for k, (n, u) in enumerate(crumbs)) + "</nav>"
    doc = f"""<!DOCTYPE html>
<html lang="en" data-theme="light">
<head>
<meta charset="utf-8">
{BASE404 if path == "404.html" else ""}
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{E(full_title)}</title>
<meta name="description" content="{E(desc)}">
<link rel="canonical" href="{url}">
<meta name="robots" content="{"index,follow" if index else "noindex,follow"}">
<meta property="og:type" content="{ptype}"><meta property="og:site_name" content="{NAME}">
<meta property="og:title" content="{E(full_title)}"><meta property="og:description" content="{E(desc)}">
<meta property="og:url" content="{url}"><meta property="og:image" content="{SITE}/assets/img/og.png">
<meta name="twitter:card" content="summary_large_image">
<meta name="theme-color" content="#0b5cff">
<link rel="icon" href="{r}assets/img/logo.svg" type="image/svg+xml">
<link rel="manifest" href="{r}manifest.webmanifest">
<link rel="preconnect" href="https://fonts.googleapis.com"><link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800&family=Space+Grotesk:wght@600;700&display=swap" rel="stylesheet">
<link rel="stylesheet" href="{r}assets/css/site.css">
{"" if noads else ADSENSE}
<script>try{{var t=localStorage.getItem('b2b-theme');if(t)document.documentElement.setAttribute('data-theme',t);else if(matchMedia('(prefers-color-scheme: dark)').matches)document.documentElement.setAttribute('data-theme','dark')}}catch(e){{}}</script>
<script type="application/ld+json">{json.dumps(ld if len(ld) > 1 else ld[0])}</script>
</head>
<body data-root="{r}">
<a class="skip" href="#main">Skip to content</a>
<div class="topbar"><div class="container"><a class="js-owner" href="{r}contact/" data-x="dGNhdG5vYy9za3Jvdy5iZXcvLzpzcHR0aA==" rel="noopener">contact, if you are interested in this website/domain name/Sponsorship/Advertisement/Partnership</a></div></div>
<header class="site-header"><div class="container nav-wrap">
<a class="logo" href="{r or './'}" aria-label="{NAME} home"><img src="{r}assets/img/logo.svg" alt="" width="34" height="34"><span>B2B<b>.Marketing</b></span></a>
<nav class="main-nav" id="main-nav" aria-label="Main"><ul>{nav}</ul></nav>
<div class="nav-actions">
<button class="icon-btn js-search-open" aria-label="Search">⌕</button>
<button class="icon-btn js-theme" aria-label="Toggle dark mode">◐</button>
<a class="btn btn-sm btn-primary hide-sm" href="{r}growth-audit/">Free Growth Audit</a>
<button class="icon-btn burger js-burger" aria-label="Menu" aria-expanded="false" aria-controls="main-nav">☰</button>
</div></div></header>
{crumb_html}
<main id="main">
{body}
</main>
<footer class="site-footer"><div class="container">
<div class="foot-grid">
<div><a class="logo" href="{r or './'}"><img src="{r}assets/img/logo.svg" alt="" width="30" height="30"><span>B2B<b>.Marketing</b></span></a>
<p class="muted">Free playbooks, calculators, templates and expert matching for B2B marketers, founders and revenue teams.</p>
<form class="js-form news-form" data-form="Newsletter signup" novalidate>
<label for="nl-{slugify(path) or 'home'}" class="sr-only">Work email</label>
<input id="nl-{slugify(path) or 'home'}" type="email" name="email" placeholder="Work email" required>
<input type="text" name="_gotcha" class="hp" tabindex="-1" autocomplete="off">
<button class="btn btn-primary" type="submit">Subscribe</button>
<p class="form-msg" role="status"></p></form></div>
<div><h4>Learn</h4><ul><li><a href="{r}guides/">Playbooks</a></li><li><a href="{r}tools/">Free tools</a></li><li><a href="{r}templates/">Templates</a></li><li><a href="{r}glossary/">Glossary</a></li><li><a href="{r}news/">News</a></li><li><a href="{r}videos/">Videos</a></li></ul></div>
<div><h4>Grow</h4><ul><li><a href="{r}growth-audit/">Free growth audit</a></li><li><a href="{r}agencies/">Find an agency</a></li><li><a href="{r}stack/">Martech stack</a></li><li><a href="{r}jobs/">Jobs &amp; talent</a></li><li><a href="{r}contests/">Contests &amp; prizes</a></li></ul></div>
<div><h4>Company</h4><ul><li><a href="{r}about/">About</a></li><li><a href="{r}advertise/">Advertise &amp; sponsor</a></li><li><a href="{r}support/">Support us</a></li><li><a href="{r}contact/">Contact</a></li><li><a href="{r}privacy/">Privacy</a></li><li><a href="{r}terms/">Terms</a></li><li><a href="{r}disclaimer/">Disclaimer &amp; trademarks</a></li><li><a href="{r}cookies/">Cookies</a></li></ul></div>
</div>
<div class="foot-legal"><p>© {YEAR} {NAME}. All rights reserved. Original content on this site is protected by copyright. {NAME} is an independent publication and is not affiliated with, endorsed by or connected to any company, publication or trademark using the words "B2B Marketing". Third-party names and logos belong to their respective owners. <a href="{r}disclaimer/">Read the full disclaimer</a>.</p></div>
</div></footer>
<div class="cookie js-cookie" hidden role="dialog" aria-label="Cookie consent"><p>We use cookies for analytics and to show ads from Google and its partners. <a href="{r}cookies/">Learn more</a>.</p><div><button class="btn btn-sm btn-ghost js-cookie-no">Essential only</button><button class="btn btn-sm btn-primary js-cookie-yes">Accept</button></div></div>
<div class="search-modal js-search" hidden role="dialog" aria-modal="true" aria-label="Search"><div class="search-box"><input type="search" class="js-search-input" placeholder="Search playbooks, tools, terms…" aria-label="Search"><button class="icon-btn js-search-close" aria-label="Close search">✕</button><ul class="js-search-results"></ul></div></div>
<script src="{r}assets/js/site.js" defer></script>
{extra_js.replace("{r}", r)}
</body></html>"""
    out = os.path.join(ROOT, path if path.endswith(".html") else os.path.join(path, "index.html"))
    os.makedirs(os.path.dirname(out), exist_ok=True)
    with open(out, "w", encoding="utf-8") as f:
        f.write(doc)
    if index:
        PAGES.append((path if path != "index.html" else "", title, desc))

def hero(kicker, h1, sub, ctas=""):
    return f'<section class="page-hero"><div class="container"><p class="kicker">{kicker}</p><h1>{h1}</h1><p class="lead">{sub}</p>{ctas}</div></section>'

def faq_html(faqs):
    items = "".join(f"<details><summary>{E(q)}</summary><p>{E(a)}</p></details>" for q, a in faqs)
    return f'<section class="faq"><h2 id="faq">Frequently asked questions</h2>{items}</section>'

def faq_ld(faqs):
    return {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [{"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]}

CTA_BOX = lambda r: f'''<aside class="cta-box"><div><h3>Want an expert to look at your numbers?</h3><p>Get a free, no-obligation B2B growth audit and a shortlist of vetted specialists matched to your goals and budget.</p></div><a class="btn btn-primary" href="{r}growth-audit/">Get my free audit →</a></aside>'''

def opt(v, l, d): return f'<option value="{v}"{" selected" if v == d else ""}>{E(l)}</option>'

# ---------- HOME ----------
def build_home():
    tools = "".join(f'<a class="card tool-card" href="tools/{t["slug"]}/"><span class="ico">{t["icon"]}</span><h3>{E(t["title"])}</h3><p>{E(t["desc"])}</p></a>' for t in TOOLS[:6])
    guides = "".join(f'<a class="card" href="guides/{g["slug"]}/"><span class="tag">{g["cat"]}</span><h3>{E(g["title"])}</h3><p>{E(g["desc"])}</p><span class="meta">{g["mins"]} min read</span></a>' for g in GUIDES[:6])
    body = f'''
<section class="hero"><div class="container hero-grid">
<div><p class="kicker">The free B2B growth toolkit</p>
<h1>Plan, launch and measure <span class="grad">B2B marketing</span> that fills the pipeline.</h1>
<p class="lead">Practical playbooks, free calculators, copy-ready templates, a live news feed and a matching service that connects you with vetted B2B specialists, all free to use.</p>
<div class="hero-ctas"><a class="btn btn-primary btn-lg" href="growth-audit/">Get a free growth audit</a><a class="btn btn-ghost btn-lg" href="tools/">Explore free tools</a></div>
<ul class="trust"><li>✓ {len(GUIDES)} in-depth playbooks</li><li>✓ {len(TOOLS)} free calculators</li><li>✓ {len(GLOSSARY)}+ terms explained</li><li>✓ Updated every 6 hours</li></ul></div>
<div class="hero-card" aria-hidden="true"><div class="hc-row"><span>Pipeline target</span><b>$1,000,000</b></div><div class="hc-bars"><i style="--h:92%"></i><i style="--h:70%"></i><i style="--h:48%"></i><i style="--h:30%"></i><i style="--h:16%"></i></div><div class="hc-labels"><span>Leads</span><span>MQL</span><span>SQL</span><span>Opp</span><span>Won</span></div><div class="hc-row small"><span>LTV:CAC</span><b class="ok">3.4 : 1</b></div><div class="hc-row small"><span>CAC payback</span><b>10.2 mo</b></div></div>
</div></section>
<section class="section"><div class="container"><div class="sec-head"><h2>Free B2B marketing calculators</h2><a href="tools/">All tools →</a></div><div class="grid g3">{tools}</div></div></section>
<section class="section alt"><div class="container"><div class="sec-head"><h2>Playbooks that turn strategy into pipeline</h2><a href="guides/">All playbooks →</a></div><div class="grid g3">{guides}</div></div></section>
<section class="section"><div class="container lead-split">
<div><p class="kicker">Lead generation, done for you</p><h2>Get matched with vetted B2B growth specialists</h2><p>Tell us about your company, goals and budget in two minutes. You will receive a readiness score instantly, and our team will reply with a free audit summary and up to three vetted agencies or consultants who fit your needs. No cost and no obligation.</p>
<ul class="checks"><li>Demand gen, ABM, SEO, paid media and RevOps specialists</li><li>Pre-screened for B2B experience and results</li><li>Your details are shared only with partners you approve</li></ul>
<a class="btn btn-primary btn-lg" href="growth-audit/">Start my free audit →</a></div>
<div class="stat-grid"><div><b>2 min</b><span>to complete</span></div><div><b>Free</b><span>no obligation</span></div><div><b>3</b><span>matched experts</span></div><div><b>1 day</b><span>typical reply</span></div></div>
</div></section>
<section class="section alt"><div class="container"><div class="sec-head"><h2>Latest B2B marketing news</h2><a href="news/">All news →</a></div><div class="grid g3 js-news" data-limit="6"><div class="skeleton"></div><div class="skeleton"></div><div class="skeleton"></div></div></div></section>
<section class="section"><div class="container"><div class="sec-head"><h2>Watch &amp; learn</h2><a href="videos/">All videos →</a></div><div class="grid g3 js-videos" data-limit="3"><div class="skeleton"></div><div class="skeleton"></div><div class="skeleton"></div></div></div></section>
<section class="section alt"><div class="container grid g4 promo">
<a class="card" href="contests/"><span class="ico">🏆</span><h3>Contests &amp; prizes</h3><p>Enter the B2B Campaign of the Year and monthly challenges.</p></a>
<a class="card" href="jobs/"><span class="ico">💼</span><h3>Jobs &amp; talent</h3><p>Hire B2B marketers or join the talent network.</p></a>
<a class="card" href="advertise/"><span class="ico">📣</span><h3>Advertise &amp; sponsor</h3><p>Reach B2B decision-makers with sponsorships and featured listings.</p></a>
<a class="card" href="support/"><span class="ico">❤</span><h3>Support us</h3><p>Help keep the tools, playbooks and prizes free for everyone.</p></a>
</div></section>'''
    ld = {"@context": "https://schema.org", "@type": "WebSite", "name": NAME, "url": SITE + "/", "potentialAction": {"@type": "SearchAction", "target": SITE + "/search/?q={q}", "query-input": "required name=q"}}
    page("index.html", f"{NAME} — Free B2B Marketing Playbooks, Tools & Expert Matching", "Free B2B marketing playbooks, calculators, templates, live news and a free growth audit that matches you with vetted B2B specialists.", body, jsonld=ld, extra_js='<script src="{r}assets/js/feeds.js" defer></script>')

# ---------- GUIDES ----------
def build_guides():
    cards = "".join(f'<a class="card" href="{g["slug"]}/"><span class="tag">{g["cat"]}</span><h3>{E(g["title"])}</h3><p>{E(g["desc"])}</p><span class="meta">{g["mins"]} min read</span></a>' for g in GUIDES)
    cats = sorted({g["cat"] for g in GUIDES})
    pills = '<div class="pills js-filter" data-target=".js-cards">' + '<button class="pill active" data-f="all">All</button>' + "".join(f'<button class="pill" data-f="{c}">{c}</button>' for c in cats) + "</div>"
    cards = "".join(f'<a class="card" data-cat="{g["cat"]}" href="{g["slug"]}/"><span class="tag">{g["cat"]}</span><h3>{E(g["title"])}</h3><p>{E(g["desc"])}</p><span class="meta">{g["mins"]} min read</span></a>' for g in GUIDES)
    body = hero("Playbooks", "B2B marketing playbooks", "In-depth, practical guides on strategy, channels, operations and analytics, written for marketers who need results this quarter.") + f'<section class="section"><div class="container">{pills}<div class="grid g3 js-cards">{cards}</div></div></section>'
    page("guides/", "B2B Marketing Playbooks & Guides", "In-depth B2B marketing playbooks: ABM, demand generation, lead scoring, SEO and AI search, LinkedIn, email, attribution and more.", body, crumbs=[("Playbooks", "guides/")])
    for i, g in enumerate(GUIDES):
        content, toc = md(g["body"])
        r = "../../"
        tk = "".join(f"<li>{E(t)}</li>" for t in g["takeaways"])
        toc_html = "".join(f'<li><a href="#{a}">{E(h)}</a></li>' for a, h in toc) + '<li><a href="#faq">FAQ</a></li>'
        related = [x for x in GUIDES if x["slug"] != g["slug"]][:3] if i > 2 else [x for x in GUIDES if x["slug"] != g["slug"]][3:6]
        rel = "".join(f'<a class="card" href="{r}guides/{x["slug"]}/"><span class="tag">{x["cat"]}</span><h3>{E(x["title"])}</h3></a>' for x in related)
        body = f'''<article class="container article">
<header class="art-head"><span class="tag">{g["cat"]}</span><h1>{E(g["title"])}</h1><p class="lead">{E(g["desc"])}</p><p class="meta">By the {NAME} editorial team · Updated {TODAY} · {g["mins"]} min read</p></header>
<div class="art-grid"><div class="art-body">
<div class="takeaways"><h2 class="h4">Key takeaways</h2><ul>{tk}</ul></div>
{content}
{CTA_BOX(r)}
{faq_html(g["faq"])}
<div class="share"><span>Share:</span><a class="js-share" data-net="linkedin" href="#">LinkedIn</a><a class="js-share" data-net="x" href="#">X</a><a class="js-share" data-net="copy" href="#">Copy link</a></div>
</div>
<aside class="art-side"><div class="sticky"><h2 class="h5">On this page</h2><ol class="toc">{toc_html}</ol><a class="btn btn-primary btn-block" href="{r}growth-audit/">Free growth audit</a><a class="btn btn-ghost btn-block" href="{r}tools/">Free calculators</a></div></aside>
</div>
<section class="related"><h2>Related playbooks</h2><div class="grid g3">{rel}</div></section>
</article>'''
        ld = [{"@context": "https://schema.org", "@type": "Article", "headline": g["title"], "description": g["desc"], "datePublished": "2026-11-18", "dateModified": TODAY, "author": {"@type": "Organization", "name": NAME + " editorial team"}, "publisher": {"@type": "Organization", "name": NAME}, "mainEntityOfPage": f"{SITE}/guides/{g['slug']}/"}, faq_ld(g["faq"])]
        page(f"guides/{g['slug']}/", g["title"], g["desc"], body, jsonld=ld, crumbs=[("Playbooks", "guides/"), (g["title"], f"guides/{g['slug']}/")], ptype="article")

# ---------- TOOLS ----------
def field(t, i):
    fid, label, typ, default, extra = i
    if typ == "select":
        return f'<label>{E(label)}<select name="{fid}" id="{fid}">{"".join(opt(v, l, default) for v, l in extra)}</select></label>'
    if typ == "textarea":
        return f'<label>{E(label)}<textarea name="{fid}" id="{fid}" rows="3">{E(str(default))}</textarea></label>'
    step = ' step="any" min="0"' if typ == "number" else ""
    return f'<label>{E(label)}<input type="{typ}" name="{fid}" id="{fid}" value="{E(str(default))}"{step}></label>'

def build_tools():
    cards = "".join(f'<a class="card tool-card" href="{t["slug"]}/"><span class="ico">{t["icon"]}</span><h3>{E(t["title"])}</h3><p>{E(t["desc"])}</p></a>' for t in TOOLS)
    body = hero("Free tools", "Free B2B marketing calculators", "Run the numbers behind your pipeline, budget and campaigns. Everything runs in your browser and nothing you type is stored.") + f'<section class="section"><div class="container grid g3">{cards}</div></section>'
    page("tools/", "Free B2B Marketing Calculators & Tools", "Free B2B marketing calculators: CAC payback, LTV:CAC, ROI, pipeline planner, lead scoring, budget allocator, UTM builder and more.", body, crumbs=[("Tools", "tools/")])
    for t in TOOLS:
        r = "../../"
        about, _ = md(t["about"])
        fields = "".join(field(t, i) for i in t["inputs"])
        others = "".join(f'<li><a href="{r}tools/{x["slug"]}/">{x["icon"]} {E(x["title"])}</a></li>' for x in TOOLS if x["slug"] != t["slug"])
        body = f'''<section class="container tool-page">
<header class="art-head"><span class="tag">Free tool</span><h1>{t["icon"]} {E(t["title"])}</h1><p class="lead">{E(t["desc"])}</p></header>
<div class="tool-grid"><form class="calc js-calc" data-tool="{t["slug"]}" onsubmit="return false">{fields}<button class="btn btn-primary" type="submit">Calculate</button></form>
<div class="calc-out js-out" aria-live="polite"><p class="muted">Results appear here.</p></div></div>
<div class="art-grid"><div class="art-body">{about}{CTA_BOX(r)}</div><aside class="art-side"><div class="sticky"><h2 class="h5">More free tools</h2><ul class="toc">{others}</ul></div></aside></div>
</section>'''
        ld = {"@context": "https://schema.org", "@type": "WebApplication", "name": t["title"], "applicationCategory": "BusinessApplication", "operatingSystem": "Any", "offers": {"@type": "Offer", "price": "0", "priceCurrency": "USD"}, "description": t["desc"]}
        page(f"tools/{t['slug']}/", t["title"], t["desc"], body, jsonld=ld, crumbs=[("Tools", "tools/"), (t["title"], f"tools/{t['slug']}/")], extra_js='<script src="{r}assets/js/tools.js" defer></script>')

# ---------- GLOSSARY ----------
def build_glossary():
    letters = sorted({g[0][0].upper() for g in GLOSSARY})
    az = '<nav class="az">' + "".join(f'<a href="#l-{l}">{l}</a>' for l in letters) + "</nav>"
    items, cur = [], None
    for term, d in sorted(GLOSSARY, key=lambda x: x[0].lower()):
        L = term[0].upper()
        if L != cur:
            items.append(f'<h2 id="l-{L}" class="letter">{L}</h2>'); cur = L
        items.append(f'<div class="term" id="{slugify(term)}"><h3>{E(term)}</h3><p>{E(d)}</p></div>')
    body = hero("Glossary", "B2B marketing glossary", f"{len(GLOSSARY)} essential B2B marketing, sales and revenue terms explained in plain English.") + f'<section class="section"><div class="container narrow"><input class="input js-term-filter" type="search" placeholder="Filter terms…" aria-label="Filter terms">{az}{"".join(items)}</div></section>'
    ld = {"@context": "https://schema.org", "@type": "DefinedTermSet", "name": "B2B marketing glossary", "hasDefinedTerm": [{"@type": "DefinedTerm", "name": t, "description": d} for t, d in GLOSSARY]}
    page("glossary/", "B2B Marketing Glossary: 65+ Terms Explained", "Plain-English definitions of B2B marketing terms: ABM, CAC, LTV, MQL, SQL, intent data, attribution, RevOps and more.", body, jsonld=ld, crumbs=[("Glossary", "glossary/")])

# ---------- STACK ----------
def build_stack():
    cats = sorted({s[1] for s in STACK})
    pills = '<div class="pills js-filter" data-target=".js-cards">' + '<button class="pill active" data-f="all">All</button>' + "".join(f'<button class="pill" data-f="{c}">{c}</button>' for c in cats) + "</div>"
    cards = "".join(f'<div class="card stack-card" data-cat="{c}"><span class="tag">{c}</span><h3>{E(n)}</h3><p>{E(d)}</p><a href="{u}" target="_blank" rel="noopener nofollow">Visit site ↗</a></div>' for n, c, u, d in STACK)
    body = hero("Martech stack", "B2B martech stack directory", f"{len(STACK)} tools B2B teams use across CRM, automation, ABM, data, SEO, analytics, ads and AI, organised by job to be done.", '<a class="btn btn-primary" href="../advertise/#listing">Feature your tool</a>') + f'<section class="section"><div class="container"><input class="input js-card-search" type="search" placeholder="Search tools…" aria-label="Search tools">{pills}<div class="grid g3 js-cards">{cards}</div><p class="muted small">Listings are editorial summaries and not endorsements. Product names are trademarks of their owners. Some links may become affiliate links in future; we will label them clearly.</p></div></section>'
    page("stack/", "B2B Martech Stack Directory", "Directory of B2B marketing technology: CRM, marketing automation, ABM and intent data, prospecting, SEO, analytics, advertising and AI tools.", body, crumbs=[("Martech Stack", "stack/")])

# ---------- TEMPLATES ----------
def build_templates():
    blocks = "".join(f'<div class="tpl" id="{s}"><div class="tpl-head"><h2 class="h4">{E(t)}</h2><button class="btn btn-sm btn-ghost js-copy" data-copy="#tpl-{s}">Copy</button></div><pre id="tpl-{s}">{E(c)}</pre></div>' for s, t, c in TEMPLATES)
    toc = "".join(f'<li><a href="#{s}">{E(t)}</a></li>' for s, t, _ in TEMPLATES)
    body = hero("Templates", "Copy-ready B2B marketing templates", "ICP worksheets, campaign briefs, cold emails, nurture sequences, SLAs and more. Copy, paste and adapt.") + f'<section class="section"><div class="container art-grid"><div class="art-body">{blocks}{CTA_BOX("../")}</div><aside class="art-side"><div class="sticky"><h2 class="h5">Templates</h2><ol class="toc">{toc}</ol></div></aside></div></section>'
    page("templates/", "Free B2B Marketing Templates", "Free copy-ready B2B marketing templates: ICP worksheet, campaign brief, cold email, nurture sequence, marketing-sales SLA, UTM conventions and more.", body, crumbs=[("Templates", "templates/")])

# ---------- FEEDS ----------
def build_feeds():
    body = hero("Auto-updated every 6 hours", "B2B marketing news", "Headlines from leading marketing, martech and search publications, gathered automatically. Click through to read each story at its source.") + '<section class="section"><div class="container"><input class="input js-news-search" type="search" placeholder="Filter headlines…" aria-label="Filter headlines"><div class="pills js-news-sources"></div><p class="muted small js-updated"></p><div class="grid g3 js-news" data-limit="120"><div class="skeleton"></div><div class="skeleton"></div><div class="skeleton"></div></div><p class="muted small">Headlines and short excerpts link to the original publishers, who own the content.</p></div></section>'
    page("news/", "B2B Marketing News (Updated Daily)", "Latest B2B marketing, martech, SEO and demand generation headlines from leading publications, updated automatically.", body, crumbs=[("News", "news/")], extra_js='<script src="{r}assets/js/feeds.js" defer></script>')
    body = hero("Auto-updated", "B2B marketing videos", "Fresh tutorials and talks from leading B2B marketing, SEO and sales channels on YouTube.") + '<section class="section"><div class="container"><p class="muted small js-updated"></p><div class="grid g3 js-videos" data-limit="60"><div class="skeleton"></div><div class="skeleton"></div><div class="skeleton"></div></div><p class="muted small">Videos are embedded from YouTube and belong to their creators.</p></div></section>'
    page("videos/", "B2B Marketing Videos & Tutorials", "Watch the latest B2B marketing, SEO, demand generation and sales videos from leading channels, updated automatically.", body, crumbs=[("Videos", "videos/")], extra_js='<script src="{r}assets/js/feeds.js" defer></script>')

# ---------- LEAD GEN ----------
def build_audit():
    sizes = [("1-10", "1–10"), ("11-50", "11–50"), ("51-200", "51–200"), ("201-1000", "201–1,000"), ("1000+", "1,000+")]
    goals = ["More qualified leads", "Account-based marketing", "SEO & AI search visibility", "Paid media (LinkedIn/Google)", "Marketing automation & CRM", "Content & thought leadership", "RevOps & attribution", "Website conversion"]
    goal_html = "".join(f'<label class="chk"><input type="checkbox" name="goals" value="{g}"> {g}</label>' for g in goals)
    body = f'''<section class="page-hero"><div class="container"><p class="kicker">Free · 2 minutes · No obligation</p><h1>Get your free B2B growth audit</h1><p class="lead">Answer a few questions to receive an instant growth-readiness score, a free audit summary from our team and up to three vetted specialists matched to your goals.</p></div></section>
<section class="section"><div class="container audit-grid">
<form class="js-form js-wizard card wizard" data-form="Growth audit lead" novalidate>
<div class="progress" aria-hidden="true"><i class="js-prog"></i></div><p class="muted small js-stepnum">Step 1 of 4</p>
<fieldset class="step active"><legend>About your company</legend>
<label>Company name<input name="company" required autocomplete="organization"></label>
<label>Website<input name="website" type="url" placeholder="https://" required></label>
<label>Company size<select name="size" required><option value="">Select…</option>{"".join(f'<option value="{v}">{l}</option>' for v, l in sizes)}</select></label>
<label>Industry<input name="industry" placeholder="e.g. SaaS, manufacturing, logistics" required></label></fieldset>
<fieldset class="step"><legend>Your numbers</legend>
<label>Average deal size / ACV<select name="acv" required><option value="">Select…</option><option>Under $5k</option><option>$5k–$25k</option><option>$25k–$100k</option><option>$100k+</option></select></label>
<label>Monthly marketing budget<select name="budget" required><option value="">Select…</option><option>Under $5k</option><option>$5k–$20k</option><option>$20k–$75k</option><option>$75k+</option></select></label>
<label>Do you track pipeline by source in a CRM?<select name="crm" required><option value="">Select…</option><option value="yes">Yes, reliably</option><option value="partly">Partly</option><option value="no">No</option></select></label>
<label>Timeline<select name="timeline" required><option value="">Select…</option><option>Ready now</option><option>Within 3 months</option><option>Researching</option></select></label></fieldset>
<fieldset class="step"><legend>What do you need help with?</legend><div class="chk-grid">{goal_html}</div>
<label>Biggest challenge right now<textarea name="challenge" rows="3" placeholder="e.g. lots of leads but few become opportunities"></textarea></label></fieldset>
<fieldset class="step"><legend>Where should we send your audit?</legend>
<label>Full name<input name="name" required autocomplete="name"></label>
<label>Work email<input name="email" type="email" required autocomplete="email"></label>
<label>Job title<input name="title" required autocomplete="organization-title"></label>
<label>Phone (optional)<input name="phone" type="tel" autocomplete="tel"></label>
<label class="chk"><input type="checkbox" name="consent" value="yes" required> I agree to be contacted about my audit and to share my details with up to three matched partners I approve. See our <a href="../privacy/">privacy policy</a>.</label></fieldset>
<input type="text" name="_gotcha" class="hp" tabindex="-1" autocomplete="off">
<div class="wiz-nav"><button type="button" class="btn btn-ghost js-prev" hidden>← Back</button><button type="button" class="btn btn-primary js-next">Next →</button><button type="submit" class="btn btn-primary js-submit" hidden>Get my free audit</button></div>
<p class="form-msg" role="status"></p>
<div class="score js-score" hidden></div>
</form>
<aside><div class="card"><h2 class="h4">What you get</h2><ul class="checks"><li>Instant growth-readiness score</li><li>Free audit summary of your funnel, channels and quick wins</li><li>Up to 3 vetted specialists matched to budget and goals</li><li>Zero cost and no obligation to hire</li></ul></div>
<div class="card"><h2 class="h4">Are you an agency or consultant?</h2><p>Join our partner network to receive qualified B2B leads.</p><a class="btn btn-ghost" href="../agencies/#join">Apply as a partner</a></div></aside>
</div></section>'''
    page("growth-audit/", "Free B2B Growth Audit & Expert Matching", "Get a free B2B marketing growth audit, an instant readiness score and up to three vetted specialists matched to your goals and budget.", body, crumbs=[("Free growth audit", "growth-audit/")])

def simple_form(name, fields, button, note=""):
    f = ""
    for fd in fields:
        lab, nm, typ = fd[0], fd[1], fd[2]
        req = " required" if (len(fd) < 4 or fd[3]) else ""
        if typ == "textarea": f += f'<label>{lab}<textarea name="{nm}" rows="4"{req}></textarea></label>'
        elif typ.startswith("select:"): f += f'<label>{lab}<select name="{nm}"{req}><option value="">Select…</option>' + "".join(f"<option>{o}</option>" for o in typ[7:].split("|")) + "</select></label>"
        else: f += f'<label>{lab}<input name="{nm}" type="{typ}"{req}></label>'
    return f'<form class="js-form card form" data-form="{name}" novalidate>{f}<input type="text" name="_gotcha" class="hp" tabindex="-1" autocomplete="off"><label class="chk"><input type="checkbox" name="consent" value="yes" required> I agree to the <a href="../privacy/">privacy policy</a>.</label><button class="btn btn-primary" type="submit">{button}</button><p class="form-msg" role="status"></p>{note}</form>'

def build_community():
    # Agencies
    specs = ["Demand generation", "Account-based marketing", "B2B SEO & content", "LinkedIn & paid media", "Marketing automation / HubSpot", "Salesforce & RevOps", "Website & CRO", "Events & webinars", "Brand & positioning"]
    sp = "".join(f'<div class="card"><h3>{s}</h3><p>Vetted specialists available. Tell us your goals and we will match you.</p><a href="../growth-audit/">Get matched →</a></div>' for s in specs)
    body = hero("Agency directory", "Find a vetted B2B marketing agency", "Skip the guesswork. Describe your goals once and we introduce up to three pre-screened agencies or consultants with relevant B2B experience.", '<a class="btn btn-primary" href="../growth-audit/">Get matched free</a>') + f'''<section class="section"><div class="container"><h2>Browse by specialty</h2><div class="grid g3">{sp}</div></div></section>
<section class="section alt" id="join"><div class="container split"><div><h2>List your agency</h2><p>Receive qualified, consent-based B2B leads that match your specialty, deal size and region. Standard and featured listings are available, and every partner is reviewed before approval.</p><ul class="checks"><li>Consent-based leads only</li><li>Specialty and budget matching</li><li>Featured placement options</li></ul></div>
{simple_form("Agency listing application", [("Agency name","agency","text"),("Website","website","url"),("Contact name","name","text"),("Work email","email","email"),("Specialties","specialties","text"),("Typical client budget","budget","select:Under $5k/mo|$5k–$20k/mo|$20k+/mo"),("Regions served","regions","text"),("Tell us about your best B2B result","about","textarea")], "Apply to list")}</div></section>'''
    page("agencies/", "Find a B2B Marketing Agency (Free Matching)", "Find vetted B2B marketing agencies and consultants for demand gen, ABM, SEO, paid media and RevOps, or list your agency to receive qualified leads.", body, crumbs=[("Agencies", "agencies/")])
    # Jobs
    body = hero("Jobs & talent", "B2B marketing jobs & talent network", "Hire experienced B2B marketers, join our talent network, or write for B2B.Marketing.") + f'''<section class="section"><div class="container grid g3">
<div class="card"><h2 class="h4">Hiring?</h2><p>Post a B2B marketing role and we will share it with our talent network and newsletter audience.</p><a class="btn btn-primary" href="#post">Post a job</a></div>
<div class="card"><h2 class="h4">Looking for work?</h2><p>Join the talent network to hear about roles and freelance projects that match your skills.</p><a class="btn btn-ghost" href="#talent">Join the network</a></div>
<div class="card"><h2 class="h4">We're hiring contributors</h2><p>We pay for original, expert B2B playbooks, research and tool ideas. Editors, writers and video creators are welcome to apply.</p><a class="btn btn-ghost" href="#write">Apply to contribute</a></div></div></section>
<section class="section alt" id="post"><div class="container split"><div><h2>Post a job</h2><p>Reach marketers who read playbooks on ABM, demand gen, RevOps and SEO. Standard and featured posts are available, and we will confirm details and pricing by reply.</p></div>{simple_form("Job post request", [("Company","company","text"),("Role title","role","text"),("Location / remote","location","text"),("Salary range","salary","text",False),("Job link","link","url"),("Your name","name","text"),("Work email","email","email"),("Description","description","textarea")], "Submit job")}</div></section>
<section class="section" id="talent"><div class="container split"><div><h2>Join the talent network</h2><p>Tell us your specialty and availability. We only share your profile with employers you approve.</p></div>{simple_form("Talent network signup", [("Full name","name","text"),("Email","email","email"),("Specialty","specialty","select:Demand gen|ABM|Content & SEO|Paid media|Marketing ops / RevOps|Product marketing|Brand|Other"),("Experience (years)","years","number"),("LinkedIn / portfolio URL","profile","url"),("Availability","availability","select:Full-time|Freelance|Both")], "Join network")}</div></section>
<section class="section alt" id="write"><div class="container split"><div><h2>Write for B2B.Marketing</h2><p>Pitch an original playbook, data study or teardown. We do not accept promotional posts or paid links.</p></div>{simple_form("Contributor application", [("Full name","name","text"),("Email","email","email"),("Writing samples (URLs)","samples","text"),("Your pitch","pitch","textarea")], "Send pitch")}</div></section>'''
    page("jobs/", "B2B Marketing Jobs, Talent Network & Contributors", "Post B2B marketing jobs, join the B2B marketing talent network, or apply to write for B2B.Marketing.", body, crumbs=[("Jobs & talent", "jobs/")])
    # Contests
    body = hero("Contests & prizes", "B2B Campaign of the Year &amp; monthly challenges", "Showcase your best work, learn from peers and win prizes. Entry is free.", '<a class="btn btn-primary" href="#enter">Enter now</a>') + f'''<section class="section"><div class="container grid g3">
<div class="card"><span class="ico">🏆</span><h2 class="h4">B2B Campaign of the Year</h2><p>Annual award across ABM, demand gen, content, events and brand. Winners are featured on the homepage and newsletter and receive a winner's badge and prize package.</p></div>
<div class="card"><span class="ico">⚡</span><h2 class="h4">Monthly challenge</h2><p>A new brief each month, such as "Rewrite this landing page" or "Design a 5-email nurture". The best entry wins a featured spotlight and a prize.</p></div>
<div class="card"><span class="ico">🎓</span><h2 class="h4">Student &amp; newcomer track</h2><p>For people starting a B2B marketing career. Winners get mentorship sessions with experienced marketers and a public portfolio feature.</p></div></div></section>
<section class="section alt"><div class="container narrow"><h2>How judging works</h2><ol><li>Entries are scored on strategy (30%), creativity (25%), measurable results (30%) and clarity (15%).</li><li>A panel of practitioners reviews shortlisted entries; sponsors never judge.</li><li>Winners are announced on this page and in our newsletter.</li></ol>
<h2>Rules</h2><ul><li>Free to enter; no purchase necessary. Void where prohibited.</li><li>You must own or have permission to submit the work. Remove confidential client data.</li><li>By entering you allow us to feature your entry summary with credit.</li><li>Prizes are non-transferable; sponsors may provide prizes and will be disclosed.</li><li>We may update dates and prizes; changes will be posted here.</li></ul>
<p>Want to sponsor a prize? <a href="../advertise/">See sponsorship options</a>.</p></div></section>
<section class="section" id="enter"><div class="container split"><div><h2>Submit your entry</h2><p>Share a link to your case study, deck or video and a short summary of the results.</p></div>{simple_form("Contest entry", [("Full name","name","text"),("Email","email","email"),("Company","company","text"),("Category","category","select:Campaign of the Year — ABM|Campaign of the Year — Demand gen|Campaign of the Year — Content|Campaign of the Year — Events|Monthly challenge|Student & newcomer"),("Entry link","link","url"),("Results summary","summary","textarea")], "Submit entry")}</div></section>'''
    page("contests/", "B2B Marketing Contests, Awards & Prizes", "Enter the B2B Campaign of the Year, monthly B2B marketing challenges and the newcomer track. Free to enter with prizes and features.", body, crumbs=[("Contests", "contests/")])
    # Support
    tiers = [("☕", "Coffee", "$5", "Keeps a calculator running for a month."), ("🚀", "Supporter", "$25", "Funds a new template or playbook update."), ("🏅", "Champion", "$100", "Helps fund contest prizes and promotions."), ("💎", "Patron", "$500+", "Funds a new tool and earns a thank-you listing.")]
    tc = "".join(f'<div class="card tier"><span class="ico">{i}</span><h3>{n}</h3><b class="price">{p}</b><p>{d}</p><button class="btn btn-ghost js-tier" data-tier="{n} ({p})">Choose {n}</button></div>' for i, n, p, d in tiers)
    body = hero("Support B2B.Marketing", "Keep B2B marketing knowledge free", "Your support pays for operations, promotions and marketing, hiring writers and developers, and contest prizes. Every contribution keeps the tools free for everyone.") + f'''<section class="section"><div class="container grid g4">{tc}</div></section>
<section class="section alt"><div class="container split"><div><h2>Where your support goes</h2><ul class="checks"><li><b>Operations:</b> hosting, data refresh, tooling</li><li><b>Promotions &amp; marketing:</b> reaching more B2B professionals</li><li><b>Hiring talent:</b> paying expert writers, editors and developers</li><li><b>Contests &amp; prizes:</b> rewarding the community's best work</li></ul><p class="muted small">Contributions are voluntary support for an independent publication and are not tax-deductible charitable donations. After you submit a pledge we reply with secure payment options such as card or PayPal.</p><div class="js-paylink"></div></div>
{simple_form("Support pledge", [("Your name","name","text"),("Email","email","email"),("Tier / amount","tier","text"),("Frequency","frequency","select:One-time|Monthly|Yearly"),("Use my support for","use","select:Wherever it's needed most|Operations|Promotions & marketing|Hiring talent|Contests & prizes"),("Message (optional)","message","textarea",False)], "Pledge support")}</div></section>'''
    page("support/", "Support B2B.Marketing — Donate & Sponsor", "Support B2B.Marketing with a one-time or monthly contribution to fund free tools, playbooks, hiring and contest prizes.", body, crumbs=[("Support us", "support/")])
    # Advertise
    pk = [("Featured tool listing", "Top placement in the martech stack directory with logo, description and link.", "listing"), ("Newsletter sponsorship", "Sponsored slot in our B2B marketing newsletter, with one sponsor per issue.", "newsletter"), ("Playbook / tool sponsorship", "Sponsor a playbook or calculator with clear 'Sponsored by' labelling.", "sponsor"), ("Contest sponsorship", "Sponsor a prize or category in our awards and monthly challenges.", "contest"), ("Lead partnership", "Receive consent-based, matched B2B leads for your service.", "leads"), ("Domain & website partnership", "Interested in this domain, this website or a strategic partnership? Contact the owner.", "domain")]
    pc = "".join(f'<div class="card" id="{a}"><h3>{n}</h3><p>{d}</p></div>' for n, d, a in pk)
    body = hero("Advertise, sponsor & partner", "Reach B2B decision-makers", "Put your brand in front of marketers, founders and revenue leaders when they are actively planning growth.") + f'''<section class="section"><div class="container grid g3">{pc}</div></section>
<section class="section alt"><div class="container split"><div><h2>Request the media kit</h2><p>Tell us your goals and we will reply with audience details, availability and pricing. All sponsored content is clearly labelled and follows our editorial guidelines.</p><p>For the domain name, website acquisition or partnership enquiries, use the <a class="js-owner" href="../contact/" data-x="dGNhdG5vYy9za3Jvdy5iZXcvLzpzcHR0aA==">owner contact page</a>.</p></div>
{simple_form("Advertising / sponsorship inquiry", [("Company","company","text"),("Your name","name","text"),("Work email","email","email"),("Interested in","interest","select:Featured listing|Newsletter sponsorship|Playbook/tool sponsorship|Contest sponsorship|Lead partnership|Domain / website / partnership"),("Budget","budget","select:Under $1k|$1k–$5k|$5k–$20k|$20k+"),("Details","details","textarea")], "Request media kit")}</div></section>'''
    page("advertise/", "Advertise, Sponsor & Partner with B2B.Marketing", "Advertising, newsletter sponsorship, featured listings, contest sponsorship, lead partnerships and domain or website partnership with B2B.Marketing.", body, crumbs=[("Advertise", "advertise/")])

# ---------- COMPANY / LEGAL ----------
def legal(path, title, desc, text, crumb):
    content, _ = md(text)
    body = hero("Legal" if crumb not in ("About",) else "About", title, desc) + f'<section class="section"><div class="container narrow prose">{content}<p class="muted small">Last updated: {TODAY}</p></div></section>'
    page(path, title, desc, body, crumbs=[(crumb, path)])

def build_company():
    legal("about/", "About B2B.Marketing", "An independent resource helping B2B teams plan, launch and measure marketing that grows pipeline.", """
## Our mission
B2B.Marketing exists to make practical B2B growth knowledge free and usable. We publish in-depth playbooks, build free calculators and templates, curate the latest industry news and videos, and connect companies with vetted specialists when they need hands-on help.

## What we publish
- **Playbooks** on strategy, channels, operations and analytics.
- **Free tools** that run entirely in your browser.
- **Templates** you can copy and adapt.
- **News and videos** refreshed automatically from leading publications and channels, always linking back to the original source.

## How we make money
We keep the site free through advertising (including Google AdSense), clearly labelled sponsorships, partner referrals from our free growth audit (only with your consent), job posts and reader support. Sponsors never influence our editorial rankings or recommendations.

## Editorial standards
Our content is written and reviewed by the editorial team for accuracy and practicality. We avoid inflated claims, explain assumptions in our calculators and correct errors promptly. If you spot something wrong, please tell us through the contact page.
""", "About")
    body = hero("Contact", "Contact B2B.Marketing", "Questions, corrections, partnerships or press. Send us a message and we will reply as soon as we can.") + f'''<section class="section"><div class="container split"><div><h2>How can we help?</h2><ul class="checks"><li>Editorial questions and corrections</li><li>Advertising, sponsorship and partnerships</li><li>Agency listings and lead partnerships</li><li>Interest in this website or domain name</li></ul><p>For website, domain, sponsorship, advertisement or partnership interest you can also use the <a class="js-owner" href="./" data-x="dGNhdG5vYy9za3Jvdy5iZXcvLzpzcHR0aA==" rel="noopener">owner contact page</a>.</p></div>
{simple_form("General contact", [("Your name","name","text"),("Email","email","email"),("Topic","topic","select:General question|Correction|Advertising / sponsorship|Partnership|Website / domain interest|Press"),("Message","message","textarea")], "Send message")}</div></section>'''
    page("contact/", "Contact B2B.Marketing", "Contact B2B.Marketing for questions, corrections, advertising, sponsorship, partnerships or interest in this website or domain.", body, crumbs=[("Contact", "contact/")])
    legal("privacy/", "Privacy Policy", "How B2B.Marketing collects, uses and protects information.", """
## Who we are
B2B.Marketing ("we", "us") operates this website. This policy explains what we collect and why.

## Information you give us
When you submit a form (growth audit, newsletter, contact, job, contest, listing or support pledge) we receive the information you enter. Form submissions are delivered to us by email through a third-party form-processing service (FormSubmit). We use the information to respond, provide the service you requested and, for growth audits, to introduce you to up to three partners only with your consent.

## Calculators
Our calculators run entirely in your browser. Values you type into them are not sent to us.

## Cookies and advertising
We use Google AdSense to show ads. Third-party vendors, including Google, use cookies to serve ads based on your prior visits to this and other websites. Google's use of advertising cookies enables it and its partners to serve ads based on visits to this site and/or other sites on the Internet. You may opt out of personalised advertising by visiting Google Ads Settings (https://adssettings.google.com) or www.aboutads.info. In the EEA, UK and Switzerland, ads are shown in line with Google's consent requirements. See our Cookie Policy for details.

## Embedded content
Video pages embed YouTube content using privacy-enhanced mode. Loading a video may set cookies controlled by YouTube.

## Sharing
We do not sell personal information. We share it only with service providers needed to run the site (hosting, form delivery, advertising) and with matched partners when you explicitly agree.

## Retention and your rights
We keep submissions only as long as needed for the purpose collected. You may request access, correction or deletion at any time through the contact page. Depending on where you live (for example under GDPR, UK GDPR, CCPA/CPRA or PIPEDA) you may have additional rights.

## Children
This site is intended for business professionals and is not directed at children under 16.

## Changes
We may update this policy and will post the new date on this page.
""", "Privacy")
    legal("terms/", "Terms of Use", "The rules for using B2B.Marketing.", """
## Acceptance
By using this website you agree to these terms. If you do not agree, please do not use the site.

## Informational content
Content, calculators and templates are provided for general information and education. They are not legal, financial or professional advice. Results from calculators depend on the assumptions you enter.

## Intellectual property
Original text, design, code and graphics on this site are owned by B2B.Marketing and protected by copyright. You may copy templates for your own business use. You may not republish our playbooks or tools in bulk without written permission.

## User submissions
When you submit content (contest entries, job posts, listings, pitches) you confirm you have the right to do so and grant us a non-exclusive licence to review and, where stated, display a summary with credit.

## Third-party links and partners
We link to third-party websites and may introduce you to partner agencies. We are not responsible for their content, services or practices. Any agreement you make with a partner is between you and that partner.

## Contests
Contests are governed by the rules published on the contests page.

## Limitation of liability
The site is provided "as is" without warranties. To the fullest extent permitted by law we are not liable for losses arising from use of the site.

## Changes
We may update these terms at any time by posting a new version on this page.
""", "Terms")
    legal("disclaimer/", "Disclaimer, Trademark & Copyright Notice", "Independence, trademark and copyright disclosures for B2B.Marketing.", """
## Independence and trademark disclosure
B2B.Marketing is an independent website. It is **not affiliated with, endorsed by, sponsored by or connected to** any company, publication, event, agency or registered trademark that uses the words "B2B Marketing", "B2BMarketing", or similar names, including any similarly named websites or organisations. The phrase "B2B marketing" is used on this site in its ordinary, descriptive sense: marketing from one business to another.

## Third-party trademarks
All product names, company names, logos and brands mentioned on this site (for example in the martech stack directory, news feed or videos) are the property of their respective owners. Their use is for identification and commentary only and does not imply endorsement.

## Copyright
© B2B.Marketing. Original content on this site, including playbooks, calculators, templates, design and code, is protected by copyright. News headlines and excerpts are short references that link to the original publishers, who own that content. Embedded videos remain the property of their creators and are displayed through YouTube's embedding service.

## Advertising and sponsorship disclosure
This site displays ads, including Google AdSense ads, and may publish clearly labelled sponsored content or listings. We may receive referral fees when we introduce consenting users to partners. Compensation never changes our editorial assessments.

## No professional advice
Information is general in nature and not a substitute for professional advice tailored to your situation.

## Copyright concerns
If you believe content on this site infringes your rights, please contact us through the contact page with details and we will review and respond promptly.
""", "Disclaimer")
    legal("cookies/", "Cookie Policy", "How B2B.Marketing uses cookies and similar technologies.", """
## What are cookies?
Cookies are small text files stored on your device that help websites work and provide information to site owners and advertisers.

## Cookies we use
- **Essential:** remember your theme and cookie choice (stored in your browser's local storage).
- **Advertising:** Google AdSense and its partners may use cookies to show and measure ads, including personalised ads where permitted.
- **Embedded media:** YouTube may set cookies when you play a video.

## Your choices
Use the cookie banner to accept or limit non-essential cookies. You can also delete cookies in your browser settings and manage ad personalisation at https://adssettings.google.com.
""", "Cookies")

def build_misc():
    body = hero("Search", "Search B2B.Marketing", "Find playbooks, tools, templates and glossary terms.") + '<section class="section"><div class="container narrow"><input class="input js-page-search" type="search" placeholder="Search…" aria-label="Search"><ul class="js-page-results results"></ul></div></section>'
    page("search/", "Search", "Search B2B.Marketing playbooks, tools and glossary.", body, index=False)
    body = '<section class="page-hero"><div class="container"><p class="kicker">404</p><h1>Page not found</h1><p class="lead">The page you are looking for has moved or does not exist.</p><a class="btn btn-primary" href="./">Go home</a> <a class="btn btn-ghost" href="tools/">Free tools</a></div></section>'
    page("404.html", "Page not found", "This page could not be found.", body, index=False, noads=True)

def write_static():
    with open(os.path.join(ROOT, "sitemap.xml"), "w") as f:
        f.write('<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n')
        for p, _, _ in PAGES:
            pr = "1.0" if p == "" else ("0.8" if p.count("/") == 1 else "0.7")
            f.write(f"<url><loc>{SITE}/{p}</loc><lastmod>{TODAY}</lastmod><priority>{pr}</priority></url>\n")
        f.write("</urlset>\n")
    with open(os.path.join(ROOT, "robots.txt"), "w") as f:
        f.write(f"User-agent: *\nAllow: /\nDisallow: /search/\n\nSitemap: {SITE}/sitemap.xml\n")
    with open(os.path.join(ROOT, "ads.txt"), "w") as f:
        f.write("google.com, pub-6620975821265271, DIRECT, f08c47fec0942fa0\n")
    idx = [{"t": t, "u": p, "d": d} for p, t, d in PAGES]
    idx += [{"t": term, "u": "glossary/#" + slugify(term), "d": d} for term, d in GLOSSARY]
    with open(os.path.join(ROOT, "data", "search-index.json"), "w") as f:
        json.dump(idx, f, separators=(",", ":"))
    with open(os.path.join(ROOT, "manifest.webmanifest"), "w") as f:
        json.dump({"name": NAME, "short_name": "B2B.Mkt", "start_url": "./", "display": "standalone", "background_color": "#ffffff", "theme_color": "#0b5cff", "icons": [{"src": "assets/img/logo.svg", "sizes": "any", "type": "image/svg+xml"}]}, f)
    open(os.path.join(ROOT, ".nojekyll"), "w").close()
    for fn in ("news.json", "videos.json"):
        p = os.path.join(ROOT, "data", fn)
        if not os.path.exists(p):
            with open(p, "w") as f: json.dump({"updated": None, "items": []}, f)

if __name__ == "__main__":
    build_home(); build_guides(); build_tools(); build_glossary(); build_stack(); build_templates(); build_feeds()
    build_audit(); build_community(); build_company(); build_misc(); write_static()
    print(f"Built {len(PAGES)} indexable pages")
