---
title: Gold/SPX switching system was positive through dot-com and subprime crises
created: 2026-10-08
updated: 2026-10-08
type: claim
tags: [momentum, commodities, equities, drawdown, backtest, claim]
sources: [raw/articles/returnstream-gold-sp500-switching.md]
confidence: low
status: untested
testable: true
origin: source
tested_by: [studies/gold-spx-switching-replication]
---

# Claim

Per [[returnstream]]'s backtest of [[gold-spx-switching-strategy]]: the system gained
**+7.2% March 2000 – October 2002** (dot-com collapse, SPX −40.9%, gold +14.5%) and
**+5.2% November 2007 – March 2009** (subprime crisis, SPX −46.1%, gold +17.0%).

- If real, the crisis behavior matters more than the headline CAGR — positive absolute
  return in both windows would make this a genuine tail-hedge rotation, not just a
  beta-chasing curve.
- Caveat: gold was actually up in both windows, so a naive "hold the stronger asset"
  rule rotating to gold at the switch could explain most of it. The claim's strength
  depends on *when* it switched, which the undisclosed rules hide.
- Test: same protocol as [[gold-spx-switching-outperforms-both-assets]]
  ([[gold-spx-switching-replication]]); evaluate fixed crisis windows separately.
