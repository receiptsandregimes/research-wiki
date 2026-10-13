# Wiki Schema

## Domain
Quantitative trading research. This wiki is Frank's trading brain: it ingests
external sources (articles, papers, strategy writeups, posts, data claims),
records Frank's 30-years-of-trading knowledge for re-research, and tracks the
studies we run to verify, refute, or quantify claims. Everything here is either
a recorded claim, evidence about a claim, or a study that tests one.

## Layers
```
research-wiki/
├── SCHEMA.md            # this file
├── index.md             # catalog of all pages
├── log.md               # chronological action log (append-only)
├── raw/                 # Layer 1: immutable sources (articles, papers, transcripts, assets)
├── claims/              # Layer 2: atomic testable claims ("X factor has positive IC in equities")
├── concepts/            # Layer 2: topics, strategies, indicators, microstructure phenomena
├── entities/            # Layer 2: people, firms, funds, datasets, instruments, books
├── studies/             # Layer 2: our own studies — proposal, protocol, results, verdict
├── questions/           # Layer 2: live open questions / hypothesis backlog (our own wonderings)
├── comparisons/         # Layer 2: side-by-side analyses
└── queries/             # Layer 2: filed answers worth keeping
```

**Layer 1 — raw/:** immutable. Corrections go in Layer 2, never in raw.
The public repo carries **citation cards** in `raw/` (metadata, attributed
facts/numbers in our words, short attributed quotes, link). The verbatim full
texts, scraped images, and verbatim transcripts live in `raw_local/`
(gitignored private store, backed up to the private `research-wiki-internal`
repo). Frank-recollection transcripts are **paraphrased** for the public card.
**Layer 2 — the wiki:** agent-owned. Created/updated per ingest and per study.
**Layer 3 — SCHEMA.md:** this file.

## Public contract (this repo is PUBLIC)

The wiki is the public research record for the Receipts & Regimes channel
(@receiptsandregimes). Videos pose questions from `questions/` and publish
verdicts from `studies/`; descriptions and on-screen citations link wiki pages
by slug.

- **Slug stability:** once a video cites a page slug, never rename or delete
  that page. Supersede via `_archive/` with a pointer stub if a page must go.
- **Permalinks:** the wiki publishes at
  <https://wiki.receiptsandregimes.com/> — URL = repo path minus `.md`
  (`claims/qs-rotation-beats-both-buyhold.md` →
  `/claims/qs-rotation-beats-both-buyhold`). Video descriptions cite these
  brand URLs; GitHub blob URLs remain as the canonical-source fallback. Same
  slug rule governs both. Site build: `site/quartz.config.yaml` +
  `.github/workflows/deploy.yml` (Quartz 5, pinned).
- **Video links:** pages cite videos via frontmatter `videos: [video-slug]`
  (slug = the `research-videos/videos/<slug>/` directory). Log video
  publish/verdict events in `log.md`.
- **Short links (rcpts.link):** YouTube truncates full brand permalinks in the
  collapsed description view, so descriptions may cite `https://rcpts.link/<code>`
  301 aliases. Registry: `shorts.yaml` (source of truth); sync:
  `site/shorts/sync.py` + `.github/workflows/shorts.yml` (Cloudflare
  dynamic-redirect rules on the rcpts.link zone). Codes are permanent once
  published — never reassign or recycle. They are a display alias only: the
  canonical permalink stays repo-path-minus-`.md`, and full permalinks remain
  the citation form in wiki pages, studies, and receipts.
- **Nothing third-party full-text:** ingests write the verbatim source into
  `raw_local/` and a citation card into `raw/`. No scraped images in git.
  Short quotes must be attributed and minimal. Vendor numbers are recorded as
  attributed facts (they're what the source reports), never as our findings.
- **Frank's knowledge:** public transcripts pages are paraphrases; verbatim
  records stay in `raw_local/`.
- **Licensing:** original content CC BY 4.0 (see LICENSE); README carries the
  no-investment-advice disclaimer. Don't weaken either.
- **No secrets, ever:** no credentials, account names, broker names, or PII —
  public repo means every commit is a potential publication.

## The claim → study loop (core workflow)
1. Ingest a source → extract **claims** into `claims/` (one file per atomic,
   testable claim; status lifecycle below).
2. Claims with `testable: true` become candidates for **studies** in `studies/`.
   A study links to the claims it tests and to the concepts it touches.
3. Study results update the claim's `status` and `confidence` and are
   cross-linked from the claim page.
4. Frank's remembered/heuristic knowledge is ingested the same way: recorded as
   a claim with `origin: frank` (`confidence` unset until re-researched), then
   researched for the record.

### Questions: the warm layer (backlog of live wonderings)
A **question** is something WE wonder, not an assertion we are verifying. It has
no numbers yet and often no protocol yet — it is the stage between a spark
(ingest, study verdict, source disagreement, Frank's intuition) and a formal
claim/study pair. Examples of what belongs here: "does the cash leg earn its
keep?", "what happens when both assets fall together?" — questions no source
asserts but whose answers shape which claims matter.

- One file per question in `questions/`, `type: question`.
- Every question records `spawned_by:` (claims/concepts/studies that triggered
  it) so lineage is traceable, and a **first cheap check** — the smallest piece
  of work that would sharpen or kill it.
- A question is NOT a claim: it carries no confidence and no numbers. The moment
  it sharpens into a testable assertion, write the claim + study and promote the
  question (keep the page as lineage).

**Question status lifecycle:**
`open → active (being sharpened) → promoted (claim+study exist) | answered
(filed in queries/, no study needed) | dropped (not worth bandwidth — say why)`

**Feedback edge:** every study verdict section must list the questions the
result opened, each filed as a `questions/` page (or linked to an existing
one). This is what makes the loop compound instead of draining.

Lint rule: surface `open`/`active` questions untouched for >30 days (stale
backlog) and `open` questions with no `spawned_by` (unsourced curiosity —
either find the spark or drop it).

### Claim status lifecycle
`untested → in-progress → supported | refuted | mixed | inconclusive`
plus `dodged` (not worth testing; note why).

## Conventions
- File names: lowercase, hyphens, no spaces (e.g., `momentum-cross-sectional.md`)
- Every page starts with YAML frontmatter (below)
- `[[wikilinks]]` everywhere; minimum 2 outbound links per page
- Bump `updated` on every edit; every new page goes in `index.md`; every action
  goes in `log.md`
- Provenance: append `^[raw/articles/source.md]` to paragraphs whose claims
  trace to a specific source (required on multi-source synthesis pages)
- Money rule: no number enters the wiki without a source or a study citation.
  Backtest figures record engine, period, costs, and slippage assumptions.
- Frank's remembered heuristics are labeled `origin: frank` and are NOT marked
  supported until independently re-researched.

## Frontmatter (Layer 2 pages)
```yaml
---
title: Page Title
created: YYYY-MM-DD
updated: YYYY-MM-DD
type: claim | concept | entity | study | question | comparison | query
tags: [from taxonomy below]
sources: [raw/articles/source-name.md]
confidence: high | medium | low     # how well-supported
contested: true                     # unresolved contradiction present
contradictions: [other-page-slug]
# claim-only:
status: untested | in-progress | supported | refuted | mixed | inconclusive | dodged
testable: true | false
origin: source | frank | derived
tested_by: [studies/study-slug]
# question-only:
status: open | active | promoted | answered | dropped
priority: 1 | 2 | 3                 # 1 = work on it next; backlog ordering
spawned_by: [claims/x, studies/y]   # what triggered the wondering
promoted_to: [claims/z, studies/w]  # when promoted
answered_by: queries/slug           # when answered without a study
# any page cited by a video:
videos: [video-slug]                # stable slug; see Public contract
---
```

### Question page sections (required)
Question (one sentence) · Why it matters (what it would change if answered) ·
First cheap check (smallest experiment/sketch) · Status notes (dated bullets).

### Study page sections (required)
Question · Claims tested (wikilinks) · Data & assumptions (universe, period,
costs, engine/code path) · Method · Results (with numbers) · Verdict ·
Next tests prompted. Study code lives with the study under
`studies/<slug>/code/` or references an external repo by commit hash.

## raw/ frontmatter (citation cards)
```yaml
---
source_url: https://example.com/article   # if applicable
origin: web | paper | frank-recollection | paste
ingested: YYYY-MM-DD
sha256: <hex of the verbatim full text in raw_local/>
full_text: raw_local/articles/slug.md (private store)
---
```
Re-ingest: recompute sha256 over the raw_local full text — skip if identical,
flag drift if different. New ingests: write full text to `raw_local/`, card to
`raw/`, never the reverse.

## Tag Taxonomy
Add new tags HERE before using them.
- Asset classes: equities, futures, options, fx, crypto, rates, commodities
- Strategy families: momentum, mean-reversion, carry, value, vol, stat-arb,
  market-making, trend-following, event-driven, ml-alpha
- Microstructure: liquidity, spread, impact, order-flow, venue, latency
- Risk & portfolio: risk, position-sizing, drawdown, leverage, correlation, rebalancing
- Evidence: backtest, live-trading, academic, anecdote, data-quality, overfitting
- Process: study, claim, heuristic, mistake, edge, cost, question
- Meta: comparison, history, person, firm, book, dataset

## Page Thresholds
- **Create a page** when an entity/concept appears in 2+ sources OR is central
  to one source; **every atomic testable claim gets a claims/ page**
- **Add to existing page** when a source mentions something already covered
- **DON'T create pages** for passing mentions or out-of-domain material
- **Split** pages over ~200 lines; **archive** superseded pages to `_archive/`

## Update Policy (contradictions)
1. Newer sources generally supersede — but a study result always beats an
   external claim regardless of date.
2. Genuinely contradictory: note both positions with dates and sources.
3. Mark `contradictions:` in frontmatter.
4. Flag for Frank's review in the lint report.
