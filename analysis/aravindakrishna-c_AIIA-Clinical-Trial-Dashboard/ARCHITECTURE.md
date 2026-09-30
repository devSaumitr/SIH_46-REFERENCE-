# ARCHITECTURE — aravindakrishna-c_AIIA-Clinical-Trial-Dashboard

**Source:** `repositories/aravindakrishna-c_AIIA-Clinical-Trial-Dashboard/`
**Generated:** 2026-09-30
**Evidence hierarchy:** code > config > schema > tests > docs > README

## High-Level Pattern


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


## Detailed Evidence

### Frontend

- **Entry points found:** frontend/src/main.tsx
- **Components/pages:** 34 files
- **State/Routing:** Unknown

### Backend

- **Entry points found:** backend/app/main.py
- **API routes discovered:** 1 groups
  - backend\app\api\router.py: include_router count 11
- **Framework:** package.json

### Database

- **Schema files:** backend\app\database\init_db.py: 60KB seed (SQLAlchemy)
- **Migrations:** Unknown / Not found
- **Seed:** Unknown

### Authentication / External Services / AI / Data Pipelines / Deployment

- **Auth:** backend/app/core/security.py: JWT HS256 + passlib
- **External services:** CTRI scrape (AyuSphere) / Supabase (AyuTrial) / Vercel Blob (AyuSphere) / Neon (AyuSphere) — only if code found
- **AI/ML:** Not present / Not found
- **Data pipelines:** AyuSphere: CTRI scrape -> seed-real; Vedraya: demo:seed deterministic; AyuTrial: mockData -> localStorage
- **Deployment:** Dockerfile, docker-compose.yml, vercel.json, render.yaml

### Tests & Verification

- **Test configs:** Unknown / Not found
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
