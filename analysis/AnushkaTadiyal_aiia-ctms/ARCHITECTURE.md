# ARCHITECTURE — AnushkaTadiyal_aiia-ctms

**Source:** `repositories/AnushkaTadiyal_aiia-ctms/`
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
        -> tests: none (test: echo error)
        -> deploy: none (no Dockerfile)
```

Evidence:
- `repositories/AnushkaTadiyal_aiia-ctms/server/seed.js:1` — 57KB, seeds 24 trials 30 AEs, users, sites
- `repositories/AnushkaTadiyal_aiia-ctms/client/src/pages/TrialDetailPage.jsx:1` — 37KB
- `repositories/AnushkaTadiyal_aiia-ctms/server/package.json:1` — dependencies: {
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
    "better-s


## Detailed Evidence

### Frontend

- **Entry points found:** client/src/main.jsx
- **Components/pages:** 18 files
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
- **Deployment:** Unknown / Not found

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
