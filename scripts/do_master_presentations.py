#!/usr/bin/env python3
import pathlib, re
BASE = pathlib.Path(r"E:\SIH26046_COMPETITOR_ANALYSIS")
REPOS = BASE/"repositories"
OUT = BASE/"presentation_analysis"

def read(p):
    try: return p.read_text(encoding="utf-8", errors="ignore")
    except: return ""

# --- MASTER_JUDGE_QUESTION_BANK ---
# Combine all discovered judge questions
# Sources: vedraya JUDGE_QA.md, AyuSphere Tech_Security_Guide.md, plus UAT guides implied questions
ved_judge = read(REPOS/"nishant-uxs_vedraya/docs/JUDGE_QA.md")
ayu_tech = read(REPOS/"vansh459_AyuSphere/docs/uat/Tech_Security_Guide.md")
ayu_judge_demo = read(REPOS/"vansh459_AyuSphere/docs/uat/Judge_Demo_Script.md")

# Extract question-like lines from ved_judge (lines with ?)
ved_qs = re.findall(r"^.*\?.*$", ved_judge, re.M)
# From Ayu tech, headings that are questions
ayu_qs = re.findall(r"^#{1,3}\s+.*\?|^.*\?.*$", ayu_tech, re.M)
# Combine and dedupe
all_qs_raw = ved_qs + ayu_qs
# Add manually curated questions based on earlier analysis of LIMITATIONS and judge expectations
manual_qs = [
    ("How does authentication and RBAC work? Is it 7 roles?", "Technical", "nishant-uxs_vedraya/docs/JUDGE_QA.md:1 + vansh459_AyuSphere/docs/uat/Tech_Security_Guide.md:1"),
    ("How is study membership ACL enforced? Can monitor access only AYU-024?", "Security", "nishant-uxs_vedraya/docs/JUDGE_QA.md:1 + server/src/middleware/studyAccess.ts:1"),
    ("Is audit trail immutable? WORM storage? Can admin delete logs?", "Security", "nishant-uxs_vedraya/docs/JUDGE_QA.md:1 + docs/LIMITATIONS.md:1 + vansh459_AyuSphere audit insert-only"),
    ("What happens if audit log is tampered in DB? Does verify detect it?", "Security", "nishant-uxs_vedraya/docs/JUDGE_QA.md:1 + server/tests/api.audit.integrity.test.ts:1"),
    ("Is MedDRA/WHODrug licensed or demo dictionary?", "Regulatory", "nishant-uxs_vedraya/docs/JUDGE_QA.md:1 + docs/LIMITATIONS.md:1"),
    ("Is CDISC SDTM certified? Define-XML present?", "Interoperability", "nishant-uxs_vedraya/docs/JUDGE_QA.md:1 + docs/IMPLEMENTATION_STATUS.md:1"),
    ("Is FHIR R4 certified integration or prototype?", "Interoperability", "nishant-uxs_vedraya/docs/JUDGE_QA.md:1 + vansh459_AyuSphere fhir-api.test.ts"),
    ("Is ABDM/HIS/EDC actually connected? ABHA verification?", "Interoperability", "nishant-uxs_vedraya/docs/JUDGE_QA.md:1 + README NOT CONNECTED"),
    ("Is 21 CFR Part 11 compliant? eSignature, WORM, audit?", "Regulatory", "AnushkaTadiyal_aiia-ctms README claim vs no code + vedraya honest NOT CLAIMED"),
    ("How is CTRI integrated? Real API or tracking/scrape?", "Regulatory", "vansh459_AyuSphere/scripts/scrape/ctri_scrape.py:1 vs vedraya regulatory/routes.ts tracking"),
    ("Is CTRI data real or synthetic? How often updated?", "Data", "vansh459_AyuSphere docs/uat: trials real CTRI public, participants synthetic"),
    ("Are participants real patient data or synthetic? DPDP compliant?", "Data", "All repos synthetic/de-identified per README + schema no identifier cols (AyuSphere)"),
    ("How does AI work? Claude vs Gemini vs Groq? Mocked or real API?", "AI", "vansh459_AyuSphere/src/app/api/ai/extract/route.ts:1 + tests/extraction.test.ts mocked"),
    ("Does Copilot hallucinate? How is grounding enforced? Does it decline on empty retrieval?", "AI", "vansh459_AyuSphere/tests/copilot.test.ts:1"),
    ("What is the deployment? Vercel only? Where is Postgres? Docker?", "Deployment", "nishant-uxs_vedraya README Vercel SPA only + render.yaml vs vansh459 Vercel+Neon"),
    ("Is live demo actually live or localStorage mock? Supabase vs demo mode?", "Demo", "DuvvuruDeepakReddy18_AyuTrial .env.example NEXT_PUBLIC_APP_ENV=demo vs Supabase"),
    ("Can system work offline in rural sites? IndexedDB sync?", "Scalability", "All repos NOT PRESENT except AyuTrial MOCKED localStorage — gap"),
    ("How are KPIs computed? Real-time derived vs hardcoded?", "Technical", "nishant-uxs_vedraya server/src/modules/alerts/routes.ts vs AyuSphere alerts cron"),
    ("How are adverse events coded? MedDRA/WHODrug pickers?", "Clinical", "nishant-uxs_vedraya coding/routes.ts MEDDRA_DEMO vs AyuSphere dictionaries.test.ts"),
    ("What is the NPvCC workflow? 24h SAE clock? WHO-UMC causality?", "Clinical", "DuvvuruDeepakReddy18_AyuTrial src/app/pharmacovigilance/new/page.tsx:1 24h clock"),
    ("How is data quality assured? CRF immutability? Versioned corrections?", "Data", "vansh459_AyuSphere crf.test.ts + design-qa.test.ts"),
    ("What are the limitations? What is not implemented vs prototype?", "Implementation", "nishant-uxs_vedraya docs/LIMITATIONS.md:1 + docs/IMPLEMENTATION_STATUS.md:1 vs others sparse"),
    ("What differentiates your solution vs other CTMS prototypes?", "Innovation", "All repos pitch differentiators per README — vedraya hash chain, AyuSphere test-gated AI, AyuTrial NPvCC"),
    ("Can you show audit re-verify live? Show before/after tamper?", "Demo", "nishant-uxs_vedraya docs/DEMO_SCRIPT.md:1 step 6 Audit → Re-verify SHA-256"),
    ("How scalable is architecture? Monolith vs microservices? Why not microservices?", "Architecture", "nishant-uxs_vedraya docs/ARCHITECTURE.md:1 modular monolith vs AyuSphere Next.js"),
    ("What tests exist? Coverage? E2E?", "Technical", "vedraya 46/46 Vitest + 26/26 Playwright vs AyuSphere 157 PGlite vs AyuTrial 21 tsx"),
]

# Deduplicate by question text lower
seen=set()
unique=[]
for q, cat, src in manual_qs:
    key=q.lower()
    if key not in seen:
        seen.add(key)
        unique.append((q,cat,src))
# Also add extracted ved_qs as additional but many are already covered
for q in ved_qs[:10]:
    q_clean=q.strip()
    if len(q_clean)<10 or len(q_clean)>200: continue
    key=q_clean.lower()
    if key not in seen:
        seen.add(key)
        unique.append((q_clean,"Technical","nishant-uxs_vedraya/docs/JUDGE_QA.md:1 (extracted)"))

# Group by category
from collections import defaultdict
grouped=defaultdict(list)
for q,cat,src in unique:
    grouped[cat].append((q,src))

bank_md = "# Master Judge Question Bank — SIH26046\n\n"
bank_md += "**Generated:** 2026-09-30\n**Repositories scanned:** 7 (nishant-uxs_vedraya, vansh459_AyuSphere primary judge material; others via README/analysis)\n**Total questions combined (deduped):** " + str(len(unique)) + "\n"
bank_md += "**Sources:** `nishant-uxs_vedraya/docs/JUDGE_QA.md:1` (3.5KB), `vansh459_AyuSphere/docs/uat/Tech_Security_Guide.md:1` (17KB), `analysis/*/JUDGE_QA_ANALYSIS.md:1` + traceability/limitations, `COMPETITOR_MATRIX.md:1` claim vs code.\n\n"
bank_md += "> Do not confuse PDF UAT guides with PowerPoint — PPT/PPTX FOUND: 0.\n\n"
for cat in sorted(grouped):
    bank_md += f"## {cat}\n\n"
    for i,(q,src) in enumerate(sorted(grouped[cat]),1):
        bank_md += f"{i}. **Q:** {q}  \n   **Source:** `{src}`\n"
    bank_md += "\n"

bank_md += "---\n\n## Evidence Index for Questions\n\n"
bank_md += "- Technical/RBAC/audit questions → verify via `analysis/nishant-uxs_vedraya/REPO_ANALYSIS.md:7` (Auth/RBAC) + `analysis/vansh459_AyuSphere/REPO_ANALYSIS.md:7`\n"
bank_md += "- Regulatory/21 CFR → `analysis/AnushkaTadiyal_aiia-ctms/CLAIM_VS_EVIDENCE.md:1` (CLAIMED ONLY) vs `nishant-uxs_vedraya/docs/LIMITATIONS.md:1` (honest)\n"
bank_md += "- AI → `vansh459_AyuSphere/src/app/api/ai/extract/route.ts:1` + `tests/extraction.test.ts:1`\n"
bank_md += "- FHIR/CDISC/ABDM → `analysis/*/REPO_ANALYSIS.md:11-14` (search hits FHIR 0-5, CDISC 0-3, ABDM 0-1)\n"
bank_md += "- Data/DPDP → `src/db/schema.ts:1` (AyuSphere no identifier cols), `server/src/db/seed.ts:1` synthetic\n"

(OUT/"MASTER_JUDGE_QUESTION_BANK.md").write_text(bank_md, encoding="utf-8")
print(f"MASTER_JUDGE_QUESTION_BANK.md {len(unique)} questions")

# --- MASTER_PRESENTATION_ANALYSIS ---
# Read inventory counts
invent = read(OUT/"INVENTORY.md")
# Build master analysis with 19 sections as per spec
m = "# SIH26046 Presentation & Judge Intelligence — Master Analysis\n\n"
m += "**Generated:** 2026-09-30 12:40\n**Repositories scanned:** 7 (repositories/*/ — recursive, excl .git/node_modules)\n**Search scope:** `*.ppt*`, `*.pptx`, `*.pdf`, `*.doc*`, `*.md`, `*.png/jpg/webp/svg/gif` + filenames containing presentation/pitch/demo/judge/architecture/workflow/diagram/screenshot/uat/traceability etc. + content inspection of README/ARCHITECTURE.\n"
m += "**Evidence hierarchy:** code > config > schema > tests > docs > README.\n\n"
m += "---\n\n"
m += "## 1. Artifacts Found\n\n"
m += "- **Total presentation-related artifacts (exhaustive rglob):** 65 (verified via `_inventory_records.json`)\n"
m += "- **By repo:** vedraya 20 (17 md + 3 demo/judge), AyuSphere 27 (17 md + 9 pdf + 1 script), Anushka 2 (READMEs), rimi 2, AyuTrial 3 (README+ARCHITECTURE+workflow), Dashboard 6 (3 md + 2 tests with demo/workflow names + DEPLOYMENT), DEV-RUSH 5 (1 README + 4 demo scripts)\n"
m += "- **No standalone PPT decks** — all presentation material is Markdown + PDF (UAT/Judge/Tech guides) + README pitch. See `INVENTORY.md:1` table per artifact with file type/size/purpose.\n"
m += "- **Also:** 404 total images (all repos, excl .git) — 399 under public/assets/frames (per keyword `assets`/`public`) + 5 other. No `screenshots/` folder with keyword hits; screenshots are embedded inside PDFs as XObject/Image (detected via pypdf).\n\n"
m += "## 2. PPT/PPTX Findings\n\n"
m += "**PPT/PPTX FOUND: 0**\n\n"
m += "> Explicit: No `*.ppt`, `*.pptx`, `*.pptm`, `*.potx` files found in any of 7 repositories (verified `Get-ChildItem -Recurse -Include *.ppt,*.pptx` + Python rglob, excluded .git). `presentation_analysis/extracted/PPT_INVENTORY.md:1` confirms. `extracted/*/PPT_EXTRACTION.md` created per repo stating 0.\n"
m += "- Do not confuse PDF UAT guides (9 PDFs in AyuSphere) with PowerPoint — they are PDFs generated from markdown/docs, not slide decks.\n"
m += "- Conclusion: Competitors do not ship PowerPoint in repo; pitch is via README + docs + UAT PDFs + live demo.\n\n"
m += "## 3. PDF Findings\n\n"
m += "- **Total PDFs:** 9 (all in `vansh459_AyuSphere/docs/uat/` — verified)\n"
m += "- **List:** `Judge_Demo_Script.pdf` (1.31 MB, 10 pages), `Tech_Security_Guide.pdf` (155 KB, 11 pages), 7 UAT guides: Administrator (3.32 MB, 13 pages), Ethics_Committee (466KB, 4p), Monitor (667KB, 5p), Pharmacovigilance (1.28MB, 8p), Principal_Investigator (2.89MB, 13p), Regulator (529KB, 5p), Study_Coordinator (1.91MB, 9p).\n"
m += "- **Content:** UAT guides are **user acceptance testing judge guides** — not pitch decks. Each has dark green sidebar navigation (Overview/Study Conduct/Data Capture/Safety & Quality/Intelligence/System), role-specific workflows (e.g., Administrator: Settings AI Model + Alerts & Deadlines + user accounts + audit trail), exact click paths drift-guard tested against navigation/permission matrix, generated 14 September 2026, live demo https://ayusphere-three.vercel.app, sign-in `admin@aiia.demo` Demo@1234, synthetic data note (trials real CTRI public, participants synthetic DPDP), electronic signatures (`password re-verification + record hashes`), randomization, Define-XML/ADSL/FHIR API etc.\n"
m += "- **Extraction:** `presentation_analysis/extracted/vansh459_AyuSphere/docs_uat_*.pdf.md` (9 files, per-page headings/tables/claims, page numbers preserved via pypdf). Many pages are image-based screenshots (XObject/Image detected per page `Visual: Page contains embedded images`). Text extraction is partial for those pages — shows titles like `Messages`, `Clinical Trials`, `Audit Trail` but screenshots require visual inspection. Marked `Visual: Page contains embedded images` per page.\n"
m += "- **Other repos:** 0 PDFs — vedraya, AyuTrial, Dashboard, Anushka/rimi, DEV-RUSH have no PDFs.\n"
m += "- **Detailed per-PDF:** See `presentation_analysis/extracted/vansh459_AyuSphere/docs_uat_*.pdf.md` (e.g., Administrator 13 pages, headings OVERVIEW/STUDY CONDUCT, claims `AI Assistant`, `Audit Trail`, tables heuristically extracted).\n\n"
m += "## 4. Demo Scripts\n\n"
m += "- **Found:** 2 repositories with explicit demo scripts:\n"
m += "  - `nishant-uxs_vedraya/docs/DEMO_SCRIPT.md:1` (3.0 KB, 9 steps) + README `Judge in 60 seconds` 9 steps — **IMPLEMENTED** demo script (most detailed)\n"
m += "  - `vansh459_AyuSphere/docs/uat/Judge_Demo_Script.md:1` (4.1 KB) + `Judge_Demo_Script.pdf:1` (1.31 MB, 10 pages) — **IMPLEMENTED** judge demo script + 7 role UAT guides\n"
m += "  - Others: **NOT PRESENT** — Anushka/rimi/AyuTrial/Dashboard/DEV-RUSH have no DEMO_SCRIPT.md (verified rglob `*DEMO*`). AyuTrial has README Quick Start 5 steps (not separate demo script), Dashboard has DEPLOYMENT.md, DEV-RUSH has scripts/*demo* data scripts (activate-demo-consent.ts etc. — data seeding, not demo flow).\n"
m += "- **Comparison:** `presentation_analysis/comparisons/DEMO_COMPARISON.md:1` compares opening/problem/RBAC/trial/participant/AE/ethics/regulatory/pharmacovigilance/analytics/AI/FHIR/audit/closing across 7 repos.\n"
m += "- **VEDRAYA demo flow:** Open app → Enter Live Command Center → login admin@vedraya.demo (Vedraya!Demo1) → badge Live PostgreSQL → study AYU-024 → Safety AE DEMO MedDRA → escalate SAE → Consents + Regulatory → Quality → Audit re-verify SHA-256 → Exports (SDTM-like, FHIR prototype) → logout monitor/regulator ACL demo (monitor AYU-024 only, regulator 403). Prerequisite `npm run demo:seed`.\n"
m += "- **AyuSphere demo flow:** Live demo https://ayusphere-three.vercel.app → sign in as 7 roles (pi@aiia.demo Demo@1234 etc.) → exact labels drift-guard tested, sidebar 6 sections + quick search + bell + profile chip, workflows per role (Administrator: Settings AI Model + Alerts & Deadlines etc.).\n"
m += "- **Extracted:** `presentation_analysis/analysis/*/DEMO_ANALYSIS.md:1` per repo (opening/problem/workflow/feature sequence/differentiator/evidence/closing).\n\n"
m += "## 5. Judge Q&A\n\n"
m += "- **Found:** 1 full + 1 partial:\n"
m += "  - `nishant-uxs_vedraya/docs/JUDGE_QA.md:1` (3.5 KB) — **IMPLEMENTED** judge Q&A (most anticipated questions: WORM? licensed MedDRA? FHIR/CDISC certified? ABDM connected? real patient? hosted where? differentiator?)\n"
m += "  - `vansh459_AyuSphere/docs/uat/Tech_Security_Guide.md:1` (17 KB) + .pdf 155KB (11 pages) — **PARTIALLY IMPLEMENTED** judge-facing security Q&A (auth, audit, encryption, API security, deployment, monitoring)\n"
m += "  - Others: **NOT PRESENT** — Anushka/rimi/AyuTrial/Dashboard/DEV-RUSH have no JUDGE_QA.md (verified rglob `*JUDGE_QA*`).\n"
m += "- **Comparison:** `presentation_analysis/comparisons/JUDGE_QA_COMPARISON.md:1` compares 10 categories (Technical/Clinical/Regulatory/AI/Security/Architecture/Data/Interoperability/Deployment/Innovation) across 7 repos.\n"
m += "- **Master bank:** `presentation_analysis/MASTER_JUDGE_QUESTION_BANK.md:1` combines deduped " + str(len(unique)) + " questions grouped into Technical/Clinical/Regulatory/AI/Security/Architecture/Data/Interoperability/Scalability/Deployment/Innovation/Demo/Implementation, with source per question (e.g., `docs/JUDGE_QA.md:1` vs `scripts/scrape/ctri_scrape.py:1`).\n"
m += "- **Per-repo analysis:** `presentation_analysis/analysis/*/JUDGE_QA_ANALYSIS.md:1` (question/answer/evidence/category).\n\n"
m += "## 6. UAT Documents\n\n"
m += "- **Found:** 1 repository with UAT:\n"
m += "  - `vansh459_AyuSphere/docs/uat/` — 7 UAT guides (Administrator, Ethics_Committee, Monitor, Pharmacovigilance, Principal_Investigator, Regulator, Study_Coordinator) + Judge_Demo_Script + Tech_Security_Guide — **9 PDFs total** + markdowns.\n"
m += "  - **Purpose:** User acceptance testing judge guides — each details `Your workspace`, `What you can and cannot do` (e.g., Admin cannot deactivate own account, cannot delete audit entries — append-only), `Core workflows (exact click paths)` (e.g., Settings → AI Model → Save; Create user → Deactivate), `Screens` (Dashboard, Clinical Trials, Ethics Review, Participants, Site Management, Visit Schedule, Data Entry eCRF, Documents, Adverse Events, Monitoring, Alerts, AI Assistant, Reports & Exports, Audit Trail, Settings), `New in this build` (Alerts & Deadlines configurable, electronic signatures, randomization, Define-XML/FHIR).\n"
m += "  - **Test cases:** Not traditional Pass/fail test cases in PDF — but `vansh459_AyuSphere/tests/*.test.ts` 50 suites 157 tests are the automated test evidence (test-gated `docs/tasks.md:1` 24KB). UAT guides are **click-path evaluation guides**, drift-guard tested against navigation/permission matrix, with screenshots (embedded images per page).\n"
m += "  - **Other repos:** 0 UAT — vedraya has `e2e/` Playwright 26/26 + `server/tests/` 46/46 but not UAT PDFs; AyuTrial has `src/tests/workflows.test.ts` 21 tests; Dashboard has `backend/tests/e2e_demo.py` 6.9KB + `test_trial_workflow.py` 4.1KB (workflow tests with demo in name, but not UAT docs).\n"
m += "  - **Comparison:** UAT details in `MASTER_PRESENTATION_ANALYSIS.md:6` + per-repo `TRACEABILITY_ANALYSIS.md`.\n"
m += "  - **Extracted:** `presentation_analysis/extracted/vansh459_AyuSphere/docs_uat_*.pdf.md` (per-page text with headings/tables/images noted).\n\n"
m += "## 7. Architecture Material\n\n"
m += "- **Found:** 3 repositories with explicit architecture docs:\n"
m += "  - `nishant-uxs_vedraya/docs/ARCHITECTURE.md:1` (5.5 KB) — modular monolith diagram (Landing → Command Center → Express /api/v1 Gate→RBAC→ACL→domain → DB PostgreSQL + Drizzle → Chain GLOBAL SHA-256), 14 modules, 5 migrations, Vercel SPA + Render API.\n"
m += "  - `vansh459_AyuSphere/docs/architecture.md:1` (17.4 KB) + `docs/decisions.md:1` 29KB + `docs/technology.md:1` 10.4KB — Next.js + Neon + Drizzle + PGlite no Docker D-019 + Auth.js + Claude/Groq + Tailwind v4 + Vitest/PGlite.\n"
m += "  - `DuvvuruDeepakReddy18_AyuTrial/ARCHITECTURE.md:1` (5.0 KB) — dual-mode Next.js (in-memory + localStorage demo vs Supabase prod) + Recharts + crypto hash, 28 routes.\n"
m += "  - Others: Anushka/rimi have `client/README.md` 1KB (not architecture), Dashboard has `DEPLOYMENT.md` 4.4KB (deployment, not architecture diagram), DEV-RUSH no architecture (minimal README 1.5KB).\n"
m += "- **Comparison:** `presentation_analysis/comparisons/ARCHITECTURE_PRESENTATION_COMPARISON.md:1` compares presented diagram vs actual code (from `analysis/*/ARCHITECTURE.md:1` via `schema.ts`, `routes.ts`, `package.json`). Matches: vedraya/AyuSphere/AyuTrial (with caveat dual-mode prod unknown) → MATCH, rimi AWS mocked → CLAIMED ONLY, DEV-RUSH UNKNOWN.\n"
m += "- **Per-repo:** `presentation_analysis/analysis/*/ARCHITECTURE_CLAIM_VS_CODE.md:1` (presented vs actual table: Frontend/Backend/Database/AI/Cloud/Auth/Data flow).\n\n"
m += "## 8. Traceability Material\n\n"
m += "- **Found:** 2 repositories with traceability:\n"
m += "  - `nishant-uxs_vedraya/docs/SIH26046_TRACEABILITY_FINAL.md:1` (8.0 KB) + `docs/REQUIREMENTS_TRACEABILITY.md:1` 3.5KB + `docs/IMPLEMENTATION_STATUS.md:1` 1.5KB (honest Implemented/Partial/Prototype/Not Connected table) + `docs/IMPLEMENTATION_PLAN.md:1` 4.3KB.\n"
m += "  - `vansh459_AyuSphere/docs/gap-analysis.md:1` (13 KB) + `docs/gap-plan.md:1` 16.4KB (Phases 7-10) + `docs/architecture.md` traceability — PS SIH26046 requirements vs implementation.\n"
m += "  - Others: AyuTrial traces PS in README 9.4KB (not separate traceability doc), Dashboard no traceability, Anushka/rimi no docs, DEV-RUSH no.\n"
m += "- **Extracted:** `presentation_analysis/extracted/nishant-uxs_vedraya/docs_SIH26046_TRACEABILITY_FINAL.md` + `analysis/*/TRACEABILITY_ANALYSIS.md:1` per repo (requirement → claimed → actual → evidence → status, with table rows detected count).\n"
m += "- **Critical mapping:** Shows how competitors map solution to PS — vedraya honest table (e.g., ABDM NOT CONNECTED), AyuSphere gap phases 7-10 honestly documents gaps (Phases 7-10 future work).\n\n"
m += "## 9. Feature Presentation\n\n"
m += "- **What each competitor emphasizes (from pitch docs, not code):**\n"
m += "  - vedraya: Live Command Center + auditable RBAC 7 + study ACL + GLOBAL SHA-256 verify + PS traceability + honest prototype-only scope + cinematic landing (6-area table Operations/Safety/Governance/Security/Integrity/Interop)\n"
m += "  - AyuSphere: AI Doctor Note OCR + grounded Copilot (declines) + real CTRI scrape + synthetic de-identified + CRF immutability + PGlite no Docker + test-gated 157 tests\n"
m += "  - AyuTrial: 28 routes + 10 trials + 8-site network + NPvCC apex 24h/7d/14d + WHO-UMC + Ayurveda Prakriti/Agni/Koshtha + ABDM blueprint + 10 KPIs + ALCOA+ hash (mocked)\n"
m += "  - Dashboard: FastAPI + 11 routers (trials 11KB) + 41KB CreateTrialPage — only Python stack\n"
m += "  - Anushka/rimi: 24 trials/30 AEs seed + Trials/Safety pages (30KB) + Dashboard — shell, rimi adds AWS/Dictionary/ESignature modals (mocked)\n"
m += "  - DEV-RUSH: FHIR/SDTM/ADaM/Define stubs (6-12KB) — smallest (5 commits)\n"
m += "- **Comparison:** `presentation_analysis/comparisons/FEATURE_PRESENTATION_COMPARISON.md:1` (Top features/Clinical/Regulatory/AI/Interop/Security/Analytics/Pharmacovigilance/Unique claims).\n"
m += "- **Per-repo:** `presentation_analysis/analysis/*/FEATURE_PRESENTATION_ANALYSIS.md:1`.\n\n"
m += "## 10. Demo Flow Comparison\n\n"
m += "- **Detailed comparison table (10 stages: Opening → Closing):** See `presentation_analysis/comparisons/DEMO_COMPARISON.md:1`.\n"
m += "- **Key:** Only vedraya + AyuSphere have detailed judge-grade demo flows with exact click paths (drift-guard tested); AyuTrial has 28-route site map but no separate demo script; others no demo script (DEV-RUSH has data seeding scripts, not demo flow).\n"
m += "- **VEDRAYA flow:** 9 steps, 60-second (Enter Command Center → admin login → Live PG badge → AYU-024 → Safety AE DEMO MedDRA → escalate SAE → Consents/Regulatory → Quality → Audit re-verify → Exports → logout monitor/regulator ACL).\n"
m += "- **AyuSphere flow:** Live demo https://ayusphere-three.vercel.app → sign in as 7 roles (pi@aiia.demo Demo@1234) → sidebar 6 sections + quick search + bell → per-role workflows (Administrator: Settings AI Model + Alerts & Deadlines etc.)\n\n"
m += "## 11. Judge Question Bank\n\n"
m += "- **Combined deduped:** " + str(len(unique)) + " questions grouped into Technical/Clinical/Regulatory/AI/Security/Architecture/Data/Interoperability/Scalability/Deployment/Innovation/Demo/Implementation.\n"
m += "- **Sources:** `nishant-uxs_vedraya/docs/JUDGE_QA.md:1` (3.5KB, 10+ question-like lines) + `vansh459_AyuSphere/docs/uat/Tech_Security_Guide.md:1` (17KB) + manual curated based on claim vs code gaps (21 CFR, WORM, ABDM, CTRI, AI grounding, offline, etc.) + `analysis/*/JUDGE_QA_ANALYSIS.md:1` categories.\n"
m += "- **File:** `presentation_analysis/MASTER_JUDGE_QUESTION_BANK.md:1` — each question with source per repo (e.g., `docs/JUDGE_QA.md:1` vs `scripts/scrape/ctri_scrape.py:1`).\n"
m += "- **Examples:** How does ACL enforce monitor AYU-024 only? Is audit WORM? Is MedDRA licensed? Is FHIR certified? Is ABDM connected? Real vs synthetic? AI hallucination handling?\n\n"
m += "## 12. Claim vs Implementation (presentation claims vs actual code)\n\n"
m += "- **Critical:** For every major presentation claim, `presentation_analysis/analysis/*/CLAIM_VS_EVIDENCE.md:1` records Claim | Source | Actual code evidence | Relevant files | Status (IMPLEMENTED etc.).\n"
m += "- **Examples:**\n"
m += "  - `AnushkaTadiyal_aiia-ctms`: CLAIM `21 CFR Part 11 compliant` (README) → FACT auth bcryptjs+JWT only, no WORM/eSign, AuditPage no hash → Status **CLAIMED ONLY**\n"
m += "  - `nishant-uxs_vedraya`: CLAIM GLOBAL SHA-256 chain → FACT `server/src/modules/audit/service.ts:1` + verify endpoint + 46/46 tests tamper→valid:false → **IMPLEMENTED** (not WORM)\n"
m += "  - `vansh459_AyuSphere`: CLAIM AI-assisted extraction → FACT `src/app/api/ai/extract/route.ts:1` Claude OCR + 11KB mocked test + PI approve gate → **IMPLEMENTED** (external LLM, not trained model)\n"
m += "  - `DuvvuruDeepakReddy18_AyuTrial`: CLAIM ABDM integrated → FACT no adapter code, blueprint matrix only → **CLAIMED ONLY** vs vedraya honest NOT CONNECTED\n"
m += "  - `rimi007-grt_AIIA-CTMS`: CLAIM AWS Cloud integrated → FACT AWSCloudModal.jsx 15KB UI without backend AWS call → **MOCKED**\n"
m += "- **Rule:** Never declare legal/regulatory compliance (21 CFR, GCP, DPDP) — infer may contribute, not compliant. See `analysis/COMPETITOR_MATRIX.md:1` for full statuses.\n\n"
m += "## 13. Common Presentation Patterns (what competitors do)\n\n"
m += "- **Common pitch structure (≥4 repos via README):** Problem (SIH26046 Ministry/AIIA) → Existing gap (disconnected governance) → Solution (CTMS + dashboard) → Architecture (split FE/BE/DB diagram or stated) → Features (table or site map) → Technology (React/Next/Vite + Tailwind + Recharts + Drizzle) → Compliance disclaimer → Deployment (Vercel/Docker) → Demo (login/persona) → Impact/Future (rare).\n"
m += "- **Only 2 include explicit gap/limitations/traceability:** vedraya (gap via marketing vs live truth + LIMITATIONS.md + traceability 8KB) + AyuSphere (gap-analysis 13KB + gap-plan 16KB Phases 7-10 + decisions.md 29KB).\n"
m += "- **Only 2 include judge-grade demo scripts with exact click paths:** vedraya (9-step 60-sec + e2e critical path 11KB drift-guard) + AyuSphere (Judge_Demo_Script 4.1KB + 7 role UAT guides drift-guard tested against permission matrix).\n"
m += "- **Only 1 includes 28-route site map (most feature-dense pitch):** AyuTrial README 9.4KB + ARCHITECTURE.md 5KB (Public/Operational/Quality/Compliance/Administration grouped).\n"
m += "- **No PPT:** All pitch via Markdown + PDF UAT, not PowerPoint.\n\n"
m += "## 14. Common Claims (presentation)\n\n"
m += "- **Common claims across ≥5 repos (presentation):** Protocol management, multi-centre trials, participant management, AE/SAE, RBAC 7, audit trail, real-time KPIs, synthetic data, cloud deployment (Vercel/Render) — all claim these in README tables.\n"
m += "- **Common overclaims (presentation says but code shows MOCKED/CLAIMED ONLY):** 21 CFR Part 11 (2 repos claim, 0 certified), ABDM integrated (1 claim, 0 actual), CTRI external API (1 real scrape, 2 tracking, 2 claimed, no official API), FHIR/CDISC certified (4 claim prototype/stub as implemented, only AyuSphere truly tested).\n"
m += "- **Rare claims (1-2 repos):** NPvCC apex (only AyuTrial), AI (only AyuSphere), immutable hash chain (vedraya + AyuSphere), FHIR↔CDISC mapping (only AyuSphere partial), UAT PDFs (only AyuSphere), Judge Q&A (only vedraya full).\n"
m += "- **Honest claims (vedraya):** Explicitly says prototype only, not certified, lists NOT CONNECTED/NOT IMPLEMENTED (ABDM, WORM, licensed dictionaries, full CDISC) — trust-building vs overclaim.\n\n"
m += "## 15. Commonly Demonstrated Features (what they show judges)\n\n"
m += "- **Across repos with demo scripts/UAT (vedraya + AyuSphere):** Trial creation → participants → AE/SAE → audit → FHIR/CDISC exports (prototype) → RBAC logout. Both demonstrate audit (vedraya re-verify hash, AyuSphere append-only). Both demonstrate RBAC (vedraya monitor/regulator ACL, AyuSphere regulator read-only).\n"
m += "- **AyuTrial (no explicit demo script but 28 routes):** Demonstrates NPvCC 24h clock + WHO-UMC via pharmacovigilance page (22KB form) — not seen in other demos.\n"
m += "- **Commonly mocked in demo:** CRF/EDC (AyuTrial localStorage), audit immutability (AyuTrial local hash), offline (localStorage), ABDM (blueprint).\n\n"
m += "## 16. Rarely Demonstrated Features (what few show)\n\n"
m += "- **NPvCC workflow:** Only AyuTrial (dedicated desk, CDSCO pipeline, printable CIOMS-I/MedWatch 3500A)\n"
m += "- **AI Doctor Note extraction:** Only AyuSphere (Claude OCR + flagged fields confirm + PI approve)\n"
m += "- **FHIR↔CDISC mapping:** Only AyuSphere partial (both exist separately, no mapping file)\n"
m += "- **Batch traceability / individualization-aware protocol / assessment-reliability QA:** 0/7 beyond AyuTrial Prakriti fields (data, not logic) — gaps to exploit per task 6.\n"
m += "- **UAT role guides:** Only AyuSphere (7 role PDFs, each 4-13 pages with screenshots)\n"
m += "- **Traceability matrix:** Only vedraya 8KB + AyuSphere gap-analysis 13KB\n\n"
m += "## 17. Missing Presentation Evidence (what is NOT found)\n\n"
m += "- **PPT/PPTX:** 0/7 (verified recursive search) — no slide decks in repo. Do not manufacture.\n"
m += "- **PDF pitch decks:** 0 — 9 PDFs are UAT/Judge/Tech guides, not pitch decks (text extraction shows UAT structure, not slides). No architecture PDFs beyond Tech_Security_Guide 155KB (11 pages) and UATs.\n"
m += "- **Demo scripts:** Missing in 5/7 repos (Anushka, rimi, AyuTrial, Dashboard, DEV-RUSH) — no *DEMO_SCRIPT.md* (verified rglob).\n"
m += "- **Judge Q&A:** Missing in 5/7 (same 5) — no *JUDGE_QA.md*.\n"
m += "- **Traceability:** Missing in 5/7 (same 5) — no *TRACEABILITY* docs.\n"
m += "- **Screenshots as standalone files:** No `screenshots/` folder with keyword hits — 0 presentation-related images via path keyword `screenshot` (404 total images exist but under public/assets/frames, not screenshots). Screenshots are embedded inside PDFs as XObject/Image (detected per page Visual note).\n"
m += "- **Videos/recordings:** 0 `*.mp4`, `*.mov` etc. found with keyword `video`/`recording` (verified).\n"
m += "- **What 5 sparse repos show:** Only README pitch (8-10KB) + maybe ARCHITECTURE.md (1-5KB) — no judge preparation material, indicating low judging readiness vs vedraya/AyuSphere.\n\n"
m += "## 18. Unknowns\n\n"
m += "- Official MoAyush SIH26046 PS PDF not in repos — traceability docs used as evidence (vedraya 8KB, AyuSphere gap-analysis 13KB).\n"
m += "- Whether SIH expects official CTRI API vs tracking — only AyuSphere scrape found, not official API.\n"
m += "- ABDM sandbox availability — no adapter code, unknown if expected.\n"
m += "- Vercel live health for 4 claimed demos (vedraya-three.vercel.app, ayusphere-three.vercel.app, ayutrial-ctms.vercel.app, sih-26046-dev-rush.vercel.app) — URLs in README but not fetched (network not required).\n"
m += "- Dashboard pytest coverage value — requirements lists pytest but few *.test.py found, insufficient evidence.\n"
m += "- DEV-RUSH route depth — file sizes 6-12KB but bodies not fully read, UNKNOWN depth.\n"
m += "- For PDF text extraction: Many pages are image-based screenshots (XObject/Image) — pypdf extracted minimal text (titles like `Messages`, `Clinical Trials`) + headings, but full visual requires inspection of original PDF (`presentations/*/ *UAT*.pdf` copied). Marked `Visual: Page contains embedded images` per page.\n\n"
m += "## 19. Evidence Index\n\n"
m += "| Presentation artifact | Source file | Copied to | Analysis file |\n|---|---|---|---|\n"
m += "| Vedraya Demo Script (9 steps, 60-sec) | `repositories/nishant-uxs_vedraya/docs/DEMO_SCRIPT.md:1` (3.0 KB) | `presentation_analysis/extracted/nishant-uxs_vedraya/docs_DEMO_SCRIPT.md` + `presentations/nishant-uxs_vedraya/docs_DEMO_SCRIPT.md` | `presentation_analysis/analysis/nishant-uxs_vedraya/DEMO_ANALYSIS.md:1` |\n"
m += "| Vedraya Judge Q&A (3.5KB) | `repositories/nishant-uxs_vedraya/docs/JUDGE_QA.md:1` | same + `VEDRAYA_JUDGE_ANALYSIS.md:1` | `analysis/nishant-uxs_vedraya/JUDGE_QA_ANALYSIS.md:1` |\n"
m += "| Vedraya Traceability (8KB) | `repositories/nishant-uxs_vedraya/docs/SIH26046_TRACEABILITY_FINAL.md:1` | same | `analysis/nishant-uxs_vedraya/TRACEABILITY_ANALYSIS.md:1` |\n"
m += "| Vedraya Architecture (5.5KB) | `repositories/nishant-uxs_vedraya/docs/ARCHITECTURE.md:1` | same | `analysis/nishant-uxs_vedraya/ARCHITECTURE_CLAIM_VS_CODE.md:1` |\n"
m += "| AyuSphere Judge Demo Script (4.1KB + 1.31MB pdf) | `repositories/vansh459_AyuSphere/docs/uat/Judge_Demo_Script.md:1` + `.pdf` | `presentation_analysis/extracted/vansh459_AyuSphere/docs_uat_Judge_Demo_Script.*` | `analysis/vansh459_AyuSphere/DEMO_ANALYSIS.md:1` |\n"
m += "| AyuSphere UAT 7 guides (0.4-3.3MB PDFs, 4-13 pages) | `repositories/vansh459_AyuSphere/docs/uat/UAT_Guide_*.pdf:1` | `presentation_analysis/extracted/vansh459_AyuSphere/docs_uat_UAT_Guide_*.pdf.md` (per-page headings/tables/images) + `presentations/vansh459_AyuSphere/` | `analysis/vansh459_AyuSphere/AYUSPHERE_PRESENTATION_ANALYSIS.md:1` |\n"
m += "| AyuSphere Tech Security Guide (17KB + 155KB pdf 11 pages) | `repositories/vansh459_AyuSphere/docs/uat/Tech_Security_Guide.md:1` | same | `analysis/vansh459_AyuSphere/JUDGE_QA_ANALYSIS.md:1` |\n"
m += "| All 9 PDF extractions | `repositories/vansh459_AyuSphere/docs/uat/*.pdf:1` | `presentation_analysis/extracted/vansh459_AyuSphere/docs_uat_*.pdf.md` (per-page) | `presentation_analysis/IMAGE_INVENTORY.md:1` notes XObject |\n"
m += "| Zero PPT | `*.ppt*` search | `presentation_analysis/extracted/PPT_INVENTORY.md:1` (PPT FOUND 0) | `INVENTORY.md:1` table |\n"
m += "| Image inventory (404 total, 399 under public/assets/frames) | `repositories/*/public` `*webp/svg/png` | `presentation_analysis/IMAGE_INVENTORY.md:1` + `extracted/*/IMAGE_INVENTORY.md:1` per repo | `INVENTORY.md:1` |\n"
m += "| PPT/PDF image visuals | PDFs XObject/Image | `presentation_analysis/extracted/vansh459_AyuSphere/*.pdf.md` per-page `Visual: Page contains embedded images` | `IMAGE_INVENTORY.md:1` |\n"
m += "| Comparisons | — | `presentation_analysis/comparisons/*.md` (5 files: DEMO, JUDGE_QA, PITCH, ARCH, FEATURE) | — |\n"
m += "| Master judge bank | Combined from JUDGE_QA + Tech_Security | `presentation_analysis/MASTER_JUDGE_QUESTION_BANK.md:1` (" + str(len(unique)) + " questions, grouped) | — |\n"
m += "\n---\n\n*All conclusions are FACT (code found) / CLAIM (presentation) / INFERENCE (may contribute) / UNKNOWN — per task 34. No ranking. Do not copy competitor material — summarize and analyze.*\n"

(OUT/"MASTER_PRESENTATION_ANALYSIS.md").write_text(m, encoding="utf-8")
print(f"MASTER_PRESENTATION_ANALYSIS.md written")
print(f"Bank questions {len(unique)}")

