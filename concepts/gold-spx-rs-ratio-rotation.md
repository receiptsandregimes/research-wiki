---
title: Gold & SPX Ratio-Momentum Rotation (QuantifiedStrategies)
created: 2026-10-08
updated: 2026-10-08
type: concept
tags: [commodities, equities, momentum, trend-following, backtest, drawdown]
sources: [raw/articles/quantifiedstrategies-gold-sp500-rotation.md]
confidence: low
---

# Gold & SPX Ratio-Momentum Rotation (QuantifiedStrategies)

A fully-disclosed two-asset rotation from [[quantified-strategies]]: hold whichever
of S&P 500 / gold is favored by the price-ratio-vs-moving-average signal, decided at
each month end. Unlike the [[gold-spx-switching-strategy]] (Returnstream) variant
there is **no cash/T-bill leg and no absolute-momentum filter** — you are always in
one of the two assets.

## Rules (fully disclosed in the free article)
1. Monthly closing prices; S&P 500 price index (Yahoo `^GSPC`) and monthly spot gold.
2. Compute the S&P 500 / gold price ratio and its **20-month SMA**.
3. Ratio above SMA next-month signal → long S&P 500 for the coming month.
4. Ratio below SMA → long gold for the coming month.
5. Rebalance at month close, repeat. Always fully invested.

## Claimed results (author backtest, 1985/86 – Jul 2020, no costs stated)
| Metric | Rotation | S&P 500 B&H | Gold B&H |
|---|---|---|---|
| CAGR | 9.9% | n/a (not stated) | n/a |
| Max DD | 22% | 55% | n/a |

Equity chart (100k, Jul 1986 → Jul 2020): rotation ≈ 2.35M, SPX ≈ 1.4M, gold ≈ 0.55M.
Per-asset accumulated gains "pretty equal" — SPX months and gold months each
contributed roughly half the strategy's return.

## Librarian assessment
- Signal is fully specified → trivially replicable; unlike [[returnstream]] the paywall
  hides nothing essential.
- **Dividend exclusion is the big one**: `^GSPC` is price-only, and the strategy sits in
  SPX most months. SPX total return ≈ price return + ~2%/yr over this window, so
  dividend-adjusted SPX buy-and-hold likely matches or beats the 9.9% figure; the
  drawdown edge (22% vs 55%) is the more durable part of the claim.
- Edge is window-dependent: the equity curves only separate around/after the GFC;
  before 2008 the rotation trailed SPX. Backtest stops Jul 2020, missing gold's
  2024–25 run.
- 20-month SMA is a high-smoothing choice; only that length was tested — parameter
  sensitivity unexamined by the author.

## Open questions
- Does the claim survive dividend-adjusted SPX and realistic costs?
- Sensitivity to SMA length (10/15/20/30 months)?
- Would adding the Returnstream-style cash leg improve the DD profile further, or
  just cut returns?
- Intra-ratio direction confusion: article body uses SPX/gold ratio, summary image
  says gold/SPX with the same buy rule — replication must pin the direction down.

See claims [[qs-rotation-beats-both-buyhold]], [[qs-rotation-gfc-divergence]],
[[qs-rotation-asset-contributions-equal]] and test plan
[[gold-spx-ratio-rotation-replication]].
