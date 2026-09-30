# Claim vs Implementation — nishant-uxs_vedraya

**Repository:** `nishant-uxs_vedraya`
**Generated:** 2026-09-30
**Evidence hierarchy:** code > config > schema > tests > docs > README

See `analysis/nishant-uxs_vedraya/REPO_ANALYSIS.md:21` for full feature table (21 features). This file summarizes major claims from presentation docs vs actual code.

| Claim | Source (presentation) | Actual code evidence | Relevant files | Status |
|---|---|---|---|---|
| GLOBAL SHA-256 hash chain | README.md + docs/AUDIT.md | `server/src/modules/audit/service.ts:1` + verify endpoint + 46/46 tests tamper→valid:false | `server/tests/api.audit.integrity.test.ts:1` | **IMPLEMENTED** (not WORM) |
| Licensed MedDRA | Not claimed (honest) | `MEDDRA_DEMO` demo dictionary, LIMITATIONS says not licensed | `server/src/modules/coding/routes.ts:1` | **PARTIALLY IMPLEMENTED** (demo) |
| ABDM integrated | Not claimed (honest NOT CONNECTED) | `/interop/adapters` NOT CONNECTED | `server/src/modules/interop/*` | **NOT PRESENT** (honest) |

> Use `analysis/COMPETITOR_MATRIX.md:1` for full status per feature. Example above shows critical claims.
