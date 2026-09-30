# Claim vs Implementation — DuvvuruDeepakReddy18_AyuTrial

**Repository:** `DuvvuruDeepakReddy18_AyuTrial`
**Generated:** 2026-09-30
**Evidence hierarchy:** code > config > schema > tests > docs > README

See `analysis/DuvvuruDeepakReddy18_AyuTrial/REPO_ANALYSIS.md:21` for full feature table (21 features). This file summarizes major claims from presentation docs vs actual code.

| Claim | Source (presentation) | Actual code evidence | Relevant files | Status |
|---|---|---|---|---|
| 21 CFR-like audit | README | audit via `src/lib/crypto.ts:1` local hash, not WORM | `src/app/audit-logs/page.tsx:1` | **MOCKED** (localStorage) |
| ABDM integration readiness | README + interoperability page | No adapter code, blueprint matrix only | `src/app/interoperability/page.tsx:1` | **CLAIMED ONLY** (blueprint) |
| NPvCC apex + 24h SAE clock | README + pharmacovigilance page | `src/app/pharmacovigilance/new/page.tsx:1` 22KB SAE form WHO-UMC | `src/lib/mockData.ts:1` | **IMPLEMENTED** (NPvCC strongest) |

> Use `analysis/COMPETITOR_MATRIX.md:1` for full status per feature. Example above shows critical claims.
