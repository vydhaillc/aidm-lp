# Offer landing-page builder

`braces/index.html` is the theme *and* offer 3. Every other page is generated
from it:

```
python3 tools/lp/build.py
```

- `lpkit.py` — does the transform: swaps the head, nav, hero lockup, offer
  card, promotion band, the before/after-or-steps band, film wall, feature
  rows, price points, FAQ, contact and legal, then fixes asset depth.
- `offers_a.py` / `offers_b.py` — the eight English offers.
- `offers_es.py` — the two Spanish offers, plus `CHROME`, the literal-string
  swaps that translate everything the template hard-codes.
- `extra.css` — the rules the offer pages need that the braces page does not
  (steps band, "also published" list, ranged prices, three-up film rail).

Rules that keep the family consistent:

- **Never** name a layout modifier `.rev` — that is the review card, and its
  `display:flex` is declared later in the sheet. The feature-row modifier is
  `.flip`.
- The intraoral before/after rail is orthodontics only. Give an offer
  `cases=` to keep it; otherwise supply `steps=` and it is replaced.
- Shared assets live at the repo root (`/aidm-lp-assets/`, `/assets/cases/`).
  A page nested one level deeper (`es/…`) gets its `../` prefixes fixed
  automatically from the slug.
- Prices, inclusions and fine print come from the approved promotions sheet.
  Anything sourced elsewhere (AIDM's `pricing-draft`) is not approved for
  advertising and must be signed off before the page takes traffic.
