---
title: Gold/SPX relative-strength switching beats both assets on CAGR and max drawdown (1977–2026)
created: 2026-10-08
updated: 2026-10-12
type: claim
tags: [momentum, commodities, equities, backtest, drawdown, claim]
sources: [raw/articles/returnstream-gold-sp500-switching.md]
confidence: low
status: untested
testable: true
origin: source
tested_by: [studies/gold-spx-switching-replication]
videos: [open-question-gold-spx-rotation]
---

# Claim

A switching system that holds the stronger of gold vs the S&P 500 on trailing relative
strength, parking in money markets when neither beats the 3-month T-bill, achieved
(1977–2026): **CAGR 12.7% vs SPX 9.0% and gold 7.5%; max drawdown 31% vs SPX 53% and
gold 62%**.

- Source: [[returnstream]] vendor backtest, presented in
  [[gold-spx-switching-strategy]]. Single source, undisclosed rules (in paid ebook),
  undisclosed data vendor, no transaction costs stated.
- Why it might be true: momentum/rotation premia are well documented; gold-equity low
  correlation genuinely helps drawdown math.
- Why to be skeptical: undisclosed parameters + vendor incentive = overfitting risk;
  "vastly outperforms" over a window that includes gold's 2001–11 and 2024–26 runs.
- Test: [[gold-spx-switching-replication]] — reconstruct plausible rule variants and
  see if the CAGR/DD profile is robust, parameter-sensitive, or unreachable.
