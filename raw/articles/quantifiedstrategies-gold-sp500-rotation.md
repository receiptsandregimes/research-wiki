---
source_url: https://www.quantifiedstrategies.com/rotation-strategy-in-gold-and-sp500/
origin: web
ingested: 2026-10-08
sha256: d651e66e1208043eb383e31803fb6b0705ecce6164af331ad417a643121c0431
full_text: raw_local/articles/quantifiedstrategies-gold-sp500-rotation.md (private store — this is a citation card; sha256 covers the stored full text)
---

# Rotation Strategy In S&P 500 And Gold (SPY & GLD) — citation card

Author: Oddmund Groette, quantifiedstrategies.com (published 2025-03-06 per page
metadata). Full article text is third-party copyrighted and is NOT republished
here; it is held in the private raw layer for provenance (sha256 above). The
rule set and numbers below are recorded as facts attributed to the source, in
our own words, with short attributed quotes.

## The system as stated by the source

- Monthly data. At each month-end, compute the ratio of S&P 500 price to gold
  price and compare it to the ratio's 20-month simple moving average.
- Ratio above its 20-month SMA → hold the S&P 500 the following month.
  Ratio below → hold gold the following month. Always in exactly one asset;
  no cash leg.
- The site's own summary phrasing: the strategy switches "in and out of the
  S&P 500 and gold by using the gold and S&P 500 ratio."
- Note: the direction of the ratio differs between the article body (S&P/gold)
  and the site's summary image (gold/S&P); the operative body rule is as above.

## Numbers as reported by the source (vendor claims, unverified)

| Metric | Rotation strategy | S&P 500 B&H | Gold B&H |
|---|---|---|---|
| CAGR | 9.9% | not stated | not stated |
| Max drawdown | 22% | 55% | not stated |

- Period: 1985 (chart starts July 1986) to July 2020; monthly bars.
- Data: monthly spot gold and S&P 500 price index (GSPC) from Yahoo Finance;
  the author states GSPC is not dividend-adjusted and that dividends are
  "a major part of the total return" — i.e. the benchmark is understated.
- No transaction costs stated. Only the 20-month SMA length was tested.
- Source's characterization: strategy trailed the S&P 500 until 2008/09, then
  pulled ahead; at the March 2009 SPX low the strategy portfolio made a new
  high; per-asset contributions were "pretty equal."

## Chart inventory (descriptions; images in private store / on the source page)

- `gold-rotation.gif` — S&P/gold ratio vs its 20-month SMA, 1985–2020.
- `gld-vs-spy-chart.gif` — equity curves of 100k from Jul 1986: rotation
  ends ~2.35M vs SPX ~1.4M vs gold ~0.55M; divergence after 2009.
- `gold-vs-sp500.gif` — accumulated per-asset contributions (both ~equal).
- `sp500-and-gold-rotation-strategy-1024x643.jpg` — site summary card.

## Provenance caveats

- The formal "Trading Rules" block on the page is members-only; the rules
  recorded above are those stated in the free body text.
- Article is internally inconsistent about 1985 vs 1986 start.

Related: [[gold-spx-rs-ratio-rotation]] · [[qs-rotation-beats-both-buyhold]] ·
[[qs-rotation-gfc-divergence]] · [[qs-rotation-asset-contributions-equal]] ·
[[quantified-strategies]]
