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

## 2026-10-12 — receipts-lab seed: gold/SPX study family

- Seeded receipts-lab studies/gold-spx-ratio-rotation-replication/ for gold-spx-ratio-rotation-replication
- Seeded receipts-lab studies/gold-spx-switching-replication/ for gold-spx-switching-replication
- Seeded receipts-lab studies/co-rally-tax/ for co-rally-tax
- Seeded receipts-lab studies/filtered-levered-gold-vs-bnh/ for filtered-levered-gold-vs-bnh
- All four proposed studies share one data pull, seeded as a batch (receipts-lab
  commit 48d9db9). Shared stdlib fetch script (identical copy per study):
  FRED TB3MS, Yahoo ^SPX/SPY/GC=F, Shiller ie_data.xls; LBMA/GOLD via
  NDATALINK_API_KEY. Verified reachable 2026-10-12.
- Source reality check (recorded in each code README's disclosure block):
  FRED GOLDPMGBD228NL retired (HTTP 404) — wiki protocols naming it diverge
  accordingly; prices.lbma.org.uk and Stooq bot-walled from scripts; free
  keyless gold starts 2000 (GC=F), so full-history gold (1971/1977/1985 ->)
  needs a free Nasdaq Data Link key. Pre-1984 SPX via Shiller stitched to
  Yahoo (seam-normalized); Shiller file ends 2023-09 as served.
- dual-momentum-on-gold-spx stays unseeded on purpose: synthesis question fed
  by these four; seeding it now would invert the dependency order.

## 2026-10-12 — data infrastructure: LBMA fix feeds declared dead; composite gold leg adopted

- Verified: our PRIMARY gold mirror (forex-centuries LBMA daily) froze at
  2026-02-25 — its upstream (prices.lbma.org.uk/json) is the Incapsula wall that
  killed it repo-wide; every public daily-fix mirror shares that upstream, so
  free live LBMA fix data is gone (corroborated: datahub gold-prices fell back
  to Pink Sheet monthly averages; NDLC delisted; FRED retired 2022).
- Frozen history pinned sha256 86057834…fb24d9 (1968-04-01→2026-02-25).
- New gold-leg architecture recorded in [[lbma-gold-price]]: frozen fix history
  + seam-normalized live extension on GLD total returns (GC=F month-ends as
  second opinion, Pink Sheet monthly-average cross-check). Basis measured:
  GC=F-vs-fix month-end median 0.36%, p90 1.21%, max 4.75% @ 2026-01 — the seam
  window is the record's worst basis month; level-splicing banned, returns only.
- receipts-lab fetch script updated accordingly (GLD added to universe; mirror
  reclassified frozen-history; header cites this page). Paid licensed fix feed
  (metals-api class) noted as the only fix-grade continuation — deferred.
