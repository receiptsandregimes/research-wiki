---
title: Dual momentum
created: 2026-10-08
updated: 2026-10-08
type: concept
tags: [momentum, trend-following, risk, concept]
sources: [raw/transcripts/frank-gold-convexity-dual-momentum-2026-10-08.md]
confidence: medium
---

# Dual momentum

Combining **relative momentum** ("which asset is strongest?" → choose among
assets) with **absolute/time-series momentum** ("is it trending up at all?" →
else cash). Coined and systematized by [[gary-antonacci]] (*Dual Momentum
Investing*, 2013; GEM/GAA portfolios). Antonacci's stated finding: relative
momentum adds return but does little for drawdown; absolute momentum cuts
drawdown at some return cost; the combination is where the synergy lives.

## Why this page is the round's keystone

Our two seed articles are degenerate cases of dual momentum — which is why
neither can honestly answer the disagreement between them:

| System | Relative leg | Absolute leg |
|---|---|---|
| [[gold-spx-rs-ratio-rotation]] ([[quantified-strategies]]) | yes (ratio vs 20-mo SMA) | **no** — always in something |
| [[gold-spx-switching-strategy]] ([[returnstream]]) | yes (RS lookback) | yes (T-bill filter) — rules paywalled |
| Proper dual momentum (our test) | yes | yes, disclosed |

That makes [[does-the-cash-leg-earn-its-keep]] a re-run of Antonacci's central
claim on the gold/SPX pair specifically — a documented claim to verify, not a
cold-start curiosity. Frank's position: the dual-momentum frame is the right
skeleton for gold exposure given its option-like behavior
([[gold-as-call-option]]), and it subsumes the trend-filter question
([[gold-trend-filter-underperforms-bnh]] — "we're adding a filter to other
things").

## Open questions this frame opens

- Do gold and SPX want ONE dual-momentum overlay (shared cash signal) or
  per-asset absolute filters? Related to [[rotation-onset-co-rally]]: with two
  assets and one relative leg, co-move onsets force a single-hold and give up
  the slower riser.
- Antonacci's evidence is stocks/bonds/global equities; gold's autocorrelation
  structure and 1980–2000 chop are a harder environment — his parameters
  (12-mo lookback) may not transfer.

## Related

[[gold-spx-ratio-rotation-replication]] · [[gold-spx-switching-replication]] ·
all momentum-family pages in `claims/` · [[gold-as-call-option]]
