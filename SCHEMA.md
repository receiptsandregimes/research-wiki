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
├── comparisons/         # Layer 2: side-by-side analyses
└── queries/             # Layer 2: filed answers worth keeping
```

**Layer 1 — raw/:** immutable. Corrections go in Layer 2, never in raw.
**Layer 2 — the wiki:** agent-owned. Created/updated per ingest and per study.
**Layer 3 — SCHEMA.md:** this file.

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
type: claim | concept | entity | study | comparison | query
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
---
```

### Study page sections (required)
Question · Claims tested (wikilinks) · Data & assumptions (universe, period,
costs, engine/code path) · Method · Results (with numbers) · Verdict ·
Next tests prompted. Study code lives with the study under
`studies/<slug>/code/` or references an external repo by commit hash.

## raw/ frontmatter
```yaml
---
source_url: https://example.com/article   # if applicable
origin: web | paper | frank-recollection | paste
ingested: YYYY-MM-DD
sha256: <hex of body below frontmatter>
---
```
Re-ingest: recompute sha256 — skip if identical, flag drift if different.

## Tag Taxonomy
Add new tags HERE before using them.
- Asset classes: equities, futures, options, fx, crypto, rates, commodities
- Strategy families: momentum, mean-reversion, carry, value, vol, stat-arb,
  market-making, trend-following, event-driven, ml-alpha
- Microstructure: liquidity, spread, impact, order-flow, venue, latency
- Risk & portfolio: risk, position-sizing, drawdown, leverage, correlation, rebalancing
- Evidence: backtest, live-trading, academic, anecdote, data-quality, overfitting
- Process: study, claim, heuristic, mistake, edge, cost
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
