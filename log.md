# Wiki Log

> Chronological record of all wiki actions. Append-only.
> Format: `## [YYYY-MM-DD] action | subject`
> Actions: ingest, update, query, lint, create, archive, delete
> When this file exceeds 500 entries, rotate: rename to log-YYYY.md, start fresh.

## [2026-10-08] create | Wiki initialized
- Domain: quantitative trading research (the trading brain)
- Structure: raw/, claims/, concepts/, entities/, studies/, comparisons/, queries/
- Schema customized with claim→study loop and `origin: frank` recollection workflow

## [2026-10-08] ingest | Returnstream — Gold and S&P500 Switching Strategy
- Raw: raw/articles/returnstream-gold-sp500-switching.md (sha256 c110c9cb…); note: rule list behind paid ebook, absent from scraped HTML
- Assets: raw/assets/returnstream-gold-sp500/ (7 webp charts; tables transcribed into raw)
- Created: concepts/gold-spx-switching-strategy.md
- Created: entities/returnstream.md
- Created claims (all untested, testable, origin: source):
  - claims/gold-spx-switching-outperforms-both-assets.md
  - claims/switching-positive-in-dotcom-subprime.md
  - claims/gold-trend-filter-underperforms-bnh.md
- Created study proposal: studies/gold-spx-switching-replication.md (proposed, not run)
- Updated index.md (6 pages)
