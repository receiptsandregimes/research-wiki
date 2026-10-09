---
title: QuantifiedStrategies
created: 2026-10-08
updated: 2026-10-08
type: entity
tags: [firm, backtest]
sources: [raw/articles/quantifiedstrategies-gold-sp500-rotation.md]
confidence: medium
---

# QuantifiedStrategies

Strategy blog/membership site (quantifiedstrategies.com), principal author Oddmund
Groette. Publishes free articles with rule descriptions + backtest equity curves;
code and "formal" trading-rule blocks are membership-only.

## Relevance as a source
- Middle ground between honest research and [[returnstream]]-style teaser marketing:
  the free article body usually *does* state the operative signal (as in
  [[gold-spx-rs-ratio-rotation]]), but execution details (data adjustments, costs,
  exact rebalance mechanics) are often left vague.
- House style quirks to account for when replicating: price-index SPX data from
  Yahoo (`^GSPC`, dividends excluded), no costs stated, monthly bars, backtests that
  often end well before the article's publish date.
- Site is behind a bot-verification wall for plain HTTP scrapes (ingest via browser).

## Source-quality notes
- [[qs-rotation-beats-both-buyhold]], [[qs-rotation-gfc-divergence]],
  [[qs-rotation-asset-contributions-equal]] are all from the author's own backtests —
  reproducible but unverified until we run
  [[gold-spx-ratio-rotation-replication]].
- Author self-flags the dividend omission in the article body — more transparent than
  most vendor sites.
