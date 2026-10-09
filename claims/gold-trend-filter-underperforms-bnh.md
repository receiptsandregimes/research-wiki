---
title: Gold 1-year trend filter cuts drawdown but underperforms gold buy-and-hold
created: 2026-10-08
updated: 2026-10-08
type: claim
tags: [trend-following, commodities, backtest, drawdown, claim]
sources: [raw/articles/returnstream-gold-sp500-switching.md]
confidence: low
status: untested
testable: true
origin: source
tested_by: [studies/gold-spx-switching-replication]
---

# Claim

Holding gold only when its trailing 1-year trend is positive (else cash) "helps mitigate
some drawdowns ... but falls short of beating the simple buy-and-hold returns in the
long run" — per [[returnstream]]'s chart (~1975–2023), in
[[gold-spx-switching-strategy]].

- Interesting because it inverts the usual trend-following pitch: on a single
  long-uptrend asset with violent mean-chop (gold 1980–2000), the whipsaw cost of a
  12-month filter can exceed its crash-avoidance benefit.
- Chart-only claim (no stats table in article); curves converge by 2023 — sensitive to
  the chosen end date and to gold's post-2024 rally.
- Test: cheap to check in [[gold-spx-switching-replication]] as the baseline leg
  (gold-only trend vs gold B&H, 1971+ using London Fix / spot).
