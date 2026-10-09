---
title: Does the gold-trend-filter-underperforms-B&H result survive past 2023?
created: 2026-10-08
updated: 2026-10-08
type: question
tags: [trend-following, commodities, backtest, question]
sources: []
status: open
priority: 2
spawned_by: [gold-trend-filter-underperforms-bnh, returnstream]
---

# Question

Returnstream's chart shows a 1-yr gold trend filter converging with gold
buy-and-hold by ~2023 — did gold's 2024–26 rally flip the comparison, making
the vendor's own chart stale the day it was published?

## Why it matters

This claim is the most generalizable one in the wiki: whipsaw cost of a
12-month filter on a long-uptrend asset can exceed its crash-avoidance benefit
(whipsaw is bounded by volatility; trend-following's crash-payoff scales with
trend persistence; an asset that mean-chops for 20 years then compounds —
stocks 1982–2026, gold 2001–2026 — wins the trend-following game while chop
dominates). If the reversal is just gold's recent run, the lesson needs a
bigger sample: rerun the same trend-filter-vs-B&H test on SPX and on a third
asset (BTC if we allow it, or TLT/bonds since 2000). A cross-asset pattern here
is a wiki-grade concept page; a gold-only result is an artifact.

## First cheap check

Gold trend filter vs B&H, 1971→present, monthly, LBMA/FRED data — this is
already the baseline leg of [[gold-spx-switching-replication]]. Then SPX
1950→present as the out-of-sample.

## Status notes

- 2026-10-08: opened. Note the irony: the source that admits this is a
  vendor marketing switching — one honest chart worth verifying on its own.
