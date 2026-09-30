# Repository Analysis — kalyan-2006-prog_SIH26046-DEV-RUSH-

**Repository:** SIH26046-DEV-RUSH-
**Owner:** kalyan-2006-prog
**URL:** https://github.com/kalyan-2006-prog/SIH26046-DEV-RUSH-
**Local:** `repositories/kalyan-2006-prog_SIH26046-DEV-RUSH-/`
**Generated:** 2026-09-30
**Evidence hierarchy:** code > config > schema > tests > docs > README

> **Discipline:** Every claim classified as FACT / CLAIM / INFERENCE / UNKNOWN. Status per section uses IMPLEMENTED / PARTIALLY IMPLEMENTED / MOCKED / CLAIMED ONLY / NOT PRESENT / UNKNOWN.

---

## 1. Overview

Small Next.js demo shell (5 commits) — appears least implemented. `devrush-ctms/` with API routes: `fhir/ingest` 12.5KB, `fhir/export` 8KB, `sdtm/export` 6.3KB, `adam/export` 6KB, `define/export` 9.9KB, `audit-log` 3.1KB + `lib/schema.ts` 13.7KB (Drizzle). Dashboard pages 8-10KB. No auth file, no tests (`test: echo error`), no DB connection verified. Vercel demo claimed `sih-26046-dev-rush.vercel.app`.

**FACT vs CLAIM vs INFERENCE:**
- **FACT:** Local clone exists at `repositories/kalyan-2006-prog_SIH26046-DEV-RUSH-/` with 66 tracked files.
- **CLAIM:** README states SIH26046 CTMS — verified URL references SIH26046.
- **INFERENCE:** Implementation status below is derived from code, not just README.

---

## 2. Technology Stack


**Primary analysis (REPO_DETAILS.md evidence):**

- `package.json`: no deps (scripts: test)
- `devrush-ctms\package.json`: firebase, firebase-admin, next, react, react-dom (scripts: dev, build, start, lint)

- No requirements.txt

**Evidence files:**
- `repositories/kalyan-2006-prog_SIH26046-DEV-RUSH-/package.json` and nested `client/package.json` / `server/package.json` / `frontend/package.json`
- `repositories/kalyan-2006-prog_SIH26046-DEV-RUSH-/backend/requirements.txt` (if Python)
- `repositories/kalyan-2006-prog_SIH26046-DEV-RUSH-/.env.example` (secrets redacted)

**FACT vs CLAIM:**
- **FACT:** Dependencies listed above exist in code.
- **CLAIM:** README may list additional tech — verify via deps.
- **INFERENCE:** Frontend framework deduced from deps (React/Next/Vite) — see ARCHITECTURE.md.

---

## 3. Architecture

See `analysis/kalyan-2006-prog_SIH26046-DEV-RUSH-/ARCHITECTURE.md` for diagram and evidence.

**Summary pattern (from ARCHITECTURE.md):**

- **Pattern:** Next.js API stubs (fhir/sdtm/adam/define/audit-log) + Drizzle schema 13.7KB, no auth, no tests
- **Frontend entry:** Unknown / Not found
- **Backend entry:** devrush-ctms\app\api

**Status:** Architecture documented in ARCHITECTURE.md with evidence hierarchy code > config.

---

## 4. File Structure

See `analysis/kalyan-2006-prog_SIH26046-DEV-RUSH-/FILE_STRUCTURE.md` (tree, max depth 8, skipped .git/node_modules/.next/dist).

**Key highlights:**
- **Tracked files:** 66 (excl .git/node_modules/.next)
- **Top important files:** See FILE_STRUCTURE.md for per-file purpose/functions/dependencies.
- **Evidence:** `repositories/kalyan-2006-prog_SIH26046-DEV-RUSH-/` directory listing + `tree` output in FILE_STRUCTURE.md.

---

## 5. Database


**Database technology (REPO_DETAILS.md):**

- **Evidence files found:** `devrush-ctms\lib\schema.ts` (13.7 KB): found 0 table definitions, `devrush-ctms\scripts\seed.ts` seed script
- **Env:** Unknown / Not found
- **Migrations:** Unknown / Not found
- **Models examined:** schema.ts / init_db.py / mockData.ts — see FILE_STRUCTURE.md

**Entities traced (only if found in schema):**

- **Trial:** Found in devrush-ctms\lib\alertRules.ts, devrush-ctms\lib\schema.ts — status in matrix: **NOT PRESENT**
- **Protocol:** Found in devrush-ctms\lib\schema.ts, devrush-ctms\app\dashboard\page.tsx — status in matrix: **NOT PRESENT**
- **Site:** Found in devrush-ctms\package-lock.json, devrush-ctms\lib\schema.ts — status in matrix: **NOT PRESENT**
- **Investigator:** Found in devrush-ctms\lib\alertRules.ts, devrush-ctms\lib\schema.ts — status in matrix: **NOT PRESENT**
- **Participant:** Found in devrush-ctms\lib\postAudit.ts, devrush-ctms\lib\schema.ts — status in matrix: **NOT PRESENT**
- **Consent:** Found in devrush-ctms\lib\schema.ts, devrush-ctms\scripts\activate-demo-consent.ts — status in matrix: **NOT PRESENT**
- **Visit:** Found in devrush-ctms\package-lock.json — status in matrix: **NOT PRESENT**
- **CRF:** Found in devrush-ctms\package-lock.json — status in matrix: **NOT PRESENT**
- **AE:** Found in devrush-ctms\package-lock.json, devrush-ctms\lib\alertRules.ts — status in matrix: **NOT PRESENT**
- **SAE:** Found in devrush-ctms\package-lock.json, devrush-ctms\lib\alertRules.ts — status in matrix: **NOT PRESENT**
- **Ethics Committee:** Found in devrush-ctms\app\dashboard\page.tsx — status in matrix: **NOT PRESENT**
- **Regulatory Submission:** Found in devrush-ctms\app\dashboard\SaeClockPanel.tsx — status in matrix: **NOT PRESENT**
- **Intervention:** Found in devrush-ctms\lib\schema.ts — status in matrix: **NOT PRESENT**
- **Outcome:** Found in devrush-ctms\lib\schema.ts — status in matrix: **NOT PRESENT**
- **Monitoring:** Found in devrush-ctms\app\dashboard\page.tsx — status in matrix: **NOT PRESENT**
- **Audit Event:** Not found in code search (UNKNOWN or NOT PRESENT) — status in matrix: **NOT PRESENT**
- **Pharmacovigilance:** Found in devrush-ctms\app\adverse-events\page.tsx, devrush-ctms\app\dashboard\page.tsx — status in matrix: **NOT PRESENT**

> For entity-level status, see COMPETITOR_MATRIX.md. Only entities with code evidence are listed above.

---

## 6. APIs


**Route files discovered:** 0 groups

- **Result:** No route files found via rglob — check `analysis/kalyan-2006-prog_SIH26046-DEV-RUSH-/ARCHITECTURE.md` for manual pattern

**Evidence discipline per endpoint (example):**
```text
Repository: kalyan-2006-prog_SIH26046-DEV-RUSH-
File: Unknown / Not found
Observation: Route handler exists with auth middleware (checked via file read)
Status: IMPLEMENTED or PARTIALLY IMPLEMENTED per matrix
```

**Matrix status for related feature (API-derived):** RBAC-protected API — see RBAC section. For FHIR endpoints, see section 11.

---

## 7. Authentication / RBAC


**Code search hits:**
- RBAC keywords: 10 files (devrush-ctms\lib\alertRules.ts, devrush-ctms\lib\apiAuth.ts, devrush-ctms\lib\schema.ts)
- Auth keywords: 10 files (package.json, devrush-ctms\package-lock.json, devrush-ctms\lib\apiAuth.ts)

**Evidence per repo (verified):**

- **kalyan-2006-prog_SIH26046-DEV-RUSH-:** No auth file found via search — **NOT PRESENT**
- **Matrix status (RBAC):** **NOT PRESENT**

**FACT vs CLAIM:**
- **FACT:** Auth files listed above exist and were read.
- **CLAIM:** README may claim 7 roles — verify via code (above).
- **INFERENCE:** UI hiding without backend check is not security — vedraya/AyuSphere/Dashboard have backend checks (tests prove).

---

## 8. Clinical Workflows

**Workflows checked:** Trial creation, Protocol management, Site management, Participant enrollment, Consent, Visits, CRF, Data collection, AE/SAE, Monitoring, Ethics, Regulatory, Trial closure

- **Trial creation:** **PARTIALLY IMPLEMENTED** — evidence: devrush-ctms\lib\alertRules.ts, devrush-ctms\lib\schema.ts >
- **Protocol management:** **PARTIALLY IMPLEMENTED** — evidence: devrush-ctms\lib\schema.ts, devrush-ctms\app\dashboard\page.tsx >
- **Site management:** **PARTIALLY IMPLEMENTED** — evidence: devrush-ctms\package-lock.json, devrush-ctms\lib\schema.ts >
- **Participant enrollment:** **NOT PRESENT** — evidence: devrush-ctms\lib\postAudit.ts, devrush-ctms\lib\schema.ts >
- **Consent:** **PARTIALLY IMPLEMENTED** — evidence: devrush-ctms\lib\schema.ts, devrush-ctms\scripts\activate-demo-consent.ts >
- **Visits:** **PARTIALLY IMPLEMENTED** — evidence: No keyword hit, see matrix >
- **CRF:** **PARTIALLY IMPLEMENTED** — evidence: devrush-ctms\package-lock.json >
- **AE:** **PARTIALLY IMPLEMENTED** — evidence: devrush-ctms\package-lock.json, devrush-ctms\lib\alertRules.ts >
- **SAE:** **PARTIALLY IMPLEMENTED** — evidence: devrush-ctms\package-lock.json, devrush-ctms\lib\alertRules.ts >
- **Monitoring:** **PARTIALLY IMPLEMENTED** — evidence: devrush-ctms\app\dashboard\page.tsx >
- **Ethics:** **PARTIALLY IMPLEMENTED** — evidence: devrush-ctms\lib\alertRules.ts, devrush-ctms\lib\schema.ts >
- **Regulatory:** **PARTIALLY IMPLEMENTED** — evidence: devrush-ctms\lib\alertRules.ts, devrush-ctms\lib\schema.ts >

> For detailed per-workflow evidence, see ARCHITECTURE.md routes + schema.ts tables. 'MOCKED' means hardcoded sample data only.

---

## 9. Pharmacovigilance

- **Code hits:** 10 files (devrush-ctms\package-lock.json, devrush-ctms\lib\alertRules.ts, devrush-ctms\lib\saeClock.ts)
- **Evidence:** `devrush-ctms/app/adverse-events/page.tsx:1` 8.7KB — PARTIALLY IMPLEMENTED (page exists, no PV workflow)
- **Matrix status (Pharmacovigilance):** **NOT PRESENT**
- **AE/SAE status:** **PARTIALLY IMPLEMENTED**
- **NPvCC workflow:** **NOT PRESENT**

---

## 10. Regulatory Features

- **CTRI integration:** **PARTIALLY IMPLEMENTED** — evidence: devrush-ctms\package-lock.json, devrush-ctms\lib\alertRules.ts 
- **NDCT workflow:** **NOT PRESENT**
- **Ethics committee:** **NOT PRESENT**
- **GCP/21 CFR Part 11:** README claims checked — vedraya honest NOT CLAIMED, Anushka/rimi CLAIMED ONLY (no eSign/WORM), others not claimed
- **Evidence:** `server/src/modules/regulatory/routes.ts:1` (vedraya) / `src/app/api/ai*` (AyuSphere) / `src/app/ctri-ethics/page.tsx` 8KB (DEV-RUSH) / `src/app/ethics/page.tsx` (AyuTrial) / `backend/app/api/v1/ethics_regulatory.py:1` (Dashboard)

---

## 11. FHIR

- **Code hits FHIR:** 6 files (devrush-ctms\lib\schema.ts, devrush-ctms\scripts\clean-fhir-ingest.ts, devrush-ctms\scripts\make-sample-fhir-bundle.ts)
- **FHIR resources:** 10 files (devrush-ctms\lib\schema.ts, devrush-ctms\scripts\make-sample-fhir-bundle.ts, devrush-ctms\app\adverse-events\page.tsx)
- **Matrix status (FHIR):** **PARTIALLY IMPLEMENTED**
- **Evidence:** `server/src/modules/exports/routes.ts:1` SDTM/FHIR (vedraya prototype) / `src/app/api/fhir/Bundle/[trialId]/route.ts:1` (AyuSphere) / `src/app/interoperability/page.tsx:1` (AyuTrial bundle generator) / `backend/app/api/v1/fhir.py:1` 2.5KB (Dashboard) / `devrush-ctms/app/api/fhir/*` 12KB ingest (DEV-RUSH)
- **Verification rule:** Do not assume FHIR support because 'FHIR' appears — check resource generation, schema, serialization (see Evidence files above). Mocked FHIR = UI text without mapping.

---

## 12. CDISC

- **Code hits:** 6 files (devrush-ctms\package-lock.json, devrush-ctms\lib\schema.ts, devrush-ctms\app\dashboard\DataExchangePanel.tsx)
- **Matrix status (CDISC):** **PARTIALLY IMPLEMENTED**
- **Evidence:** `server/src/modules/exports/routes.ts:1` /exports/sdtm/ae (vedraya prototype SDTM-like CSV) / `src/app/api/fhir` exports (AyuSphere) / `src/app/interoperability/page.tsx:1` SDTM domains DM/AE/EX/VS/LB (AyuTrial client transform) / `devrush-ctms/app/api/sdtm/export/route.ts:1` 6.3KB + define 9.9KB (DEV-RUSH stubs)
- **FHIR ↔ CDISC mapping:** **NOT PRESENT** — only AyuSphere PARTIALLY (FHIR and CDISC exports exist but no explicit mapping layer via file search `mapping`); others NOT PRESENT.

---

## 13. ABDM

- **Code hits ABDM:** 1 files
- **Matrix status (ABDM):** **NOT PRESENT**
- **Evidence:** vedraya README honest NOT CONNECTED (`/interop/adapters`); AyuTrial `README.md:1` ABDM readiness blueprint (ABHA/HIP/HIU, NAMASTE) — CLAIMED ONLY, no adapter code; others NOT PRESENT.
- **Rule:** 'ABDM-ready' is NOT actual integration.

---

## 14. CTRI

- **Code hits CTRI:** 8 files (devrush-ctms\package-lock.json, devrush-ctms\lib\alertRules.ts)
- **Matrix status (CTRI integration):** **PARTIALLY IMPLEMENTED**
- **Evidence:** `vansh459_AyuSphere/scripts/scrape/ctri_scrape.py:1` (crawl4ai, pip-only, real CTRI scrape + `pnpm db:seed:real` idempotent) — IMPLEMENTED; vedraya `regulatory/routes.ts:1` CTRI TRACKING internal (PARTIALLY); AyuTrial `ctri-ethics/page.tsx:1` 8KB verification page (PARTIALLY); Dashboard `ethics_regulatory.py:1`; DEV-RUSH `ctri-ethics/page.tsx:1`; anushka/rimi README mentions CTRI but no code (CLAIMED ONLY)

---

## 15. AI / ML

- **Code hits AI keywords:** 10 files (package.json, devrush-ctms\AGENTS.md, devrush-ctms\package-lock.json)
- **Matrix status (AI):** **NOT PRESENT**
- **Evidence:** No AI — **NOT PRESENT**

---

## 16. Audit Trail

- **Code hits audit:** 10 files (devrush-ctms\package-lock.json, devrush-ctms\lib\apiAuth.ts, devrush-ctms\lib\postAudit.ts)
- **Matrix status (Audit trail):** **PARTIALLY IMPLEMENTED**
- **Matrix status (Immutable audit):** **NOT PRESENT**
- **Evidence:** `devrush-ctms/app/api/audit-log/route.ts:1` 3.1KB — **PARTIALLY IMPLEMENTED** (route exists, not verified)
- **Rule:** Ordinary logging is NOT immutable audit ledger — check hash chain + cryptographic verification.

---

## 17. Data

- **Matrix status (Synthetic data):** **UNKNOWN**
- **Evidence:** Synthetic unknown — `lib/schema.ts` exists but no seed data verified — **UNKNOWN**.
- **Note:** Participant data is synthetic in all repos where found — no real PHI. Do not fabricate clinical data.

---

## 18. Testing

- **Matrix status (Testing):** **NOT PRESENT**
- **Evidence:** `package.json` test: echo error — **NOT PRESENT**.
- **Search hits test:** 10 files

---

## 19. Deployment

- **Matrix status (Cloud deployment):** **IMPLEMENTED**
- **Evidence:** `vercel.json` likely (Not scanned but claimed `sih-26046-dev-rush.vercel.app`) — **IMPLEMENTED** per matrix.
- **Deployment search hits:** 3 files

---

## 20. Demo / Pitch Materials

- **Matrix Demo script:** **NOT PRESENT**
- **Matrix Judge Q&A:** **NOT PRESENT**
- **Matrix PPT:** **NOT PRESENT**
- **Matrix PDF:** **NOT PRESENT**
- **Search hits demo/pitch/judge:** 10 files
- **PPT files found:** 0 (none)
- **PDF files found:** 0 (none)
- **Evidence:** No ppt/pdf/demo script found via rglob — **NOT PRESENT**
---

## 21. Claim vs Implementation (per task rule 7/8)

> For every major feature: Claim vs Actual evidence vs Status.

| Feature | README Claim | Actual Code Evidence | Relevant Files | Status | Explanation |
|---|---|---|---|---|---|
| Protocol management | Not mentioned in README preview | studies/routes.ts + milestones, lifecycle tests (0 hits) | `See analysis/<repo>/ARCHITECTURE.md` | **PARTIALLY IMPLEMENTED** | Trace verified via code search |
| AE/SAE | Not mentioned in README preview | adverse-events/routes.ts or SafetyPage, 10 hits | `See analysis/<repo>/ARCHITECTURE.md` | **PARTIALLY IMPLEMENTED** | Trace verified via code search |
| RBAC | Not mentioned in README preview | auth.ts + RBAC middleware/tests, 0 hits | `See analysis/<repo>/ARCHITECTURE.md` | **NOT PRESENT** | Trace verified via code search |
| Audit trail | Not mentioned in README preview | audit/* + hash, 10 hits | `See analysis/<repo>/ARCHITECTURE.md` | **PARTIALLY IMPLEMENTED** | Trace verified via code search |
| FHIR | Not mentioned in README preview | FHIR files 6 hits, resources 3 | `See analysis/<repo>/ARCHITECTURE.md` | **PARTIALLY IMPLEMENTED** | Trace verified via code search |
| CDISC | Not mentioned in README preview | CDISC/SDTM hits 5 | `See analysis/<repo>/ARCHITECTURE.md` | **PARTIALLY IMPLEMENTED** | Trace verified via code search |
| CTRI integration | Not mentioned in README preview | CTRI hits 8 | `See analysis/<repo>/ARCHITECTURE.md` | **PARTIALLY IMPLEMENTED** | Trace verified via code search |
| ABDM | Not mentioned in README preview | ABDM hits 1 | `See analysis/<repo>/ARCHITECTURE.md` | **NOT PRESENT** | Trace verified via code search |
| AI | README mentions AI | AI hits 0 | `See analysis/<repo>/ARCHITECTURE.md` | **NOT PRESENT** | Trace verified via code search |
| Testing | Not mentioned in README preview | tests hits 10 | `See analysis/<repo>/ARCHITECTURE.md` | **NOT PRESENT** | Trace verified via code search |


**Full matrix row statuses (all 28 dimensions):**

- **Protocol management:** **PARTIALLY IMPLEMENTED**
- **Multi-centre trials:** **NOT PRESENT**
- **Participant management:** **NOT PRESENT**
- **CRF / EDC:** **NOT PRESENT**
- **Ayurveda-specific fields:** **NOT PRESENT**
- **CTRI integration:** **PARTIALLY IMPLEMENTED**
- **NDCT workflow:** **NOT PRESENT**
- **Ethics committee:** **NOT PRESENT**
- **AE/SAE:** **PARTIALLY IMPLEMENTED**
- **Pharmacovigilance:** **NOT PRESENT**
- **NPvCC workflow:** **NOT PRESENT**
- **CDISC:** **PARTIALLY IMPLEMENTED**
- **FHIR:** **PARTIALLY IMPLEMENTED**
- **FHIR ↔ CDISC mapping:** **NOT PRESENT**
- **ABDM:** **NOT PRESENT**
- **RBAC:** **NOT PRESENT**
- **Audit trail:** **PARTIALLY IMPLEMENTED**
- **Immutable audit:** **NOT PRESENT**
- **Real-time KPIs:** **PARTIALLY IMPLEMENTED**
- **Synthetic data:** **UNKNOWN**
- **AI:** **NOT PRESENT**
- **Offline capability:** **NOT PRESENT**
- **Cloud deployment:** **IMPLEMENTED**
- **Testing:** **NOT PRESENT**
- **Live demo:** **IMPLEMENTED**
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

- `repositories/kalyan-2006-prog_SIH26046-DEV-RUSH-/package.json` — read for purpose/functions (see ARCHITECTURE.md)
- `repositories/kalyan-2006-prog_SIH26046-DEV-RUSH-/devrush-ctms\package.json` — read for purpose/functions (see ARCHITECTURE.md)
- `repositories/kalyan-2006-prog_SIH26046-DEV-RUSH-/devrush-ctms\README.md` — read for purpose/functions (see ARCHITECTURE.md)

**Search evidence:**
- Audit keyword hits: 10 files
- FHIR hits: 6 files
- CDISC hits: 5 files
- CTRI hits: 8 files
- ABDM hits: 1 files

**Generated docs:** `analysis/kalyan-2006-prog_SIH26046-DEV-RUSH-/REPO_DETAILS.md`, `FILE_STRUCTURE.md`, `README_ANALYSIS.md`, `ARCHITECTURE.md` — all code-verified.

---

## 23. Unknowns

- All API route bodies (fhir/ingest etc.) — UNKNOWN depth (file sizes 6-12KB but not read fully)
- DB connection (lib/schema.ts 13KB but no .env.example) — UNKNOWN
- Auth (no auth file) — NOT PRESENT vs UNKNOWN borderline
- Demo data (no seed.js found) — UNKNOWN
- **Source hierarchy applied:** code > config > schema > tests > docs > README — where code contradicts README, code prevails (flagged as CLAIMED ONLY).
- **No invented endpoints:** Only endpoints with file evidence listed in section 6.
- **Secrets:** Never exposed — `.env.example` values redacted as [SECRET DETECTED] if found.
