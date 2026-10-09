---
title: Gold/SPX ratio-SMA rotation beats both buy-and-holds (1985–2020, CAGR 9.9% / max DD 22%)
created: 2026-10-08
updated: 2026-10-08
type: claim
tags: [momentum, commodities, equities, backtest, drawdown, claim]
sources: [raw/articles/quantifiedstrategies-gold-sp500-rotation.md]
confidence: low
status: untested
testable: true
origin: source
tested_by: [studies/gold-spx-ratio-rotation-replication]
---

# Claim

A monthly rotation between S&P 500 and gold, driven by the S&P/gold price ratio vs
its 20-month SMA, achieved (1985–Jul 2020) **CAGR 9.9% with max drawdown 22%**, vs
S&P 500 buy-and-hold max DD 55% — and beat both buy-and-holds on the equity chart
(≈2.35M vs 1.4M SPX vs 0.55M gold on 100k from Jul 1986).

- Source: [[quantified-strategies]] backtest, rules fully disclosed, presented in
  [[gold-spx-rs-ratio-rotation]]. No transaction costs stated; **dividends explicitly
  excluded** (`^GSPC` price index).
- Why it might be true: relative-strength rotation between low-correlation assets is a
  well-documented family; the 2001–09 gold regime alone can flip the DD comparison.
- Why to be skeptical: dividend exclusion inflates the strategy's relative CAGR by
  ~2%/yr of SPX exposure time; single tested parameter (20-month SMA); edge appears
  only post-2008; backtest window cherry-ended Jul 2020.
- Test: [[gold-spx-ratio-rotation-replication]] — direct replication (rules are fully
  specified), price-only and total-return variants, cost sensitivity, SMA-length grid.
