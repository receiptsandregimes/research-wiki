---
title: Gold behaves like a call option; a momentum filter plus leverage makes the bleed tolerable
created: 2026-10-08
updated: 2026-10-08
type: claim
tags: [momentum, trend-following, commodities, options, position-sizing, leverage, claim]
sources: [raw/transcripts/frank-gold-convexity-dual-momentum-2026-10-08.md]
status: untested
testable: true
origin: frank
tested_by: []
---

# Claim

Frank's heuristic, from 30 years of trading (recorded faithfully; untested):
gold has call-option-like convexity — it bleeds a portfolio through its
lost-decade chop (1980–2000), but the bleed "doesn't hurt all that bad if you
add the momentum filter and add the position with leverage." I.e. trend-filter
gold to suppress the chop years, and size the filtered exposure levered, and
the option-like payoff profile survives net of the bleed.

- `origin: frank` — recorded for the record, to be independently re-researched.
- Why it might be true: the filter truncates the premium-payments phase (the
  1980–2000 bleed is almost entirely below the 200-month MA / negative
  12-month trend); leverage on the filtered (trend-positive) subset is how
  optionality gets expressed in a linear-instrument portfolio. Related vendor
  evidence cuts both ways: [[gold-trend-filter-underperforms-bnh]] says the
  filter costs return vs gold B&H — but says nothing about risk-adjusted or
  levered comparison, which is the claim's actual ground.
- Why to be skeptical: whipsaw costs in choppy-but-rising stretches (2003–06
  type regimes) plus financing cost on the leverage can eat the convexity;
  the claim's truth depends heavily on the financing rate and filter
  parameters — testable but parameter-sensitive.
- Test (to propose): gold trend-filtered, 1971+, at leverage 1×/2×/3× vs a
  bill-financed and margin-financed cost model; compare CAGR, max DD, and
  worst-5-year rolling return vs gold B&H and vs T-bills. Key stat: does the
  filter+leverage combo ever produce a rolling 5-year loss worse than B&H's?
