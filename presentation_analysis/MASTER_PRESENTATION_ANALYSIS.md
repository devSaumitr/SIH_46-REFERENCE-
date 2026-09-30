# SIH26046 Presentation & Judge Intelligence — Master Analysis

**Generated:** 2026-09-30 12:40
**Repositories scanned:** 7 (repositories/*/ — recursive, excl .git/node_modules)
**Search scope:** `*.ppt*`, `*.pptx`, `*.pdf`, `*.doc*`, `*.md`, `*.png/jpg/webp/svg/gif` + filenames containing presentation/pitch/demo/judge/architecture/workflow/diagram/screenshot/uat/traceability etc. + content inspection of README/ARCHITECTURE.
**Evidence hierarchy:** code > config > schema > tests > docs > README.

---

## 1. Artifacts Found

- **Total presentation-related artifacts (exhaustive rglob):** 65 (verified via `_inventory_records.json`)
- **By repo:** vedraya 20 (17 md + 3 demo/judge), AyuSphere 27 (17 md + 9 pdf + 1 script), Anushka 2 (READMEs), rimi 2, AyuTrial 3 (README+ARCHITECTURE+workflow), Dashboard 6 (3 md + 2 tests with demo/workflow names + DEPLOYMENT), DEV-RUSH 5 (1 README + 4 demo scripts)
- **No standalone PPT decks** — all presentation material is Markdown + PDF (UAT/Judge/Tech guides) + README pitch. See `INVENTORY.md:1` table per artifact with file type/size/purpose.
- **Also:** 404 total images (all repos, excl .git) — 399 under public/assets/frames (per keyword `assets`/`public`) + 5 other. No `screenshots/` folder with keyword hits; screenshots are embedded inside PDFs as XObject/Image (detected via pypdf).

## 2. PPT/PPTX Findings

**PPT/PPTX FOUND: 0**

> Explicit: No `*.ppt`, `*.pptx`, `*.pptm`, `*.potx` files found in any of 7 repositories (verified `Get-ChildItem -Recurse -Include *.ppt,*.pptx` + Python rglob, excluded .git). `presentation_analysis/extracted/PPT_INVENTORY.md:1` confirms. `extracted/*/PPT_EXTRACTION.md` created per repo stating 0.
- Do not confuse PDF UAT guides (9 PDFs in AyuSphere) with PowerPoint — they are PDFs generated from markdown/docs, not slide decks.
- Conclusion: Competitors do not ship PowerPoint in repo; pitch is via README + docs + UAT PDFs + live demo.

## 3. PDF Findings

- **Total PDFs:** 9 (all in `vansh459_AyuSphere/docs/uat/` — verified)
- **List:** `Judge_Demo_Script.pdf` (1.31 MB, 10 pages), `Tech_Security_Guide.pdf` (155 KB, 11 pages), 7 UAT guides: Administrator (3.32 MB, 13 pages), Ethics_Committee (466KB, 4p), Monitor (667KB, 5p), Pharmacovigilance (1.28MB, 8p), Principal_Investigator (2.89MB, 13p), Regulator (529KB, 5p), Study_Coordinator (1.91MB, 9p).
- **Content:** UAT guides are **user acceptance testing judge guides** — not pitch decks. Each has dark green sidebar navigation (Overview/Study Conduct/Data Capture/Safety & Quality/Intelligence/System), role-specific workflows (e.g., Administrator: Settings AI Model + Alerts & Deadlines + user accounts + audit trail), exact click paths drift-guard tested against navigation/permission matrix, generated 14 September 2026, live demo https://ayusphere-three.vercel.app, sign-in `admin@aiia.demo` Demo@1234, synthetic data note (trials real CTRI public, participants synthetic DPDP), electronic signatures (`password re-verification + record hashes`), randomization, Define-XML/ADSL/FHIR API etc.
- **Extraction:** `presentation_analysis/extracted/vansh459_AyuSphere/docs_uat_*.pdf.md` (9 files, per-page headings/tables/claims, page numbers preserved via pypdf). Many pages are image-based screenshots (XObject/Image detected per page `Visual: Page contains embedded images`). Text extraction is partial for those pages — shows titles like `Messages`, `Clinical Trials`, `Audit Trail` but screenshots require visual inspection. Marked `Visual: Page contains embedded images` per page.
- **Other repos:** 0 PDFs — vedraya, AyuTrial, Dashboard, Anushka/rimi, DEV-RUSH have no PDFs.
- **Detailed per-PDF:** See `presentation_analysis/extracted/vansh459_AyuSphere/docs_uat_*.pdf.md` (e.g., Administrator 13 pages, headings OVERVIEW/STUDY CONDUCT, claims `AI Assistant`, `Audit Trail`, tables heuristically extracted).

## 4. Demo Scripts

- **Found:** 2 repositories with explicit demo scripts:
  - `nishant-uxs_vedraya/docs/DEMO_SCRIPT.md:1` (3.0 KB, 9 steps) + README `Judge in 60 seconds` 9 steps — **IMPLEMENTED** demo script (most detailed)
  - `vansh459_AyuSphere/docs/uat/Judge_Demo_Script.md:1` (4.1 KB) + `Judge_Demo_Script.pdf:1` (1.31 MB, 10 pages) — **IMPLEMENTED** judge demo script + 7 role UAT guides
  - Others: **NOT PRESENT** — Anushka/rimi/AyuTrial/Dashboard/DEV-RUSH have no DEMO_SCRIPT.md (verified rglob `*DEMO*`). AyuTrial has README Quick Start 5 steps (not separate demo script), Dashboard has DEPLOYMENT.md, DEV-RUSH has scripts/*demo* data scripts (activate-demo-consent.ts etc. — data seeding, not demo flow).
- **Comparison:** `presentation_analysis/comparisons/DEMO_COMPARISON.md:1` compares opening/problem/RBAC/trial/participant/AE/ethics/regulatory/pharmacovigilance/analytics/AI/FHIR/audit/closing across 7 repos.
- **VEDRAYA demo flow:** Open app → Enter Live Command Center → login admin@vedraya.demo (Vedraya!Demo1) → badge Live PostgreSQL → study AYU-024 → Safety AE DEMO MedDRA → escalate SAE → Consents + Regulatory → Quality → Audit re-verify SHA-256 → Exports (SDTM-like, FHIR prototype) → logout monitor/regulator ACL demo (monitor AYU-024 only, regulator 403). Prerequisite `npm run demo:seed`.
- **AyuSphere demo flow:** Live demo https://ayusphere-three.vercel.app → sign in as 7 roles (pi@aiia.demo Demo@1234 etc.) → exact labels drift-guard tested, sidebar 6 sections + quick search + bell + profile chip, workflows per role (Administrator: Settings AI Model + Alerts & Deadlines etc.).
- **Extracted:** `presentation_analysis/analysis/*/DEMO_ANALYSIS.md:1` per repo (opening/problem/workflow/feature sequence/differentiator/evidence/closing).

## 5. Judge Q&A

- **Found:** 1 full + 1 partial:
  - `nishant-uxs_vedraya/docs/JUDGE_QA.md:1` (3.5 KB) — **IMPLEMENTED** judge Q&A (most anticipated questions: WORM? licensed MedDRA? FHIR/CDISC certified? ABDM connected? real patient? hosted where? differentiator?)
  - `vansh459_AyuSphere/docs/uat/Tech_Security_Guide.md:1` (17 KB) + .pdf 155KB (11 pages) — **PARTIALLY IMPLEMENTED** judge-facing security Q&A (auth, audit, encryption, API security, deployment, monitoring)
  - Others: **NOT PRESENT** — Anushka/rimi/AyuTrial/Dashboard/DEV-RUSH have no JUDGE_QA.md (verified rglob `*JUDGE_QA*`).
- **Comparison:** `presentation_analysis/comparisons/JUDGE_QA_COMPARISON.md:1` compares 10 categories (Technical/Clinical/Regulatory/AI/Security/Architecture/Data/Interoperability/Deployment/Innovation) across 7 repos.
- **Master bank:** `presentation_analysis/MASTER_JUDGE_QUESTION_BANK.md:1` combines deduped 36 questions grouped into Technical/Clinical/Regulatory/AI/Security/Architecture/Data/Interoperability/Scalability/Deployment/Innovation/Demo/Implementation, with source per question (e.g., `docs/JUDGE_QA.md:1` vs `scripts/scrape/ctri_scrape.py:1`).
- **Per-repo analysis:** `presentation_analysis/analysis/*/JUDGE_QA_ANALYSIS.md:1` (question/answer/evidence/category).

## 6. UAT Documents

- **Found:** 1 repository with UAT:
  - `vansh459_AyuSphere/docs/uat/` — 7 UAT guides (Administrator, Ethics_Committee, Monitor, Pharmacovigilance, Principal_Investigator, Regulator, Study_Coordinator) + Judge_Demo_Script + Tech_Security_Guide — **9 PDFs total** + markdowns.
  - **Purpose:** User acceptance testing judge guides — each details `Your workspace`, `What you can and cannot do` (e.g., Admin cannot deactivate own account, cannot delete audit entries — append-only), `Core workflows (exact click paths)` (e.g., Settings → AI Model → Save; Create user → Deactivate), `Screens` (Dashboard, Clinical Trials, Ethics Review, Participants, Site Management, Visit Schedule, Data Entry eCRF, Documents, Adverse Events, Monitoring, Alerts, AI Assistant, Reports & Exports, Audit Trail, Settings), `New in this build` (Alerts & Deadlines configurable, electronic signatures, randomization, Define-XML/FHIR).
  - **Test cases:** Not traditional Pass/fail test cases in PDF — but `vansh459_AyuSphere/tests/*.test.ts` 50 suites 157 tests are the automated test evidence (test-gated `docs/tasks.md:1` 24KB). UAT guides are **click-path evaluation guides**, drift-guard tested against navigation/permission matrix, with screenshots (embedded images per page).
  - **Other repos:** 0 UAT — vedraya has `e2e/` Playwright 26/26 + `server/tests/` 46/46 but not UAT PDFs; AyuTrial has `src/tests/workflows.test.ts` 21 tests; Dashboard has `backend/tests/e2e_demo.py` 6.9KB + `test_trial_workflow.py` 4.1KB (workflow tests with demo in name, but not UAT docs).
  - **Comparison:** UAT details in `MASTER_PRESENTATION_ANALYSIS.md:6` + per-repo `TRACEABILITY_ANALYSIS.md`.
  - **Extracted:** `presentation_analysis/extracted/vansh459_AyuSphere/docs_uat_*.pdf.md` (per-page text with headings/tables/images noted).

## 7. Architecture Material

- **Found:** 3 repositories with explicit architecture docs:
  - `nishant-uxs_vedraya/docs/ARCHITECTURE.md:1` (5.5 KB) — modular monolith diagram (Landing → Command Center → Express /api/v1 Gate→RBAC→ACL→domain → DB PostgreSQL + Drizzle → Chain GLOBAL SHA-256), 14 modules, 5 migrations, Vercel SPA + Render API.
  - `vansh459_AyuSphere/docs/architecture.md:1` (17.4 KB) + `docs/decisions.md:1` 29KB + `docs/technology.md:1` 10.4KB — Next.js + Neon + Drizzle + PGlite no Docker D-019 + Auth.js + Claude/Groq + Tailwind v4 + Vitest/PGlite.
  - `DuvvuruDeepakReddy18_AyuTrial/ARCHITECTURE.md:1` (5.0 KB) — dual-mode Next.js (in-memory + localStorage demo vs Supabase prod) + Recharts + crypto hash, 28 routes.
  - Others: Anushka/rimi have `client/README.md` 1KB (not architecture), Dashboard has `DEPLOYMENT.md` 4.4KB (deployment, not architecture diagram), DEV-RUSH no architecture (minimal README 1.5KB).
- **Comparison:** `presentation_analysis/comparisons/ARCHITECTURE_PRESENTATION_COMPARISON.md:1` compares presented diagram vs actual code (from `analysis/*/ARCHITECTURE.md:1` via `schema.ts`, `routes.ts`, `package.json`). Matches: vedraya/AyuSphere/AyuTrial (with caveat dual-mode prod unknown) → MATCH, rimi AWS mocked → CLAIMED ONLY, DEV-RUSH UNKNOWN.
- **Per-repo:** `presentation_analysis/analysis/*/ARCHITECTURE_CLAIM_VS_CODE.md:1` (presented vs actual table: Frontend/Backend/Database/AI/Cloud/Auth/Data flow).

## 8. Traceability Material

- **Found:** 2 repositories with traceability:
  - `nishant-uxs_vedraya/docs/SIH26046_TRACEABILITY_FINAL.md:1` (8.0 KB) + `docs/REQUIREMENTS_TRACEABILITY.md:1` 3.5KB + `docs/IMPLEMENTATION_STATUS.md:1` 1.5KB (honest Implemented/Partial/Prototype/Not Connected table) + `docs/IMPLEMENTATION_PLAN.md:1` 4.3KB.
  - `vansh459_AyuSphere/docs/gap-analysis.md:1` (13 KB) + `docs/gap-plan.md:1` 16.4KB (Phases 7-10) + `docs/architecture.md` traceability — PS SIH26046 requirements vs implementation.
  - Others: AyuTrial traces PS in README 9.4KB (not separate traceability doc), Dashboard no traceability, Anushka/rimi no docs, DEV-RUSH no.
- **Extracted:** `presentation_analysis/extracted/nishant-uxs_vedraya/docs_SIH26046_TRACEABILITY_FINAL.md` + `analysis/*/TRACEABILITY_ANALYSIS.md:1` per repo (requirement → claimed → actual → evidence → status, with table rows detected count).
- **Critical mapping:** Shows how competitors map solution to PS — vedraya honest table (e.g., ABDM NOT CONNECTED), AyuSphere gap phases 7-10 honestly documents gaps (Phases 7-10 future work).

## 9. Feature Presentation

- **What each competitor emphasizes (from pitch docs, not code):**
  - vedraya: Live Command Center + auditable RBAC 7 + study ACL + GLOBAL SHA-256 verify + PS traceability + honest prototype-only scope + cinematic landing (6-area table Operations/Safety/Governance/Security/Integrity/Interop)
  - AyuSphere: AI Doctor Note OCR + grounded Copilot (declines) + real CTRI scrape + synthetic de-identified + CRF immutability + PGlite no Docker + test-gated 157 tests
  - AyuTrial: 28 routes + 10 trials + 8-site network + NPvCC apex 24h/7d/14d + WHO-UMC + Ayurveda Prakriti/Agni/Koshtha + ABDM blueprint + 10 KPIs + ALCOA+ hash (mocked)
  - Dashboard: FastAPI + 11 routers (trials 11KB) + 41KB CreateTrialPage — only Python stack
  - Anushka/rimi: 24 trials/30 AEs seed + Trials/Safety pages (30KB) + Dashboard — shell, rimi adds AWS/Dictionary/ESignature modals (mocked)
  - DEV-RUSH: FHIR/SDTM/ADaM/Define stubs (6-12KB) — smallest (5 commits)
- **Comparison:** `presentation_analysis/comparisons/FEATURE_PRESENTATION_COMPARISON.md:1` (Top features/Clinical/Regulatory/AI/Interop/Security/Analytics/Pharmacovigilance/Unique claims).
- **Per-repo:** `presentation_analysis/analysis/*/FEATURE_PRESENTATION_ANALYSIS.md:1`.

## 10. Demo Flow Comparison

- **Detailed comparison table (10 stages: Opening → Closing):** See `presentation_analysis/comparisons/DEMO_COMPARISON.md:1`.
- **Key:** Only vedraya + AyuSphere have detailed judge-grade demo flows with exact click paths (drift-guard tested); AyuTrial has 28-route site map but no separate demo script; others no demo script (DEV-RUSH has data seeding scripts, not demo flow).
- **VEDRAYA flow:** 9 steps, 60-second (Enter Command Center → admin login → Live PG badge → AYU-024 → Safety AE DEMO MedDRA → escalate SAE → Consents/Regulatory → Quality → Audit re-verify → Exports → logout monitor/regulator ACL).
- **AyuSphere flow:** Live demo https://ayusphere-three.vercel.app → sign in as 7 roles (pi@aiia.demo Demo@1234) → sidebar 6 sections + quick search + bell → per-role workflows (Administrator: Settings AI Model + Alerts & Deadlines etc.)

## 11. Judge Question Bank

- **Combined deduped:** 36 questions grouped into Technical/Clinical/Regulatory/AI/Security/Architecture/Data/Interoperability/Scalability/Deployment/Innovation/Demo/Implementation.
- **Sources:** `nishant-uxs_vedraya/docs/JUDGE_QA.md:1` (3.5KB, 10+ question-like lines) + `vansh459_AyuSphere/docs/uat/Tech_Security_Guide.md:1` (17KB) + manual curated based on claim vs code gaps (21 CFR, WORM, ABDM, CTRI, AI grounding, offline, etc.) + `analysis/*/JUDGE_QA_ANALYSIS.md:1` categories.
- **File:** `presentation_analysis/MASTER_JUDGE_QUESTION_BANK.md:1` — each question with source per repo (e.g., `docs/JUDGE_QA.md:1` vs `scripts/scrape/ctri_scrape.py:1`).
- **Examples:** How does ACL enforce monitor AYU-024 only? Is audit WORM? Is MedDRA licensed? Is FHIR certified? Is ABDM connected? Real vs synthetic? AI hallucination handling?

## 12. Claim vs Implementation (presentation claims vs actual code)

- **Critical:** For every major presentation claim, `presentation_analysis/analysis/*/CLAIM_VS_EVIDENCE.md:1` records Claim | Source | Actual code evidence | Relevant files | Status (IMPLEMENTED etc.).
- **Examples:**
  - `AnushkaTadiyal_aiia-ctms`: CLAIM `21 CFR Part 11 compliant` (README) → FACT auth bcryptjs+JWT only, no WORM/eSign, AuditPage no hash → Status **CLAIMED ONLY**
  - `nishant-uxs_vedraya`: CLAIM GLOBAL SHA-256 chain → FACT `server/src/modules/audit/service.ts:1` + verify endpoint + 46/46 tests tamper→valid:false → **IMPLEMENTED** (not WORM)
  - `vansh459_AyuSphere`: CLAIM AI-assisted extraction → FACT `src/app/api/ai/extract/route.ts:1` Claude OCR + 11KB mocked test + PI approve gate → **IMPLEMENTED** (external LLM, not trained model)
  - `DuvvuruDeepakReddy18_AyuTrial`: CLAIM ABDM integrated → FACT no adapter code, blueprint matrix only → **CLAIMED ONLY** vs vedraya honest NOT CONNECTED
  - `rimi007-grt_AIIA-CTMS`: CLAIM AWS Cloud integrated → FACT AWSCloudModal.jsx 15KB UI without backend AWS call → **MOCKED**
- **Rule:** Never declare legal/regulatory compliance (21 CFR, GCP, DPDP) — infer may contribute, not compliant. See `analysis/COMPETITOR_MATRIX.md:1` for full statuses.

## 13. Common Presentation Patterns (what competitors do)

- **Common pitch structure (≥4 repos via README):** Problem (SIH26046 Ministry/AIIA) → Existing gap (disconnected governance) → Solution (CTMS + dashboard) → Architecture (split FE/BE/DB diagram or stated) → Features (table or site map) → Technology (React/Next/Vite + Tailwind + Recharts + Drizzle) → Compliance disclaimer → Deployment (Vercel/Docker) → Demo (login/persona) → Impact/Future (rare).
- **Only 2 include explicit gap/limitations/traceability:** vedraya (gap via marketing vs live truth + LIMITATIONS.md + traceability 8KB) + AyuSphere (gap-analysis 13KB + gap-plan 16KB Phases 7-10 + decisions.md 29KB).
- **Only 2 include judge-grade demo scripts with exact click paths:** vedraya (9-step 60-sec + e2e critical path 11KB drift-guard) + AyuSphere (Judge_Demo_Script 4.1KB + 7 role UAT guides drift-guard tested against permission matrix).
- **Only 1 includes 28-route site map (most feature-dense pitch):** AyuTrial README 9.4KB + ARCHITECTURE.md 5KB (Public/Operational/Quality/Compliance/Administration grouped).
- **No PPT:** All pitch via Markdown + PDF UAT, not PowerPoint.

## 14. Common Claims (presentation)

- **Common claims across ≥5 repos (presentation):** Protocol management, multi-centre trials, participant management, AE/SAE, RBAC 7, audit trail, real-time KPIs, synthetic data, cloud deployment (Vercel/Render) — all claim these in README tables.
- **Common overclaims (presentation says but code shows MOCKED/CLAIMED ONLY):** 21 CFR Part 11 (2 repos claim, 0 certified), ABDM integrated (1 claim, 0 actual), CTRI external API (1 real scrape, 2 tracking, 2 claimed, no official API), FHIR/CDISC certified (4 claim prototype/stub as implemented, only AyuSphere truly tested).
- **Rare claims (1-2 repos):** NPvCC apex (only AyuTrial), AI (only AyuSphere), immutable hash chain (vedraya + AyuSphere), FHIR↔CDISC mapping (only AyuSphere partial), UAT PDFs (only AyuSphere), Judge Q&A (only vedraya full).
- **Honest claims (vedraya):** Explicitly says prototype only, not certified, lists NOT CONNECTED/NOT IMPLEMENTED (ABDM, WORM, licensed dictionaries, full CDISC) — trust-building vs overclaim.

## 15. Commonly Demonstrated Features (what they show judges)

- **Across repos with demo scripts/UAT (vedraya + AyuSphere):** Trial creation → participants → AE/SAE → audit → FHIR/CDISC exports (prototype) → RBAC logout. Both demonstrate audit (vedraya re-verify hash, AyuSphere append-only). Both demonstrate RBAC (vedraya monitor/regulator ACL, AyuSphere regulator read-only).
- **AyuTrial (no explicit demo script but 28 routes):** Demonstrates NPvCC 24h clock + WHO-UMC via pharmacovigilance page (22KB form) — not seen in other demos.
- **Commonly mocked in demo:** CRF/EDC (AyuTrial localStorage), audit immutability (AyuTrial local hash), offline (localStorage), ABDM (blueprint).

## 16. Rarely Demonstrated Features (what few show)

- **NPvCC workflow:** Only AyuTrial (dedicated desk, CDSCO pipeline, printable CIOMS-I/MedWatch 3500A)
- **AI Doctor Note extraction:** Only AyuSphere (Claude OCR + flagged fields confirm + PI approve)
- **FHIR↔CDISC mapping:** Only AyuSphere partial (both exist separately, no mapping file)
- **Batch traceability / individualization-aware protocol / assessment-reliability QA:** 0/7 beyond AyuTrial Prakriti fields (data, not logic) — gaps to exploit per task 6.
- **UAT role guides:** Only AyuSphere (7 role PDFs, each 4-13 pages with screenshots)
- **Traceability matrix:** Only vedraya 8KB + AyuSphere gap-analysis 13KB

## 17. Missing Presentation Evidence (what is NOT found)

- **PPT/PPTX:** 0/7 (verified recursive search) — no slide decks in repo. Do not manufacture.
- **PDF pitch decks:** 0 — 9 PDFs are UAT/Judge/Tech guides, not pitch decks (text extraction shows UAT structure, not slides). No architecture PDFs beyond Tech_Security_Guide 155KB (11 pages) and UATs.
- **Demo scripts:** Missing in 5/7 repos (Anushka, rimi, AyuTrial, Dashboard, DEV-RUSH) — no *DEMO_SCRIPT.md* (verified rglob).
- **Judge Q&A:** Missing in 5/7 (same 5) — no *JUDGE_QA.md*.
- **Traceability:** Missing in 5/7 (same 5) — no *TRACEABILITY* docs.
- **Screenshots as standalone files:** No `screenshots/` folder with keyword hits — 0 presentation-related images via path keyword `screenshot` (404 total images exist but under public/assets/frames, not screenshots). Screenshots are embedded inside PDFs as XObject/Image (detected per page Visual note).
- **Videos/recordings:** 0 `*.mp4`, `*.mov` etc. found with keyword `video`/`recording` (verified).
- **What 5 sparse repos show:** Only README pitch (8-10KB) + maybe ARCHITECTURE.md (1-5KB) — no judge preparation material, indicating low judging readiness vs vedraya/AyuSphere.

## 18. Unknowns

- Official MoAyush SIH26046 PS PDF not in repos — traceability docs used as evidence (vedraya 8KB, AyuSphere gap-analysis 13KB).
- Whether SIH expects official CTRI API vs tracking — only AyuSphere scrape found, not official API.
- ABDM sandbox availability — no adapter code, unknown if expected.
- Vercel live health for 4 claimed demos (vedraya-three.vercel.app, ayusphere-three.vercel.app, ayutrial-ctms.vercel.app, sih-26046-dev-rush.vercel.app) — URLs in README but not fetched (network not required).
- Dashboard pytest coverage value — requirements lists pytest but few *.test.py found, insufficient evidence.
- DEV-RUSH route depth — file sizes 6-12KB but bodies not fully read, UNKNOWN depth.
- For PDF text extraction: Many pages are image-based screenshots (XObject/Image) — pypdf extracted minimal text (titles like `Messages`, `Clinical Trials`) + headings, but full visual requires inspection of original PDF (`presentations/*/ *UAT*.pdf` copied). Marked `Visual: Page contains embedded images` per page.

## 19. Evidence Index

| Presentation artifact | Source file | Copied to | Analysis file |
|---|---|---|---|
| Vedraya Demo Script (9 steps, 60-sec) | `repositories/nishant-uxs_vedraya/docs/DEMO_SCRIPT.md:1` (3.0 KB) | `presentation_analysis/extracted/nishant-uxs_vedraya/docs_DEMO_SCRIPT.md` + `presentations/nishant-uxs_vedraya/docs_DEMO_SCRIPT.md` | `presentation_analysis/analysis/nishant-uxs_vedraya/DEMO_ANALYSIS.md:1` |
| Vedraya Judge Q&A (3.5KB) | `repositories/nishant-uxs_vedraya/docs/JUDGE_QA.md:1` | same + `VEDRAYA_JUDGE_ANALYSIS.md:1` | `analysis/nishant-uxs_vedraya/JUDGE_QA_ANALYSIS.md:1` |
| Vedraya Traceability (8KB) | `repositories/nishant-uxs_vedraya/docs/SIH26046_TRACEABILITY_FINAL.md:1` | same | `analysis/nishant-uxs_vedraya/TRACEABILITY_ANALYSIS.md:1` |
| Vedraya Architecture (5.5KB) | `repositories/nishant-uxs_vedraya/docs/ARCHITECTURE.md:1` | same | `analysis/nishant-uxs_vedraya/ARCHITECTURE_CLAIM_VS_CODE.md:1` |
| AyuSphere Judge Demo Script (4.1KB + 1.31MB pdf) | `repositories/vansh459_AyuSphere/docs/uat/Judge_Demo_Script.md:1` + `.pdf` | `presentation_analysis/extracted/vansh459_AyuSphere/docs_uat_Judge_Demo_Script.*` | `analysis/vansh459_AyuSphere/DEMO_ANALYSIS.md:1` |
| AyuSphere UAT 7 guides (0.4-3.3MB PDFs, 4-13 pages) | `repositories/vansh459_AyuSphere/docs/uat/UAT_Guide_*.pdf:1` | `presentation_analysis/extracted/vansh459_AyuSphere/docs_uat_UAT_Guide_*.pdf.md` (per-page headings/tables/images) + `presentations/vansh459_AyuSphere/` | `analysis/vansh459_AyuSphere/AYUSPHERE_PRESENTATION_ANALYSIS.md:1` |
| AyuSphere Tech Security Guide (17KB + 155KB pdf 11 pages) | `repositories/vansh459_AyuSphere/docs/uat/Tech_Security_Guide.md:1` | same | `analysis/vansh459_AyuSphere/JUDGE_QA_ANALYSIS.md:1` |
| All 9 PDF extractions | `repositories/vansh459_AyuSphere/docs/uat/*.pdf:1` | `presentation_analysis/extracted/vansh459_AyuSphere/docs_uat_*.pdf.md` (per-page) | `presentation_analysis/IMAGE_INVENTORY.md:1` notes XObject |
| Zero PPT | `*.ppt*` search | `presentation_analysis/extracted/PPT_INVENTORY.md:1` (PPT FOUND 0) | `INVENTORY.md:1` table |
| Image inventory (404 total, 399 under public/assets/frames) | `repositories/*/public` `*webp/svg/png` | `presentation_analysis/IMAGE_INVENTORY.md:1` + `extracted/*/IMAGE_INVENTORY.md:1` per repo | `INVENTORY.md:1` |
| PPT/PDF image visuals | PDFs XObject/Image | `presentation_analysis/extracted/vansh459_AyuSphere/*.pdf.md` per-page `Visual: Page contains embedded images` | `IMAGE_INVENTORY.md:1` |
| Comparisons | — | `presentation_analysis/comparisons/*.md` (5 files: DEMO, JUDGE_QA, PITCH, ARCH, FEATURE) | — |
| Master judge bank | Combined from JUDGE_QA + Tech_Security | `presentation_analysis/MASTER_JUDGE_QUESTION_BANK.md:1` (36 questions, grouped) | — |

---

*All conclusions are FACT (code found) / CLAIM (presentation) / INFERENCE (may contribute) / UNKNOWN — per task 34. No ranking. Do not copy competitor material — summarize and analyze.*
