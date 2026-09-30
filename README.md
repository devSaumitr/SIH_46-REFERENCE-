# SIH26046_COMPETITOR_ANALYSIS — Repository Extraction + Deep Competitor Analysis

**Generated:** 2026-09-30 12:38
**Problem:** SIH26046 — AIIA Clinical Trial Management System / Clinical Trials Dashboard (Ministry of Ayush / All India Institute of Ayurveda). Real-time, cloud-based, GCP-compliant CTMS for Ayurveda, CDISC/FHIR-interoperable, role-based KPIs, ethics/regulatory (CTRI/NDCT 2019) + pharmacovigilance (NPvCC for ASU&H).
**Task:** OPENCODE MASTER TASK — Phases 1 (extraction & organization) + 2 (deep code-level competitor analysis) — both done, not stopped after repo list.
**Evidence hierarchy:** code > config > schema > tests > docs > README — every status verified against actual files, not just button/page/README.

---

## Quick Start

```powershell
tree /F E:\SIH26046_COMPETITOR_ANALYSIS
cat E:\SIH26046_COMPETITOR_ANALYSIS\analysis\COMPETITOR_MATRIX.md
cat E:\SIH26046_COMPETITOR_ANALYSIS\analysis\MASTER_ANALYSIS.md
cat E:\SIH26046_COMPETITOR_ANALYSIS\MASTER_PROMPT.md
```

## Directory Structure (as requested, exactly)

```text
SIH26046_COMPETITOR_ANALYSIS/
│
├── README.md                              # YOU ARE HERE
│
├── repositories/                          # 7 repos, each independent, preserved structure, excluded .git/node_modules in analysis
│   ├── AnushkaTadiyal_aiia-ctms/          # https://github.com/AnushkaTadiyal/aiia-ctms (56 files)
│   ├── vansh459_AyuSphere/                # https://github.com/vansh459/AyuSphere (282 files, AI + CTRI scrape)
│   ├── aravindakrishna-c_AIIA-Clinical-Trial-Dashboard/ # https://github.com/aravindakrishna-c/AIIA-Clinical-Trial-Dashboard (153 files, FastAPI)
│   ├── rimi007-grt_AIIA-CTMS/             # https://github.com/rimi007-grt/AIIA-CTMS (72 files, fork + Docker)
│   ├── nishant-uxs_vedraya/               # https://github.com/nishant-uxs/vedraya (533 files, honest prototype + judge docs)
│   ├── DuvvuruDeepakReddy18_AyuTrial/     # https://github.com/DuvvuruDeepakReddy18/AyuTrial (57 files, 28 routes, NPvCC)
│   └── kalyan-2006-prog_SIH26046-DEV-RUSH-/ # https://github.com/kalyan-2006-prog/SIH26046-DEV-RUSH- (66 files, stubs)
│
├── analysis/
│   ├── COMPETITOR_MATRIX.md               # 28×7 evidence-based matrix (IMPLEMENTED etc., no ranking)
│   ├── MASTER_ANALYSIS.md                 # Master synthesis (22 sections: tech, matrix, workflows, FHIR/CDISC, RBAC, audit, AI, gaps, evidence index)
│   ├── AnushkaTadiyal_aiia-ctms/
│   │   ├── REPO_ANALYSIS.md               # 23 sections (Overview → Unknowns)
│   │   ├── REPO_DETAILS.md                # name, owner, URL, language, FE/BE/DB, framework, deploy, license, size, tests, docs, SIH relevance
│   │   ├── FILE_STRUCTURE.md              # tree (max depth 8) + per-file purpose/functions/dependencies
│   │   ├── README_ANALYSIS.md             # complete README + extracted claims + trust verification
│   │   └── ARCHITECTURE.md                # diagram + DB + API + auth + AI + pipelines + deployment evidence
│   ├── vansh459_AyuSphere/... (same 5)
│   ├── aravindakrishna-c_AIIA-Clinical-Trial-Dashboard/... (same)
│   ├── rimi007-grt_AIIA-CTMS/... (same)
│   ├── nishant-uxs_vedraya/... (same + VEDRAYA special investigation)
│   ├── DuvvuruDeepakReddy18_AyuTrial/... (same)
│   └── kalyan-2006-prog_SIH26046-DEV-RUSH-/... (same)
│
├── presentations/
│   ├── nishant-uxs_vedraya/
│   │   ├── PRESENTATION_INVENTORY.md      # search results: PPT 0, PDF 0, demo 3
│   │   ├── docs_DEMO_SCRIPT.md            # 3.0 KB copied
│   │   ├── docs_JUDGE_QA.md               # 3.5 KB copied
│   │   ├── docs_SIH26046_TRACEABILITY_FINAL.md # 8.0 KB copied
│   │   ├── docs_IMPLEMENTATION_STATUS.md  # 1.5 KB
│   │   ├── docs_RBAC.md                   # 3.6 KB
│   │   └── docs_ARCHITECTURE.md           # 5.5 KB
│   ├── vansh459_AyuSphere/
│   │   ├── PRESENTATION_INVENTORY.md      # search: PPT 0, PDF 9
│   │   ├── docs_architecture.md           # 17.4 KB copied
│   │   ├── docs_uat_Judge_Demo_Script.md  # 4.1 KB copied
│   │   ├── docs_uat_Judge_Demo_Script.pdf # 1.31 MB copied
│   │   ├── docs_uat_Tech_Security_Guide.md # 17.0 KB copied
│   │   ├── docs_uat_Tech_Security_Guide.pdf # 155 KB copied
│   │   ├── docs_uat_UAT_Guide_Administrator.pdf # 3.32 MB copied
│   │   ├── docs_uat_UAT_Guide_Ethics_Committee.pdf # 466 KB
│   │   ├── docs_uat_UAT_Guide_Monitor.pdf # 667 KB
│   │   ├── docs_uat_UAT_Guide_Pharmacovigilance.pdf # 1.28 MB
│   │   ├── docs_uat_UAT_Guide_Principal_Investigator.pdf # 2.89 MB
│   │   ├── docs_uat_UAT_Guide_Regulator.pdf # 529 KB
│   │   └── docs_uat_UAT_Guide_Study_Coordinator.pdf # 1.91 MB
│   ├── AnushkaTadiyal_aiia-ctms/PRESENTATION_INVENTORY.md # PPT 0, PDF 0, demo 0
│   ├── aravindakrishna-c_AIIA-Clinical-Trial-Dashboard/PRESENTATION_INVENTORY.md # 0,0,0
│   ├── rimi007-grt_AIIA-CTMS/PRESENTATION_INVENTORY.md # 0,0,0
│   ├── DuvvuruDeepakReddy18_AyuTrial/PRESENTATION_INVENTORY.md + ARCHITECTURE.md (5.0 KB) # demo 1 (generic)
│   └── kalyan-2006-prog_SIH26046-DEV-RUSH-/PRESENTATION_INVENTORY.md # 0,0,0
│
├── evidence/                              # reserved (additional exports if needed)
│
├── scripts/
│   ├── extract_repos.ps1 / .py            # original SIH_46 extractors (tree + stats + README inventory)
│   ├── generate_inventory.py              # generated REPO_DETAILS/FILE_STRUCTURE/README_ANALYSIS for 7 repos (new location)
│   ├── generate_architecture.py           # generated ARCHITECTURE.md for 7 repos
│   ├── generate_repo_analysis.py         # generated REPO_ANALYSIS.md 23 sections per repo (claim vs actual, evidence)
│   └── do_presentations.py               # searched PPT/PDF/DEMO_SCRIPT/JUDGE_QA → presentations/
│
├── MASTER_PROMPT.md                       # Reusable prompt for future AI (where repos are, what they contain, what is/isn’t implemented, how to work safely)
│
└── (additional docs in E:\SIH_46 for history)
    ├── E:\SIH_46\docs\REPOSITORY_UNDERSTANDING_REPORT.md
    ├── E:\SIH_46\docs\REPOSITORIES_OVERVIEW.md
    ├── E:\SIH_46\docs\COMPETITOR_MATRIX.md
    └── E:\SIH_46\MASTER_PROMPT.md (7-rule version)
```

## How We Verified (not shallow README)

- **Cloned separately:** 7 repos at `repositories/<owner>_<repo>/` with `git clone --depth 1`, preserved structure, excluded `.git`/`node_modules`/`__pycache__`/`dist`/`build`/`.next` in analysis.
- **Read every README:** `analysis/<repo>/README_ANALYSIS.md` has complete raw README + extracted purpose/features/arch/setup/tech/DB/APIs/AI/standards/compliance/deploy/demo/limitations, with `CLAIM vs FACT` notes.
- **Inspected actual code:** `analysis/<repo>/FILE_STRUCTURE.md` (tree) + `ARCHITECTURE.md` (frontend/backend/API/DB/auth/AI/pipelines) + `REPO_ANALYSIS.md` (DB tables, APIs with `Method: Endpoint: File:`, RBAC, audit `hash`/`SHA`, workflows, FHIR `ResearchStudy` search, CDISC `SDTM` search, ABDM `ABDM` search, etc.).
- **Claim vs Implementation:** For every major feature `analysis/<repo>/REPO_ANALYSIS.md:21` has table: Feature | README claim | Actual code evidence | Relevant files | Status (IMPLEMENTED etc.) | Explanation — statuses use only 6 allowed values.
- **Statuses rule:** Not IMPLEMENTED merely because button/page/dashboard card/sample data/README says so — traced via `schema.ts`, `routes.ts`, `init_db.py`, `mockData.ts`, `tests`.

## Key Results (neutral, no ranking)

**28-row matrix highlights (see `analysis/COMPETITOR_MATRIX.md:1`):**
- **Zero PPT** across 7 repos (verified `*.ppt/*.pptx` search) — `presentations/*/PRESENTATION_INVENTORY.md` confirms.
- **PDF only AyuSphere** (9 PDFs: Judge + 7 UAT + Tech Security) — others 0.
- **Demo script + Judge Q&A both only vedraya** (`DEMO_SCRIPT.md` 3KB + `JUDGE_QA.md` 3.5KB + `SIH26046_TRACEABILITY_FINAL.md` 8KB) — AyuSphere has Judge script + Tech guide partial.
- **AI only AyuSphere** (Claude extract + Groq Copilot, 157 tests) — others NOT PRESENT (AyuTrial WHO-UMC is rule-based, not AI).
- **Immutable audit hash chain:** only vedraya (GLOBAL SHA-256 + verify `valid:false` on tamper, 46/46 Vitest + 26/26 Playwright) + AyuSphere (insert-only + withAudit) IMPLEMENTED; AyuTrial MOCKED (localStorage).
- **NPvCC:** only AyuTrial IMPLEMENTED (dedicated apex, 24h SAE clock).
- **CTRI real scrape:** only AyuSphere IMPLEMENTED (`scripts/scrape/ctri_scrape.py` crawl4ai + `pnpm db:seed:real`); others tracking/claimed only.
- **FHIR↔CDISC mapping:** 0 actual mapping layer — only AyuSphere PARTIALLY (both exist separately) — key gap to exploit.
- **Common gaps to exploit:** batch traceability (0/7), individualization-aware protocol (0 logic), assessment-reliability QA (0), offline capability (1 MOCKED), ABDM real (0, 1 blueprint), WORM/eSign (0 certified, 2 CLAIMED ONLY).

**Technology landscape:** React 19 Vite (5), Next.js 16 (3), Express (3), FastAPI (1), Postgres/Drizzle/SQLAlchemy/SQLite, Auth.js/Argon2/PyJWT, Vitest/Playwright/pytest, Vercel/Render/Docker.

## File Counts

- **Repositories:** 7 cloned, 7 succeeded, 0 failed
- **Analysis files:** 35 (7×5) + COMPETITOR_MATRIX.md + MASTER_ANALYSIS.md = 37 (+ 7×PRESENTATION_INVENTORY.md)
- **Presentations copied:** vedraya 6 docs + AyuSphere 11 files (9 PDFs + 2 md) + AyuTrial 1 generic = 18 files copied + 7 inventories
- **Scripts:** 7 generators + 2 extractors

## How to Use

1. **Future AI:** Feed `MASTER_PROMPT.md` — it tells where repos are, what they contain, what files matter, what is/isn’t implemented, unknowns, how to distinguish claim vs verified, how to inspect code first.
2. **Deep dive per repo:** `analysis/<repo>/REPO_ANALYSIS.md` (23 sections, evidence per claim).
3. **Compare competitors:** `analysis/COMPETITOR_MATRIX.md` (28 rows, neutral).
4. **Synthesis:** `analysis/MASTER_ANALYSIS.md` (22 sections, common/rare/mocked/claimed, gaps, evidence index).
5. **Presentations:** `presentations/<repo>/PRESENTATION_INVENTORY.md` + copied `DEMO_SCRIPT.md`/`JUDGE_QA.md`/PDFs.

## Evidence Discipline Example

```text
Repository: nishant-uxs_vedraya
File: server/src/modules/audit/service.ts:1
Function: writeAudit(sequence, previousHash, eventHash)
Observation: append-only audit with GLOBAL SHA-256 chain, verify endpoint returns valid:false on tamper (tested api.audit.integrity.test.ts:1)
Status: IMPLEMENTED
```

vs

```text
CLAIM: README says 21 CFR Part 11
FACT: Repo has auth + audit
INFERENCE: May contribute to Part 11-style requirements
Do NOT conclude: “System is 21 CFR Part 11 compliant.”
```

## License

- `AnushkaTadiyal_aiia-ctms`: MIT (package.json)
- `rimi007-grt_AIIA-CTMS`: MIT
- `kalyan-2006-prog_SIH26046-DEV-RUSH-`: ISC
- `vansh459_AyuSphere`, `aravindakrishna-c_AIIA-Clinical-Trial-Dashboard`, `nishant-uxs_vedraya`, `DuvvuruDeepakReddy18_AyuTrial`: **No explicit open-source license identified** — do not copy without checking license.

## Security

Never exposed secrets — `.env.example` values redacted as `SECRET DETECTED — VALUE REDACTED` where found. No API keys/passwords/tokens committed. `analysis/<repo>/REPO_ANALYSIS.md:12` lists env vars without values.

## Final Principle Fulfilled

> **Source code > configuration > DB > tests > docs > README > claim** — Inspected first, verified second, classified third, compared fourth, documented fifth. No invented missing information; Unknown where insufficient evidence.

---

*This README is the package guide. For completion report, see below or run `cat README.md`.*
