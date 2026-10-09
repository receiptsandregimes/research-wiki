---
title: SPX-months and gold-months contributed roughly equally to rotation strategy returns
created: 2026-10-08
updated: 2026-10-08
type: claim
tags: [momentum, commodities, equities, backtest, correlation, claim]
sources: [raw/articles/quantifiedstrategies-gold-sp500-rotation.md]
confidence: low
status: untested
testable: true
origin: source
tested_by: [studies/gold-spx-ratio-rotation-replication]
---

# Claim

In the [[gold-spx-rs-ratio-rotation]] backtest (1986–2020), accumulated percentage
gains earned while holding the S&P 500 and while holding gold were "pretty equal" —
neither asset leg dominates the strategy's return.

- Source: [[quantified-strategies]] per-asset contribution chart (both curves end
  ≈150–180% cumulative by month ~403), in [[gold-spx-rs-ratio-rotation]].
- Why it might be true: the two regimes are cleanly separated in time — SPX months
  accumulate 1985–2000, gold months accumulate 2001–12, then SPX again post-2013.
  Consistent with the published chart.
- Why to be skeptical: equal *summed* monthly gains ≠ equal *compounded* contribution
  (order matters); also an artifact of the chosen start date — begin in 1990 and the
  SPX leg likely dominates, begin in 2000 and gold dominates.
- Test: [[gold-spx-ratio-rotation-replication]] — decompose realized monthly strategy
  returns by leg; report both summed and log-accumulated splits across start dates.
