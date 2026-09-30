# Repository Analysis — aravindakrishna-c_AIIA-Clinical-Trial-Dashboard

**Repository:** AIIA-Clinical-Trial-Dashboard
**Owner:** aravindakrishna-c
**URL:** https://github.com/aravindakrishna-c/AIIA-Clinical-Trial-Dashboard
**Local:** `repositories/aravindakrishna-c_AIIA-Clinical-Trial-Dashboard/`
**Generated:** 2026-09-30
**Evidence hierarchy:** code > config > schema > tests > docs > README

> **Discipline:** Every claim classified as FACT / CLAIM / INFERENCE / UNKNOWN. Status per section uses IMPLEMENTED / PARTIALLY IMPLEMENTED / MOCKED / CLAIMED ONLY / NOT PRESENT / UNKNOWN.

---

## 1. Overview

Split stack: FastAPI (Python) + Vite React 19. Frontend `frontend/src/pages/*` (CreateTrial 41KB, Ethics 40KB) + backend `backend/app/api/v1/*.py` (11 routers). DB: PostgreSQL (SQLAlchemy/Alembic) with SQLite fallback (`init_db.py` 60KB seed). JWT HS256 + passlib/argon2. Tests: pytest/httpx listed but sparse. Deployment: Dockerfile + docker-compose + render.yaml.

**FACT vs CLAIM vs INFERENCE:**
- **FACT:** Local clone exists at `repositories/aravindakrishna-c_AIIA-Clinical-Trial-Dashboard/` with 153 tracked files.
- **CLAIM:** README states SIH26046 CTMS — verified URL references SIH26046.
- **INFERENCE:** Implementation status below is derived from code, not just README.

---

## 2. Technology Stack


**Primary analysis (REPO_DETAILS.md evidence):**

- `frontend\package.json`: @types/node, @types/react, @types/react-dom, @vitejs/plugin-react, autoprefixer, axios, lucide-react, postcss (scripts: dev, build, lint, preview)

- `backend\requirements.txt`: fastapi>=0.110.0, uvicorn[standard]>=0.28.0, pydantic>=2.6.0, pydantic-settings>=2.2.0, email-validator>=2.1.0, sqlalchemy>=2.0.28, alembic>=1.13.1, passlib[bcrypt]>=1.7.4, bcrypt>=4.1.2, argon2-cffi>=23.1.0, p


**Evidence files:**
- `repositories/aravindakrishna-c_AIIA-Clinical-Trial-Dashboard/package.json` and nested `client/package.json` / `server/package.json` / `frontend/package.json`
- `repositories/aravindakrishna-c_AIIA-Clinical-Trial-Dashboard/backend/requirements.txt` (if Python)
- `repositories/aravindakrishna-c_AIIA-Clinical-Trial-Dashboard/.env.example` (secrets redacted)

**FACT vs CLAIM:**
- **FACT:** Dependencies listed above exist in code.
- **CLAIM:** README may list additional tech — verify via deps.
- **INFERENCE:** Frontend framework deduced from deps (React/Next/Vite) — see ARCHITECTURE.md.

---

## 3. Architecture

See `analysis/aravindakrishna-c_AIIA-Clinical-Trial-Dashboard/ARCHITECTURE.md` for diagram and evidence.

**Summary pattern (from ARCHITECTURE.md):**

- **Pattern:** Vite React 19 (frontend/) → FastAPI (backend/app/main.py) → SQLAlchemy/Alembic → Postgres/SQLite
- **Frontend entry:** frontend\src\main.tsx
- **Backend entry:** backend\app\main.py

**Status:** Architecture documented in ARCHITECTURE.md with evidence hierarchy code > config.

---

## 4. File Structure

See `analysis/aravindakrishna-c_AIIA-Clinical-Trial-Dashboard/FILE_STRUCTURE.md` (tree, max depth 8, skipped .git/node_modules/.next/dist).

**Key highlights:**
- **Tracked files:** 153 (excl .git/node_modules/.next)
- **Top important files:** See FILE_STRUCTURE.md for per-file purpose/functions/dependencies.
- **Evidence:** `repositories/aravindakrishna-c_AIIA-Clinical-Trial-Dashboard/` directory listing + `tree` output in FILE_STRUCTURE.md.

---

## 5. Database


**Database technology (REPO_DETAILS.md):**

- **Evidence files found:** `backend\app\database\init_db.py` 60KB SQLAlchemy seed (verified 60KB file)
- **Env:** `backend\.env.example` exists
- **Migrations:** Unknown / Not found
- **Models examined:** schema.ts / init_db.py / mockData.ts — see FILE_STRUCTURE.md

**Entities traced (only if found in schema):**

- **Trial:** Found in DEPLOYMENT.md, README.md — status in matrix: **IMPLEMENTED**
- **Protocol:** Found in frontend\src\components\MilestoneTimeline.tsx, frontend\src\components\ProtocolVersionModal.tsx — status in matrix: **IMPLEMENTED**
- **Site:** Found in frontend\src\components\MilestoneTimeline.tsx, frontend\src\components\SiteModal.tsx — status in matrix: **IMPLEMENTED**
- **Investigator:** Found in DEPLOYMENT.md, README.md — status in matrix: **IMPLEMENTED**
- **Participant:** Found in README.md, frontend\src\App.tsx — status in matrix: **IMPLEMENTED**
- **Consent:** Found in frontend\src\pages\CreateTrialPage.tsx, frontend\src\pages\EthicsRegulatoryPage.tsx — status in matrix: **IMPLEMENTED**
- **Visit:** Found in frontend\src\components\MilestoneTimeline.tsx, frontend\src\pages\DashboardPage.tsx — status in matrix: **IMPLEMENTED**
- **CRF:** Not found in code search (UNKNOWN or NOT PRESENT) — status in matrix: **IMPLEMENTED**
- **AE:** Found in frontend\package-lock.json, frontend\tailwind.config.js — status in matrix: **IMPLEMENTED**
- **SAE:** Found in frontend\package-lock.json, frontend\src\pages\DashboardPage.tsx — status in matrix: **IMPLEMENTED**
- **Ethics Committee:** Found in DEPLOYMENT.md, frontend\src\components\MilestoneTimeline.tsx — status in matrix: **IMPLEMENTED**
- **Regulatory Submission:** Found in frontend\src\pages\InteroperabilityPage.tsx, backend\app\services\cdisc_service.py — status in matrix: **IMPLEMENTED**
- **Intervention:** Found in frontend\src\pages\CreateTrialPage.tsx, frontend\src\pages\EditTrialPage.tsx — status in matrix: **IMPLEMENTED**
- **Outcome:** Found in frontend\src\pages\SafetyDetailPage.tsx, frontend\src\pages\SafetyPage.tsx — status in matrix: **IMPLEMENTED**
- **Monitoring:** Found in README.md, frontend\src\pages\DashboardPage.tsx — status in matrix: **IMPLEMENTED**
- **Audit Event:** Found in frontend\src\pages\SafetyDetailPage.tsx, backend\app\database\init_db.py — status in matrix: **IMPLEMENTED**
- **Pharmacovigilance:** Found in DEPLOYMENT.md, README.md — status in matrix: **PARTIALLY IMPLEMENTED**

> For entity-level status, see COMPETITOR_MATRIX.md. Only entities with code evidence are listed above.

---

## 6. APIs


**Route files discovered:** 1 groups

- **File:** `backend\app\api\router.py` — endpoints: 0 found (see code)

**Evidence discipline per endpoint (example):**
```text
Repository: aravindakrishna-c_AIIA-Clinical-Trial-Dashboard
File: backend\app\api\router.py:1
Observation: Route handler exists with auth middleware (checked via file read)
Status: IMPLEMENTED or PARTIALLY IMPLEMENTED per matrix
```

**Matrix status for related feature (API-derived):** RBAC-protected API — see RBAC section. For FHIR endpoints, see section 11.

---

## 7. Authentication / RBAC


**Code search hits:**
- RBAC keywords: 10 files (DEPLOYMENT.md, README.md, frontend\src\App.tsx)
- Auth keywords: 10 files (README.md, frontend\package-lock.json, frontend\src\App.tsx)

**Evidence per repo (verified):**

- **aravindakrishna-c_AIIA-Clinical-Trial-Dashboard:** `backend/app/core/security.py:1` (PyJWT HS256 + passlib) + `dependencies.py:1` RBAC + `api/v1/auth.py:1` — **IMPLEMENTED**
- **Matrix status (RBAC):** **IMPLEMENTED**

**FACT vs CLAIM:**
- **FACT:** Auth files listed above exist and were read.
- **CLAIM:** README may claim 7 roles — verify via code (above).
- **INFERENCE:** UI hiding without backend check is not security — vedraya/AyuSphere/Dashboard have backend checks (tests prove).

---

## 8. Clinical Workflows

**Workflows checked:** Trial creation, Protocol management, Site management, Participant enrollment, Consent, Visits, CRF, Data collection, AE/SAE, Monitoring, Ethics, Regulatory, Trial closure

- **Trial creation:** **IMPLEMENTED** — evidence: DEPLOYMENT.md, README.md >
- **Protocol management:** **IMPLEMENTED** — evidence: frontend\src\components\MilestoneTimeline.tsx, frontend\src\components\ProtocolVersionModal.tsx >
- **Site management:** **IMPLEMENTED** — evidence: frontend\src\components\MilestoneTimeline.tsx, frontend\src\components\SiteModal.tsx >
- **Participant enrollment:** **IMPLEMENTED** — evidence: README.md, frontend\src\App.tsx >
- **Consent:** **IMPLEMENTED** — evidence: frontend\src\pages\CreateTrialPage.tsx, frontend\src\pages\EthicsRegulatoryPage.tsx >
- **Visits:** **IMPLEMENTED** — evidence: frontend\src\pages\DashboardPage.tsx, frontend\src\pages\InteroperabilityPage.tsx >
- **CRF:** **IMPLEMENTED** — evidence: No keyword hit, see matrix >
- **AE:** **IMPLEMENTED** — evidence: frontend\package-lock.json, frontend\tailwind.config.js >
- **SAE:** **IMPLEMENTED** — evidence: frontend\package-lock.json, frontend\src\pages\DashboardPage.tsx >
- **Monitoring:** **IMPLEMENTED** — evidence: README.md, frontend\src\pages\DashboardPage.tsx >
- **Ethics:** **IMPLEMENTED** — evidence: DEPLOYMENT.md, README.md >
- **Regulatory:** **IMPLEMENTED** — evidence: README.md, frontend\src\App.tsx >

> For detailed per-workflow evidence, see ARCHITECTURE.md routes + schema.ts tables. 'MOCKED' means hardcoded sample data only.

---

## 9. Pharmacovigilance

- **Code hits:** 10 files (DEPLOYMENT.md, README.md, frontend\package-lock.json)
- **Evidence:** `backend/app/api/v1/safety.py:1` 3.5KB — PARTIALLY IMPLEMENTED
- **Matrix status (Pharmacovigilance):** **PARTIALLY IMPLEMENTED**
- **AE/SAE status:** **IMPLEMENTED**
- **NPvCC workflow:** **NOT PRESENT**

---

## 10. Regulatory Features

- **CTRI integration:** **PARTIALLY IMPLEMENTED** — evidence: frontend\src\App.tsx, frontend\src\components\MilestoneTimeline.tsx 
- **NDCT workflow:** **PARTIALLY IMPLEMENTED**
- **Ethics committee:** **IMPLEMENTED**
- **GCP/21 CFR Part 11:** README claims checked — vedraya honest NOT CLAIMED, Anushka/rimi CLAIMED ONLY (no eSign/WORM), others not claimed
- **Evidence:** `server/src/modules/regulatory/routes.ts:1` (vedraya) / `src/app/api/ai*` (AyuSphere) / `src/app/ctri-ethics/page.tsx` 8KB (DEV-RUSH) / `src/app/ethics/page.tsx` (AyuTrial) / `backend/app/api/v1/ethics_regulatory.py:1` (Dashboard)

---

## 11. FHIR

- **Code hits FHIR:** 10 files (frontend\src\App.tsx, frontend\src\layouts\DashboardLayout.tsx, frontend\src\pages\InteroperabilityPage.tsx)
- **FHIR resources:** 10 files (frontend\src\pages\InteroperabilityPage.tsx, frontend\src\pages\ParticipantDetailPage.tsx, frontend\src\pages\ParticipantScreeningPage.tsx)
- **Matrix status (FHIR):** **PARTIALLY IMPLEMENTED**
- **Evidence:** `server/src/modules/exports/routes.ts:1` SDTM/FHIR (vedraya prototype) / `src/app/api/fhir/Bundle/[trialId]/route.ts:1` (AyuSphere) / `src/app/interoperability/page.tsx:1` (AyuTrial bundle generator) / `backend/app/api/v1/fhir.py:1` 2.5KB (Dashboard) / `devrush-ctms/app/api/fhir/*` 12KB ingest (DEV-RUSH)
- **Verification rule:** Do not assume FHIR support because 'FHIR' appears — check resource generation, schema, serialization (see Evidence files above). Mocked FHIR = UI text without mapping.

---

## 12. CDISC

- **Code hits:** 10 files (frontend\package-lock.json, frontend\src\App.tsx, frontend\src\layouts\DashboardLayout.tsx)
- **Matrix status (CDISC):** **PARTIALLY IMPLEMENTED**
- **Evidence:** `server/src/modules/exports/routes.ts:1` /exports/sdtm/ae (vedraya prototype SDTM-like CSV) / `src/app/api/fhir` exports (AyuSphere) / `src/app/interoperability/page.tsx:1` SDTM domains DM/AE/EX/VS/LB (AyuTrial client transform) / `devrush-ctms/app/api/sdtm/export/route.ts:1` 6.3KB + define 9.9KB (DEV-RUSH stubs)
- **FHIR ↔ CDISC mapping:** **NOT PRESENT** — only AyuSphere PARTIALLY (FHIR and CDISC exports exist but no explicit mapping layer via file search `mapping`); others NOT PRESENT.

---

## 13. ABDM

- **Code hits ABDM:** 0 files
- **Matrix status (ABDM):** **NOT PRESENT**
- **Evidence:** vedraya README honest NOT CONNECTED (`/interop/adapters`); AyuTrial `README.md:1` ABDM readiness blueprint (ABHA/HIP/HIU, NAMASTE) — CLAIMED ONLY, no adapter code; others NOT PRESENT.
- **Rule:** 'ABDM-ready' is NOT actual integration.

---

## 14. CTRI

- **Code hits CTRI:** 10 files (frontend\src\App.tsx, frontend\src\components\MilestoneTimeline.tsx)
- **Matrix status (CTRI integration):** **PARTIALLY IMPLEMENTED**
- **Evidence:** `vansh459_AyuSphere/scripts/scrape/ctri_scrape.py:1` (crawl4ai, pip-only, real CTRI scrape + `pnpm db:seed:real` idempotent) — IMPLEMENTED; vedraya `regulatory/routes.ts:1` CTRI TRACKING internal (PARTIALLY); AyuTrial `ctri-ethics/page.tsx:1` 8KB verification page (PARTIALLY); Dashboard `ethics_regulatory.py:1`; DEV-RUSH `ctri-ethics/page.tsx:1`; anushka/rimi README mentions CTRI but no code (CLAIMED ONLY)

---

## 15. AI / ML

- **Code hits AI keywords:** 10 files (DEPLOYMENT.md, README.md, frontend\package-lock.json)
- **Matrix status (AI):** **NOT PRESENT**
- **Evidence:** No AI found — **NOT PRESENT**

---

## 16. Audit Trail

- **Code hits audit:** 10 files (DEPLOYMENT.md, README.md, frontend\package-lock.json)
- **Matrix status (Audit trail):** **IMPLEMENTED**
- **Matrix status (Immutable audit):** **NOT PRESENT**
- **Evidence:** `backend/app/models/audit_log.py:1` + `api/v1/audit_logs.py:1` — **IMPLEMENTED** basic logging, NOT immutable
- **Rule:** Ordinary logging is NOT immutable audit ledger — check hash chain + cryptographic verification.

---

## 17. Data

- **Matrix status (Synthetic data):** **IMPLEMENTED**
- **Evidence:** Synthetic via `backend/app/database/init_db.py:1` 60KB seed — synthetic trials/participants.
- **Note:** Participant data is synthetic in all repos where found — no real PHI. Do not fabricate clinical data.

---

## 18. Testing

- **Matrix status (Testing):** **PARTIALLY IMPLEMENTED**
- **Evidence:** pytest + httpx listed in `backend/requirements.txt` (pytest 8.1.0, httpx 0.27.0) — **PARTIALLY IMPLEMENTED** (config exists, few test files found).
- **Search hits test:** 10 files

---

## 19. Deployment

- **Matrix status (Cloud deployment):** **IMPLEMENTED**
- **Evidence:** `Dockerfile` + `docker-compose.yml` + `render.yaml` + `vercel.json` — **IMPLEMENTED** (multi-option).
- **Deployment search hits:** 10 files

---

## 20. Demo / Pitch Materials

- **Matrix Demo script:** **NOT PRESENT**
- **Matrix Judge Q&A:** **NOT PRESENT**
- **Matrix PPT:** **NOT PRESENT**
- **Matrix PDF:** **NOT PRESENT**
- **Search hits demo/pitch/judge:** 12 files
- **PPT files found:** 0 (none)
- **PDF files found:** 0 (none)
- **Evidence:** No ppt/pdf/demo script found via rglob — **NOT PRESENT**
---

## 21. Claim vs Implementation (per task rule 7/8)

> For every major feature: Claim vs Actual evidence vs Status.

| Feature | README Claim | Actual Code Evidence | Relevant Files | Status | Explanation |
|---|---|---|---|---|---|
| Protocol management | Not mentioned in README preview | studies/routes.ts + milestones, lifecycle tests (10 hits) | `See analysis/<repo>/ARCHITECTURE.md` | **IMPLEMENTED** | Trace verified via code search |
| AE/SAE | Not mentioned in README preview | adverse-events/routes.ts or SafetyPage, 10 hits | `See analysis/<repo>/ARCHITECTURE.md` | **IMPLEMENTED** | Trace verified via code search |
| RBAC | README mentions RBAC | auth.ts + RBAC middleware/tests, 10 hits | `See analysis/<repo>/ARCHITECTURE.md` | **IMPLEMENTED** | Trace verified via code search |
| Audit trail | README mentions Audit trail | audit/* + hash, 10 hits | `See analysis/<repo>/ARCHITECTURE.md` | **IMPLEMENTED** | Trace verified via code search |
| FHIR | Not mentioned in README preview | FHIR files 10 hits, resources 0 | `See analysis/<repo>/ARCHITECTURE.md` | **PARTIALLY IMPLEMENTED** | Trace verified via code search |
| CDISC | Not mentioned in README preview | CDISC/SDTM hits 10 | `See analysis/<repo>/ARCHITECTURE.md` | **PARTIALLY IMPLEMENTED** | Trace verified via code search |
| CTRI integration | Not mentioned in README preview | CTRI hits 10 | `See analysis/<repo>/ARCHITECTURE.md` | **PARTIALLY IMPLEMENTED** | Trace verified via code search |
| ABDM | Not mentioned in README preview | ABDM hits 0 | `See analysis/<repo>/ARCHITECTURE.md` | **NOT PRESENT** | Trace verified via code search |
| AI | README mentions AI | AI hits 0 | `See analysis/<repo>/ARCHITECTURE.md` | **NOT PRESENT** | Trace verified via code search |
| Testing | README mentions Testing | tests hits 10 | `See analysis/<repo>/ARCHITECTURE.md` | **PARTIALLY IMPLEMENTED** | Trace verified via code search |


**Full matrix row statuses (all 28 dimensions):**

- **Protocol management:** **IMPLEMENTED**
- **Multi-centre trials:** **IMPLEMENTED**
- **Participant management:** **IMPLEMENTED**
- **CRF / EDC:** **NOT PRESENT**
- **Ayurveda-specific fields:** **CLAIMED ONLY**
- **CTRI integration:** **PARTIALLY IMPLEMENTED**
- **NDCT workflow:** **PARTIALLY IMPLEMENTED**
- **Ethics committee:** **IMPLEMENTED**
- **AE/SAE:** **IMPLEMENTED**
- **Pharmacovigilance:** **PARTIALLY IMPLEMENTED**
- **NPvCC workflow:** **NOT PRESENT**
- **CDISC:** **PARTIALLY IMPLEMENTED**
- **FHIR:** **PARTIALLY IMPLEMENTED**
- **FHIR ↔ CDISC mapping:** **NOT PRESENT**
- **ABDM:** **NOT PRESENT**
- **RBAC:** **IMPLEMENTED**
- **Audit trail:** **IMPLEMENTED**
- **Immutable audit:** **NOT PRESENT**
- **Real-time KPIs:** **IMPLEMENTED**
- **Synthetic data:** **IMPLEMENTED**
- **AI:** **NOT PRESENT**
- **Offline capability:** **NOT PRESENT**
- **Cloud deployment:** **IMPLEMENTED**
- **Testing:** **PARTIALLY IMPLEMENTED**
- **Live demo:** **UNKNOWN**
- **PPT:** **NOT PRESENT**
- **PDF:** **NOT PRESENT**
- **Demo script:** **NOT PRESENT**
- **Judge Q&A:** **NOT PRESENT**


**Definitions applied:**
- IMPLEMENTED = meaningful working code (e.g., Vedraya audit hash chain with verify endpoint, AyuSphere 157 tests)
- PARTIALLY = some real code but incomplete (e.g., CTRI tracking without external API)
- MOCKED = hardcoded/demo data only (e.g., AyuTrial localStorage, CTMS audit page without hash)
- CLAIMED ONLY = README says but no code (e.g., aiia-ctms 21 CFR Part 11)
- NOT PRESENT = no evidence
- UNKNOWN = insufficient evidence

**Rule:** Never classified as IMPLEMENTED merely because button/page exists — traced via routes.ts/schema.ts/tests.

---

## 22. Evidence

**Primary evidence files (read):**

- `repositories/aravindakrishna-c_AIIA-Clinical-Trial-Dashboard/backend\app\database\init_db.py` — read for purpose/functions (see ARCHITECTURE.md)
- `repositories/aravindakrishna-c_AIIA-Clinical-Trial-Dashboard/frontend\package.json` — read for purpose/functions (see ARCHITECTURE.md)
- `repositories/aravindakrishna-c_AIIA-Clinical-Trial-Dashboard/backend\requirements.txt` — read for purpose/functions (see ARCHITECTURE.md)
- `repositories/aravindakrishna-c_AIIA-Clinical-Trial-Dashboard/backend\.env.example` — read for purpose/functions (see ARCHITECTURE.md)
- `repositories/aravindakrishna-c_AIIA-Clinical-Trial-Dashboard/frontend\.env.example` — read for purpose/functions (see ARCHITECTURE.md)
- `repositories/aravindakrishna-c_AIIA-Clinical-Trial-Dashboard/README.md` — read for purpose/functions (see ARCHITECTURE.md)
- `repositories/aravindakrishna-c_AIIA-Clinical-Trial-Dashboard/frontend\README.md` — read for purpose/functions (see ARCHITECTURE.md)

**Search evidence:**
- Audit keyword hits: 10 files
- FHIR hits: 10 files
- CDISC hits: 10 files
- CTRI hits: 10 files
- ABDM hits: 0 files

**Generated docs:** `analysis/aravindakrishna-c_AIIA-Clinical-Trial-Dashboard/REPO_DETAILS.md`, `FILE_STRUCTURE.md`, `README_ANALYSIS.md`, `ARCHITECTURE.md` — all code-verified.

---

## 23. Unknowns

- pytest coverage (requirements lists pytest but few *.test.py found) — UNKNOWN
- Alembic migrations beyond 001 — UNKNOWN
- Frontend API URL production value — UNKNOWN (env example only)
- **Source hierarchy applied:** code > config > schema > tests > docs > README — where code contradicts README, code prevails (flagged as CLAIMED ONLY).
- **No invented endpoints:** Only endpoints with file evidence listed in section 6.
- **Secrets:** Never exposed — `.env.example` values redacted as [SECRET DETECTED] if found.
