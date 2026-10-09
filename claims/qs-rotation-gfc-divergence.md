---
title: Rotation strategy trailed SPX until the GFC, then took off (new portfolio high while SPX made new low, Mar 2009)
created: 2026-10-08
updated: 2026-10-08
type: claim
tags: [momentum, commodities, equities, backtest, drawdown, risk, claim]
sources: [raw/articles/quantifiedstrategies-gold-sp500-rotation.md]
confidence: low
status: untested
testable: true
origin: source
tested_by: [studies/gold-spx-ratio-rotation-replication]
---

# Claim

The [[gold-spx-rs-ratio-rotation]] strategy **underperformed S&P 500 buy-and-hold
until the 2008/09 crisis and outperformed after**, because during the crisis "when
the S&P 500 made a new low in March 2009, the portfolio made a new high" — allowing
it to compound off a much higher base afterward.

- Source: [[quantified-strategies]] equity-curve reading, 1986–2020, in
  [[gold-spx-rs-ratio-rotation]].
- Why it might be true: the signal rotated into gold during H2-2008/early-2009
  (SPX/gold ratio collapsed below its 20-month SMA fast), and gold was roughly flat
  to up in that window — mechanically consistent with the chart.
- Why to be skeptical: this is a *narrative of one crisis*. The claim's strength is
  that a single regime event drives the entire long-run equity-curve separation,
  which is the definition of path dependence, not demonstrated robustness.
- Test: [[gold-spx-ratio-rotation-replication]] — compute rolling 5-yr relative
  performance of rotation vs SPX and the exact Mar-2009 drawdown/high facts from data;
  check how many distinct windows produce the outperformance.
