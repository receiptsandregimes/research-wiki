---
title: Gold & SPX Switching Strategy
created: 2026-10-08
updated: 2026-10-08
see_also: [gold-spx-rs-ratio-rotation]
type: concept
tags: [commodities, equities, momentum, trend-following, backtest, drawdown]
sources: [raw/articles/returnstream-gold-sp500-switching.md]
confidence: low
---

# Gold & SPX Switching Strategy

A two-asset timing strategy from [[returnstream]]: alternate capital between gold and
the S&P 500 based on relative trailing strength, with a risk-free-rate escape hatch.
A simpler, fully-disclosed sibling with the same economic idea (no cash leg) is
[[gold-spx-rs-ratio-rotation]] ([[quantified-strategies]] variant).

## Rules (as publicly described)
- Measure relative strength of gold vs S&P 500 from each asset's trailing performance;
  hold whichever shows stronger momentum.
- **Risk-free rate filter:** if *neither* asset outperforms the 3-month T-bill yield,
  move to a money-market instrument.
- **The full rule set is NOT disclosed** — the article's rule list is empty in the
  published HTML and lives in a paid ebook; the 1977+ backtest spreadsheet is also paid.
  Lookback lengths, rebalance frequency, and switch thresholds are unknown.

## Claimed results (vendor backtest, 1977–2026, growth of $1,000)
| Metric | Gold | SPX | System |
|---|---|---|---|
| CAGR | 7.5% | 9.0% | 12.7% |
| Max DD | 62% | 53% | 31% |

Stress windows: +7.2% Mar 2000–Oct 2002 (dot-com), +5.2% Nov 2007–Mar 2009 (subprime),
vs SPX −40.9% / −46.1%. Drawdowns claimed "markedly more shallow and more brief" than
either asset. No costs, slippage, or engine stated — vendor marketing material.

The article also shows a gold-only 1-year trend filter (hold gold when trailing 1-yr
trend positive, else cash): it trims drawdowns but "falls short of beating the simple
buy-and-hold returns in the long run."

## Assessment
Classic two-asset momentum rotation; the edge claim rests entirely on an undisclosed,
unreproducible vendor backtest. Plausible family (time-series + relative momentum is
well documented) but the specific numbers are unverifiable as published. See
[[gold-spx-switching-outperforms-both-assets]], [[gold-trend-filter-underperforms-bnh]],
[[switching-positive-in-dotcom-subprime]], and test plan
[[gold-spx-switching-replication]].

## Open questions
- Exact lookback(s), rebalance cadence, tie-breaks, and filter comparison convention
  (total return vs price vs annualized?) — would need the paid ebook.
- Does gold-vs-cash momentum add anything over SPX-only trend following?
- Sensitivity of the 12.7% CAGR to the undisclosed parameters (overfitting risk).
