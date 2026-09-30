# ARCHITECTURE — rimi007-grt_AIIA-CTMS

**Source:** `repositories/rimi007-grt_AIIA-CTMS/`
**Generated:** 2026-09-30
**Evidence hierarchy:** code > config > schema > tests > docs > README

## High-Level Pattern


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
        -> tests: test_rbac_matrix.js
        -> deploy: Dockerfile + apprunner.yaml + render.yaml (rimi)
```

Evidence:
- `repositories/rimi007-grt_AIIA-CTMS/server/seed.js:1` — 57KB, seeds 24 trials 30 AEs, users, sites
- `repositories/rimi007-grt_AIIA-CTMS/client/src/pages/TrialDetailPage.jsx:1` — 37KB
- `repositories/rimi007-grt_AIIA-CTMS/server/package.json:1` — dependencies: {
  "name": "server",
  "version": "1.0.0",
  "description": "",
  "main": "index.js",
  "scripts": {
    "test": "echo \"Error: no test specified\" && exit 1"
  },
  "keywords": [],
  "author": "",
  "license": "ISC",
  "type": "commonjs",
  "dependencies": {
    "bcryptjs": "^3.0.3",
    "cors": "


## Detailed Evidence

### Frontend

- **Entry points found:** client/src/main.jsx
- **Components/pages:** 23 files
- **State/Routing:** Unknown

### Backend

- **Entry points found:** server/index.js
- **API routes discovered:** 0 groups
  - Unknown / Not found
- **Framework:** package.json, package.json

### Database

- **Schema files:** Unknown / Not found
- **Migrations:** Unknown / Not found
- **Seed:** server\seed.js

### Authentication / External Services / AI / Data Pipelines / Deployment

- **Auth:** Unknown / Not found
- **External services:** CTRI scrape (AyuSphere) / Supabase (AyuTrial) / Vercel Blob (AyuSphere) / Neon (AyuSphere) — only if code found
- **AI/ML:** Not present / Not found
- **Data pipelines:** AyuSphere: CTRI scrape -> seed-real; Vedraya: demo:seed deterministic; AyuTrial: mockData -> localStorage
- **Deployment:** Dockerfile, render.yaml, apprunner.yaml

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
