# Claim vs Implementation — vansh459_AyuSphere

**Repository:** `vansh459_AyuSphere`
**Generated:** 2026-09-30
**Evidence hierarchy:** code > config > schema > tests > docs > README

See `analysis/vansh459_AyuSphere/REPO_ANALYSIS.md:21` for full feature table (21 features). This file summarizes major claims from presentation docs vs actual code.

| Claim | Source (presentation) | Actual code evidence | Relevant files | Status |
|---|---|---|---|---|
| AI-assisted extraction | README.md + docs/architecture.md | `src/app/api/ai/extract/route.ts:1` + tests 11KB mocked | `tests/extraction.test.ts:1` | **IMPLEMENTED** (external LLM, not trained model) |
| CTRI real scrape | docs + scripts | `scripts/scrape/ctri_scrape.py:1` crawl4ai + seed-real idempotent | `src/db/seed-real.ts` | **IMPLEMENTED** |
| FHIR R4 | README | `src/app/api/fhir/Bundle/[trialId]/route.ts:1` + fhir-api.test.ts 8KB | `src/app/api/fhir/*` | **IMPLEMENTED** |

> Use `analysis/COMPETITOR_MATRIX.md:1` for full status per feature. Example above shows critical claims.
