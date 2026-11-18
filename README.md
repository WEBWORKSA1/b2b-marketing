# B2B.Marketing

Free B2B marketing playbooks, calculators, templates, auto-updating news/videos and a lead-generating growth-audit / expert-matching service. Static site for GitHub Pages (main branch, root).

- Build: `python3 scripts/build.py`
- Auto-refresh: `.github/workflows/refresh.yml` runs `scripts/refresh.py` every 6 hours (news RSS + YouTube), rebuilds and commits.
- Content lives in `content/` (guides, tools, glossary, stack, templates).
- Optional donation payment link: create `assets/js/config.js` with `window.B2B_PAYLINK="https://..."` and include it before site.js.
- Research and phase-wise build prompt: `docs/`.

© B2B.Marketing. Independent site, not affiliated with any similarly named company or trademark.
