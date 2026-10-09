---
source_url: https://returnstream.com/gold-sp500-switching-strategy/
origin: web
ingested: 2026-10-08
sha256: 1704ba0f98f79e7ff580e6d3c7e2c116d781df5bc0a5f6d28567b66f16a777fa
full_text: raw_local/articles/returnstream-gold-sp500-switching.md (private store — this is a citation card; sha256 covers the stored full text)
drift: original ingest hash c110c9cbd6b93189cc0dd7a55caf626f63ba18c3b219b3de4a2807e62d85c15b; stored body no longer hashes to it (annotation text appears to have been appended after hashing, but the exact diff is unrecoverable); re-hashed 2026-10-12 against stored body per re-ingest rule; flagged, not silently corrected
---

# Gold & SPX Switching Strategy — citation card

Source: Returnstream (returnstream.com). Full article text is third-party
copyrighted and is NOT republished here; it is held in the private raw layer
for provenance (sha256 above). The site sells the full rule set (ebook) and
backtest spreadsheet; only publicly displayed content is recorded, as facts
attributed to the source.

## The system as stated by the source

- Measure the trailing relative strength of gold vs the S&P 500; hold the
  asset with stronger trailing momentum.
- Risk-free-rate filter: if neither asset outperforms the 3-month T-bill
  yield, move to a money-market position (cash leg).
- The site first considers a simpler variant — hold gold when its trailing
  1-year trend is positive, cash when negative — and reports it cuts some
  drawdowns but loses to gold buy-and-hold over the long run, motivating the
  two-asset switch.
- The site's formal rule list ("Here are the basic rules of this strategy:")
  renders EMPTY in the public page — the full rule set is behind a paid ebook;
  the 1977+ backtest spreadsheet is also paid. Everything below is what the
  public page displays.

## Numbers as reported by the source (vendor claims, unverified)

Growth-of-$1,000 backtest, 1977–2026 (as displayed on the page):

| | GOLD | SPX | SYSTEM |
|---|---|---|---|
| CAROR | 7.5% | 9.0% | 12.7% |
| Max DD | 62% | 53% | 31% |

Stress windows:

| Period | GOLD | SPX | SYSTEM |
|---|---|---|---|
| Dot-com (Mar 2000 – Oct 2002) | 14.5% | -40.9% | 7.2% |
| Subprime (Nov 2007 – Mar 2009) | 17.0% | -46.1% | 5.2% |

- No universe definition, no cost assumptions, no reimplementation disclosed;
  treat all figures as vendor claims. This is exactly what our replications
  ([[gold-spx-switching-replication]]) exist to test.

## Chart inventory (descriptions; images in private store / on the source page)

- spot-price-history.webp — gold spot history; underwater.webp — gold B&H
  underwater chart; TF-backtest.webp — 1-yr trend gold system vs B&H;
  system-eq-curve.webp — growth of $1,000 with CAROR/MAX DD legend;
  stress-eq-curve.webp / stress-perf.webp — stress windows;
  underwater-2.webp — system vs assets drawdowns 1977+.

Related: [[gold-spx-switching-strategy]] ·
[[gold-spx-switching-outperforms-both-assets]] ·
[[switching-positive-in-dotcom-subprime]] ·
[[gold-trend-filter-underperforms-bnh]] · [[returnstream]]
