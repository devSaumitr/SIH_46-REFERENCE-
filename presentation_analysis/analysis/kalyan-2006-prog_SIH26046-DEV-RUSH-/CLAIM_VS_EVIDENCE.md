# Claim vs Implementation — kalyan-2006-prog_SIH26046-DEV-RUSH-

**Repository:** `kalyan-2006-prog_SIH26046-DEV-RUSH-`
**Generated:** 2026-09-30
**Evidence hierarchy:** code > config > schema > tests > docs > README

See `analysis/kalyan-2006-prog_SIH26046-DEV-RUSH-/REPO_ANALYSIS.md:21` for full feature table (21 features). This file summarizes major claims from presentation docs vs actual code.

| Claim | Source (presentation) | Actual code evidence | Relevant files | Status |
|---|---|---|---|---|
| FHIR ingest/export | README (implied) | `devrush-ctms/app/api/fhir/ingest/route.ts:1` 12.5KB + export 8KB | `lib/schema.ts:1` 13.7KB | **PARTIALLY IMPLEMENTED** (stubs, 5 commits) |
| SDTM/ADaM/Define | routes exist | 6-9KB stubs, no tests | `app/api/sdtm/export/route.ts:1` | **PARTIALLY IMPLEMENTED** |

> Use `analysis/COMPETITOR_MATRIX.md:1` for full status per feature. Example above shows critical claims.
