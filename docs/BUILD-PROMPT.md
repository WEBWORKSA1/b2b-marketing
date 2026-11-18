# B2B.Marketing — Phase-wise build prompt

## The idea (why this wins)
**B2B.Marketing = the free B2B growth toolkit + expert-match marketplace.**
Free calculators, playbooks, templates, a martech stack directory and an auto-updating news/video feed pull in high-intent B2B traffic (marketing/software keywords carry some of the highest AdSense CPCs). That traffic converts into a **Free B2B Growth Audit / Get-Matched** lead flow, where each qualified lead can be sold to or shared with vetted agencies and vendors. Secondary revenue: sponsored listings, newsletter and page sponsorships, job posts, contest sponsorships and reader support.

Revenue stack, in order of expected size:
1. Qualified B2B leads (audit / expert match) — $50–$300 per qualified lead in agency referral markets.
2. Google AdSense on content + tools pages.
3. Sponsorships / featured listings / advertising.
4. Job posts and talent network.
5. Contest sponsorships and entry upgrades.
6. Donations ("Support B2B.Marketing").

---

## Phase 1 — Foundation & compliance
Build a static, GitHub Pages-compatible site (plain HTML/CSS/JS, no server) for the domain **B2B.Marketing**.
- Global header with a top bar on every page: "contact, if you are interested in this website/domain name/Sponsorship/Advertisement/Partnership", linked to the owner's contact page. The URL is decoded by JS at runtime and not printed as text.
- One contact email for the entire site, never shown in HTML. It is assembled in JS from encoded fragments only at form submission.
- AdSense Auto Ads script in every `<head>` (client `ca-pub-6620975821265271`), `ads.txt` at root.
- Required pages: About, Contact, Privacy Policy (AdSense/cookies/third-party vendors), Terms, Disclaimer + Trademark/Copyright notice, Cookie Policy, 404.
- Cookie-consent banner, accessible nav, skip link, dark/light theme, responsive mobile menu.
- SEO: unique titles/meta, canonical URLs, Open Graph, JSON-LD (Organization, WebSite+SearchAction, Article, FAQPage, BreadcrumbList), sitemap.xml, robots.txt, relative links so it works on github.io and the custom domain.

## Phase 2 — Content engine (AdSense approval depth)
- 10+ long-form, original playbooks (ABM, demand gen, lead scoring, B2B SEO + AI search, LinkedIn, email, content, attribution, sales–marketing alignment, budgeting, events/webinars, PLG). Each with a key-takeaways box, TOC, FAQ, and related links.
- Glossary of 60+ B2B terms with anchors.
- Copy-ready templates (ICP worksheet, campaign brief, cold email, nurture sequence, SLA, UTM conventions, webinar run-of-show, case-study outline).

## Phase 3 — Interactive tools
Client-side calculators with explanatory content: CAC & payback, LTV:CAC, marketing ROI, funnel/pipeline reverse-planner, lead-scoring builder, budget allocator, UTM builder, ABM account tiering, email subject-line checker, webinar ROI. Each tool ends with a "Get an expert to review your numbers" CTA into the lead form.

## Phase 4 — Lead generation (core revenue)
- `/growth-audit/`: multi-step form (company, size, ACV, goals, budget, timeline, channels, contact) with a progress bar, instant on-screen readiness score, consent checkbox, honeypot.
- Lead magnets: playbook download gate, newsletter, "Get matched with a vetted agency".
- Sticky CTA, exit-intent-free design (AdSense-friendly), inline CTAs inside guides and tools.

## Phase 5 — Community & monetization modules
- Martech stack directory (filter by category, search), "Submit/feature your tool".
- Agency directory + "List your agency".
- Jobs & talent: post a job, join the talent network, write-for-us.
- Contests: B2B Campaign of the Year + monthly challenges with prizes, rules, entry form.
- Support/donate: tiers (Coffee, Supporter, Champion, Patron) and one-time or monthly pledge form; uses of funds (operations, promotions, marketing, hiring, prizes).
- Advertise/sponsor/partner page with a media-kit style package grid + inquiry form.

## Phase 6 — Self-updating automation
- GitHub Actions workflow (every 6h + manual + on push): fetches RSS headlines from public B2B marketing publications and latest videos from B2B marketing YouTube channels, writes `data/news.json` and `data/videos.json`, refreshes the sitemap `lastmod`, and commits to `main`.
- Pages render that data client-side with skeleton loaders and graceful fallbacks.

## Phase 7 — QA, deploy, grow
- Link check, HTML validation, Lighthouse (performance/accessibility/SEO), mobile test.
- Push to `webworksa1/b2b-marketing` on `main`; GitHub Pages → Deploy from branch `main` / root; custom domain `b2b.marketing` + HTTPS.
- After launch: submit sitemap to Search Console, apply for AdSense once 20–30 indexed pages exist, then add affiliate links to the stack directory.
