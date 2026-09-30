# Claim vs Implementation — AnushkaTadiyal_aiia-ctms

**Repository:** `AnushkaTadiyal_aiia-ctms`
**Generated:** 2026-09-30
**Evidence hierarchy:** code > config > schema > tests > docs > README

See `analysis/AnushkaTadiyal_aiia-ctms/REPO_ANALYSIS.md:21` for full feature table (21 features). This file summarizes major claims from presentation docs vs actual code.

| Claim | Source (presentation) | Actual code evidence | Relevant files | Status |
|---|---|---|---|---|
| 21 CFR Part 11 compliant | README.md:1 | Auth: bcryptjs+JWT only, no WORM/eSign, AuditPage no hash | `server/package.json:1`, `server/routes/audit.js:1` | **CLAIMED ONLY** |
| CTRI integration | README.md | No CTRI file, no scrape | rglob CTRI 0 hits | **CLAIMED ONLY** |

> Use `analysis/COMPETITOR_MATRIX.md:1` for full status per feature. Example above shows critical claims.
