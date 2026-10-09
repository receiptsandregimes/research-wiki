---
title: Filtered-Levered Gold vs Gold Buy-and-Hold (the option-shape test)
created: 2026-10-08
updated: 2026-10-08
type: study
tags: [trend-following, commodities, leverage, position-sizing, backtest, study]
sources: [raw/transcripts/frank-gold-convexity-dual-momentum-2026-10-08.md]
status: proposed
---

# Study: Filtered-Levered Gold vs Gold Buy-and-Hold

## Question

Does a trend-filtered gold position, levered 2–3× with a stated financing
model, beat gold buy-and-hold on CAGR while never producing a rolling-5-year
loss worse than B&H's — i.e. does the [[gold-as-call-option]] shape survive
net of whipsaw and carry? (Frank's heuristic, on trial.)

## Claims tested

- [[gold-call-option-filtered-levered]] (primary)
- [[gold-trend-filter-underperforms-bnh]] (same baseline leg; unfiltered vs filtered)

## Data & assumptions

- Gold monthly (and daily for whipsaw sensitivity), 1971-08 → present (LBMA PM
  fix / FRED proxy). Bills: TB3MS. Margin-rate proxy for the levered leg;
  report bill-financed AND margin-financed variants — financing cost IS the
  premium in this trade.
- Filters: 12-mo total return > 0; 200-day MA (daily variant); 20-mo MA
  (monthly). Filter ON → target exposure L ∈ {1, 2, 3}; filter OFF → cash.
  Position from prior month-end data; costs 10 bps per unit exposure change.
- Engine: pandas under `studies/filtered-levered-gold-vs-bnh/code/`.
- Benchmarks: gold B&H, T-bills, and 60/40 (the honest "what else would you
  hold" comparator for a levered sleeve).

## Method

1. Unfiltered vs filtered 1× (reproduces/updates the Returnstream chart —
   answers [[gold-trend-filter-post-2023]]).
2. Leverage sweep: CAGR, max DD, Sharpe, worst rolling-5-year total return
   per L × financing model. The claim survives only if worst-5yr never worse
   than B&H while CAGR ≥ 2× B&H-ish at L=2.
3. Regime decomposition: 1980–2000 (the bleed), 2001–11, 2013–19, 2024–26
   separately — where does leverage help vs where does it compound a whipsaw?
4. Sensitivity: filter family × lookback × rebalance frequency; report the
   heatmap so we see if the surviving region is wide or one lucky cell.

## Questions this study must answer or update

- [[gold-trend-filter-post-2023]]
- [[does-the-cash-leg-earn-its-keep]] (this is absolute momentum in its purest single-asset form)

## Results

(pending — no code run yet)

## Verdict

(pending)

## Next tests prompted

- If survives: port to [[dual-momentum]] on gold/SPX/bills (proper Antonacci
  on our pair) — becomes its own study if the co-rally question demands
  hold-both variants.
- If financing cost kills it at 3× but not 2×: the claim's honest form is
  rate-regime-dependent — check 1977–81 (double-digit bills) separately; that
  window likely falsifies naive leverage.
