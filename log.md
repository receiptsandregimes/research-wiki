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

## [2026-10-08] ingest | QuantifiedStrategies — S&P 500 & Gold Rotation Strategy
- Raw: raw/articles/quantifiedstrategies-gold-sp500-rotation.md (sha256 d651e66e…);
  site bot-walls plain HTTP — captured via browser; formal rules block members-only
  but operative signal fully stated in free body text
- Assets: raw/assets/quantifiedstrategies-gold-sp500-rotation/ (4 images from
  ~/Downloads/quantified, all described in raw)
- Created: concepts/gold-spx-rs-ratio-rotation.md
- Created: entities/quantified-strategies.md
- Created claims (all untested, testable, origin: source):
  - claims/qs-rotation-beats-both-buyhold.md
  - claims/qs-rotation-gfc-divergence.md
  - claims/qs-rotation-asset-contributions-equal.md
- Created study proposal: studies/gold-spx-ratio-rotation-replication.md (proposed, not run)
- Updated: concepts/gold-spx-switching-strategy.md, entities/returnstream.md,
  studies/gold-spx-switching-replication.md (cross-links between the two
  gold/SPX rotation variants)
- Updated index.md (12 pages)

## [2026-10-08] create | Questions layer added to schema + backlog seeded
- SCHEMA.md: new `questions/` layer (warm backlog between spark and claim/study),
  `type: question`, status lifecycle open→active→promoted|answered|dropped,
  spawned_by/promoted_to/answered_by fields, first-cheap-check section,
  feedback edge (study verdicts must file questions), stale-backlog lint rule,
  `question` tag added to taxonomy.
- Created questions/does-the-cash-leg-earn-its-keep.md (P1)
- Created questions/both-assets-down-regimes.md (P1)
- Created questions/dividend-exclusion-edge-hole.md (P2)
- Created questions/gold-trend-filter-post-2023.md (P2)
- Updated: studies/gold-spx-ratio-rotation-replication.md,
  studies/gold-spx-switching-replication.md ("Questions this study must answer
  or update" sections cross-linking the backlog)
- Updated index.md (16 pages)

## [2026-10-08] ingest | Frank recollection — gold convexity, co-rally onsets, dual momentum cap
- Raw: raw/transcripts/frank-gold-convexity-dual-momentum-2026-10-08.md
  (origin: frank-recollection, sha256 ed6a3584…). Editorial note: London Gold
  Pool collapse verifies to March 1968 (LBMA/Wikipedia); Frank's "late 1968"
  date + SPX-ATH pairing flagged for verification, record left as stated.
- Created claims (origin: frank, untested, testable):
  - claims/gold-call-option-filtered-levered.md
  - claims/rotation-onset-co-rally.md
- Created concepts: concepts/dual-momentum.md (round's keystone — both seed
  systems shown as degenerate cases), concepts/gold-as-call-option.md
  (contested: momentum-entry [Frank] vs contrarian-entry [Kaeppel])
- Created entities: entities/frank.md, entities/gary-antonacci.md,
  entities/jay-kaeppel.md
- Created study proposals: studies/filtered-levered-gold-vs-bnh.md,
  studies/co-rally-tax.md (both proposed, not run)
- Created question: questions/dual-momentum-on-gold-spx.md (P1);
  updated questions/does-the-cash-leg-earn-its-keep.md (reframed as
  Antonacci's claim on our pair; Frank's working prior recorded)
- Updated index.md (26 pages)

## 2026-10-12 — public go-live restructure (Receipts & Regimes work-in-public)

- Repo re-scoped as the PUBLIC research record for @receiptsandregimes; SCHEMA
  gains a "Public contract" section (slug stability, `videos:` links, citation
  cards, no third-party full text/images in git, paraphrased transcripts,
  CC BY 4.0 + disclaimer, no-secrets rule).
- raw/articles/*.md rewritten as CITATION CARDS (attributed facts/rules/
  numbers, short quotes, links); full texts + 11 scraped images + verbatim
  Frank transcript moved to raw_local/ (gitignored; archived to private
  research-wiki-internal repo + local history bundle).
- raw/transcripts/frank-... page is now a paraphrase; verbatim stays private.
- Deleted stray root article.txt (unmanaged duplicate of QS article).
- Added README.md (public interface + disclaimer) and LICENSE (CC BY 4.0
  text / MIT code; third-party cited content stays with its authors).
- Added videos: [open-question-gold-spx-rotation] to the 7 pages cited by
  Open Question #1 (3 claims, 3 questions, dual-momentum concept).
- Drift flag: returnstream stored body did not match its ingest sha256
  (pre-existing; annotation-era diff unrecoverable). Re-hashed and flagged on
  the card, not silently corrected. QS + transcript hashes verified clean.
- Study code will live in a public companion dev repo, referenced by commit
  hash per SCHEMA.
- 2026-10-12 (later): history scrubbed via git-filter-repo (full texts, scraped
  images, verbatim transcript, stray article.txt exist in NO commit; originals
  live only in raw_local/ + private research-wiki-internal + local bundle).
  Repo flipped PUBLIC; companion public dev repo `receipts-lab` created
  (study code, referenced by commit hash); video packets' Code & notes links
  pointed at receipts-lab.
