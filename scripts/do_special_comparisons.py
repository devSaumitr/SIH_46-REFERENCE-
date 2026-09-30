#!/usr/bin/env python3
import pathlib, re
BASE = pathlib.Path(r"E:\SIH26046_COMPETITOR_ANALYSIS")
REPOS = BASE/"repositories"
OUT = BASE/"presentation_analysis"
COMP = OUT/"comparisons"
COMP.mkdir(parents=True, exist_ok=True)

# Helper read
def read(p): 
    try: return p.read_text(encoding="utf-8", errors="ignore")
    except: return ""

# --- VEDRAYA special ---
ved_path = REPOS/"nishant-uxs_vedraya"
ved_demo = read(ved_path/"docs/DEMO_SCRIPT.md")
ved_judge = read(ved_path/"docs/JUDGE_QA.md")
ved_trace = read(ved_path/"docs/SIH26046_TRACEABILITY_FINAL.md")
ved_arch = read(ved_path/"docs/ARCHITECTURE.md")
ved_readme = read(ved_path/"README.md")
ved_special = f"""# VEDRAYA Special Extraction — Judge Intelligence

**Repository:** `nishant-uxs_vedraya` (`https://github.com/nishant-uxs/vedraya`)
**Generated:** 2026-09-30
**Files analyzed:** `docs/DEMO_SCRIPT.md` (3.0 KB), `docs/JUDGE_QA.md` (3.5 KB), `docs/SIH26046_TRACEABILITY_FINAL.md` (8.0 KB), `docs/ARCHITECTURE.md` (5.5 KB), `docs/` (14 md), `README.md` (16.3 KB)

## 1. Demo Sequence (from DEMO_SCRIPT.md)

```markdown
{ved_demo[:6000]}
```

**Analysis:**
- **What shown first:** Open app → Enter Live Command Center → login `admin@vedraya.demo` (password `Vedraya!Demo1`) → confirm badge **Command Center · Live PostgreSQL** → open study **AYU-024** → Sites/Investigators/Participants → Safety AE → DEMO MedDRA coding → escalate SAE → reporting due / notify → Consents + Regulatory (IEC / CTRI TRACKING / NDCT) → Quality + alerts → Audit **Re-verify SHA-256 chain** → `AUDIT CHAIN: VERIFIED` → Exports/Interop (SDTM-like, FHIR prototype, adapters NOT CONNECTED) → logout → `monitor@vedraya.demo` (AYU-024 only) → `regulator@vedraya.demo` (no create UI, API 403)
- **Prerequisite:** `npm run demo:seed` (clears E2E-ST-* pollution, restores AYU-* portfolio)
- **Timing:** 9 steps, 60-second judge flow (README Judge in 60 seconds + docs/DEMO_SCRIPT.md)
- **Evidence shown:** Live PostgreSQL numbers after sign-in (README notes marketing landing is conceptual, live numbers from PG), deterministic seed.

## 2. Judge Questions Anticipated (from JUDGE_QA.md)

```markdown
{ved_judge[:6000]}
```

**Categories extracted (heuristic):**
- Technical: WORM? → NOT WORM but hash-chain verify; Auth: Argon2 + sid + CSRF; RBAC 7 + ACL
- Security: Audit tamper → valid:false test; Rate limiting pluggable
- Regulatory: Licensed MedDRA? → DEMO dictionary MEDDRA_DEMO, not licensed; CDISC certified? → SDTM-like prototype, not certified
- Architecture: ABDM/HIS/EDC connected? → NOT CONNECTED (`/interop/adapters`)
- Data: Real patient? → Synthetic only, de-identified
- Compliance: GCP-ASU/DPDP certified? → Process support, not certified (LIMITATIONS.md)
- Deployment: Where hosted? → Vercel SPA only (API + Postgres separate per README)
- See `analysis/nishant-uxs_vedraya/JUDGE_QA_ANALYSIS.md:1` for per-question categories.

## 3. PS Mapping (from SIH26046_TRACEABILITY_FINAL.md)

```markdown
{ved_trace[:6000]}
```

**Heuristic extraction:** Table rows with SIH requirement → Claimed implementation → Actual evidence. Example rows (first 5):
{chr(10).join(read(ved_path/"docs/SIH26046_TRACEABILITY_FINAL.md").splitlines()[:20])}

**Evidence vs claim per task 21:** Use `analysis/nishant-uxs_vedraya/TRACEABILITY_ANALYSIS.md:1` + `REPO_ANALYSIS.md:21` matrix. Honest Implemented/Partial/Prototype/Not Connected table in `docs/IMPLEMENTATION_STATUS.md:1` 1.5KB lists what has code vs not.

## 4. Claimed Differentiators (from README)

- **Stated differentiator:** Auditable RBAC + study membership ACL (monitor AYU-024 only) + GLOBAL SHA-256 hash chain re-verify (not WORM) + honest prototype-only scope + PS traceability.
- **Architecture differentiator:** Modular monolith (not microservices), 14 domain modules, 5 Drizzle migrations, separate Vercel SPA vs Render API.

## 5. Evidence (what actually demonstrated)

- **Implemented (code):** Auth (Argon2, sid), RBAC 7 (`ROLE_DEFS`), ACL (`studyAccess.ts`), studies/sites/participants/milestones, KPIs, consent, audit chain verified (`api.audit.integrity.test.ts:1` tamper → valid:false, seed → valid:true), Command Center UI (`src/components/sections/CommandCenter.tsx`)
- **Partial:** Regulatory/CTRI/NDCT tracking internal, no external CTRI API
- **Prototype:** MedDRA_DEMO/WHODRUG_DEMO (not licensed), SDTM-like AE CSV, FHIR R4 ResearchStudy/Subject
- **Not Connected:** ABDM/HIS/EDC adapters
- **Not Implemented:** Licensed dictionaries, full CDISC, Define-XML, WORM, eSign, IWRS (per LIMITATIONS.md:1)
- **Tests:** Vitest 46/46 + Playwright 26/26 (most credible)

## 6. Technical/Security/Compliance Claims

- **Security claims:** Argon2, sid HttpOnly, CSRF double-submit, Helmet, Zod, rate limiting, RBAC, ACL — **IMPLEMENTED** (tested `api.auth.rbac.test.ts:1`)
- **Compliance claims:** Not claimed certified — explicitly says prototype only, needs validation (`README.md:1` disclaimer). **FACT vs CLAIM:** Do not conclude compliant.
- **Screenshots:** No standalone screenshots folder; 360 webp `public/vedraya/frames-alpha/` are cinematic landing frames (visual identity, not dashboard screenshots). Dashboard screenshots are seen live in Command Center after login, not as static assets.

## 7. What is Actually Demonstrated (60-sec)

Proves: login → RBAC (monitor/regulator ACL) → study dossier → AE escalate → audit verify → exports. Does not demonstrate: ABDM, licensed MedDRA, WORM, offline.

**Source files:** `docs/DEMO_SCRIPT.md:1`, `docs/JUDGE_QA.md:1`, `docs/SIH26046_TRACEABILITY_FINAL.md:1`, `docs/IMPLEMENTATION_STATUS.md:1`, `docs/RBAC.md:1` 3.6KB, `docs/SECURITY.md:1`, `e2e/ctms-critical-path.spec.ts:1` 11KB.
"""
(OUT/"VEDRAYA_JUDGE_ANALYSIS.md").write_text(ved_special, encoding="utf-8")
# also copy to analysis
(OUT/f"analysis/nishant-uxs_vedraya/VEDRAYA_JUDGE_ANALYSIS.md").write_text(ved_special, encoding="utf-8")
print("VEDRAYA_JUDGE_ANALYSIS.md")

# --- AYUSPHERE special ---
ayu_path = REPOS/"vansh459_AyuSphere"
ayu_readme = read(ayu_path/"README.md")
ayu_arch = read(ayu_path/"docs/architecture.md")
ayu_gap = read(ayu_path/"docs/gap-analysis.md")
ayu_tech = read(ayu_path/"docs/technology.md")
ayu_demo_md = read(ayu_path/"docs/uat/Judge_Demo_Script.md")
ayu_tech_guide = read(ayu_path/"docs/uat/Tech_Security_Guide.md")
ayu_uat_list = list((ayu_path/"docs/uat").glob("*.pdf"))
ayu_special = f"""# AYUSPHERE Special Extraction — Presentation Intelligence

**Repository:** `vansh459_AyuSphere` (`https://github.com/vansh459/AyuSphere`, Team Bob The Builder)
**Generated:** 2026-09-30
**Files analyzed:** `README.md` (2.8 KB), `docs/architecture.md` (17.4 KB), `docs/gap-analysis.md` (13 KB), `docs/gap-plan.md` (16.4 KB), `docs/technology.md` (10.4 KB), `docs/uat/Judge_Demo_Script.md` (4.1 KB) + `.pdf` (1.31 MB), 7 UAT guides (0.4-3.3MB), `docs/uat/Tech_Security_Guide.md` (17KB)

## 1. AI Claims (from README + architecture)

```markdown
{ayu_readme[:3000]}
```

**AI architecture (from docs/architecture.md snippet):**
```markdown
{ayu_arch[:4000]}
```

**Analysis:**
- **AI Input:** Doctor Note text/images (Vercel Blob), trial docs for Copilot grounding, alert thresholds.
- **Processing:** `src/app/api/ai/extract/route.ts:1` Claude OCR/extraction (Anthropic SDK 0.125, low-confidence flag, draft never auto-commits, must confirm flagged fields, only PI can approve via `api/ai/approve`), `src/app/api/ai/copilot/route.ts:1` grounded Copilot (declines on empty retrieval, LangChain/Groq), `src/app/api/guide/route.ts:1` Sphera guide (Groq).
- **Model/API:** Claude (Anthropic SDK) + Gemini fallback + Groq (Sphera) — prompt-based, external LLM API, not trained model. API keys in env (`ANTHROPIC_API_KEY`, `GEMINI_API_KEY`, `GROQ_API_KEY`), configurable in Settings → AI Model (overrides env per `docs/technology.md`).
- **Output:** Extracted fields (draft), grounded answer, approved record (via withAudit).
- **Evidence:** `tests/extraction.test.ts:1` 11KB mocked Claude pipeline, `tests/copilot.test.ts:1` 4KB declines, `tests/ai-provider.test.ts:1` 7KB, `tests/guide-chat.test.ts:1` 9KB.
- **Claim vs Implementation:** **IMPLEMENTED** (external LLM API) — not trained model. Demo data synthetic, no real PHI. See `analysis/vansh459_AyuSphere/REPO_ANALYSIS.md:15`.

## 2. CTRI (from README + scripts)

```markdown
{ayu_gap[:3000]}
```

**Evidence:** `scripts/scrape/ctri_scrape.py:1` (crawl4ai, pip-only, no Docker) scrapes real public CTRI registry records (titles, CTRI numbers, interventions, sponsors, sites/states) politely, seeds via `pnpm db:seed:real` idempotent (`src/db/seed-real.ts` + `seed.test.ts` 2.8KB). **All participant-level data is synthetic** (`src/db/seed.ts` fixed faker seed, no identifier cols by schema). Participants table has no identifier columns — de-identification by schema. See `analysis/vansh459_AyuSphere/CLAIM_VS_EVIDENCE.md:1` — CTRI **IMPLEMENTED** (scrape, not official API).

## 3. FHIR

- **Claim:** FHIR R4 ResearchStudy/Subject (README)
- **Code:** `src/app/api/fhir/Bundle/[trialId]/route.ts:1`, `src/app/api/fhir/ResearchStudy/[id]/route.ts:1`, `src/app/api/fhir/import/route.ts:1`, `tests/fhir-api.test.ts:1` 8KB (PGlite). **IMPLEMENTED** per matrix (FHIR Bundle + import). See `REPO_ANALYSIS.md:11`.

## 4. CDISC

- **Claim:** CDISC SDTM/CDASH (README)
- **Code:** SDTM datasets via `src/app/api/export/route.ts:1`, `tests/exports.test.ts:1` 10KB, `tests/dictionaries.test.ts:1` (MedDRA demo). **IMPLEMENTED** per matrix (CDISC datasets/exports), but mapping heuristic: FHIR↔CDISC mapping **PARTIALLY IMPLEMENTED** (both exist separate, no explicit mapping file found via `mapping` search — see REPO_ANALYSIS 12).

## 5. UAT (from docs/uat/*.pdf + .md)

**Files:** 1 Judge_Demo_Script.md (4.1KB) + .pdf (1.31MB) + 7 UAT guides (Administrator 3.32MB, PI 2.83MB, Coordinator 1.91MB, Pharmacovigilance 1.25MB, Monitor 667KB, Ethics 466KB, Regulator 529KB) + Tech_Security_Guide.md 17KB + .pdf 155KB.

**Judge Demo Script snippet:**
```markdown
{ayu_demo_md[:4000]}
```

**Tech Security Guide snippet:**
```markdown
{ayu_tech_guide[:4000]}
```

**Structure per UAT guide (heuristic from extracted PDFs):** Each PDF has 4-13 pages, embedded screenshots (XObject/Image), drift-guard tested click paths (labels tested against navigation/permission matrix), role-specific workflows (e.g., Administrator: Settings AI Model + Alerts & Deadlines + user accounts + audit trail). See `presentation_analysis/extracted/vansh459_AyuSphere/docs_uat_UAT_Guide_Administrator.pdf.md` for per-page headings/tables (though image-heavy pages have minimal text extraction — visual inspection needed for screenshots).

**Test cases:** Not traditional test cases with Pass/fail in PDF — but `tests/*.test.ts` 50 suites 157 tests are the test evidence (test-gated `docs/tasks.md:1` 24KB: every task shipped after gate passes — lifecycle, CRF immutability, AE clock, Copilot grounding, etc.). UAT guides are **user-facing click paths**, not automated test reports.

## 6. Judge Material (from Judge_Demo_Script)

- **Demo script:** 4.1KB markdown + 1.31MB PDF — live demo: https://ayusphere-three.vercel.app, sign in as 7 roles (pi@aiia.demo etc., password Demo@1234), exact labels drift-guard tested.
- **Evaluation guides:** 7 role PDFs (Administrator etc.) — each details what role can/cannot do (e.g., Admin can configure AI models/alert rules but cannot deactivate own account, cannot delete audit entries — append-only).
- **Technical guide:** 17KB md + 155KB pdf — AUTH_SECRET, DATABASE_URL, AI provider order (Gemini first, then Anthropic), Groq model `openai/gpt-oss-20b`, Vercel Blob.
- **No PPT decks** — presentation is via markdown/docs + UAT PDFs, not PowerPoint.

## 7. Security / Architecture

- **Architecture:** Next.js 16 App Router + TypeScript + Neon Postgres + Drizzle + PGlite (in-process, no Docker anywhere per docs) + Tailwind v4 + hand-owned shadcn + Framer Motion + Vitest/PGlite + Sphera (Groq) + Vercel Blob + Recharts for analytics.
- **Security claims (from Tech_Security_Guide):** Auth.js v5 (7 roles, JWT), audit insert-only (`withAudit()`), CRF immutability + versioned corrections, AE escalation clock, alert idempotency, regulator read-only, one-font/two-sizes design QA (`design-qa.test.ts`). See `REPO_ANALYSIS.md:16` for immutable audit status **IMPLEMENTED**.

## 8. Unknowns

- No ppt/pptx — pitch is docs + live demo, not slide deck.
- Some PDFs are image-heavy (screenshots) — pypdf extracted only minimal text (see `presentation_analysis/extracted/.../UAT_Guide_*.pdf.md` Visual notes: page contains embedded images).

**Evidence:** `docs/uat/Judge_Demo_Script.md:1`, `docs/uat/*.pdf` 9 files, `docs/architecture.md:1`, `scripts/scrape/ctri_scrape.py:1`, `src/app/api/ai/*:1`, `tests/*.test.ts:1` 50 suites.
"""
(OUT/"AYUSPHERE_PRESENTATION_ANALYSIS.md").write_text(ayu_special, encoding="utf-8")
(OUT/f"analysis/vansh459_AyuSphere/AYUSPHERE_PRESENTATION_ANALYSIS.md").write_text(ayu_special, encoding="utf-8")
print("AYUSPHERE_PRESENTATION_ANALYSIS.md")

# --- Comparisons ---
# Load per-repo demo/judge data for comparisons
# DEMO_COMPARISON
demo_comp = """# Demo Comparison — Across 7 Competitors

**Generated:** 2026-09-30
**Evidence:** `presentation_analysis/analysis/*/DEMO_ANALYSIS.md:1` + `docs/DEMO_SCRIPT.md` raw, not README claim alone.
**Do NOT rank.**

## Matrix

| Stage | nishant-uxs_vedraya | vansh459_AyuSphere | DuvvuruDeepakReddy18_AyuTrial | aravindakrishna-c_AIIA-Clinical-Trial-Dashboard | AnushkaTadiyal_aiia-ctms | rimi007-grt_AIIA-CTMS | kalyan-2006-prog_SIH26046-DEV-RUSH- |
|---|---|---|---|---|---|---|---|
| **Opening** | Open app → Enter Live Command Center → login admin@vedraya.demo (Vedraya!Demo1) → badge Live PostgreSQL | Live demo https://ayusphere-three.vercel.app → sign in as pi@aiia.demo (Demo@1234) | Landing page Ministry of Ayush branding → 1-click persona launcher (no password) → login page | No demo script — README only — Unknown | No demo script — Unknown | No demo script — Unknown | No demo script — Unknown |
| **Problem framing** | SIH26046 Ministry of Ayush / AIIA + traceability matrix docs/SIH26046_TRACEABILITY_FINAL.md 8KB | SIH26046 Ministry of Ayush · AIIA + gap-analysis.md 13KB / gap-plan.md 16KB | SIH26046 Organization Ministry of Ayush, Institution AIIA, Domain CTMS + NPvCC | README SIH26046 (sparse) | README SIH26046, keywords ctms | README Aayu-Setu CTMS Ministry of Ayush | No problem framing doc — minimal README 1.5KB |
| **Login/RBAC** | 7 roles demo via admin login, then monitor@vedraya.demo (AYU-024 only) → regulator@vedraya.demo (403) — ACL tested | 7 roles via Auth.js JWT (pi, coordinator, monitor, ethics, pv, admin, regulator read-only) — Tested regulator.test.ts | 7 personas via 1-click switcher (admin.ctms@aiia.gov.in etc.) no password — demo persona, not real auth | Login page (frontend) + FastAPI JWT — no judge persona docs | AuthPage.jsx JWT — no demo persona doc | Same as Anushka + test_rbac_matrix.js | No demo script — seed-demo scripts (activate-demo-consent.ts etc.) |
| **Trial creation** | Study AYU-024 lifecycle transitions (studies/routes.ts) | Clinical Trials → trial lifecycle state machine (lifecycle.test.ts) | /studies + /studies/new GCP-ASU form + 10-stage pipeline /studies/[id] 27KB | trials.py POST /trials (11KB) + frontend CreateTrialPage 41KB | TrialsPage 30KB + TrialDetail 37KB — basic CRUD | Same | Dashboard/[trialId] page 9.6KB — stub |
| **Protocol** | Milestones per study (milestones/routes.ts) | Amendments (`amendments.test.ts`) + lifecycle | Milestone tracker tabbed dossiers | trials.py includes protocol fields | No protocol differentiator | No | No |
| **Participant** | Participants CRUD (participants/routes.ts) screened/enrolled | Participants de-identified by schema (no identifier cols) | Synthetic participants registry DEMO-0001 + participant dossier | participants.py 7.3KB | basic | basic | NOT PRESENT |
| **Clinical data / CRF** | Participants + AE (no full eCRF) — PARTIALLY | CRF immutability + versioned corrections (crf.test.ts) IMPLEMENTED | Scheduled visit adherence matrix + Ayush exams (Prakriti/Agni/Koshtha) — MOCKED | NOT PRESENT | NOT PRESENT | NOT PRESENT | NOT PRESENT |
| **AE/SAE** | Safety → AE → DEMO MedDRA coding → escalate SAE → reporting due / notify | AE escalation clock (ae-service.test.ts) + safety signals | pharmacovigilance NPvCC + 24h SAE countdown + WHO-UMC (pharmacovigilance/new 22KB) | safety.py 3.5KB | SafetyPage 30KB | SafetyPage 39KB | adverse-events page 8.7KB |
| **Ethics** | Ethics committees via regulatory routes | Ethics Review (ethics@ role) | Institutional Ethics Committee workflow (Prof Joshi) | ethics_regulatory.py 4.4KB | EthicsPage 12KB | EthicsPage | NOT PRESENT |
| **Regulatory** | Regulatory / CTRI TRACKING / NDCT (tracking) | CTRI real scrape + regulatory workflow | Statutory compliance matrix GCP-ASU/ICMR/NDCT + CTRI verification | ethics_regulatory.py | CLAIMED ONLY | CLAIMED ONLY | ctri-ethics page 8KB |
| **Pharmacovigilance** | PARTIALLY (no NPvCC) | PV officer + signals | NPvCC apex IMPLEMENTED (dedicated) + CDSCO | PARTIALLY | NOT PRESENT | NOT PRESENT | NOT PRESENT |
| **Analytics** | Portfolio KPIs + computed alerts (enrolment lag, open SAE) | Real-time KPIs + alerts cron idempotency | 10 computed KPIs + 7 Recharts + 24h SAE clock | dashboard.py 1.6KB | DashboardPage 25KB PARTIALLY | DashboardPage 34KB | dashboard page 10.6KB |
| **AI** | NOT PRESENT (honest) | Doctor Note OCR + grounded Copilot (declines on empty) — IMPLEMENTED | NOT PRESENT (WHO-UMC rule) | NOT PRESENT | NOT PRESENT | NOT PRESENT | NOT PRESENT |
| **FHIR/CDISC** | Exports/Interop → SDTM-like AE · FHIR R4 prototype · adapters NOT CONNECTED | FHIR Bundle + SDTM exports (fhir-api.test.ts, exports.test.ts) | CDISC SDTM DM/AE/EX/VS/LB + FHIR R4 bundle inspector + ABDM blueprint NOT CONNECTED | FHIR 2.5KB stub | NOT PRESENT | NOT PRESENT | FHIR ingest 12.5KB / SDTM stubs |
| **Audit** | Audit → Re-verify SHA-256 chain → AUDIT CHAIN: VERIFIED (audit/service.ts GLOBAL) | Audit Trail append-only (withAudit) — admin cannot delete | Audit-logs ALCOA+ ledger + SHA-256 local hash (mocked) | audit_logs.py | AuditPage 9KB | AuditPage 33KB | audit-log route 3.1KB |
| **Closing** | Logout → monitor/regulator ACL demo, then verdict (see VEDRAYA_JUDGE_ANALYSIS) | Role scores evaluation axes (Administrator guide: All four axes) | Settings regulatory deadline rules editor | Unknown | Unknown | Unknown | Unknown |
| **Evidence demo exists** | YES (DEMO_SCRIPT.md 3KB + Judge in 60 seconds README + e2e critical path 11KB) | YES (Judge_Demo_Script.md 4.1KB + pdf 1.31MB + 7 UAT guides) | No explicit demo script — README is pitch, 28 routes + mockData is demo | No demo script | No demo script | No demo script | No demo script (scripts/activate-demo* are data scripts) |

> **Common:** All with demo emphasize trial creation → participants → AE/SAE → audit. Only vedraya + AyuSphere have detailed judge-grade demo scripts with exact click paths drift-guard tested; AyuTrial emphasizes NPvCC 24h clock.

"""
(COMP/"DEMO_COMPARISON.md").write_text(demo_comp, encoding="utf-8")
print("DEMO_COMPARISON.md")

# JUDGE_QA_COMPARISON
judge_comp = """# Judge Q&A Comparison — Across 7 Competitors

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

"""
(COMP/"JUDGE_QA_COMPARISON.md").write_text(judge_comp, encoding="utf-8")
print("JUDGE_QA_COMPARISON.md")

# PITCH_COMPARISON
pitch_comp = """# Pitch / Presentation Structure Comparison

**Generated:** 2026-09-30
**Evidence:** README.md + docs/* + UAT PDFs (not PPT, PPT=0)
**Do NOT rank.**

## Presented Pitch Structure (what order they pitch)

| Structure element | vedraya (README + docs) | AyuSphere (README + docs/architecture) | AyuTrial (README 9.4KB) | AIIA-Dashboard (README 9.1KB) | Anushka (README 8.8KB) | rimi (README 10.1KB) | DEV-RUSH (README 1.5KB) |
|---|---|---|---|---|---|---|---|
| **Problem** | SIH26046 traceability + Overview table (Operations/Safety/Governance) | SIH26046 gap-analysis.md 13KB + gap-plan.md 16KB (Phases 7-10) | Executive Product Overview (AIIA + Ministry of Ayush unified command centre + NPvCC apex) | README Problem SIH26046 (sparse) | README 8.8KB SIH26046 (brief) | README 10KB Aayu-Setu enterprise pitch | Minimal README 1.5KB (no pitched problem) |
| **Existing gap** | Marketing landing narrative vs Live Command Center truth (README clarifies) | docs/gap-analysis vs gap-plan — honestly documents gaps (Phases 7-10) | Existing multi-centre governance disconnected | Not pitched as gap | Not pitched | Not pitched | Not pitched |
| **Solution** | Consolidates ops into single demoable stack (6-area table) | AI-assisted Clinical Research Intelligence Platform (Bob The Builder) | AIIA CTMS + NPvCC apex platform (enterprise cloud) | Phase 1 RBAC dashboard (7 roles) | CTMS 4 dashboards (claimed) | Enterprise Aayu-Setu (same as Anushka but AWS modals) | DEV-RUSH CTMS FHIR/SDTM stubs |
| **Architecture** | Modular monolith diagram (Landing → Command Center → Express /api/v1 → PG → chain) + 14 modules | Next.js + Neon + Drizzle + PGlite + AI (Claude/Groq) diagram via docs/architecture.md 17KB | Next.js 16 + Supabase + localStorage dual-mode diagram (ARCHITECTURE.md 5KB) | Frontend/Vite → FastAPI → SQLAlchemy/Alembic → Postgres diagram (not explicit but inferred) | client/server split (App.jsx → Express → SQLite) — not diagrammed | Same as Anushka + Dockerfile/apprunner | Next.js API stubs (no diagram) |
| **Features** | Table: Operations/Safety/Governance/Security/Integrity/Interop (6 rows, explicit prototype/not connected) | Stack + Quickstart + Tests (task gates) + Notes (CTRI real + synthetic) | Key Highlights table (10 rows: multi-study, 8 sites, NPvCC 24h clock, WHO-UMC, ALCOA+ hash, CDISC/FHIR, ABDM blueprint, ethics, 7 RBAC, persona simulator) + Site Map 28 routes | Not table — pages CreateTrial/Ethics etc. | Pages: Trials, Safety, Audit, Users (not table) | Same + AWS/Dictionary modals | Routes: adverse-events, audit-logs, ctri-ethics, fhir etc. |
| **Workflow** | Sequence: Study → Sites → Participants → AE escalate → Consent/Regulatory → Quality → Audit verify → Exports → RBAC logout | docs/workflow.md 14.5KB + loading-skeletons + performance-audit | Site Map 28 routes grouped Public/Operational/Quality/Compliance/Administration | Not documented as workflow | Not workflow diagram | Not | Not |
| **Technology** | Badge table (TypeScript 5, React 19, Postgres 16, Vitest 46/46, Playwright 26/26) | Stack: Next 16 + TS + Neon + Auth.js + Claude + Tailwind v4 + Framer Motion + Vitest/PGlite | Tech Stack: Next.js, TS5, Tailwind Ayush tokens, Recharts, Supabase, crypto | Tech: Vite, React, FastAPI, SQLAlchemy, Docker | Tech: React, Express, SQLite, Socket.io | Tech: same + Docker/AWS | Tech: Next.js, Drizzle |
| **AI** | NOT PRESENT (honest) | AI Assistant + Reports/Exports (Copilot grounding) — docs/architecture AI section | NOT PRESENT (WHO-UMC rule claimed but not AI) | NOT PRESENT | NOT PRESENT | NOT PRESENT | NOT PRESENT |
| **Compliance** | Standards & compliance boundary table (MedDRA DEMO not licensed, CDISC prototype, FHIR prototype, ABDM NOT CONNECTED, CTRI tracking, ALCOA+ not legal) + LIMITATIONS.md | Not compliance table — but DPDP note (participants synthetic, no PHI) + audit append-only | Security, Compliance & Limitations 4-bullet disclaimer (prototype requires validation) | Not compliance table | CLAIMED ONLY 21 CFR (no evidence) | CLAIMED ONLY | Not |
| **Interoperability** | Honest Interop section (FHIR R4 prototype, SDTM-like, ABDM NOT CONNECTED) | FHIR/SDTM exports (fhir-api.test) — docs/architecture includes FHIR/CDISC | Interoperability 3 bullets (SDTM, Define-XML, FHIR R4, ABDM blueprint) | fhir.py stub | Not | Not | FHIR ingest/export stubs |
| **Security** | Security verification table (7 checks: 401 unauth studies, 403 without CSRF, regulator 403, monitor 403, audit 405, tamper valid:false, seed valid:true — all PASS) + docs/SECURITY.md 1.7KB | Tech_Security_Guide.md 17KB (auth, audit, encryption, deployment) | RBI? — Demo Credentials table 7 personas, RBAC section | Not security table | AuthPage JWT | Same | Not |
| **Demo** | Judge in 60 seconds 9 steps + DEMO_SCRIPT.md 3KB + Judge Q&A 3.5KB + LIVE badge | Quickstart pnpm dev → demo logins Demo@1234 + pnpm verify (typecheck+vitest) + Judge_Demo_Script.md 4.1KB + UAT guides 7 PDFs | Quick Start 5 steps (clone→install→env→dev→build/test 21/21) + Evaluator Quick Access persona switcher | DEPLOYMENT.md 4.4KB + run_localhost.bat | No demo script — install:all | No demo script | devrush-ctms scripts/*demo* |
| **Impact** | Cinematic landing identity + operational truth in Live Command Center (README) | Problem SIH26046 (gap-analysis) — impact implicit via KPIs | Institutional branding Ministry of Ayush + AIIA | Not impact section | Not | Not | Not |
| **Future scope** | Roadmap from limitations table (Current prototype → Production hardening → Interoperability) + CHANGELOG 0.8KB | gap-plan.md Phases 7-10 (future work) + tasks.md 24KB | Not future scope — disclaimer prototype | Not | Not | Not | Not |

> **Common structure across pitched READMEs:** Problem → Solution → Stack → Quickstart → Routes/Features → Deployment/Demo → Limitations/Disclaimer. Only vedraya + AyuSphere include explicit gap/limitations/traceability docs; AyuTrial includes 28-route site map + Key Highlights table (most feature-dense pitch); others sparse.

"""
(COMP/"PITCH_COMPARISON.md").write_text(pitch_comp, encoding="utf-8")
print("PITCH_COMPARISON.md")

# ARCHITECTURE_PRESENTATION_COMPARISON
arch_comp = """# Architecture Presentation Comparison — Presented vs Actual Code

**Generated:** 2026-09-30
**Evidence:** `analysis/*/ARCHITECTURE.md:1` (actual) vs `analysis/*/ARCHITECTURE_CLAIM_VS_CODE.md:1` (presented)
**Do NOT rank.**

## Matrix: Presented Diagram (from docs/ARCHITECTURE.md or README) vs Actual Code (from routes.ts/schema.ts/package.json)

| Repository | Presented Architecture (what pitch shows) | Actual Code Architecture (verified) | Match? | Difference |
|---|---|---|---|---|
| **nishant-uxs_vedraya** | Modular monolith diagram: Client (Landing + Live Command Center React/Vite) → API (Express /api/v1 Gate→RBAC→ACL→domain) → DB (PostgreSQL + Drizzle) → Chain (GLOBAL SHA-256) ; Landing -.CTA-> CC ; CC --> Gate etc. From `docs/ARCHITECTURE.md:1` 5.5KB + README mermaid flowchart | Same as presented: 14 modules `server/src/modules/*`, middleware `auth.ts`/`studyAccess.ts`, schema 441 lines 5 migrations, audit service, CommandCenter.tsx, Vitest 46/46 + Playwright 26/26, Vercel SPA + Render API | **MATCH** (presented honestly) | Presented notes adapters NOT CONNECTED, honest about prototype limits |
| **vansh459_AyuSphere** | Next.js 16 App Router + Neon Postgres + Drizzle + PGlite (no Docker D-019) + Auth.js + Claude/Groq + Tailwind v4 + Framer Motion diagram via `docs/architecture.md:1` 17KB + `docs/decisions.md:1` 29KB | Same: `src/db/schema.ts:1` 576 lines, `src/app/api/ai/*:1` (extract/copilot), Neon + PGlite, Vitest 157, no Docker | **MATCH** | Presented includes AI pipeline (Claude extract → draft → PI approve) which exists in code; honest about test-gated tasks |
| **DuvvuruDeepakReddy18_AyuTrial** | Dual-mode: Next.js App Router → In-memory + localStorage (demo) vs Supabase (prod) → Recharts + crypto hash, 28 routes, from `ARCHITECTURE.md:1` 5KB + README site map | Same: `src/lib/mockData.ts:1` 58KB in-memory (10 trials) + `supabase/` migrations but env demo default, `src/app/*` 28 routes, `src/lib/crypto.ts:1` local hash | **MATCH** but demo vs prod gap: presented shows Supabase as prod-ready but code defaults to localStorage — **INFERENCE:** prod mode UNKNOWN |
| **aravindakrishna-c_AIIA-Clinical-Trial-Dashboard** | Split: Vite React (frontend) → FastAPI → SQLAlchemy/Alembic → Postgres/SQLite, from `DEPLOYMENT.md:1` 4.4KB + README | Same: `frontend/package.json` Vite 8 + React 19, `backend/app/main.py:1` FastAPI, `backend/app/api/router.py:1` 11 routers, `backend/app/database/init_db.py:1` 60KB | **MATCH** (no explicit diagram but inferred) | Presented does not show FHIR as stub (2.5KB) — actual code shows stub |
| **AnushkaTadiyal_aiia-ctms** | Split: Vite React (client/src/App.jsx) → Express → SQLite better-sqlite3, from `client/README.md:1` 1KB + root README 8.8KB (no diagram) | Same: `server/index.js:1` Express 5, `client/src/App.jsx:1` 5.5KB routing, `server/seed.js:1` 57KB SQLite | **MATCH** | Presented no diagram — actual matches simple split |
| **rimi007-grt_AIIA-CTMS** | Same as Anushka + AWS Cloud modal + Docker, from `README.md:1` 10KB (no diagram) | Same: adds `client/src/components/AWSCloudModal.jsx:1` 15KB, `Dockerfile`, `apprunner.yaml`, same seed.js 57KB — modals mocked | **MATCH** for base, but AWS not actually integrated — **CLAIMED ONLY** vs presented as integrated |
| **kalyan-2006-prog_SIH26046-DEV-RUSH-** | No presented diagram — README 1.5KB minimal | Next.js API stubs (`app/api/fhir/ingest` 12.5KB + define 9.9KB etc.) + Drizzle schema 13.7KB, no auth, no tests, 5 commits | **UNKNOWN** (no presented diagram to compare) | Presented minimal vs actual stubs — actual is demo shell |

> **Conclusion:** 4 repos match presented vs actual (vedraya, AyuSphere, Dashboard, AyuTrial dual-mode with caveat), 2 match but overclaim (rimi AWS), 1 no diagram (DEV-RUSH). Only vedraya explicitly marks adapters NOT CONNECTED and honest prototype limits.

"""
(COMP/"ARCHITECTURE_PRESENTATION_COMPARISON.md").write_text(arch_comp, encoding="utf-8")
print("ARCHITECTURE_PRESENTATION_COMPARISON.md")

# FEATURE_PRESENTATION_COMPARISON
feat_comp = """# Feature Presentation Comparison — What Competitors Emphasize

**Generated:** 2026-09-30
**Evidence:** README tables, docs/*.md, `analysis/*/FEATURE_PRESENTATION_ANALYSIS.md:1`, `COMPETITOR_MATRIX.md:1`
**Do NOT rank.**

## Matrix: Top Features Emphasized (from pitch docs)

| Category | vedraya (honest) | AyuSphere (test-gated) | AyuTrial (NPvCC-heavy) | Dashboard (FastAPI) | Anushka (shell) | rimi (fork+modals) | DEV-RUSH (stubs) |
|---|---|---|---|---|---|---|---|
| **Top features emphasized** | Live Command Center + auditable RBAC + SHA-256 verify + PS traceability | AI Doctor Note OCR + grounded Copilot + real CTRI scrape + CRF immutability + PGlite | 28 routes + NPvCC 24h SAE clock + WHO-UMC + 10 trials 8 sites + ABDM blueprint | 11 FastAPI routers (trials 11KB) + 41KB CreateTrialPage | 24 trials/30 AEs seed + Trials/Safety pages | Same as Anushka + AWS/Dictionary/ESignature modals (15KB) | FHIR/SDTM/ADaM/Define route stubs (12KB ingest) |
| **Clinical features** | Studies/sites/participants/milestones + consent + AE escalate (not full eCRF) | Lifecycle state machine + CRF immutability + visit-engine + enrolment guards | Visits with Prakriti/Agni/Koshtha + dispensing + 28-route dossier | Trials/participants via FastAPI | TrialsPage 30KB + TrialDetail 37KB | Same + Dashboard 34KB | Dashboard/[trialId] 9.6KB |
| **Regulatory features** | Consent + ethics + regulatory CTRI/NDCT tracking (partial) + deviations/queries | Gap analysis vs plan (Phases 7-10) + ethics review via auth | GCP-ASU/ICMR/NDCT matrix + CTRI verification + vernacular consent | ethics_regulatory.py 4.4KB | CLAIMED CTRI | CLAIMED CTRI | ctri-ethics page 8KB |
| **AI features** | NOT PRESENT (honest) | Claude extract (low-confidence flag, PI approve) + Groq/Gemini fallback + Sphera guide | NOT PRESENT (WHO-UMC rule) | NOT PRESENT | NOT PRESENT | NOT PRESENT | NOT PRESENT |
| **Interoperability** | FHIR R4 prototype (ResearchStudy/Subject read) + SDTM-like AE CSV + CSV export + adapters NOT CONNECTED (honest) | FHIR Bundle/[trialId] + import + SDTM + exports (fhir-api.test 8KB, exports.test 10KB) | CDISC SDTM DM/AE/EX/VS/LB + Define-XML + FHIR bundle generator + ABDM readiness matrix | FHIR 2.5KB stub | NOT PRESENT | NOT PRESENT | FHIR ingest 12.5KB + export 8KB + SDTM 6.3KB |
| **Security** | Argon2 + sid HttpOnly + CSRF double-submit + RBAC 7 + study ACL + Helmet + Zod + rate limit + audit 405 + tamper valid:false (verified 7 checks) | Auth.js JWT 7 + insert-only audit + CRF immutability + design QA (one-font/two-sizes) + Tech_Security_Guide 17KB | Persona switcher (mock) + audit local hash (mocked) + 7 personas | PyJWT HS256 + passlib/argon2 + dependencies.py RBAC | JWT + bcryptjs + AuthContext | Same + RBACMatrixModal MOCKED | NOT PRESENT |
| **Analytics** | Portfolio KPIs + computed alerts (enrolment lag, open SAE) | Real-time KPIs + alerts cron idempotency + dashboard-queries | 10 computed KPIs + 7 Recharts + 24h SAE clock | dashboard.py 1.6KB | DashboardPage 25KB PARTIALLY | DashboardPage 34KB | dashboard page 10.6KB |
| **Pharmacovigilance** | AE escalate + reporting due/notify + MedDRA demo coding + safety KPIs — PARTIALLY (no NPvCC) | AE escalation clock + safety signals + dictionaries — IMPLEMENTED | NPvCC apex: dedicated desk + 24h/7d/14d statutory + WHO-UMC + CDSCO — IMPLEMENTED (unique) | safety.py 3.5KB PARTIALLY | SafetyPage 30KB PARTIALLY | SafetyPage 39KB PARTIALLY | adverse-events 8.7KB PARTIALLY |
| **Unique claims** | GLOBAL SHA-256 hash chain re-verify + honest prototype-only + PS traceability 8KB + Live Command Center | Test-gated tasks 24KB (every task after gate) + PGlite no Docker + CTRI real public scrape + synthetic de-identified + AI grounded Copilot declines | NPvCC for ASU&H + 24h clock + 28 routes + 10 trials + 8-site network + Ayurveda Prakriti/Agni/Koshtha + ABDM blueprint (unique) | Only Python/FastAPI stack | Fast to demo, SQLite committed 72KB | Same as Anushka + AWS/Docker + modals mocked | Smallest (5 commits), FHIR/SDTM/ADaM/Define stubs |

> **Commonly emphasized across ≥4 repos:** Protocol/participant/AE, RBAC 7, audit trail, synthetic data, real-time KPIs, deployment (Vercel/Render).
> **Rarely emphasized (1-2 repos):** NPvCC (only AyuTrial), AI (only AyuSphere), immutable hash chain (vedraya + AyuSphere), FHIR↔CDISC mapping (only AyuSphere partial), UAT PDFs (only AyuSphere), Judge Q&A (only vedraya full).

"""
(COMP/"FEATURE_PRESENTATION_COMPARISON.md").write_text(feat_comp, encoding="utf-8")
print("FEATURE_PRESENTATION_COMPARISON.md")

print("Comparisons done")
