# AIDM® landing pages — aidm.dental

The offer pages behind AIDM®'s Google Ads, Meta ads and direct mail, built by Vydhai for the
Austin Institute of Dental Medicine. Production is **https://aidm.dental** (Vercel, auto-deploys
on push to `main`); `api/contact.js` is the lead function. The old GitHub Pages copy at
aidm.vydhai.com still builds from this repo and redirects every visitor to aidm.dental.

## Open to search and AI engines (since 2026-09-13)

Every offer page is indexable. The SEO/GEO layer is written by one script, run over the finished
HTML:

```
python3 tools/seo/apply_seo.py
```

**Run it again after any page edit or rebuild.** It is idempotent: everything it adds sits between
`<!-- seo:… -->` markers and is replaced on each run. It writes robots/canonical/hreflang/Open Graph
tags, one JSON-LD graph per page (AIDM's aidm.org entity, the offer and price points, FAQPage,
VideoObject, BreadcrumbList), the answer-first "At a glance" block, the "Current offers" footer row
and image alt text, and it regenerates `robots.txt`, `sitemap.xml`, `llms.txt` and the IndexNow key
file. Prices are read from each page, never typed into the script.

- Duplicates (`mailer/*`, `braces-v2`, `braces-lume`) are crawlable but canonical to their main page.
- `wisdom-teeth` is held `noindex` (`hold=True` in `PAGES`) until its per-tooth prices are reconciled
  with the $749 / $1,499 schedule on aidm.org/pricing.
- Adding a page: add it to `PAGES` and `OFFER_LINKS` in the script, then run it.

## Building offer pages

`tools/lp/` generates the offer pages from `braces/index.html` — see `tools/lp/README.md`. The
generator currently stops at `AssertionError: sub navcta` (the braces nav CTA changed after it was
written), so pages have been hand-edited since; fix it before relying on a rebuild.

Prices, inclusions and fine print come from AIDM's approved promotions sheet.
