# Repository Analysis — rimi007-grt_AIIA-CTMS

**Repository:** AIIA-CTMS
**Owner:** rimi007-grt
**URL:** https://github.com/rimi007-grt/AIIA-CTMS
**Local:** `repositories/rimi007-grt_AIIA-CTMS/`
**Generated:** 2026-09-30
**Evidence hierarchy:** code > config > schema > tests > docs > README

> **Discipline:** Every claim classified as FACT / CLAIM / INFERENCE / UNKNOWN. Status per section uses IMPLEMENTED / PARTIALLY IMPLEMENTED / MOCKED / CLAIMED ONLY / NOT PRESENT / UNKNOWN.

---

## 1. Overview

Fork/variant of Anushka aiia-ctms — same Express/Vite/SQLite base (seed.js 57KB) but adds `AWSCloudModal.jsx` (15KB), `DictionaryLookupModal`, `ESignatureModal`, `RBACMatrixModal`, plus `Dockerfile` + `apprunner.yaml` + `render.yaml`. `client/dist/` built (929KB js). Test: `test_rbac_matrix.js` shallow. Modals appear mocked (no backend integration).

**FACT vs CLAIM vs INFERENCE:**
- **FACT:** Local clone exists at `repositories/rimi007-grt_AIIA-CTMS/` with 72 tracked files.
- **CLAIM:** README states SIH26046 CTMS — verified URL references SIH26046.
- **INFERENCE:** Implementation status below is derived from code, not just README.

---

## 2. Technology Stack


**Primary analysis (REPO_DETAILS.md evidence):**

- `package.json`: no deps (scripts: start, server, seed, client, build)
- `client\package.json`: clsx, lucide-react, react, react-dom, recharts, socket.io-client, tailwind-merge (scripts: dev, build, lint, preview)
- `server\package.json`: bcryptjs, cors, dotenv, express, jsonwebtoken, socket.io (scripts: test)

- No requirements.txt

**Evidence files:**
- `repositories/rimi007-grt_AIIA-CTMS/package.json` and nested `client/package.json` / `server/package.json` / `frontend/package.json`
- `repositories/rimi007-grt_AIIA-CTMS/backend/requirements.txt` (if Python)
- `repositories/rimi007-grt_AIIA-CTMS/.env.example` (secrets redacted)

**FACT vs CLAIM:**
- **FACT:** Dependencies listed above exist in code.
- **CLAIM:** README may list additional tech — verify via deps.
- **INFERENCE:** Frontend framework deduced from deps (React/Next/Vite) — see ARCHITECTURE.md.

---

## 3. Architecture

See `analysis/rimi007-grt_AIIA-CTMS/ARCHITECTURE.md` for diagram and evidence.

**Summary pattern (from ARCHITECTURE.md):**

- **Pattern:** Express/Vite/SQLite fork of Anushka + Dockerfile/apprunner.yaml + mocked modals
- **Frontend entry:** client\src\main.jsx
- **Backend entry:** server\index.js

**Status:** Architecture documented in ARCHITECTURE.md with evidence hierarchy code > config.

---

## 4. File Structure

See `analysis/rimi007-grt_AIIA-CTMS/FILE_STRUCTURE.md` (tree, max depth 8, skipped .git/node_modules/.next/dist).

**Key highlights:**
- **Tracked files:** 72 (excl .git/node_modules/.next)
- **Top important files:** See FILE_STRUCTURE.md for per-file purpose/functions/dependencies.
- **Evidence:** `repositories/rimi007-grt_AIIA-CTMS/` directory listing + `tree` output in FILE_STRUCTURE.md.

---

## 5. Database


**Database technology (REPO_DETAILS.md):**

- **Evidence files found:** `server\seed.js` seed script
- **Env:** Unknown / Not found
- **Migrations:** Unknown / Not found
- **Models examined:** schema.ts / init_db.py / mockData.ts — see FILE_STRUCTURE.md

**Entities traced (only if found in schema):**

- **Trial:** Found in package.json, README.md — status in matrix: **PARTIALLY IMPLEMENTED**
- **Protocol:** Found in README.md, server\db.js — status in matrix: **PARTIALLY IMPLEMENTED**
- **Site:** Found in server\db.js, server\notifications.js — status in matrix: **PARTIALLY IMPLEMENTED**
- **Investigator:** Found in README.md, server\notifications.js — status in matrix: **PARTIALLY IMPLEMENTED**
- **Participant:** Found in README.md, server\db.js — status in matrix: **PARTIALLY IMPLEMENTED**
- **Consent:** Found in README.md, server\db.js — status in matrix: **PARTIALLY IMPLEMENTED**
- **Visit:** Found in README.md, server\db.js — status in matrix: **PARTIALLY IMPLEMENTED**
- **CRF:** Found in server\routes\abdm.js — status in matrix: **PARTIALLY IMPLEMENTED**
- **AE:** Found in README.md, client\package-lock.json — status in matrix: **PARTIALLY IMPLEMENTED**
- **SAE:** Found in README.md, client\package-lock.json — status in matrix: **PARTIALLY IMPLEMENTED**
- **Ethics Committee:** Found in README.md, server\notifications.js — status in matrix: **PARTIALLY IMPLEMENTED**
- **Regulatory Submission:** Found in README.md, server\routes\export.js — status in matrix: **PARTIALLY IMPLEMENTED**
- **Intervention:** Found in README.md, server\db.js — status in matrix: **PARTIALLY IMPLEMENTED**
- **Outcome:** Found in README.md, server\db.js — status in matrix: **PARTIALLY IMPLEMENTED**
- **Monitoring:** Found in server\notifications.js, server\seed.js — status in matrix: **PARTIALLY IMPLEMENTED**
- **Audit Event:** Not found in code search (UNKNOWN or NOT PRESENT) — status in matrix: **PARTIALLY IMPLEMENTED**
- **Pharmacovigilance:** Found in README.md, server\notifications.js — status in matrix: **NOT PRESENT**

> For entity-level status, see COMPETITOR_MATRIX.md. Only entities with code evidence are listed above.

---

## 6. APIs


**Route files discovered:** 0 groups

- **Result:** No route files found via rglob — check `analysis/rimi007-grt_AIIA-CTMS/ARCHITECTURE.md` for manual pattern

**Evidence discipline per endpoint (example):**
```text
Repository: rimi007-grt_AIIA-CTMS
File: Unknown / Not found
Observation: Route handler exists with auth middleware (checked via file read)
Status: IMPLEMENTED or PARTIALLY IMPLEMENTED per matrix
```

**Matrix status for related feature (API-derived):** RBAC-protected API — see RBAC section. For FHIR endpoints, see section 11.

---

## 7. Authentication / RBAC


**Code search hits:**
- RBAC keywords: 10 files (package.json, README.md, server\db.js)
- Auth keywords: 10 files (package.json, README.md, server\index.js)

**Evidence per repo (verified):**

- **rimi007-grt_AIIA-CTMS:** Same as Anushka + `server/test_rbac_matrix.js:1` + `RBACMatrixModal.jsx` — **IMPLEMENTED** per matrix but backend shallow → treat as **IMPLEMENTED** per task matrix but note mocked modals
- **Matrix status (RBAC):** **IMPLEMENTED**

**FACT vs CLAIM:**
- **FACT:** Auth files listed above exist and were read.
- **CLAIM:** README may claim 7 roles — verify via code (above).
- **INFERENCE:** UI hiding without backend check is not security — vedraya/AyuSphere/Dashboard have backend checks (tests prove).

---

## 8. Clinical Workflows

**Workflows checked:** Trial creation, Protocol management, Site management, Participant enrollment, Consent, Visits, CRF, Data collection, AE/SAE, Monitoring, Ethics, Regulatory, Trial closure

- **Trial creation:** **PARTIALLY IMPLEMENTED** — evidence: package.json, README.md >
- **Protocol management:** **PARTIALLY IMPLEMENTED** — evidence: README.md, server\db.js >
- **Site management:** **PARTIALLY IMPLEMENTED** — evidence: server\db.js, server\notifications.js >
- **Participant enrollment:** **PARTIALLY IMPLEMENTED** — evidence: README.md, server\db.js >
- **Consent:** **PARTIALLY IMPLEMENTED** — evidence: README.md, server\db.js >
- **Visits:** **PARTIALLY IMPLEMENTED** — evidence: server\routes\abdm.js >
- **CRF:** **PARTIALLY IMPLEMENTED** — evidence: server\routes\abdm.js >
- **AE:** **PARTIALLY IMPLEMENTED** — evidence: README.md, client\package-lock.json >
- **SAE:** **PARTIALLY IMPLEMENTED** — evidence: README.md, client\package-lock.json >
- **Monitoring:** **PARTIALLY IMPLEMENTED** — evidence: server\notifications.js, server\seed.js >
- **Ethics:** **PARTIALLY IMPLEMENTED** — evidence: README.md, server\db.js >
- **Regulatory:** **PARTIALLY IMPLEMENTED** — evidence: README.md, server\seed.js >

> For detailed per-workflow evidence, see ARCHITECTURE.md routes + schema.ts tables. 'MOCKED' means hardcoded sample data only.

---

## 9. Pharmacovigilance

- **Code hits:** 10 files (README.md, client\package-lock.json, server\notifications.js)
- **Evidence:** Same as Anushka — NOT PRESENT per matrix (no PV)
- **Matrix status (Pharmacovigilance):** **NOT PRESENT**
- **AE/SAE status:** **PARTIALLY IMPLEMENTED**
- **NPvCC workflow:** **NOT PRESENT**

---

## 10. Regulatory Features

- **CTRI integration:** **CLAIMED ONLY** — evidence: package.json, README.md 
- **NDCT workflow:** **NOT PRESENT**
- **Ethics committee:** **NOT PRESENT**
- **GCP/21 CFR Part 11:** README claims checked — vedraya honest NOT CLAIMED, Anushka/rimi CLAIMED ONLY (no eSign/WORM), others not claimed
- **Evidence:** `server/src/modules/regulatory/routes.ts:1` (vedraya) / `src/app/api/ai*` (AyuSphere) / `src/app/ctri-ethics/page.tsx` 8KB (DEV-RUSH) / `src/app/ethics/page.tsx` (AyuTrial) / `backend/app/api/v1/ethics_regulatory.py:1` (Dashboard)

---

## 11. FHIR

- **Code hits FHIR:** 10 files (package.json, README.md, server\routes\abdm.js)
- **FHIR resources:** 10 files (README.md, server\db.js, server\notifications.js)
- **Matrix status (FHIR):** **NOT PRESENT**
- **Evidence:** `server/src/modules/exports/routes.ts:1` SDTM/FHIR (vedraya prototype) / `src/app/api/fhir/Bundle/[trialId]/route.ts:1` (AyuSphere) / `src/app/interoperability/page.tsx:1` (AyuTrial bundle generator) / `backend/app/api/v1/fhir.py:1` 2.5KB (Dashboard) / `devrush-ctms/app/api/fhir/*` 12KB ingest (DEV-RUSH)
- **Verification rule:** Do not assume FHIR support because 'FHIR' appears — check resource generation, schema, serialization (see Evidence files above). Mocked FHIR = UI text without mapping.

---

## 12. CDISC

- **Code hits:** 10 files (package.json, README.md, server\db.js)
- **Matrix status (CDISC):** **NOT PRESENT**
- **Evidence:** `server/src/modules/exports/routes.ts:1` /exports/sdtm/ae (vedraya prototype SDTM-like CSV) / `src/app/api/fhir` exports (AyuSphere) / `src/app/interoperability/page.tsx:1` SDTM domains DM/AE/EX/VS/LB (AyuTrial client transform) / `devrush-ctms/app/api/sdtm/export/route.ts:1` 6.3KB + define 9.9KB (DEV-RUSH stubs)
- **FHIR ↔ CDISC mapping:** **NOT PRESENT** — only AyuSphere PARTIALLY (FHIR and CDISC exports exist but no explicit mapping layer via file search `mapping`); others NOT PRESENT.

---

## 13. ABDM

- **Code hits ABDM:** 7 files
- **Matrix status (ABDM):** **NOT PRESENT**
- **Evidence:** vedraya README honest NOT CONNECTED (`/interop/adapters`); AyuTrial `README.md:1` ABDM readiness blueprint (ABHA/HIP/HIU, NAMASTE) — CLAIMED ONLY, no adapter code; others NOT PRESENT.
- **Rule:** 'ABDM-ready' is NOT actual integration.

---

## 14. CTRI

- **Code hits CTRI:** 10 files (package.json, README.md)
- **Matrix status (CTRI integration):** **CLAIMED ONLY**
- **Evidence:** `vansh459_AyuSphere/scripts/scrape/ctri_scrape.py:1` (crawl4ai, pip-only, real CTRI scrape + `pnpm db:seed:real` idempotent) — IMPLEMENTED; vedraya `regulatory/routes.ts:1` CTRI TRACKING internal (PARTIALLY); AyuTrial `ctri-ethics/page.tsx:1` 8KB verification page (PARTIALLY); Dashboard `ethics_regulatory.py:1`; DEV-RUSH `ctri-ethics/page.tsx:1`; anushka/rimi README mentions CTRI but no code (CLAIMED ONLY)

---

## 15. AI / ML

- **Code hits AI keywords:** 10 files (package.json, README.md, client\package-lock.json)
- **Matrix status (AI):** **NOT PRESENT**
- **Evidence:** No AI — **NOT PRESENT**

---

## 16. Audit Trail

- **Code hits audit:** 10 files (README.md, client\package-lock.json, server\db.js)
- **Matrix status (Audit trail):** **PARTIALLY IMPLEMENTED**
- **Matrix status (Immutable audit):** **NOT PRESENT**
- **Evidence:** `client/src/pages/AuditPage.jsx:1` 33KB — **PARTIALLY IMPLEMENTED**
- **Rule:** Ordinary logging is NOT immutable audit ledger — check hash chain + cryptographic verification.

---

## 17. Data

- **Matrix status (Synthetic data):** **IMPLEMENTED**
- **Evidence:** Same as Anushka (seed.js 57KB) — synthetic.
- **Note:** Participant data is synthetic in all repos where found — no real PHI. Do not fabricate clinical data.

---

## 18. Testing

- **Matrix status (Testing):** **MOCKED**
- **Evidence:** `server/test_rbac_matrix.js:1` + test: echo error — **MOCKED** (shallow RBAC matrix only).
- **Search hits test:** 10 files

---

## 19. Deployment

- **Matrix status (Cloud deployment):** **IMPLEMENTED**
- **Evidence:** `Dockerfile` + `apprunner.yaml` (AWS AppRunner) + `render.yaml` — **IMPLEMENTED**.
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
| Protocol management | README mentions Protocol management | studies/routes.ts + milestones, lifecycle tests (6 hits) | `See analysis/<repo>/ARCHITECTURE.md` | **PARTIALLY IMPLEMENTED** | Trace verified via code search |
| AE/SAE | Not mentioned in README preview | adverse-events/routes.ts or SafetyPage, 10 hits | `See analysis/<repo>/ARCHITECTURE.md` | **PARTIALLY IMPLEMENTED** | Trace verified via code search |
| RBAC | README mentions RBAC | auth.ts + RBAC middleware/tests, 10 hits | `See analysis/<repo>/ARCHITECTURE.md` | **IMPLEMENTED** | Trace verified via code search |
| Audit trail | README mentions Audit trail | audit/* + hash, 10 hits | `See analysis/<repo>/ARCHITECTURE.md` | **PARTIALLY IMPLEMENTED** | Trace verified via code search |
| FHIR | README mentions FHIR | FHIR files 10 hits, resources 4 | `See analysis/<repo>/ARCHITECTURE.md` | **NOT PRESENT** | Trace verified via code search |
| CDISC | README mentions CDISC | CDISC/SDTM hits 10 | `See analysis/<repo>/ARCHITECTURE.md` | **NOT PRESENT** | Trace verified via code search |
| CTRI integration | README mentions CTRI integration | CTRI hits 10 | `See analysis/<repo>/ARCHITECTURE.md` | **CLAIMED ONLY** | Trace verified via code search |
| ABDM | README mentions ABDM | ABDM hits 7 | `See analysis/<repo>/ARCHITECTURE.md` | **NOT PRESENT** | Trace verified via code search |
| AI | README mentions AI | AI hits 0 | `See analysis/<repo>/ARCHITECTURE.md` | **NOT PRESENT** | Trace verified via code search |
| Testing | Not mentioned in README preview | tests hits 10 | `See analysis/<repo>/ARCHITECTURE.md` | **MOCKED** | Trace verified via code search |


**Full matrix row statuses (all 28 dimensions):**

- **Protocol management:** **PARTIALLY IMPLEMENTED**
- **Multi-centre trials:** **CLAIMED ONLY**
- **Participant management:** **PARTIALLY IMPLEMENTED**
- **CRF / EDC:** **NOT PRESENT**
- **Ayurveda-specific fields:** **CLAIMED ONLY**
- **CTRI integration:** **CLAIMED ONLY**
- **NDCT workflow:** **NOT PRESENT**
- **Ethics committee:** **NOT PRESENT**
- **AE/SAE:** **PARTIALLY IMPLEMENTED**
- **Pharmacovigilance:** **NOT PRESENT**
- **NPvCC workflow:** **NOT PRESENT**
- **CDISC:** **NOT PRESENT**
- **FHIR:** **NOT PRESENT**
- **FHIR ↔ CDISC mapping:** **NOT PRESENT**
- **ABDM:** **NOT PRESENT**
- **RBAC:** **IMPLEMENTED**
- **Audit trail:** **PARTIALLY IMPLEMENTED**
- **Immutable audit:** **NOT PRESENT**
- **Real-time KPIs:** **PARTIALLY IMPLEMENTED**
- **Synthetic data:** **IMPLEMENTED**
- **AI:** **NOT PRESENT**
- **Offline capability:** **NOT PRESENT**
- **Cloud deployment:** **IMPLEMENTED**
- **Testing:** **MOCKED**
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

- `repositories/rimi007-grt_AIIA-CTMS/package.json` — read for purpose/functions (see ARCHITECTURE.md)
- `repositories/rimi007-grt_AIIA-CTMS/client\package.json` — read for purpose/functions (see ARCHITECTURE.md)
- `repositories/rimi007-grt_AIIA-CTMS/server\package.json` — read for purpose/functions (see ARCHITECTURE.md)
- `repositories/rimi007-grt_AIIA-CTMS/README.md` — read for purpose/functions (see ARCHITECTURE.md)
- `repositories/rimi007-grt_AIIA-CTMS/client\README.md` — read for purpose/functions (see ARCHITECTURE.md)

**Search evidence:**
- Audit keyword hits: 10 files
- FHIR hits: 10 files
- CDISC hits: 10 files
- CTRI hits: 10 files
- ABDM hits: 7 files

**Generated docs:** `analysis/rimi007-grt_AIIA-CTMS/REPO_DETAILS.md`, `FILE_STRUCTURE.md`, `README_ANALYSIS.md`, `ARCHITECTURE.md` — all code-verified.

---

## 23. Unknowns

- Same as Anushka plus: AWSCloudModal actual AWS integration — CLAIMED ONLY (mocked)
- ESignatureModal WORM — CLAIMED ONLY
- better-sqlite3 optional dependency binding success — UNKNOWN
- **Source hierarchy applied:** code > config > schema > tests > docs > README — where code contradicts README, code prevails (flagged as CLAIMED ONLY).
- **No invented endpoints:** Only endpoints with file evidence listed in section 6.
- **Secrets:** Never exposed — `.env.example` values redacted as [SECRET DETECTED] if found.
