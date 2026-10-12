---
title: LBMA Gold Price (dataset)
created: 2026-10-12
updated: 2026-10-12
type: entity
tags: [dataset, gold, data, infrastructure]
confidence: high
---

# LBMA Gold Price (dataset)

The twice-daily London benchmark fix (AM/PM, USD/oz). Our gold-leg backbone:
daily PM fix 1968-04→, month-end extraction for the monthly gold/SPX study
family. This page is the canonical record of the feed's status and our fallback
architecture — all gold-leg protocols cite it.

## Status: no free live fix feed exists (verified 2026-10-12)

The official series still exists but is licensed-only, and every public route
to it is dead:

| Route | Status | Evidence (2026-10-12) |
|---|---|---|
| FRED `GOLDPMGBD228NLBM` | dead | IBA series dropped 2022-01-31 (HTTP 404) |
| Nasdaq Data Link `LBMA/GOLD` | dead | dataset delisted (page 404; catalog empty) |
| `prices.lbma.org.uk/json/gold_pm.json` | bot-walled | Incapsula 403, incl. from a real browser |
| Public GitHub mirrors | frozen | they pull the walled JSON above |
| LBMA paid successor (LBMTD) | wrong product | OTC volumes, not price |

The mirror this brain used as PRIMARY — `unbalancedparentheses/forex-centuries`
`data/sources/lbma/lbma_gold_daily.csv` (weekly CI pulling the LBMA JSON) —
died when the wall went up: last data row **2026-02-25**, last commit
2026-02-26. Frozen copy pinned:
`sha256 86057834bd6fca539749f150a42255e28c4cf0fac2935b265b1c13e826fb24d9`.

Ecosystem corroboration (what other projects did): datahub's `core/gold-prices`
fell back to **monthly averages** (World Bank Pink Sheet) after the Timothy
Green historical PDF went behind a login; its updater runs daily but can only
refresh averages. Free daily fix data, post-Feb-2026, exists nowhere maintained.

## What IS alive (probed 2026-10-12)

- **Yahoo `GC=F`** COMEX front-month close — daily, current to today; from 2000-09.
- **Yahoo `GLD`** adj close (NAV total-return proxy, ~0.4%/yr expense drag) —
  daily, current to today; from 2004-12.
- **World Bank Pink Sheet** monthly *average* USD/oz (CC BY 4.0), current;
  mirrors: eco3min.fr CSV (0.0% dev vs xlsx, current to 2026-09) and
  datahub `core/gold-prices` (updated 2026-10-04). Averages — cross-check only,
  not signal-grade.

## Our gold-leg architecture (adopted 2026-10-12)

1. **History 1968-04 → 2026-02:** frozen mirror above. Immutable by
   construction (sha-pinned); triple-validation vs the FRED-era dump (0.0004%
   mean dev), Pink Sheet monthly means (0.06% median), and GC=F month-ends was
   recorded 2026-10-12 and is re-runnable from the fetch script.
2. **Live extension 2026-03 →:** month-end signals computed on **GLD total
   returns** (primary; cleanest spot proxy that is current and daily), with
   **GC=F month-ends** as second opinion. Splice is **ratio-normalized at the
   seam** — same treatment as Shiller↔Yahoo for SPX — and studies run on
   within-series returns, never raw spliced levels.
3. **Cross-check every month:** composite month vs Pink Sheet monthly average;
   flag if |deviation| > 1%.

Basis, measured (month-end GC=F vs frozen fix, 2000-10→2026-01, 260 months):
median 0.36%, p90 1.21%, **max 4.75% at 2026-01** — the seam window IS the
worst basis month in the record (spot outran futures in the Jan-2026 squeeze),
which is why naive level-splicing is banned and the cross-check is mandatory.

Extension-leg fidelity (measured 2026-10-12): monthly GLD-TR vs fix returns
over 2004-12→2026-02 (254 mo): **corr 0.974**, |diff| median 0.55%, p90 1.79%.
Part of this gap is structural timing, not error: the fix prices London 15:00
while GC=F/GLD price the NY 16:00 close — any proxy we can get free prices a
different clock. Treat sub-~1%/month proxy-vs-fix differences as the noise
floor when reading gold-leg results.

## Constraints accepted

- True **daily** PM fixes after 2026-02 are unavailable free: daily-MA /
  whipsaw legs extend on GLD/GC=F basis, documented per study. Full-history
  daily remains frozen history only.
- The honest fix-grade continuation is a **paid licensed feed** (metals-api /
  MetalPriceAPI / EODHD XAU.USD class, ~$20–50/mo). Not adopted yet — decision
  point if a verdict ever hinges on fix-vs-proxy fidelity after Feb-2026.
- Vendor numbers quoted from sources that used LBMA fixes (Returnstream,
  QuantifiedStrategies) stay recorded as attributed facts; our replications run
  on the composite above.

## Cite as

`entities/lbma-gold-price.md` — gold-leg source hierarchy + frozen-history pin.
Update `updated:` and append a dated status line here whenever a feed's state
changes; fetch-script headers in receipts-lab mirror this page.
