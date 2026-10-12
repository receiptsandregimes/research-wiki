---
title: Does dual momentum with per-asset filters beat one-of-two rotation on gold/SPX?
created: 2026-10-08
updated: 2026-10-12
type: question
tags: [momentum, equities, commodities, risk, question]
sources: [raw/transcripts/frank-gold-convexity-dual-momentum-2026-10-08.md]
status: open
priority: 1
spawned_by: [dual-momentum, rotation-onset-co-rally, gold-as-call-option, gold-spx-rs-ratio-rotation, gold-spx-switching-strategy]
videos: [open-question-gold-spx-rotation]
---

# Question

If each asset gets its OWN absolute-momentum filter (hold both when both
trend, the weaker one when they split, cash when neither beats bills), does
that dominate every one-of-two rotation on our pair — or does forcing a single
hold actually help by concentrating in the faster riser?

## Why it matters

This is where the round converges. Both seed systems force ONE asset at a time
([[gold-spx-rs-ratio-rotation]], [[gold-spx-switching-strategy]]);
[[gary-antonacci]]'s frameworks (GEM) choose ONE best asset but apply absolute
filters per-asset. If [[rotation-onset-co-rally]] is real, one-of-two rules
pay a structural tax exactly when the option-like asset ([[gold-as-call-option]])
is starting to pay — and the right skeleton isn't a rotation at all, it's a
sizing rule: full weight when one trends, both when both trend, cash when
neither. Frank's own live method is closer to that than to either vendor.

## First cheap check

Three portfolios, one table, same data pull as
[[filtered-levered-gold-vs-bnh]]: (a) QS ratio rotation, (b) Antonacci GEM-style
choose-best + bills, (c) per-asset 50/50 signal (0/50/100% equity legs).
CAGR/DD/Sharpe 1971+. If (c) ≈ (a)+(b) union, the design question is answered
before any fancy protocol. Legs partly live in [[co-rally-tax]].

## Status notes

- 2026-10-08: opened from Frank's ingest ("dual momentum should cap this
  round"). Deliberately NOT promoted yet: let the QS replication and
  filtered-gold baselines land first, so this study starts from measured
  components rather than three unverified ones.
