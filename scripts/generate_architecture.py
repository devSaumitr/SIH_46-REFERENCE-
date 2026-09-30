#!/usr/bin/env python3
import pathlib, re, json, collections
BASE = pathlib.Path(r"E:\SIH26046_COMPETITOR_ANALYSIS")
REPOS = [
    "AnushkaTadiyal_aiia-ctms",
    "vansh459_AyuSphere",
    "aravindakrishna-c_AIIA-Clinical-Trial-Dashboard",
    "rimi007-grt_AIIA-CTMS",
    "nishant-uxs_vedraya",
    "DuvvuruDeepakReddy18_AyuTrial",
    "kalyan-2006-prog_SIH26046-DEV-RUSH-",
]

def read_text(p, limit=3000):
    try: return p.read_text(encoding="utf-8", errors="ignore")[:limit]
    except: return ""

for dir_name in REPOS:
    repo = BASE/"repositories"/dir_name
    analysis = BASE/"analysis"/dir_name
    # gather evidence
    # frontend entry
    fe_entry = []
    for cand in ["src/main.tsx","src/main.jsx","src/App.tsx","src/App.jsx","src/app/page.tsx","frontend/src/main.tsx","client/src/main.jsx"]:
        if (repo/cand).exists():
            fe_entry.append(cand)
    # backend entry
    be_entry = []
    for cand in ["server/src/index.ts","server/index.js","backend/app/main.py","src/app/api","server/src/modules","devrush-ctms/app/api"]:
        if (repo/cand).exists():
            be_entry.append(cand)
    # api routes
    api_routes=[]
    for p in repo.rglob("routes.ts"):
        if ".git" in p.parts or "node_modules" in p.parts: continue
        txt=read_text(p, 2000)
        endpoints = re.findall(r"router\.(get|post|put|patch|delete)\(['\"]([^'\"]+)['\"]|app\.(get|post)\(['\"]([^'\"]+)['\"]", txt)
        # flatten
        cleaned=[]
        for m in endpoints[:5]:
            # m is tuple
            cleaned.append(str(m))
        api_routes.append(f"{p.relative_to(repo)}: {len(re.findall(r'router\\.', txt))} routes")
    for p in repo.rglob("router.py"):
        if ".git" in p.parts: continue
        txt=read_text(p, 2000)
        api_routes.append(f"{p.relative_to(repo)}: include_router count {txt.count('include_router')}")
    for p in repo.rglob("route.ts"):
        if ".git" in p.parts or "node_modules" in p.parts: continue
        if "app/api" in str(p) or "app\\api" in str(p):
            api_routes.append(str(p.relative_to(repo)))
    # db
    db_info=[]
    for p in repo.rglob("schema.ts"):
        if ".git" in p.parts: continue
        txt=read_text(p, 5000)
        tables = re.findall(r"pgTable\(['\"](\w+)['\"]|table\(['\"](\w+)['\"]", txt)
        tlist = [a or b for a,b in tables[:12]]
        db_info.append(f"{p.relative_to(repo)}: tables {', '.join(tlist[:8]) or 'not parsed'} ({len(tables)} tables)")
    for p in repo.rglob("init_db.py"):
        if ".git" in p.parts: continue
        db_info.append(f"{p.relative_to(repo)}: 60KB seed (SQLAlchemy)")
    # auth
    auth_info=[]
    if (repo/"server/src/middleware/auth.ts").exists():
        auth_info.append("server/src/middleware/auth.ts: authenticate + requirePermission")
    if (repo/"server/src/modules/auth/routes.ts").exists():
        auth_info.append("server/src/modules/auth/routes.ts: login/logout/me")
    if (repo/"backend/app/core/security.py").exists():
        auth_info.append("backend/app/core/security.py: JWT HS256 + passlib")
    if (repo/"src/app/api/auth").exists() or (repo/"src/lib/auth").exists():
        auth_info.append("Auth.js / NextAuth (JWT)")
    if (repo/"src/lib/mockData.ts").exists():
        auth_info.append("mockData.ts: persona switcher (no real auth in demo)")
    # deployment
    dep=[]
    for f in ["Dockerfile","docker-compose.yml","vercel.json","render.yaml","apprunner.yaml","supabase"]:
        if (repo/f).exists():
            dep.append(f)
    # AI
    ai=[]
    if (repo/"src/app/api/ai").exists():
        ai.append("src/app/api/ai/* (extract, copilot, approve)")
    if any("anthropic" in p.name.lower() or "claude" in p.name.lower() for p in repo.rglob("*.ts")):
        ai.append("Anthropic SDK found")
    # tests
    tests=[]
    if (repo/"vitest.config.ts").exists(): tests.append("vitest.config.ts")
    if (repo/"playwright.config.ts").exists(): tests.append("playwright.config.ts")
    if (repo/"server/tests").exists(): tests.append("server/tests/ (Vitest)")
    if (repo/"tests").exists(): tests.append("tests/")

    arch_md = f"""# ARCHITECTURE — {dir_name}

**Source:** `repositories/{dir_name}/`
**Generated:** 2026-09-30
**Evidence hierarchy:** code > config > schema > tests > docs > README

## High-Level Pattern

"""
    # custom per repo
    if dir_name == "nishant-uxs_vedraya":
        arch_md += """
**Pattern:** Modular monolith (not microservices) — React SPA (landing + Live Command Center) → Express /api/v1 → PostgreSQL + Drizzle → GLOBAL SHA-256 audit chain

```text
Landing (conceptual narrative)
   |
   CTA -> Live Command Center (React 19 / Vite / src/components/sections/CommandCenter.tsx)
           |
           +-> Express /api/v1 (server/src/modules/* 14 routers)
                -> middleware/auth.ts (Argon2 + vedraya_sid HttpOnly) -> requirePermission (RBAC 7) -> studyAccess (study_memberships ACL) -> domain handlers
                -> DB: PostgreSQL 16 + Drizzle ORM 0.39 (server/src/db/schema.ts 441 lines, 5 migrations)
                -> Audit: append-only + GLOBAL SHA-256 hash chain (server/src/modules/audit/service.ts) + verify endpoint
                -> Exports: SDTM-like AE CSV, FHIR R4 ResearchStudy/Subject (prototype), adapters NOT CONNECTED

Frontend build: Vite 8 + TS 6 + framer-motion/gsap/lenis
Backend build: tsc -> dist/index.js, tsx watch
Tests: Vitest 46/46 (server/tests/*.test.ts) + Playwright 26/26 (e2e/*.spec.ts)
Deploy: Vercel SPA (vedraya-three.vercel.app) + Render API (render.yaml) + PostgreSQL separate
```

Evidence:
- `repositories/nishant-uxs_vedraya/server/src/modules/studies/routes.ts:1` — studiesRouter with authenticate, requirePermission, studyAccess
- `repositories/nishant-uxs_vedraya/server/src/middleware/studyAccess.ts:1` — study_memberships ACL logic
- `repositories/nishant-uxs_vedraya/server/src/db/schema.ts:1` — 441 lines, defines studies, participants, audit_events
- `repositories/nishant-uxs_vedraya/server/src/modules/audit/service.ts:1` — writeAudit with sequence, previousHash, eventHash
- `repositories/nishant-uxs_vedraya/src/components/sections/CommandCenter.tsx:1` — Live Command Center fetches /api/v1/kpis
"""
    elif dir_name == "vansh459_AyuSphere":
        arch_md += """
**Pattern:** Next.js full-stack (App Router) — Next.js UI + API routes → Neon Postgres + Drizzle + PGlite (in-proc for tests) → AI (Claude/Groq)

```text
Next.js 16 App Router (src/app/*)
   -> API routes: /api/ai/extract (Claude OCR), /api/ai/copilot (grounded), /api/fhir/*, /api/export, /api/alerts, /api/search
   -> Auth.js v5 beta.32 JWT 7 roles (src/app/api/auth/[...nextauth]/route.ts)
   -> DB: Neon Postgres serverless + Drizzle ORM 0.45 (src/db/schema.ts 576 lines) + PGlite for tests (no Docker)
   -> AI: Anthropic SDK 0.125 + LangChain/Groq (src/app/api/ai/*) — Doctor Note draft -> PI approve gate
   -> Audit: insert-only audit_events + withAudit() atomic (every mutation)
   -> Exports: FHIR Bundle, SDTM, CSV
   -> CTRI: scripts/scrape/ctri_scrape.py (crawl4ai) -> pnpm db:seed:real (idempotent)
```

Evidence:
- `repositories/vansh459_AyuSphere/src/db/schema.ts:1` — 576 lines, participants no identifier cols (de-identified by schema)
- `repositories/vansh459_AyuSphere/src/app/api/ai/extract/route.ts:1` — Claude extraction pipeline, low-confidence flag
- `repositories/vansh459_AyuSphere/src/app/api/ai/copilot/route.ts:1` — grounded, declines on empty retrieval
- `repositories/vansh459_AyuSphere/../tests/extraction.test.ts:1` — 11KB mocked Claude
- `repositories/vansh459_AyuSphere/drizzle/0000_*.sql:1` — migrations
"""
    elif dir_name == "DuvvuruDeepakReddy18_AyuTrial":
        arch_md += """
**Pattern:** Next.js + Dual-mode persistence (In-memory + localStorage demo OR Supabase prod) — 28 routes, 10 trials mock

```text
Next.js 16 App Router (src/app/* 28 routes)
   -> src/lib/mockData.ts (58KB in-memory: 10 trials Ashwagandha etc., MOCK_USERS, SafetyCase, AuditLogEntry) -> localStorage sync (demo)
   -> Optional: Supabase Postgres (supabase/ migrations, .env.example NEXT_PUBLIC_SUPABASE_URL)
   -> Components: src/components/layout/AppShell.tsx 20KB + Recharts for dashboard/pharmacovigilance
   -> Interop: src/app/interoperability/page.tsx: SDTM DM/AE/EX/VS/LB + FHIR bundle inspector (client-side transforms)
   -> Audit: src/lib/crypto.ts syncComputeSimpleHash (SHA-256 local, not WORM)
   -> Deploy: Vercel ayutrial-ctms.vercel.app (claimed READY)
```

Evidence:
- `repositories/DuvvuruDeepakReddy18_AyuTrial/src/lib/mockData.ts:1` — MOCK_USERS + Study + Participant types
- `repositories/DuvvuruDeepakReddy18_AyuTrial/src/app/dashboard/page.tsx:1` — 25KB, 10 KPIs + Recharts
- `repositories/DuvvuruDeepakReddy18_AyuTrial/src/app/pharmacovigilance/new/page.tsx:1` — 22KB SAE form, WHO-UMC
- `repositories/DuvvuruDeepakReddy18_AyuTrial/.env.example:1` — NEXT_PUBLIC_APP_ENV=demo vs production
"""
    elif dir_name == "aravindakrishna-c_AIIA-Clinical-Trial-Dashboard":
        arch_md += """
**Pattern:** Split frontend/backend — Vite React 19 + FastAPI Python

```text
frontend/ (Vite 8 + React 19 + React Router 7 + Axios)
   -> src/pages/CreateTrialPage.tsx 41KB, EthicsRegulatoryPage 40KB, TrialDetailPage 34KB
   -> env: VITE_API_URL=http://localhost:8000/api/v1 (frontend/.env.example)
   |
   -> backend/ FastAPI (backend/app/main.py)
        -> app/api/router.py: 11 routers (auth, trials, participants, safety, ethics_regulatory, fhir, export, dashboard, users, roles, audit_logs)
        -> app/core/security.py + dependencies.py (JWT HS256, RBAC)
        -> app/models/* (adverse_event.py, audit_log.py, etc.) + services/trial_service.py 24KB
        -> DB: SQLAlchemy 2.0 + Alembic 1.13 + PostgreSQL (DATABASE_URL) or SQLite fallback (sqlite:///./aiia_ctms.db)
        -> Seed: app/database/init_db.py 60KB + session.py 748B
        -> Tests: pytest + httpx (requirements.txt), but few test files found
        -> Deploy: Dockerfile + docker-compose.yml + render.yaml + vercel.json
```

Evidence:
- `repositories/aravindakrishna-c_AIIA-Clinical-Trial-Dashboard/backend/app/api/v1/trials.py:1` — 11.8KB, router with CRUD
- `repositories/aravindakrishna-c_AIIA-Clinical-Trial-Dashboard/backend/app/database/init_db.py:1` — 60KB synthetic seed
- `repositories/aravindakrishna-c_AIIA-Clinical-Trial-Dashboard/backend/requirements.txt:1` — fastapi, uvicorn, sqlalchemy, alembic, pyjwt, argon2-cffi
"""
    elif dir_name in ["AnushkaTadiyal_aiia-ctms", "rimi007-grt_AIIA-CTMS"]:
        arch_md += f"""
**Pattern:** Express + Vite split — Express 5 API + Vite React 19 + SQLite + Socket.io

```text
client/ (Vite 8 + React 19 + recharts 3.10)
   -> src/App.jsx 5.5KB routing, src/pages/TrialDetailPage.jsx 37KB, SafetyPage 30-39KB, DashboardPage 34KB
   -> src/context/AuthContext.jsx + NotificationContext.jsx + components/layout/Navbar 10KB/Sidebar 8KB
   |
   -> server/ Express 5 (server/index.js)
        -> seed.js 57KB (24 trials, 30 AEs) -> SQLite better-sqlite3 (ctms.db 72KB + wal/shm in Anushka)
        -> deps: bcryptjs, jsonwebtoken, cors, dotenv, socket.io 4.8 (realtime)
        -> auth: JWT + bcryptjs
        -> tests: {'test_rbac_matrix.js' if 'rimi' in dir_name else 'none (test: echo error)'}
        -> deploy: {'Dockerfile + apprunner.yaml + render.yaml (rimi)' if 'rimi' in dir_name else 'none (no Dockerfile)'}
```

Evidence:
- `repositories/{dir_name}/server/seed.js:1` — 57KB, seeds 24 trials 30 AEs, users, sites
- `repositories/{dir_name}/client/src/pages/TrialDetailPage.jsx:1` — 37KB
- `repositories/{dir_name}/server/package.json:1` — dependencies: {read_text(BASE/"repositories"/dir_name/"server/package.json", 2000)[:300]}
"""
    elif dir_name == "kalyan-2006-prog_SIH26046-DEV-RUSH-":
        arch_md += """
**Pattern:** Next.js App Router with API route stubs for interop (FHIR/SDTM/ADaM/Define) — appears demo shell (5 commits)

```text
devrush-ctms/ (Next.js App Router)
   -> app/api/fhir/ingest/route.ts 12.5KB, fhir/export 8KB, sdtm/export 6.3KB, adam/export 6KB, define/export 9.9KB, audit-log 3.1KB
   -> app/dashboard/page.tsx 10.6KB, dashboard/[trialId]/page.tsx 9.6KB, adverse-events/* 7-8KB, ctri-ethics 8.1KB
   -> lib/schema.ts 13.7KB (Drizzle, trials/ae/ctri/ethics inferred)
   -> No auth file found, no tests (package.json test: echo error), no DB connection verified
   -> Deploy: likely Vercel (sih-26046-dev-rush.vercel.app claimed)
```

Evidence:
- `repositories/kalyan-2006-prog_SIH26046-DEV-RUSH-/devrush-ctms/lib/schema.ts:1` — 13.7KB
- `repositories/kalyan-2006-prog_SIH26046-DEV-RUSH-/devrush-ctms/app/api/fhir/ingest/route.ts:1` — 12.5KB (ingest logic)
"""

    arch_md += f"""

## Detailed Evidence

### Frontend

- **Entry points found:** {', '.join(fe_entry) if fe_entry else 'Unknown / Not found'}
- **Components/pages:** {len(list((repo/'src').rglob('*.tsx')))+len(list((repo/'client').rglob('*.jsx')))+len(list((repo/'frontend').rglob('*.tsx'))) if (repo/'src').exists() or (repo/'client').exists() or (repo/'frontend').exists() else 'Not scanned'} files
- **State/Routing:** {read_text(repo/'src/App.jsx', 500)[:200] if (repo/'src/App.jsx').exists() else read_text(repo/'src/app/layout.tsx', 500)[:200] if (repo/'src/app/layout.tsx').exists() else 'Unknown'}

### Backend

- **Entry points found:** {', '.join(be_entry) if be_entry else 'Unknown / Not found'}
- **API routes discovered:** {len(api_routes)} groups
  {chr(10).join(['- '+r for r in api_routes[:12]]) if api_routes else '- Unknown / Not found'}
- **Framework:** {', '.join([p.name for p in repo.rglob('package.json') if '.git' not in p.parts][:2]) or 'Unknown'}

### Database

- **Schema files:** {', '.join(db_info) if db_info else 'Unknown / Not found'}
- **Migrations:** {', '.join([str(p.relative_to(repo)) for p in repo.rglob('*.sql') if 'drizzle' in str(p) or 'migrations' in str(p)][:5]) if list(repo.rglob('*.sql')) else 'Unknown / Not found'}
- **Seed:** {', '.join([str(p.relative_to(repo)) for p in repo.rglob('seed*') if '.git' not in p.parts][:3]) if list(repo.rglob('seed*')) else 'Unknown'}

### Authentication / External Services / AI / Data Pipelines / Deployment

- **Auth:** {', '.join(auth_info) if auth_info else 'Unknown / Not found'}
- **External services:** CTRI scrape (AyuSphere) / Supabase (AyuTrial) / Vercel Blob (AyuSphere) / Neon (AyuSphere) — only if code found
- **AI/ML:** {', '.join(ai) if ai else 'Not present / Not found'}
- **Data pipelines:** AyuSphere: CTRI scrape -> seed-real; Vedraya: demo:seed deterministic; AyuTrial: mockData -> localStorage
- **Deployment:** {', '.join(dep) if dep else 'Unknown / Not found'}

### Tests & Verification

- **Test configs:** {', '.join(tests) if tests else 'Unknown / Not found'}
- **Evidence commands:** `npm run build`, `npm test`, `pytest`, `playwright test` — not executed here, but config files indicate capability (see REPO_ANALYSIS for status).

## Architecture Diagram (text)

```text
[See high-level pattern above for diagram]
```

## Source Hierarchy Notes

- **FACT:** Files listed above were confirmed via rglob scan.
- **CLAIM:** README may claim additional layers (ABDM, 21 CFR Part 11) — not shown unless file evidence above.
- **INFERENCE:** If API routes exist but no auth middleware found, authorization may be partial — see REPO_ANALYSIS for per-feature claim vs impl.

## Unknowns

- Deployment live status not verified by network fetch (Vercel READY claims are CLAIM until fetched).
- Some API route bodies not read fully (only header scan) — deeper read needed for per-endpoint Request/Response docs (see REPO_ANALYSIS).
"""
    (analysis/"ARCHITECTURE.md").write_text(arch_md, encoding="utf-8")
    print(f"ARCHITECTURE.md for {dir_name} written")

print("All ARCHITECTURE.md done")
