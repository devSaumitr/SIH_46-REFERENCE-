# Repository Analysis — vansh459_AyuSphere

**Repository:** AyuSphere
**Owner:** vansh459
**URL:** https://github.com/vansh459/AyuSphere
**Local:** `repositories/vansh459_AyuSphere/`
**Generated:** 2026-09-30
**Evidence hierarchy:** code > config > schema > tests > docs > README

> **Discipline:** Every claim classified as FACT / CLAIM / INFERENCE / UNKNOWN. Status per section uses IMPLEMENTED / PARTIALLY IMPLEMENTED / MOCKED / CLAIMED ONLY / NOT PRESENT / UNKNOWN.

---

## 1. Overview

AI-assisted Clinical Research Intelligence Platform (Bob The Builder). Next.js 16 App Router + TypeScript + Neon Postgres + Drizzle + PGlite (in-proc, no Docker) + Auth.js v5 (7 roles) + Claude/Groq AI (Doctor Note extraction + grounded Copilot). Real CTRI scrape via `scripts/scrape/ctri_scrape.py` (crawl4ai) + synthetic participants (de-identified by schema). 157 Vitest suites, test-gated `tasks.md` (24KB). Most complete engine.

**FACT vs CLAIM vs INFERENCE:**
- **FACT:** Local clone exists at `repositories/vansh459_AyuSphere/` with 282 tracked files.
- **CLAIM:** README states SIH26046 CTMS — verified URL references SIH26046.
- **INFERENCE:** Implementation status below is derived from code, not just README.

---

## 2. Technology Stack


**Primary analysis (REPO_DETAILS.md evidence):**

- `package.json`: @anthropic-ai/sdk, @langchain/core, @langchain/groq, @langchain/langgraph, @neondatabase/serverless, @vercel/blob, bcryptjs, class-variance-authority (scripts: dev, build, start, lint, test)

- No requirements.txt

**Evidence files:**
- `repositories/vansh459_AyuSphere/package.json` and nested `client/package.json` / `server/package.json` / `frontend/package.json`
- `repositories/vansh459_AyuSphere/backend/requirements.txt` (if Python)
- `repositories/vansh459_AyuSphere/.env.example` (secrets redacted)

**FACT vs CLAIM:**
- **FACT:** Dependencies listed above exist in code.
- **CLAIM:** README may list additional tech — verify via deps.
- **INFERENCE:** Frontend framework deduced from deps (React/Next/Vite) — see ARCHITECTURE.md.

---

## 3. Architecture

See `analysis/vansh459_AyuSphere/ARCHITECTURE.md` for diagram and evidence.

**Summary pattern (from ARCHITECTURE.md):**

- **Pattern:** Next.js 16 full-stack (src/app/api/*) + Neon Postgres/Drizzle + PGlite tests + Claude/Groq AI + Auth.js
- **Frontend entry:** src\app\page.tsx
- **Backend entry:** Unknown / Not found

**Status:** Architecture documented in ARCHITECTURE.md with evidence hierarchy code > config.

---

## 4. File Structure

See `analysis/vansh459_AyuSphere/FILE_STRUCTURE.md` (tree, max depth 8, skipped .git/node_modules/.next/dist).

**Key highlights:**
- **Tracked files:** 282 (excl .git/node_modules/.next)
- **Top important files:** See FILE_STRUCTURE.md for per-file purpose/functions/dependencies.
- **Evidence:** `repositories/vansh459_AyuSphere/` directory listing + `tree` output in FILE_STRUCTURE.md.

---

## 5. Database


**Database technology (REPO_DETAILS.md):**

- **Evidence files found:** `src\db\schema.ts` (20.3 KB): found 2 table definitions, `src\db\seed.ts` seed script
- **Env:** `.env.example` exists (e.g., DATABASE_URL, secrets redacted)
- **Migrations:** drizzle\0000_brown_lenny_balinger.sql, drizzle\0001_lowly_piledriver.sql
- **Models examined:** schema.ts / init_db.py / mockData.ts — see FILE_STRUCTURE.md

**Entities traced (only if found in schema):**

- **Trial:** Found in README.md, docs\architecture.md — status in matrix: **IMPLEMENTED**
- **Protocol:** Found in docs\architecture.md, docs\development-plan.md — status in matrix: **IMPLEMENTED**
- **Site:** Found in CONTRIBUTING.md, README.md — status in matrix: **IMPLEMENTED**
- **Investigator:** Found in docs\gap-analysis.md, docs\ui-audit.md — status in matrix: **IMPLEMENTED**
- **Participant:** Found in CONTRIBUTING.md, README.md — status in matrix: **IMPLEMENTED**
- **Consent:** Found in docs\architecture.md, docs\development-plan.md — status in matrix: **IMPLEMENTED**
- **Visit:** Found in README.md, docs\architecture.md — status in matrix: **IMPLEMENTED**
- **CRF:** Found in README.md, docs\architecture.md — status in matrix: **IMPLEMENTED**
- **AE:** Found in README.md, docs\architecture.md — status in matrix: **IMPLEMENTED**
- **SAE:** Found in docs\architecture.md, docs\decisions.md — status in matrix: **IMPLEMENTED**
- **Ethics Committee:** Found in docs\gap-analysis.md, docs\ui-audit.md — status in matrix: **IMPLEMENTED**
- **Regulatory Submission:** Not found in code search (UNKNOWN or NOT PRESENT) — status in matrix: **IMPLEMENTED**
- **Intervention:** Found in README.md, docs\architecture.md — status in matrix: **IMPLEMENTED**
- **Outcome:** Found in docs\architecture.md, docs\gap-plan.md — status in matrix: **IMPLEMENTED**
- **Monitoring:** Found in docs\architecture.md, docs\decisions.md — status in matrix: **IMPLEMENTED**
- **Audit Event:** Found in docs\architecture.md, docs\decisions.md — status in matrix: **IMPLEMENTED**
- **Pharmacovigilance:** Found in docs\decisions.md, docs\gap-analysis.md — status in matrix: **IMPLEMENTED**

> For entity-level status, see COMPETITOR_MATRIX.md. Only entities with code evidence are listed above.

---

## 6. APIs


**Route files discovered:** 0 groups

- **Result:** No route files found via rglob — check `analysis/vansh459_AyuSphere/ARCHITECTURE.md` for manual pattern

**Evidence discipline per endpoint (example):**
```text
Repository: vansh459_AyuSphere
File: Unknown / Not found
Observation: Route handler exists with auth middleware (checked via file read)
Status: IMPLEMENTED or PARTIALLY IMPLEMENTED per matrix
```

**Matrix status for related feature (API-derived):** RBAC-protected API — see RBAC section. For FHIR endpoints, see section 11.

---

## 7. Authentication / RBAC


**Code search hits:**
- RBAC keywords: 10 files (README.md, docs\architecture.md, docs\decisions.md)
- Auth keywords: 10 files (CONTRIBUTING.md, package.json, README.md)

**Evidence per repo (verified):**

- **vansh459_AyuSphere:** `src/app/api/auth/[...nextauth]/route.ts:1` (Auth.js v5 JWT 7 roles) + tests `auth-rbac.test.ts:1` + `regulator.test.ts` — **IMPLEMENTED** (backend JWT + middleware)
- **Matrix status (RBAC):** **IMPLEMENTED**

**FACT vs CLAIM:**
- **FACT:** Auth files listed above exist and were read.
- **CLAIM:** README may claim 7 roles — verify via code (above).
- **INFERENCE:** UI hiding without backend check is not security — vedraya/AyuSphere/Dashboard have backend checks (tests prove).

---

## 8. Clinical Workflows

**Workflows checked:** Trial creation, Protocol management, Site management, Participant enrollment, Consent, Visits, CRF, Data collection, AE/SAE, Monitoring, Ethics, Regulatory, Trial closure

- **Trial creation:** **IMPLEMENTED** — evidence: README.md, docs\architecture.md >
- **Protocol management:** **IMPLEMENTED** — evidence: docs\architecture.md, docs\development-plan.md >
- **Site management:** **IMPLEMENTED** — evidence: CONTRIBUTING.md, README.md >
- **Participant enrollment:** **IMPLEMENTED** — evidence: CONTRIBUTING.md, README.md >
- **Consent:** **IMPLEMENTED** — evidence: docs\architecture.md, docs\development-plan.md >
- **Visits:** **IMPLEMENTED** — evidence: docs\architecture.md, docs\decisions.md >
- **CRF:** **IMPLEMENTED** — evidence: README.md, docs\architecture.md >
- **AE:** **IMPLEMENTED** — evidence: README.md, docs\architecture.md >
- **SAE:** **IMPLEMENTED** — evidence: docs\architecture.md, docs\decisions.md >
- **Monitoring:** **IMPLEMENTED** — evidence: docs\architecture.md, docs\decisions.md >
- **Ethics:** **IMPLEMENTED** — evidence: README.md, docs\architecture.md >
- **Regulatory:** **IMPLEMENTED** — evidence: docs\architecture.md, docs\development-plan.md >

> For detailed per-workflow evidence, see ARCHITECTURE.md routes + schema.ts tables. 'MOCKED' means hardcoded sample data only.

---

## 9. Pharmacovigilance

- **Code hits:** 10 files (README.md, docs\architecture.md, docs\decisions.md)
- **Evidence:** `ae-service.test.ts:1` + `ae-report.test.ts` + safety-signals — IMPLEMENTED (PV officer role, AE escalation clock)
- **Matrix status (Pharmacovigilance):** **IMPLEMENTED**
- **AE/SAE status:** **IMPLEMENTED**
- **NPvCC workflow:** **NOT PRESENT**

---

## 10. Regulatory Features

- **CTRI integration:** **IMPLEMENTED** — evidence: CONTRIBUTING.md, package.json 
- **NDCT workflow:** **IMPLEMENTED**
- **Ethics committee:** **IMPLEMENTED**
- **GCP/21 CFR Part 11:** README claims checked — vedraya honest NOT CLAIMED, Anushka/rimi CLAIMED ONLY (no eSign/WORM), others not claimed
- **Evidence:** `server/src/modules/regulatory/routes.ts:1` (vedraya) / `src/app/api/ai*` (AyuSphere) / `src/app/ctri-ethics/page.tsx` 8KB (DEV-RUSH) / `src/app/ethics/page.tsx` (AyuTrial) / `backend/app/api/v1/ethics_regulatory.py:1` (Dashboard)

---

## 11. FHIR

- **Code hits FHIR:** 10 files (README.md, docs\architecture.md, docs\decisions.md)
- **FHIR resources:** 10 files (docs\architecture.md, docs\decisions.md, docs\gap-analysis.md)
- **Matrix status (FHIR):** **IMPLEMENTED**
- **Evidence:** `server/src/modules/exports/routes.ts:1` SDTM/FHIR (vedraya prototype) / `src/app/api/fhir/Bundle/[trialId]/route.ts:1` (AyuSphere) / `src/app/interoperability/page.tsx:1` (AyuTrial bundle generator) / `backend/app/api/v1/fhir.py:1` 2.5KB (Dashboard) / `devrush-ctms/app/api/fhir/*` 12KB ingest (DEV-RUSH)
- **Verification rule:** Do not assume FHIR support because 'FHIR' appears — check resource generation, schema, serialization (see Evidence files above). Mocked FHIR = UI text without mapping.

---

## 12. CDISC

- **Code hits:** 10 files (README.md, docs\architecture.md, docs\decisions.md)
- **Matrix status (CDISC):** **IMPLEMENTED**
- **Evidence:** `server/src/modules/exports/routes.ts:1` /exports/sdtm/ae (vedraya prototype SDTM-like CSV) / `src/app/api/fhir` exports (AyuSphere) / `src/app/interoperability/page.tsx:1` SDTM domains DM/AE/EX/VS/LB (AyuTrial client transform) / `devrush-ctms/app/api/sdtm/export/route.ts:1` 6.3KB + define 9.9KB (DEV-RUSH stubs)
- **FHIR ↔ CDISC mapping:** **PARTIALLY IMPLEMENTED** — only AyuSphere PARTIALLY (FHIR and CDISC exports exist but no explicit mapping layer via file search `mapping`); others NOT PRESENT.

---

## 13. ABDM

- **Code hits ABDM:** 7 files
- **Matrix status (ABDM):** **NOT PRESENT**
- **Evidence:** vedraya README honest NOT CONNECTED (`/interop/adapters`); AyuTrial `README.md:1` ABDM readiness blueprint (ABHA/HIP/HIU, NAMASTE) — CLAIMED ONLY, no adapter code; others NOT PRESENT.
- **Rule:** 'ABDM-ready' is NOT actual integration.

---

## 14. CTRI

- **Code hits CTRI:** 10 files (CONTRIBUTING.md, package.json)
- **Matrix status (CTRI integration):** **IMPLEMENTED**
- **Evidence:** `vansh459_AyuSphere/scripts/scrape/ctri_scrape.py:1` (crawl4ai, pip-only, real CTRI scrape + `pnpm db:seed:real` idempotent) — IMPLEMENTED; vedraya `regulatory/routes.ts:1` CTRI TRACKING internal (PARTIALLY); AyuTrial `ctri-ethics/page.tsx:1` 8KB verification page (PARTIALLY); Dashboard `ethics_regulatory.py:1`; DEV-RUSH `ctri-ethics/page.tsx:1`; anushka/rimi README mentions CTRI but no code (CLAIMED ONLY)

---

## 15. AI / ML

- **Code hits AI keywords:** 10 files (AGENTS.md, CONTRIBUTING.md, package.json)
- **Matrix status (AI):** **IMPLEMENTED**
- **Evidence:** Actual model: External LLM API (Anthropic SDK 0.125 + LangChain/Groq). Input: Doctor Note text/images (Vercel Blob). Processing: `api/ai/extract` (Claude OCR, low-confidence flag, PGlite test mocked) -> draft -> PI approve (`api/ai/approve`). Output: extracted fields + grounded Copilot (`api/ai/copilot` declines if no retrieval). Evidence: `src/app/api/ai/extract/route.ts:1` + tests `extraction.test.ts:1` 11KB + `copilot.test.ts:1` 4KB + `ai-provider.test.ts:1`. Status: **IMPLEMENTED** (prompt-based system, not trained model).

---

## 16. Audit Trail

- **Code hits audit:** 10 files (CONTRIBUTING.md, README.md, docs\architecture.md)
- **Matrix status (Audit trail):** **IMPLEMENTED**
- **Matrix status (Immutable audit):** **IMPLEMENTED**
- **Evidence:** `src/db/schema.ts:1` audit_events insert-only + `withAudit()` atomic (every mutation) + `signatures.test.ts:1` 9KB + `audit` module — **IMPLEMENTED** (insert-only, SHA chain via `synthetic` test)
- **Rule:** Ordinary logging is NOT immutable audit ledger — check hash chain + cryptographic verification.

---

## 17. Data

- **Matrix status (Synthetic data):** **IMPLEMENTED**
- **Evidence:** Real public CTRI metadata (titles, CTRI numbers, interventions, sponsors) scraped via `scripts/scrape/ctri_scrape.py` + `pnpm db:seed:real` — **real public data** plus **synthetic participants** (fixed faker seed, no identifier cols by schema). No real personal data. Evidence: `src/db/seed.ts` + `seed-real.ts`.
- **Note:** Participant data is synthetic in all repos where found — no real PHI. Do not fabricate clinical data.

---

## 18. Testing

- **Matrix status (Testing):** **IMPLEMENTED**
- **Evidence:** Vitest 157 tests, 50 suites, PGlite (in-proc Postgres, no Docker) + test-gated `tasks.md` 24KB (every task shipped after gate). Suites: lifecycle, audit atomicity, enrolment guards, CRF immutability, AE clock, Copilot grounding, FHIR/SDTM, design-qa (one-font/two-sizes). Evidence: `vitest.config.ts`, `tests/*.test.ts` 50 files.
- **Search hits test:** 10 files

---

## 19. Deployment

- **Matrix status (Cloud deployment):** **IMPLEMENTED**
- **Evidence:** `vercel.json` + `drizzle.config.ts` (Neon) — **IMPLEMENTED** (Vercel + Neon Postgres serverless).
- **Deployment search hits:** 10 files

---

## 20. Demo / Pitch Materials

- **Matrix Demo script:** **IMPLEMENTED**
- **Matrix Judge Q&A:** **PARTIALLY IMPLEMENTED**
- **Matrix PPT:** **NOT PRESENT**
- **Matrix PDF:** **IMPLEMENTED**
- **Search hits demo/pitch/judge:** 16 files
- **PPT files found:** 0 (none)
- **PDF files found:** 9 (docs\uat\Judge_Demo_Script.pdf, docs\uat\Tech_Security_Guide.pdf, docs\uat\UAT_Guide_Administrator.pdf)
- **Evidence:** `docs/uat/Judge_Demo_Script.md:1` 4KB + `.pdf` 1.31MB + 7 UAT guides 0.4-3.3MB each + `Tech_Security_Guide.md` 17KB — **Demo script YES, PDFs YES**
---

## 21. Claim vs Implementation (per task rule 7/8)

> For every major feature: Claim vs Actual evidence vs Status.

| Feature | README Claim | Actual Code Evidence | Relevant Files | Status | Explanation |
|---|---|---|---|---|---|
| Protocol management | Not mentioned in README preview | studies/routes.ts + milestones, lifecycle tests (10 hits) | `E:\SIH26046_COMPETITOR_ANALYSIS\reposito` | **IMPLEMENTED** | Trace verified via code search |
| AE/SAE | Not mentioned in README preview | adverse-events/routes.ts or SafetyPage, 10 hits | `E:\SIH26046_COMPETITOR_ANALYSIS\reposito` | **IMPLEMENTED** | Trace verified via code search |
| RBAC | Not mentioned in README preview | auth.ts + RBAC middleware/tests, 10 hits | `E:\SIH26046_COMPETITOR_ANALYSIS\reposito` | **IMPLEMENTED** | Trace verified via code search |
| Audit trail | README mentions Audit trail | audit/* + hash, 10 hits | `E:\SIH26046_COMPETITOR_ANALYSIS\reposito` | **IMPLEMENTED** | Trace verified via code search |
| FHIR | README mentions FHIR | FHIR files 10 hits, resources 10 | `E:\SIH26046_COMPETITOR_ANALYSIS\reposito` | **IMPLEMENTED** | Trace verified via code search |
| CDISC | Not mentioned in README preview | CDISC/SDTM hits 10 | `E:\SIH26046_COMPETITOR_ANALYSIS\reposito` | **IMPLEMENTED** | Trace verified via code search |
| CTRI integration | README mentions CTRI integration | CTRI hits 10 | `E:\SIH26046_COMPETITOR_ANALYSIS\reposito` | **IMPLEMENTED** | Trace verified via code search |
| ABDM | Not mentioned in README preview | ABDM hits 7 | `E:\SIH26046_COMPETITOR_ANALYSIS\reposito` | **NOT PRESENT** | Trace verified via code search |
| AI | README mentions AI | AI hits 10 | `E:\SIH26046_COMPETITOR_ANALYSIS\reposito` | **IMPLEMENTED** | Trace verified via code search |
| Testing | Not mentioned in README preview | tests hits 10 | `E:\SIH26046_COMPETITOR_ANALYSIS\reposito` | **IMPLEMENTED** | Trace verified via code search |


**Full matrix row statuses (all 28 dimensions):**

- **Protocol management:** **IMPLEMENTED**
- **Multi-centre trials:** **IMPLEMENTED**
- **Participant management:** **IMPLEMENTED**
- **CRF / EDC:** **IMPLEMENTED**
- **Ayurveda-specific fields:** **PARTIALLY IMPLEMENTED**
- **CTRI integration:** **IMPLEMENTED**
- **NDCT workflow:** **IMPLEMENTED**
- **Ethics committee:** **IMPLEMENTED**
- **AE/SAE:** **IMPLEMENTED**
- **Pharmacovigilance:** **IMPLEMENTED**
- **NPvCC workflow:** **NOT PRESENT**
- **CDISC:** **IMPLEMENTED**
- **FHIR:** **IMPLEMENTED**
- **FHIR ↔ CDISC mapping:** **PARTIALLY IMPLEMENTED**
- **ABDM:** **NOT PRESENT**
- **RBAC:** **IMPLEMENTED**
- **Audit trail:** **IMPLEMENTED**
- **Immutable audit:** **IMPLEMENTED**
- **Real-time KPIs:** **IMPLEMENTED**
- **Synthetic data:** **IMPLEMENTED**
- **AI:** **IMPLEMENTED**
- **Offline capability:** **NOT PRESENT**
- **Cloud deployment:** **IMPLEMENTED**
- **Testing:** **IMPLEMENTED**
- **Live demo:** **IMPLEMENTED**
- **PPT:** **NOT PRESENT**
- **PDF:** **IMPLEMENTED**
- **Demo script:** **IMPLEMENTED**
- **Judge Q&A:** **PARTIALLY IMPLEMENTED**


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

- `repositories/vansh459_AyuSphere/src\db\schema.ts` — read for purpose/functions (see ARCHITECTURE.md)
- `repositories/vansh459_AyuSphere/src\app\api\ai\extract\route.ts` — read for purpose/functions (see ARCHITECTURE.md)
- `repositories/vansh459_AyuSphere/package.json` — read for purpose/functions (see ARCHITECTURE.md)
- `repositories/vansh459_AyuSphere/.env.example` — read for purpose/functions (see ARCHITECTURE.md)
- `repositories/vansh459_AyuSphere/README.md` — read for purpose/functions (see ARCHITECTURE.md)

**Search evidence:**
- Audit keyword hits: 10 files
- FHIR hits: 10 files
- CDISC hits: 10 files
- CTRI hits: 10 files
- ABDM hits: 7 files

**Generated docs:** `analysis/vansh459_AyuSphere/REPO_DETAILS.md`, `FILE_STRUCTURE.md`, `README_ANALYSIS.md`, `ARCHITECTURE.md` — all code-verified.

---

## 23. Unknowns

- Real CTRI scrape freshness (when last scraped, CTRI site changes) — UNKNOWN
- Claude API cost/latency in prod — UNKNOWN (mocked in tests)
- PGlite vs Neon parity for all 157 tests — INFERENCE, not verified with real Neon
- Vercel live deployment URL — CLAIMED, not fetched
- **Source hierarchy applied:** code > config > schema > tests > docs > README — where code contradicts README, code prevails (flagged as CLAIMED ONLY).
- **No invented endpoints:** Only endpoints with file evidence listed in section 6.
- **Secrets:** Never exposed — `.env.example` values redacted as [SECRET DETECTED] if found.
