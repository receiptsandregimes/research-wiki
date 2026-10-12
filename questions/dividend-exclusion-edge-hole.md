---
title: How much of the rotation edge is just the dividend exclusion?
created: 2026-10-08
updated: 2026-10-12
type: question
tags: [momentum, equities, backtest, data-quality, cost, question]
sources: []
status: open
priority: 2
spawned_by: [qs-rotation-beats-both-buyhold, quantified-strategies]
videos: [open-question-gold-spx-rotation]
---

# Question

If we swap QuantifiedStrategies' price-only `^GSPC` for total-return SPX, how
much of the rotation strategy's claimed outperformance evaporates?

## Why it matters

[[quantified-strategies]] excluded dividends while SPX carry is ~2%/yr of the
strategy's SPX-exposure time. Two possible worlds: the edge survives total
returns (rare — a vendor claim that stands, worth promoting confidence), or it
shrinks substantially (the "beats buy-and-hold" headline was a data artifact).
Either answer calibrates how we treat *every* future blog-backtest number. This
is the cheapest high-information falsification in the backlog.

## First cheap check

Identical replication, two SPX series: price index and SPY-adjusted-close proxy
(1993+ only for SPY; use a dividend-reinvestment proxy before that). Delta in
CAGR vs the source's published 9.9% is the whole answer.

## Status notes

- 2026-10-08: opened. Already folded into
  [[gold-spx-ratio-rotation-replication]] step 2 (price-only AND total-return
  variants) — this page exists so the question outlives the study either way.
