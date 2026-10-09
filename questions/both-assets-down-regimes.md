---
title: What happens to gold/SPX rotation when BOTH assets fall together?
created: 2026-10-08
updated: 2026-10-08
type: question
tags: [momentum, equities, commodities, correlation, drawdown, risk, question]
sources: []
status: open
priority: 1
spawned_by: [gold-spx-rs-ratio-rotation, gold-spx-switching-strategy, switching-positive-in-dotcom-subprime]
---

# Question

Both seed strategies assume gold and SPX regimes alternate. What do they do in
windows where *both* fall — the regime their backtest curves quietly exclude?

## Why it matters

Every DD claim in the wiki ([[qs-rotation-beats-both-buyhold]],
[[gold-spx-switching-outperforms-both-assets]]) rests on the rotation always
having a decent asset to rotate INTO. Candidate both-down regimes: Mar-2020
(gold fell with equities into the margin-call flush), Sep-2008 weeks (gold
dropped ~30% peak-to-trough before it "worked"), 2013 gold crash, 1983–2000
gold bear (rotation into gold = slow bleed while SPX ripped — the mirror
problem). If rotation bleeds in both-down windows, the published max-DD numbers
are window artifacts and the strategy's real risk is the one nobody plots.

## First cheap check

Enumerate months 1977+ where both assets' trailing 3-mo returns are negative;
overlay each rotation strategy's position and P&L in those months. A table, not
a study — it tells us whether this deserves a full study page.

## Status notes

- 2026-10-08: opened. Neither proposed study covers this; add as an explicit
  section to whichever study runs first.
