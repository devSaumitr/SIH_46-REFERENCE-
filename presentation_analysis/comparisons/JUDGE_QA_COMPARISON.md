# Judge Q&A Comparison — Across 7 Competitors

**Generated:** 2026-09-30
**Evidence:** `analysis/*/JUDGE_QA_ANALYSIS.md:1` + raw `JUDGE_QA.md` / `Tech_Security_Guide.md`
**Do NOT rank.**

## Matrix

| Category | nishant-uxs_vedraya (JUDGE_QA.md 3.5KB) | vansh459_AyuSphere (Tech_Security_Guide.md 17KB + 155KB pdf) | DuvvuruDeepakReddy18_AyuTrial | aravindakrishna-c_AIIA-Clinical-Trial-Dashboard | AnushkaTadiyal_aiia-ctms | rimi007-grt_AIIA-CTMS | kalyan-2006-prog_SIH26046-DEV-RUSH- |
|---|---|---|---|---|---|---|---|
| **Technical (auth, API, DB)** | Q: How does auth work? A: Argon2 + sid HttpOnly + CSRF + RBAC 7 + ACL (studyAccess.ts) — evidence 46/46 tests; Q: API rate limiting? A: pluggable limiter | Q: Auth? A: Auth.js v5 JWT 7 roles, regulator read-only (regulator.test.ts) — evidence 157 tests | Q: Auth? A: persona switcher (mock, no password) — actual: not real auth | Q: Auth? A: PyJWT HS256 + passlib — evidence backend/app/core/security.py:1 | Q: Auth? A: JWT bcryptjs — no ACL, no tests | Same as Anushka | Not present — no auth file |
| **Clinical (trial, Ayush)** | Q: Multi-centre? A: study_sites + study_memberships ACL (monitor AYU-024 only) — IMPLEMENTED | Q: Trial lifecycle? A: lifecycle state machine (lifecycle.test.ts) — IMPLEMENTED | Q: Ayurveda fields? A: Prakriti/Agni/Koshtha in visits — IMPLEMENTED as data | Not found | Not found | Not found | Not found |
| **Regulatory (CTRI, NDCT, GCP, 21 CFR)** | Q: 21 CFR Part 11 compliant? A: No — prototype only, no WORM/eSign, LIMITATIONS says not certified — honest | Q: CTRI? A: Real scrape via ctri_scrape.py + seed-real idempotent — IMPLEMENTED (not official API) | Q: 21 CFR? A: Disclaimer prototype requires validation | Not found | CLAIMED ONLY but no code for WORM — overclaim flagged | Same as Anushka | Not found |
| **AI** | Q: AI? A: Not present — honest | Q: AI? A: Claude extract + Groq Copilot, mocked in tests, PI approve gate | Q: AI? A: WHO-UMC rule-based, not AI | Not found | Not found | Not found | Not found |
| **Security (audit, hash, RBAC)** | Q: Immutable audit? A: GLOBAL SHA-256 chain, verify endpoint valid:false on tamper (audit.integrity.test.ts) — IMPLEMENTED, not WORM | Q: Audit? A: insert-only audit + withAudit atomic, signatures.test.ts — IMPLEMENTED | Q: Audit? A: local SHA-256 via crypto.ts, not WORM — MOCKED | Q: Audit? A: audit_logs.py — basic, not immutable | Q: Audit? A: AuditPage — no hash | Q: Audit? A: AuditPage 33KB — no hash | Q: Audit? A: audit-log route 3.1KB — partial |
| **Architecture** | Q: ABDM/HIS/EDC integrated? A: NOT CONNECTED (interop/adapters) — honest | Q: ABDM? A: Not present (no adapter) | Q: ABDM? A: blueprint readiness (claim) — no adapter | Not found | Not found | Q: AWS Cloud? A: modal mocked | Not found |
| **Data (synthetic vs real, DPDP)** | Q: Real patient? A: Synthetic only, de-identified (password Vedraya!Demo1, synthetic AYU-*) | Q: Real data? A: trials real CTRI public, participants synthetic (no identifier cols by schema, DPDP) | Q: Data? A: synthetic DEMO-0001, no PHI | Q: Data? A: synthetic via init_db 60KB | Q: Data? A: synthetic via seed 24/30 | Same | Unknown |
| **Interoperability (FHIR/CDISC)** | Q: FHIR/CDISC certified? A: prototype (FHIR R4 ResearchStudy/Subject, SDTM-like AE), not certified | Q: FHIR/CDISC? A: Bundle + SDTM IMPLEMENTED, fhir-api.test 8KB | Q: FHIR/CDISC? A: prototype bundles, not certified | Q: FHIR? A: fhir.py 2.5KB stub | Not found | Not found | Q: FHIR/CDISC? A: stubs 6-12KB PARTIALLY |
| **Deployment** | Q: Where hosted? A: Vercel SPA only (API+Postgres separate, render.yaml) — SPA claim | Q: Where? A: Vercel + Neon Postgres serverless + PGlite no Docker | Q: Where? A: Vercel ayutrial-ctms READY | Q: Where? A: Docker + compose + render + vercel | Q: Where? A: no deploy files | Q: Where? A: Dockerfile + apprunner.yaml | Q: Where? A: Vercel demo claimed |
| **Innovation/Demo** | Q: What differentiator? A: Auditable RBAC + ACL + hash chain verify + traceability | Q: Differentiator? A: Test-gated, PGlite no Docker, AI grounded Copilot | Q: Differentiator? A: NPvCC apex + 28 routes | Not found | Not found | Not found | Not found |
| **Has judge file** | YES (JUDGE_QA.md 3.5KB) | PARTIALLY (Tech_Security_Guide 17KB as judge-facing security Q&A) | NO | NO | NO | NO | NO |

> **Common question themes across repos with judge material:** WORM? licensed MedDRA? FHIR/CDISC certified? ABDM connected? Real patient data? Hosted where? Only vedraya explicitly anticipates all via LIMITATIONS/JUDGE_QA; AyuSphere anticipates via Tech_Security_Guide.

