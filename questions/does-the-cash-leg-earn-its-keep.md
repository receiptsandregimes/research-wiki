---
title: Does the T-bill cash leg earn its keep over always-in-market rotation?
created: 2026-10-08
updated: 2026-10-08
type: question
tags: [momentum, equities, commodities, risk, question]
sources: []
status: open
priority: 1
spawned_by: [gold-spx-rs-ratio-rotation, gold-spx-switching-strategy, qs-rotation-beats-both-buyhold, gold-spx-switching-outperforms-both-assets]
---

# Question

When both gold and SPX are in drawdown, does parking in T-bills (Returnstream's
escape hatch) actually improve CAGR/DD over the simpler always-in-market
[[gold-spx-rs-ratio-rotation]] — or is the cash leg marketing?

## Why it matters

This is the structural disagreement between our two seed sources, and **neither
vendor has an incentive to test the sibling system**: [[quantified-strategies]]
never adds a cash leg; [[returnstream]] never reports the no-cash variant. The
answer decides which skeleton we build on, and it generalizes to every
two-asset rotation we'll ever look at. If the cash leg adds nothing, every
"risk-managed" rotation pitch loses its main selling point.

## First cheap check

Run the fully-disclosed QS ratio rule on identical monthly data ± a cash rule
("both assets' trailing return < 3-mo T-bill → cash"), same period, same costs.
One data pull (also needed by both proposed studies), one extra column. Compare
CAGR, max DD, Sharpe, and behavior in 2008, 2020, 2022.

## Status notes

- 2026-10-08: opened from seed-article cross-reading (Frank's opinion request).
  Not promoted yet — waiting on the shared data pull; folds naturally into
  [[gold-spx-ratio-rotation-replication]] step 6 if we run that first.
