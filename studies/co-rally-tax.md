---
title: Co-Rally Tax — does one-of-two rotation give up the first leg of regime shifts?
created: 2026-10-08
updated: 2026-10-16
type: study
tags: [momentum, correlation, equities, commodities, backtest, study]
sources: [raw/transcripts/frank-gold-convexity-dual-momentum-2026-10-08.md]
status: proposed
---

# Study: Co-Rally Tax (rotation-onset test)

Code: https://github.com/receiptsandregimes/receipts-lab/tree/main/studies/co-rally-tax (status: data layer complete + independently reviewed and MERGED — DFX-1..DFX-5 landed 2026-10-15 (completion 5ada3de, battery record fix 200e0ef), review findings recorded `aa5b794`, review fixes applied `670dda9`; ff-only merged into `main` and published 2026-10-16, every hash preserved: battery 24/24 exit 0, now time-aware with absolute start/end anchors on every source. Pin is main-only — the `study/co-rally-tax` branch ref was retired at the merge; the STUDY SPEC, which is not yet written, forks a fresh branch off the then-current main tip)

## Question

Forward-lookingly, when gold AND SPX both break their own trailing highs in
the same window (a rotation onset, per [[rotation-onset-co-rally]]), how much
return does a one-of-two rotation rule ([[gold-spx-rs-ratio-rotation]]) give
up versus holding both 50/50 — and does dual momentum with per-asset absolute
filters capture the difference?

## Claims tested

- [[rotation-onset-co-rally]] (primary)
- contextualizes [[qs-rotation-gfc-divergence]] (regime-switch timing)

## Data & assumptions

- Gold + SPX (price and total-return) monthly, 1971→present (1968 LBMA-peg
  episode discussed qualitatively only — no reliable monthly SPX-vs-peg
  series; date verification pending). Gold leg per [[lbma-gold-price]]
  composite (frozen fix history + GLD/GC=F live extension; free fix feeds died
  2026-02, log 2026-10-12). Bills TB3MS. Costs 10 bps/switch.
- Onset definition (pre-registered, no hindsight labels): month t is an
  onset if BOTH assets make a new trailing-12-month high at t AND at least
  one had been >10% below its 24-month high at t−6. (Tune the 10%/6mo knobs
  in a sensitivity grid, but the base definition is fixed before looking.)

## Method

1. Enumerate onsets 1971+; for each, forward 6/12-mo returns of gold, SPX,
   50/50, ratio-rotation, and dual-momentum-with-cash on the same pair.
2. Co-rally months table: % of onset-window months where both rise together;
   rotation's realized position (the faster riser) vs 50/50 — the tax.
3. Post-onset divergence: after how many months does one-asset dominance
   reassert? (This is where rotation earns its keep; measure both sides.)
4. Report the full distribution of onsets, not a cherry-picked episode list.

## Questions this study must answer or update

- [[both-assets-down-regimes]] (mirror image: same correlation machinery)
- [[does-the-cash-leg-earn-its-keep]] (per-asset vs shared absolute filter)

## Results

(pending — no code run yet)

## Verdict

(pending)

## Next tests prompted

- If tax is large: per-asset dual momentum (hold both when both trend) is a
  structurally better skeleton than one-of-two rotation → new study.
- 1968 peg-break episode: verify Pool collapse date vs SPX ATHs before any
  historical citation of Frank's version.
