---
title: Gold/SPX Ratio-Momentum Rotation Replication (QuantifiedStrategies)
created: 2026-10-08
updated: 2026-10-12
type: study
tags: [momentum, commodities, equities, backtest, drawdown, study]
sources: [raw/articles/quantifiedstrategies-gold-sp500-rotation.md]
status: proposed
---

# Study: Gold/SPX Ratio-Momentum Rotation Replication

Code: https://github.com/frankyboots/receipts-lab/tree/main/studies/gold-spx-ratio-rotation-replication (status: protocol-only, seeded 2026-10-12)

## Question
Does the fully-disclosed [[gold-spx-rs-ratio-rotation]] signal reproduce CAGR ≈ 9.9% /
max DD ≈ 22% (1985–Jul 2020) — and does the headline edge survive dividend-adjusted
SPX data, realistic costs, and different SMA lengths?

## Claims tested
- [[qs-rotation-beats-both-buyhold]]
- [[qs-rotation-gfc-divergence]]
- [[qs-rotation-asset-contributions-equal]]

## Data & assumptions
- Universe: S&P 500 price index (matches source) AND total-return variant
  (Yahoo `^SPX` + dividend-reinvestment proxy, or `SPY` adjusted-close as proxy);
  gold monthly spot per [[lbma-gold-price]] composite leg (frozen LBMA fix
  history + seam-normalized GLD total-return live extension; the FRED
  `GOLDPMGBD228NL` named at proposal time is dead — log 2026-10-12).
- Period: 1985-01 → present (extend past source's Jul-2020 cutoff to test
  robustness through gold's 2024–25 run); monthly bars, positions from prior
  month-end data, executed next month.
- Costs: base run costless (matches source), sensitivity at 10 bps per switch.
- Engine: self-contained Python (pandas) under
  `studies/gold-spx-ratio-rotation-replication/code/`.

## Method
1. Pin down ratio direction (body: SPX/gold above SMA → long SPX; verify against the
   published ratio chart `gold-rotation.gif` peak ≈5.5 in 2000 → confirms SPX/gold).
2. Replicate 20-month SMA rule; report CAGR, max DD, Sharpe vs SPX price B&H,
   SPX total-return B&H, gold B&H.
3. Grid SMA length ∈ {10, 15, 20, 30, 40} months — expose parameter sensitivity the
   author never tested.
4. Per-leg return decomposition (summed and log-accumulated) across start dates
   1985/1990/1995/2000 — tests the "equal contributions" claim.
5. GFC facts: strategy equity high vs SPX low Mar-2009; rolling 5-yr relative
   performance.
6. Cross-check against [[gold-spx-switching-replication]] variants (does the
   Returnstream cash leg add anything over this simpler signal?).

## Questions this study must answer or update
- [[dividend-exclusion-edge-hole]] (step 2 answers it directly)
- [[does-the-cash-leg-earn-its-keep]] (step 6)
- [[both-assets-down-regimes]] (add a both-down months table to results)

## Results
(pending — no code run yet)

## Verdict
(pending)

## Next tests prompted
- Weekly/daily execution variant (monthly-bar smoothing).
- Add T-bill cash leg when *both* assets' trend negative — does DD drop below 22%?
- If replication holds with dividends included, this becomes a rare vendor-claim that
  survives contact; promote confidence accordingly.
