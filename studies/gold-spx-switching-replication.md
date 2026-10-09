---
title: Gold/SPX Switching Replication
created: 2026-10-08
updated: 2026-10-08
type: study
tags: [momentum, commodities, equities, backtest, drawdown, study]
sources: [raw/articles/returnstream-gold-sp500-switching.md]
status: proposed
---

# Study: Gold/SPX Switching Replication

## Question
Can a plausible reconstruction of [[returnstream]]'s [[gold-spx-switching-strategy]]
reproduce CAGR ≈ 12.7% / max DD ≈ 31% (1977–2026) and positive returns in the dot-com
and subprime windows — and how sensitive are those numbers to the undisclosed
parameters?

## Claims tested
- [[gold-spx-switching-outperforms-both-assets]]
- [[switching-positive-in-dotcom-subprime]]
- [[gold-trend-filter-underperforms-bnh]]

## Data & assumptions
- Universe: gold spot (LBMA PM fix or free proxy — FRED `GOLDPMGBD228NL`; or GLD/GDT
  series for modern era), S&P 500 total return (or price index + reinvested dividend
  proxy), 3-month T-bill (FRED `TB3MS`), 1977-01-01 → present, monthly bars.
- Costs: base run costless (matches vendor style), sensitivity run at 10 bps per
  switch; no leverage, fully invested.
- Engine: self-contained Python (pandas) under `studies/gold-spx-switching-replication/code/`.
- No signal-peeking: positions formed on prior month-end data, executed next month.

## Method
Because the exact rules are paywalled, grid a family of reconstructions:
1. Relative-strength lookback L ∈ {3, 6, 9, 12} months; hold asset with higher trailing
   return.
2. Risk-free filter variants: (a) both trailing returns < T-bill trailing return →
   cash; (b) both < 0.
3. Baselines: gold B&H, SPX B&H, gold-only 1-yr trend filter (tests claim 3).
Report CAGR, max DD, Sharpe per variant; stress-window returns for Mar-2000–Oct-2002
and Nov-2007–Mar-2009; heatmap of CAGR/DD across L × filter to expose parameter
sensitivity. Compare best/median variant against vendor's 12.7% / 31%.

## Results
(pending — no code run yet)

## Verdict
(pending)

## Next tests prompted
- If robust: compare against SPX-only trend + cash (does gold leg add anything?).
- Weekly execution variant to check monthly-bar smoothing effects.
- If Frank buys the ebook, rerun with the true rule set and diff.
- Cross-link: [[gold-spx-ratio-rotation-replication]] tests the fully-disclosed
  no-cash-leg sibling ([[gold-spx-rs-ratio-rotation]]) — run both and compare
  whether the T-bill escape hatch earns its keep.
