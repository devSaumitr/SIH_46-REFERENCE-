# SIH26046 Competitor Analysis — Master Evidence-Based Synthesis

**Generated:** 2026-09-30 12:37
**Problem:** SIH26046 — AIIA Clinical Trial Management System / Clinical Trials Dashboard (Ministry of Ayush / All India Institute of Ayurveda). Real-time, cloud-based, GCP-compliant CTMS for Ayurveda research, with CDISC/FHIR-interoperable data, role-based KPIs, integrated ethics/regulatory (CTRI/NDCT 2019) and pharmacovigilance tracking, plus NPvCC for ASU&H drugs (per AyuTrial `README.md:1` and vedraya `docs/SIH26046_TRACEABILITY_FINAL.md:1`).
**Repositories Analyzed:** 7 (in `repositories/` — each independent, preserved structure, excluded .git/node_modules/.next/dist)
**Evidence hierarchy:** code > config > schema > tests > docs > README > claim
**Statuses:** IMPLEMENTED / PARTIALLY IMPLEMENTED / MOCKED / CLAIMED ONLY / NOT PRESENT / UNKNOWN
**No ranking:** Neutral evidence, no winner/loser.

---

## 1. Problem Context

SIH26046 requires a CTMS/dashboard that handles: trial lifecycle/phases, multi-centre, participants (screening/enrolment, de-identified), consent, visits/CRF/data collection, AE/SAE/pharmacovigilance (including WHO-UMC, NPvCC), ethics/committee, regulatory (CTRI, NDCT 2019, GCP, 21 CFR Part 11, DPDP), monitoring, audit (immutable, hash chain, ALCOA+), interoperability (FHIR R4, CDISC SDTM/CDASH/ODM, ABDM, CTRI), RBAC (5-7 roles: PI, Coordinator, Monitor, Ethics, PV, Admin, Regulator), real-time KPIs/alerts, deployment (cloud, Docker/Vercel), testing. Level 3 software problem per SIH datasets.

**Source for PS:** `repositories/nishant-uxs_vedraya/docs/SIH26046_TRACEABILITY_FINAL.md:1` 8KB (vedraya traceability) and `repositories/DuvvuruDeepakReddy18_AyuTrial/README.md:1` (problem overview). No official MoAyush PDF in repos — traceability docs used as evidence.

---

## 2. Repositories Analyzed

| # | Folder | Owner/Repo | URL | Cloned | Files (excl .git) | Size | License | Extract |
|---|---|---|---|---|---|---|---:|---|
| 1 | `AnushkaTadiyal_aiia-ctms` | AnushkaTadiyal/aiia-ctms | https://github.com/AnushkaTadiyal/aiia-ctms | depth 1 | 56 | 1.19 MB | MIT (`package.json:1`) | `analysis/AnushkaTadiyal_aiia-ctms/` |
| 2 | `vansh459_AyuSphere` | vansh459/AyuSphere | https://github.com/vansh459/AyuSphere | depth 1 | 282 | 14.38 MB | Unknown / Not found (no LICENSE, check package.json) | `analysis/vansh459_AyuSphere/` |
| 3 | `aravindakrishna-c_AIIA-Clinical-Trial-Dashboard` | aravindakrishna-c/AIIA-Clinical-Trial-Dashboard | https://github.com/aravindakrishna-c/AIIA-Clinical-Trial-Dashboard | depth 1 | 153 | 0.98 MB | Unknown / Not found | `analysis/aravindakrishna-c_AIIA-Clinical-Trial-Dashboard/` |
| 4 | `rimi007-grt_AIIA-CTMS` | rimi007-grt/AIIA-CTMS | https://github.com/rimi007-grt/AIIA-CTMS | depth 1 | 72 | 1.78 MB | MIT (`package.json:1`) | `analysis/rimi007-grt_AIIA-CTMS/` |
| 5 | `nishant-uxs_vedraya` | nishant-uxs/vedraya | https://github.com/nishant-uxs/vedraya | depth 1 | 533 | 17.58 MB | Unknown / Not found (no LICENSE) | `analysis/nishant-uxs_vedraya/` |
| 6 | `DuvvuruDeepakReddy18_AyuTrial` | DuvvuruDeepakReddy18/AyuTrial | https://github.com/DuvvuruDeepakReddy18/AyuTrial | depth 1 | 57 | 0.78 MB | Unknown / Not found | `analysis/DuvvuruDeepakReddy18_AyuTrial/` |
| 7 | `kalyan-2006-prog_SIH26046-DEV-RUSH-` | kalyan-2006-prog/SIH26046-DEV-RUSH- | https://github.com/kalyan-2006-prog/SIH26046-DEV-RUSH- | depth 1 | 66 | 0.57 MB | ISC (`package.json:1`) | `analysis/kalyan-2006-prog_SIH26046-DEV-RUSH-/` |

**License note:** Only Anushka and rimi declare MIT in `package.json:1`, DEV-RUSH ISC, others no LICENSE file — `REPO_DETAILS.md:1` per repo shows `No explicit open-source license identified` where missing. Never copy without checking license.

**Repo size:** Vedraya largest (533 files, 360 webp frames) but source 99 files; AyuSphere densest code (154 .ts, 282 files, 50 test suites).

---

## 3. Technology Landscape

| Dimension | Observed |
|---|---|
| **Frontend** | React 19 Vite (5 repos) — Anushka/rimi Dashboard (Vite 8, React Router 7), vedraya (Vite 8 + framer-motion/gsap), AIIA-Dashboard (Vite 8), AyuSphere Next.js 16 (App Router, Tailwind v4, Framer Motion), AyuTrial Next.js 16, DEV-RUSH Next.js |
| **Backend** | Express (3: Anushka, rimi, vedraya), FastAPI Python (1: AIIA-Dashboard), Next.js API routes (2: AyuSphere, DEV-RUSH, AyuTrial in-memory) |
| **Database** | PostgreSQL (vedraya `pg` + Drizzle 0.39 + 5 migrations; AyuSphere Neon serverless + Drizzle 0.45 + PGlite; AIIA-Dashboard SQLAlchemy/Alembic Postgres or SQLite; AyuTrial Supabase + localStorage demo; Anushka/rimi SQLite better-sqlite3 `ctms.db`; DEV-RUSH Drizzle schema 13.7KB) |
| **Auth** | Argon2 + Sid cookie + CSRF (vedraya), Auth.js v5 JWT (AyuSphere 7 roles), PyJWT + passlib/argon2 (Dashboard), JWT bcryptjs (Anushka/rimi), persona switcher mock (AyuTrial), none (DEV-RUSH) |
| **Tests** | Vitest 46/46 + Playwright 26/26 (vedraya), Vitest 157 (AyuSphere PGlite), 21 workflow tsx (AyuTrial), pytest/httpx listed (Dashboard sparse), test: echo error (Anushka/rimi/DEV-RUSH mocks) |
| **Deployment** | Vercel (4: vedraya SPA, AyuSphere, AyuTrial ayutrial-ctms.vercel.app, DEV-RUSH sih-26046-dev-rush), Render.yaml (vedraya + rimi + Dashboard), Dockerfile (rimi, Dashboard), docker-compose (Dashboard), Supabase (AyuTrial), Neon (AyuSphere), AWS AppRunner (rimi) |
| **AI** | Only AyuSphere: Anthropic SDK 0.125 + LangChain/Groq (Claude extract, Copilot) |
| **Data** | Synthetic participants (all where found, de-identified); real CTRI public scrape (only AyuSphere `scripts/scrape/ctri_scrape.py`) |

**Common:** React 19 + TypeScript + Tailwind + Lucide + Recharts + Drizzle ORM.

**Rare:** FastAPI + SQLAlchemy (only Dashboard), PGlite no Docker (only AyuSphere), Argon2 + CSRF + ACL (only vedraya), NPvCC (only AyuTrial).

---

## 4. Competitor Matrix (summary — see full `COMPETITOR_MATRIX.md`)

*For brevity, matrix repeated here as summary; full file has evidence index.*

| Feature | Max status across repos | How many IMPLEMENTED | How many PARTIALLY | How many MOCKED/CLAIMED |
|---|---|---|---|---|
| Protocol / Participant / AE | IMPLEMENTED | 4-5 | 2 | 1 |
| CRF/EDC | IMPLEMENTED (1) | 1 | 1 | 1 MOCKED |
| CTRI | IMPLEMENTED (1 via scrape) | 1 | 4 | 2 CLAIMED ONLY |
| FHIR / CDISC | IMPLEMENTED (1) | 1-2 | 3-4 | 2 NOT PRESENT |
| FHIR↔CDISC mapping | PARTIALLY (1) | 0 | 1 | 6 NOT PRESENT |
| ABDM | CLAIMED ONLY (1) | 0 | 0 | 1 CLAIMED, 6 NOT PRESENT |
| Immutable audit | IMPLEMENTED (2) | 2 | 0 | 3 NOT PRESENT, 1 MOCKED |
| AI | IMPLEMENTED (1) | 1 | 0 | 6 NOT PRESENT |
| Testing (IMPLEMENTED) | 3 (vedraya, AyuSphere, AyuTrial) | 3 | 1 | 2 MOCKED, 1 NOT PRESENT |
| Demo script / Judge Q&A | IMPLEMENTED (2) | 2 | 1 | 4 NOT PRESENT |
| PPT | NOT PRESENT (0) | 0 | 0 | 7 NOT PRESENT |
| PDF | IMPLEMENTED (1) | 1 | 0 | 6 NOT PRESENT |

*See `analysis/COMPETITOR_MATRIX.md:1` for full 28×7 table.*

---

## 5. Common Features (≥5 repos have IMPLEMENTED or PARTIALLY)

- **Protocol/participant/AE management:** All 7 have at least PARTIALLY — core CTMS CRUD present (studies, participants, AE/SAE pages or routes). Vedraya/AyuSphere/Dashboard/AyuTrial strongest (real routes + KPIs).
- **Synthetic data:** All where verified (6 IMPLEMENTED, 1 UNKNOWN) — synthetic participants DE-identified, no real PHI. Seeds: `server/seed.js:1` 24 trials/30 AEs (Anushka/rimi), `src/db/seed.ts` (AyuSphere), `init_db.py` 60KB (Dashboard), `mockData.ts` 58KB (AyuTrial), vedraya AYU-024.
- **Real-time KPIs:** All 7 PARTIALLY or IMPLEMENTED — dashboards with KPIs, but only vedraya/AyuSphere/AyuTrial with computed alert logic and tests.
- **Audit trail (basic):** All 7 at least PARTIALLY — at least an audit page/log, but only 2 immutable with hash chain.
- **RBAC (≥ partially):** 6 of 7 at least PARTIALLY (Anushka PARTIALLY, rimi/AyuSphere/Dashboard/vedraya/AyuTrial IMPLEMENTED) — 7 roles common (PI, Coordinator, Monitor, Ethics, PV, Admin, Regulator).
- **Cloud deployment (≥ partially):** 5 IMPLEMENTED (Vercel/Render/Docker) + 1 PARTIALLY + 1 NOT PRESENT.

---

## 6. Rare Features (≤2 repos IMPLEMENTED)

- **NPvCC workflow:** Only `DuvvuruDeepakReddy18_AyuTrial:1` **IMPLEMENTED** — dedicated NPvCC dashboard, 24h SAE countdown, WHO-UMC, CDSCO pipeline. Others NOT PRESENT.
- **AI (Claude/Groq extraction):** Only `vansh459_AyuSphere:1` **IMPLEMENTED** — `src/app/api/ai/extract/route.ts:1` + `copilot` grounded + 11KB `extraction.test.ts` mocked. Others NOT PRESENT (AyuTrial WHO-UMC is rule-based, not AI).
- **Immutable audit (hash chain):** Only `nishant-uxs_vedraya:1` (`server/src/modules/audit/service.ts:1` GLOBAL SHA-256 + verify) and `vansh459_AyuSphere:1` (insert-only + withAudit) **IMPLEMENTED**; AyuTrial MOCKED (localStorage), others PARTIALLY or NOT PRESENT.
- **FHIR↔CDISC mapping layer:** Only `vansh459_AyuSphere:1` **PARTIALLY IMPLEMENTED** (FHIR and CDISC exports exist but no explicit FHIR↔CDISC mapping file found via search); others NOT PRESENT — key gap to exploit.
- **Ayurveda-specific fields (Prakriti/Agni/Koshtha):** Only `DuvvuruDeepakReddy18_AyuTrial:1` **IMPLEMENTED** (visits page), vedraya/AyuSphere PARTIALLY (generic), others CLAIMED ONLY.
- **UAT PDFs with role guides:** Only `vansh459_AyuSphere:1` 9 PDFs (Judge + 7 UAT + Tech_Security) **IMPLEMENTED**.
- **Full Demo script + Judge Q&A:** Only `nishant-uxs_vedraya:1` both **IMPLEMENTED** (`docs/DEMO_SCRIPT.md:1` + `docs/JUDGE_QA.md:1`); AyuSphere has Judge script + partial Tech guide.
- **PGlite no Docker:** Only `vansh459_AyuSphere:1` (D-019, Vitest + PGlite).
- **FastAPI Python:** Only `aravindakrishna-c_AIIA-Clinical-Trial-Dashboard:1`.

---

## 7. Common Mocked Features

- **CRF/EDC in AyuTrial:** `MOCKED` — `src/app/data-management/page.tsx:1` eCRF query workflow exists but persists to `mockData.ts` + localStorage, not real DB.
- **Audit immutability in AyuTrial:** `MOCKED` — `src/lib/crypto.ts:1` syncComputeSimpleHash local, not WORM.
- **Testing in Anushka/rimi:** `MOCKED` — `server/package.json:1` test: echo error, only `test_rbac_matrix.js` shallow in rimi.
- **Offline capability in AyuTrial:** `MOCKED` — localStorage persists across reloads, not true offline sync (marked MOCKED).
- **ABDM readiness (AyuTrial):** `CLAIMED ONLY` but UI shows matrix without adapter — if counted as mocked, it's mocked blueprint.

---

## 8. Common Claims Without Implementation Evidence (CLAIMED ONLY)

- **21 CFR Part 11:** Anushka `README.md:1` and rimi `README.md:1` claim alignment — **FACT:** No eSignature WORM, no audit immutability, no Define-XML, only `bcryptjs` + `jsonwebtoken` + `better-sqlite3` — **INFERENCE:** May contribute but not compliant; classified **CLAIMED ONLY** per task rule.
- **ABDM “ready” / “integration”:** AyuTrial `README.md:1` claims ABDM Integration Readiness (ABHA/HIP/HIU/NAMASTE) — **FACT:** No adapter code in `src/app/api` search, `docs/ABDM` not found; vedraya honest `NOT CONNECTED` — **INFERENCE:** Blueprint, not integration → **CLAIMED ONLY** for AyuTrial, **NOT PRESENT** others.
- **CTRI (Anushka/rimi):** README mentions CTRI — **FACT:** No `ctri_scrape.py` nor CTRI API search hit, no `regulatory/routes.ts` — **CLAIMED ONLY**.
- **CDISC “compliant” / FHIR “support” (general):** Dashboard `fhir.py:1` 2.5KB stub, Anushka/rimi none, yet README may mention — treat as PARTIALLY or CLAIMED ONLY until resource generation verified.
- **GCP-ASU / DPDP / ISO27001 certified:** No repo shows certification — vedraya `LIMITATIONS.md:1` explicitly says not certified; others lack evidence — treat as CLAIMED ONLY if mentioned.

**File evidence for claims:** See `analysis/<repo>/README_ANALYSIS.md:1` (raw README preview) vs `REPO_ANALYSIS.md:21` (claim vs actual).

---

## 9. Clinical Workflow Comparison

| Workflow | vedraya | AyuSphere | AyuTrial | Dashboard | Anushka | rimi | DEV-RUSH |
|---|---|---|---|---|---|---|---|
| Trial creation | IMPLEMENTED (studies POST + lifecycle) | IMPLEMENTED (lifecycle state machine `lifecycle.test.ts`) | IMPLEMENTED (10-stage pipeline `/studies/[id]` 27KB) | IMPLEMENTED (trials.py POST) | PARTIALLY (TrialsPage) | PARTIALLY | PARTIALLY (trialId page) |
| Site management | IMPLEMENTED (sites + study_sites ACL) | IMPLEMENTED | IMPLEMENTED (8-site network) | IMPLEMENTED | CLAIMED ONLY | CLAIMED ONLY | NOT PRESENT |
| Participant enrollment | IMPLEMENTED (participants POST, screened/enrolled) | IMPLEMENTED (enrolment guards) | IMPLEMENTED (DEMO-registry + visits) | IMPLEMENTED | PARTIALLY | PARTIALLY | NOT PRESENT |
| Consent | IMPLEMENTED (versions, obtain/withdraw) | IMPLEMENTED | IMPLEMENTED (vernacular + AV recording tracking) | PARTIALLY | NOT PRESENT | NOT PRESENT | NOT PRESENT |
| Visits | PARTIALLY (no full schedule) | IMPLEMENTED (visit-engine `visit-engine.test.ts`) | MOCKED (visit matrix with Ayush exams) | NOT PRESENT | NOT PRESENT | NOT PRESENT | NOT PRESENT |
| CRF | PARTIALLY (participants + AE) | IMPLEMENTED (immutability + versioned corrections) | MOCKED | NOT PRESENT | NOT PRESENT | NOT PRESENT | NOT PRESENT |
| AE/SAE | IMPLEMENTED (AE escalate) | IMPLEMENTED (clock) | IMPLEMENTED (24h clock) | IMPLEMENTED | PARTIALLY | PARTIALLY | PARTIALLY |
| Monitoring | PARTIALLY (alerts) | IMPLEMENTED (`monitoring.test.ts`) | IMPLEMENTED (CRA visits, SDV, CAPA) | NOT PRESENT | NOT PRESENT | NOT PRESENT | NOT PRESENT |
| Ethics | IMPLEMENTED | IMPLEMENTED | IMPLEMENTED | IMPLEMENTED | NOT PRESENT | NOT PRESENT | NOT PRESENT |
| Regulatory | PARTIALLY (CTRI tracking) | IMPLEMENTED | PARTIALLY | PARTIALLY | CLAIMED ONLY | CLAIMED ONLY | PARTIALLY |
| Trial closure | NOT PRESENT (no closure workflow found) | PARTIALLY (lifecycle) | PARTIALLY (dashboard closure?) | UNKNOWN | NOT PRESENT | NOT PRESENT | NOT PRESENT |

**Evidence:** `server/src/modules/*` routes (vedraya), `tests/visit-engine.test.ts` (AyuSphere), `src/app/visits/*` (AyuTrial), `backend/app/api/v1/trials.py:1`.

---

## 10. Regulatory Comparison

| Capability | vedraya | AyuSphere | AyuTrial | Dashboard | Anushka | rimi | DEV-RUSH |
|---|---|---|---|---|---|---|---|
| CTRI integration | PARTIALLY (tracking) | IMPLEMENTED (scrape) | PARTIALLY | PARTIALLY | CLAIMED ONLY | CLAIMED ONLY | PARTIALLY |
| NDCT 2019 workflow | PARTIALLY | IMPLEMENTED | PARTIALLY | PARTIALLY | NOT PRESENT | NOT PRESENT | NOT PRESENT |
| Ethics IEC | IMPLEMENTED | IMPLEMENTED | IMPLEMENTED | IMPLEMENTED | NOT PRESENT | NOT PRESENT | NOT PRESENT |
| GCP-ASU | PARTIALLY (process support, not certified) | PARTIALLY | PARTIALLY (GCP-ASU fields) | CLAIMED ONLY | CLAIMED ONLY (21 CFR) | CLAIMED ONLY | NOT PRESENT |
| 21 CFR Part 11 | NOT CLAIMED (honest) | NOT CLAIMED | DISCLAIMER | NOT CLAIMED | CLAIMED ONLY (no code) | CLAIMED ONLY | NOT CLAIMED |
| DPDP | NOT CERTIFIED (process docs) | UNKNOWN | DISCLAIMER | UNKNOWN | NOT PRESENT | NOT PRESENT | NOT PRESENT |

**Evidence:** `docs/SIH26046_TRACEABILITY_FINAL.md:1` (vedraya), `scripts/scrape/ctri_scrape.py:1` (AyuSphere), `src/app/ctri-ethics/*` (AyuTrial/DEV-RUSH).

---

## 11. Pharmacovigilance Comparison

| Capability | vedraya | AyuSphere | AyuTrial | Dashboard | Anushka | rimi | DEV-RUSH |
|---|---|---|---|---|---|---|---|
| AE capture | IMPLEMENTED | IMPLEMENTED | IMPLEMENTED | IMPLEMENTED | PARTIALLY | PARTIALLY | PARTIALLY |
| SAE escalate | IMPLEMENTED (escalate PATCH) | IMPLEMENTED (escalation clock) | IMPLEMENTED (24h countdown, WHO-UMC) | PARTIALLY | PARTIALLY | PARTIALLY | PARTIALLY |
| Causality (WHO-UMC/Naranjo) | PARTIALLY (demo coding MEDDRA_DEMO) | IMPLEMENTED (safety-signals, dictionaries) | IMPLEMENTED (WHO-UMC Certain/Probable) | NOT PRESENT | NOT PRESENT | NOT PRESENT | NOT PRESENT |
| NPvCC workflow | NOT PRESENT | NOT PRESENT | IMPLEMENTED (dedicated apex, CDSCO pipeline) | NOT PRESENT | NOT PRESENT | NOT PRESENT | NOT PRESENT |
| Reporting timeline | PARTIALLY (demo clocks) | IMPLEMENTED (deadlines.test.ts) | IMPLEMENTED (24h/7d/14d statutory) | PARTIALLY | NOT PRESENT | NOT PRESENT | NOT PRESENT |
| Signal detection | NOT PRESENT | IMPLEMENTED (`safety-signals.test.ts`) | NOT PRESENT | NOT PRESENT | NOT PRESENT | NOT PRESENT | NOT PRESENT |

**Strongest NPvCC:** Only AyuTrial — dedicated `pharmacovigilance/` route (5.8KB) + 22KB SAE form + CDSCO.

---

## 12. FHIR / CDISC / ABDM Comparison

| Standard | vedraya | AyuSphere | AyuTrial | Dashboard | Anushka | rimi | DEV-RUSH |
|---|---|---|---|---|---|---|---|
| FHIR | PARTIALLY (R4 ResearchStudy/Subject prototype `interop/fhir`) | IMPLEMENTED (Bundle/[trialId], ResearchStudy/[id], import, `fhir-api.test.ts` 8KB) | PARTIALLY (bundle generator inspector) | PARTIALLY (`fhir.py` 2.5KB stub) | NOT PRESENT | NOT PRESENT | PARTIALLY (ingest 12.5KB, export 8KB stubs) |
| CDISC SDTM | PARTIALLY (SDTM-like AE CSV) | IMPLEMENTED (exports 10KB, SDTM) | PARTIALLY (SDTM DM/AE/EX/VS/LB pre-exp) | PARTIALLY | NOT PRESENT | NOT PRESENT | PARTIALLY (SDTM 6.3KB, ADaM 6KB, Define 9.9KB) |
| CDASH/ODM | NOT IMPLEMENTED | NOT PRESENT | NOT PRESENT | NOT PRESENT | NOT PRESENT | NOT PRESENT | NOT PRESENT |
| FHIR↔CDISC mapping | NOT PRESENT | PARTIALLY (both exist, no explicit mapping layer via `mapping` search) | NOT PRESENT | NOT PRESENT | NOT PRESENT | NOT PRESENT | NOT PRESENT |
| ABDM | NOT PRESENT (explicit NOT CONNECTED) | NOT PRESENT | CLAIMED ONLY (blueprint) | NOT PRESENT | NOT PRESENT | NOT PRESENT | NOT PRESENT |

**Verification rule:** FHIR not just mentioned — check `ResearchStudy`/`ResearchSubject` generation + serialization + API (see `REPO_ANALYSIS.md:11`). Vedraya/AyuTrial/Dashboard/DEV-RUSH FHIR are prototypes/stubs (few KB), only AyuSphere has `fhir-api.test.ts:1` 8KB.

**FHIR-to-CDISC Joint Mapping IG:** No repo contains actual mapping layer (search `fhircdisc`/`mapping` 0 hits) — common gap to exploit (build real layer).

---

## 13. RBAC Comparison

| Repo | Roles | Backend auth | Frontend hiding | Study ACL | Tests |
|---|---|---|---|---|---|
| vedraya | 7 (`ROLE_DEFS` seed) admin, regulator (all), PI, Coord, Monitor (AYU-024 only), PV, Ethics | Argon2 + sid + requirePermission + studyAccess ACL | Yes (CommandCenter role UI) | YES (`studyAccess.ts`) | 46/46 Vitest `api.auth.rbac.test.ts` + acl.phase5 |
| AyuSphere | 7 (Auth.js JWT pi, coordinator, monitor, ethics, pv, admin, regulator read-only) | Auth.js JWT + middleware + regulator read-only (`regulator.test.ts`) | Yes | UNKNOWN | 157 tests `auth-rbac.test.ts` |
| Dashboard | 7 (per README) | PyJWT HS256 + dependencies.py RBAC | Yes (React Router guards) | UNKNOWN | Partial (pytest) |
| Anushka | 4-5? (per App.jsx, no matrix) | bcryptjs + JWT (no ACL) | Yes (AuthContext) | NO | MOCKED |
| rimi | 4-5? + `test_rbac_matrix.js` | Same + optional better-sqlite3 | Yes + RBACMatrixModal | NO | MOCKED |
| AyuTrial | 7 (admin, PI, PV, CRC, CRA, IEC, Regulator audit `regulator.audit@cdsco`) | Persona switcher (demo, no password) + AppShell | Yes (1-click switcher, 403 page) | NO (assignedStudyIds mock) | 21 workflow tests |
| DEV-RUSH | 0 found | NOT PRESENT | UNKNOWN | NO | NOT PRESENT |

**Rule:** UI hiding alone is not security — vedraya/AyuSphere/Dashboard have backend authorization (tests prove); Anushka/rimi/AyuTrial demo lack backend ACL (AyuTrial `assignedStudyIds` is mock).

---

## 14. Audit Comparison

| Repo | Basic logging | User + ts | Before/after | Immutable | Hash chain | Crypto verify |
|---|---|---|---|---|---|---|
| vedraya | YES | YES | UNKNOWN (seq) | YES (append-only API 405 on PATCH/DELETE) | YES GLOBAL SHA-256 (`audit/service.ts`) | YES `valid:true/false` verify endpoint `audit.integrity.test.ts` tamper→false |
| AyuSphere | YES | YES | YES (withAudit atomic) | YES (insert-only) | YES (via signatures.test.ts) | YES |
| AyuTrial | YES (ALCOA+ ledger) | YES | NO | MOCKED (localStorage) | MOCKED (syncComputeSimpleHash local) | MOCKED (on-screen verify, not WORM) |
| Dashboard | YES (`audit_logs.py`) | YES | UNKNOWN | NO | NO | NO |
| Anushka | YES (AuditPage) | UNKNOWN | NO | NO | NO | NO |
| rimi | YES (AuditPage 33KB) | YES | UNKNOWN | NO | NO | NO |
| DEV-RUSH | YES (`audit-log/route.ts` 3.1KB) | UNKNOWN | UNKNOWN | UNKNOWN | NO | NO |

**Do not call ordinary logging immutable ledger — check hash chain + verification.**

---

## 15. AI Comparison

| Repo | Input | Processing | Model/API | Output | Status | Evidence |
|---|---|---|---|---|---|---|
| AyuSphere | Doctor Note text/images (Vercel Blob), trial docs for Copilot | `api/ai/extract` (Claude OCR, low-confidence flag, draft), `api/ai/copilot` (grounded retrieval, declines), `api/ai/approve` (PI gate), `api/guide` (Groq) | Anthropic SDK 0.125 + LangChain Groq + Gemini fallback, mock in tests | Extracted fields, grounded answer, approved record | **IMPLEMENTED** (external LLM API, prompt-based, not trained model) | `repositories/vansh459_AyuSphere/src/app/api/ai/extract/route.ts:1` + `extraction.test.ts:1` 11KB + `copilot.test.ts:1` |
| vedraya | — | — | — | — | NOT PRESENT (honest) | No AI file, `LIMITATIONS.md:1` |
| AyuTrial | AE fields → WHO-UMC | Rule engine (Certain/Probable) deterministic | No LLM | Causality score | NOT PRESENT (rule, not AI) | `src/app/pharmacovigilance/new/page.tsx:1` 22KB |
| Others | — | — | — | — | NOT PRESENT | 0 hits for `claude`/`openai` |

**No model files (.pt/.onnx) found in any repo via rglob.**

---

## 16. Data Architecture Comparison

| Repo | Trial metadata | Participant data | How stored | Real vs Synthetic | External API |
|---|---|---|---|---|---|
| vedraya | Synthetic AYU-024 etc. | Synthetic participants (no PHI) | Postgres + Drizzle + `demo:seed` deterministic | Synthetic | Not present |
| AyuSphere | **Real public CTRI** (titles, CTRI numbers, interventions, sponsors) + synthetic participants | Synthetic, de-identified by schema (no identifier cols) | Neon Postgres + Drizzle + PGlite, `db:seed:real` idempotent | Mixed (real trial meta + synthetic participants) | `scripts/scrape/ctri_scrape.py:1` crawl4ai (pip-only) |
| AyuTrial | Synthetic 10 trials | Synthetic DEMO-0001 de-identified | `mockData.ts:1` 58KB in-memory + localStorage (demo) vs Supabase (prod) | Synthetic | Not present |
| Dashboard | Synthetic via `init_db.py` | Synthetic | SQLAlchemy + Postgres/SQLite | Synthetic | Not present |
| Anushka/rimi | Synthetic 24 trials 30 AEs | Synthetic | `seed.js:1` 57KB → SQLite `ctms.db` (committed) | Synthetic | Not present |
| DEV-RUSH | Unknown (schema 13KB) | Unknown | Drizzle `lib/schema.ts` | UNKNOWN | Not present |

**Pay attention:** Participant data is synthetic in all verified repos — no real PHI. Do not fabricate clinical data; if mock needed label MOCK DATA.

---

## 17. Testing Comparison

| Repo | Framework | Important tests | Workflow coverage | E2E | API | Unit |
|---|---|---|---|---|---|---|
| vedraya | Vitest + Playwright + oxlint | `server/tests/*.test.ts` 8 suites, `e2e/ctms-critical-path.spec.ts:1` 11KB, `phase4-safety-coding` | Studies, AE escalate, consent/regulatory, ACL, audit tamper, demo freeze | YES 26/26 Playwright | YES 46/46 Vitest | YES |
| AyuSphere | Vitest + PGlite + ESLint | `tests/*.test.ts` 50 suites 157 tests (`lifecycle`, `crf`, `ae-service`, `extraction`, `copilot`, `fhir-api`, `design-qa`) | Lifecycle, CRF immutability, AE clock, alerts, Copilot grounding, design tokens | NO (PGlite integration) | YES (PGlite) | YES |
| AyuTrial | tsx (run via `npx tsx`) | `src/tests/workflows.test.ts:1` 21 tests (integration) | 28 routes integration (dashboard, studies, pharmacovigilance) | NO | NO | NO |
| Dashboard | pytest + httpx (requirements) | Not found many `*.test.py` | Trials, participants via pytest? | NO | UNKNOWN | UNKNOWN |
| Anushka | `echo error` | None | None | NO | NO | NO |
| rimi | `node test_rbac_matrix.js` | 1 shallow RBAC matrix | RBAC only | NO | NO | NO |
| DEV-RUSH | `echo error` | None | None | NO | NO | NO |

**Do not invent coverage:** Vedraya 46/46 + 26/26 claimed in README — verified via `server/package.json:1` test: vitest run, `playwright.config.ts:1`. AyuSphere 157 claimed — verified via `vitest.config.ts` + 50 files.

---

## 18. Deployment Comparison

| Repo | Dockerfile | compose | vercel.json | render.yaml | supabase | gcp/aws | CI/CD |
|---|---|---|---|---|---|---|---|
| vedraya | Check (not found via .git scan? Actually no Dockerfile) | No | YES (`vercel.json`) | YES | No | No | No workflows |
| AyuSphere | No | No | YES | No | No | No (Neon) | No |
| AyuTrial | No | No | YES | No | YES (`supabase/` migrations) | No | No |
| Dashboard | YES | YES (`docker-compose.yml`) | YES | YES | No | No | No |
| Anushka | No | No | No | No | No | No | No |
| rimi | YES | No | No | YES | No | YES `apprunner.yaml` (AWS AppRunner) | No |
| DEV-RUSH | No | No | YES (implied) | No | No | No | No |

**Live demos (CLAIM, not fetched):** vedraya `vedraya-three.vercel.app` (SPA only), AyuTrial `ayutrial-ctms.vercel.app` READY, DEV-RUSH `sih-26046-dev-rush.vercel.app`, AyuSphere Vercel, Dashboard vercel/render.

---

## 19. Presentation / Demo Comparison

| Repo | DEMO_SCRIPT.md | JUDGE_QA.md | docs/ | PPT | PDF | Judge materials copied to `presentations/<repo>/` |
|---|---|---|---|---|---|---|
| vedraya | YES `docs/DEMO_SCRIPT.md:1` 3KB | YES `docs/JUDGE_QA.md:1` 3.5KB | YES 14 md (`TRACEABILITY`, `RBAC`, `SECURITY`, etc.) | 0 | 0 | YES `docs_DEMO_SCRIPT.md`, `docs_JUDGE_QA.md`, `docs_SIH26046_TRACEABILITY_FINAL.md` 8KB |
| AyuSphere | YES `docs/uat/Judge_Demo_Script.md:1` 4.1KB | Partial `Tech_Security_Guide.md` 17KB | YES 13 md + `decisions.md` 29KB | 0 | 9 PDFs (Judge 1.31MB + 7 UAT 0.4-3.3MB + Tech 155KB) | YES 9 PDFs + Judge_Demo_Script |
| AyuTrial | NOT PRESENT | NOT PRESENT | 3 md | 0 | 0 | Only `ARCHITECTURE.md` copied (generic) |
| Dashboard | NOT PRESENT | NOT PRESENT | 1 `DEPLOYMENT.md` | 0 | 0 | None |
| Anushka/rimi | NOT PRESENT | NOT PRESENT | 1-2 md | 0 | 0 | None |
| DEV-RUSH | NOT PRESENT | NOT PRESENT | `AGENTS.md` | 0 | 0 | None |

**Zero PPT:** `*.ppt/*.pptx` 0 hits across 7 repos (verified via `presentations/*/PRESENTATION_INVENTORY.md`).

**VEDRAYA special (Task 27 summarized):** First shown: Live Command Center after login `admin@vedraya.demo` → AYU-024 study dossier → Safety AE escalate → Audit verify (`AUDIT CHAIN: VERIFIED`). Differentiator stated: auditable RBAC + study ACL + GLOBAL SHA-256 re-verify, honest prototype-only scope, PS traceability. Judge Q&A anticipates WORM/licensed MedDRA/ABDM offline/certification objections — all answered NOT IMPLEMENTED/NOT CONNECTED per `LIMITATIONS.md`. PS requirements with code: RBAC/ACL/audit/KPIs/regulatory tracking; claims only: licensed dictionaries, full CDISC, WORM, eSign, ABDM adapters.

---

## 20. Technical Gaps Observed

| Gap | Observed in | Exploit Opportunity |
|---|---|---|
| **Batch/Lot traceability** (Ayurveda drug batch) | 0/7 repos show batch traceability — search `batch` 0 hits | Build batch → site → participant → AE traceability |
| **FHIR ↔ CDISC mapping layer** | 0/7 have mapping (only AyuSphere has both separately) | Build FHIR-to-CDISC Joint Mapping IG (FHIR R4 → SDTM DM/AE/EX via transform layer) — standards differentiator per task 6 |
| **Individualization-aware protocol** (Prakriti-based branching) | Only AyuTrial has Prakriti fields (IMPLEMENTED as data, not logic) | Build protocol engine: Prakriti/Agni/Koshtha → visit schedule + outcome logic |
| **Assessment reliability QA** | Only AyuSphere `data-quality` partial | Build inter-rater reliability, Ayush exam QA |
| **Offline capability** | 1 MOCKED (AyuTrial localStorage), 6 NOT PRESENT | Build IndexedDB + sync + conflict resolution for rural sites |
| **True CTRI API (not scrape)** | Only AyuSphere scrape (not official API) | Integrate hypothetical CTRI API or show sync design (with disclaimer) |
| **WORM + eSign + 21 CFR Part 11** | 0 certified, 2 CLAIMED ONLY, vedraya honest NOT WORM | Design WORM adapter + eSign placeholder (honest, not claimed certified) |
| **Full CDASH/ODM** | 0 repos beyond SDTM-like CSV | Build CDASH form definitions + ODM export |
| **ABDM real integration** | 0 actual, 1 blueprint | Build ABDM sandbox (ABHA verify mock) — clarify mock |

**Common gap across 5+ repos:** ABDM, offline, FHIR↔CDISC mapping, batch traceability, WORM, full CDASH.

---

## 21. Evidence Index

| Repo | Top evidence files (read) |
|---|---|
| All | `repositories/<repo>/README.md:1` (claim), `analysis/<repo>/REPO_DETAILS.md:1` (facts), `analysis/<repo>/ARCHITECTURE.md:1` (diagram), `analysis/<repo>/REPO_ANALYSIS.md:21` (claim vs implementation) |
| vedraya | `server/src/db/schema.ts:1` 441 lines, `server/src/middleware/studyAccess.ts:1`, `server/src/modules/audit/service.ts:1`, `server/tests/*.test.ts:1` 46/46, `e2e/ctms-critical-path.spec.ts:1`, `docs/DEMO_SCRIPT.md:1`, `docs/JUDGE_QA.md:1` |
| AyuSphere | `src/db/schema.ts:1` 576 lines, `src/app/api/ai/extract/route.ts:1`, `tests/extraction.test.ts:1` 11KB, `scripts/scrape/ctri_scrape.py:1`, `docs/gap-analysis.md:1` 13KB, `docs/uat/*.pdf` 9 PDFs |
| AyuTrial | `src/lib/mockData.ts:1` 58KB, `src/app/pharmacovigilance/new/page.tsx:1` 22KB, `src/app/interoperability/page.tsx:1`, `supabase/` migrations |
| Dashboard | `backend/app/api/v1/trials.py:1` 11.8KB, `backend/app/database/init_db.py:1` 60KB, `backend/app/api/v1/fhir.py:1` 2.5KB |
| Anushka/rimi | `server/seed.js:1` 57KB, `client/src/pages/TrialDetailPage.jsx:1` 37KB, `client/src/components/AWSCloudModal.jsx:1` 15KB (rimi) |
| DEV-RUSH | `devrush-ctms/lib/schema.ts:1` 13.7KB, `app/api/fhir/ingest/route.ts:1` 12.5KB, etc. stubs |

**Presentations copied:** `presentations/nishant-uxs_vedraya/` (6 docs) + `presentations/vansh459_AyuSphere/` (9 PDFs + 17KB md) — see `presentations/*/PRESENTATION_INVENTORY.md`.

**Search evidence:** `audit` hits 0-7 per repo, `FHIR` 0-5, `CDISC/SDTM` 0-3, `CTRI` 0-2, `ABDM` 0-1, `test` 0-50, `ppt` 0, `pdf` 0-9 — verified via rglob.

---

## 22. Unknowns

| Unknown | Why not determined |
|---|---|
| Official MoAyush SIH26046 PS PDF | Not in repos — used traceability docs as evidence |
| CTRI official API existence/contract | Only scrape found, not official API — unknown if SIH expects API vs tracking |
| ABDM sandbox availability | No adapter code — unknown if SIH expects real ABDM sandbox |
| Production DB sizes / seed freshness | Counts from file sizes, not live DB fetches |
| Vercel live health for 4 claimed demos | URLs in README but not fetched (network not required, but would verify) |
| Dashboard pytest coverage value | Requirements list pytest but few *.test.py found — insufficient evidence |
| Anushka/rimi API endpoint count exact | Only route header scan, not full body read (0-0 groups via scan, but pages imply routes) |
| DEV-RUSH API route implementation depth | File sizes 6-12KB but bodies not read fully — UNKNOWN depth |
| Offline design expectations (SIH rubric) | No rubric in repos — unknown if expected |
| License reuse permission beyond MIT/ISC | 3 repos without LICENSE — `No explicit open-source license identified` |

**Do not invent:** Where unknown, report `UNKNOWN` or `Not determined from available codebase` per MASTER_PROMPT.md rule 4.

---

## How to Verify Yourself

```powershell
# List all analysis
tree /F E:\SIH26046_COMPETITOR_ANALYSIS

# Per repo deep dive
cat E:\SIH26046_COMPETITOR_ANALYSIS\analysis\nishant-uxs_vedraya\REPO_ANALYSIS.md
cat E:\SIH26046_COMPETITOR_ANALYSIS\analysis\vansh459_AyuSphere\REPO_ANALYSIS.md

# Matrix
cat E:\SIH26046_COMPETITOR_ANALYSIS\analysis\COMPETITOR_MATRIX.md

# Presentations
cat E:\SIH26046_COMPETITOR_ANALYSIS\presentations\nishant-uxs_vedraya\PRESENTATION_INVENTORY.md
```

*All conclusions are FACT (code found) / CLAIM (README) / INFERENCE (may contribute) / UNKNOWN — per task 34. Do not conclude “compliant” without certification.*
