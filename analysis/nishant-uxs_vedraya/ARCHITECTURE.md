# ARCHITECTURE — nishant-uxs_vedraya

**Source:** `repositories/nishant-uxs_vedraya/`
**Generated:** 2026-09-30
**Evidence hierarchy:** code > config > schema > tests > docs > README

## High-Level Pattern


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


## Detailed Evidence

### Frontend

- **Entry points found:** src/main.tsx, src/App.tsx
- **Components/pages:** 45 files
- **State/Routing:** Unknown

### Backend

- **Entry points found:** server/src/index.ts, server/src/modules
- **API routes discovered:** 14 groups
  - server\src\modules\adverse-events\routes.ts: 0 routes
- server\src\modules\alerts\routes.ts: 0 routes
- server\src\modules\audit\routes.ts: 0 routes
- server\src\modules\auth\routes.ts: 0 routes
- server\src\modules\coding\routes.ts: 0 routes
- server\src\modules\consents\routes.ts: 0 routes
- server\src\modules\exports\routes.ts: 0 routes
- server\src\modules\investigators\routes.ts: 0 routes
- server\src\modules\milestones\routes.ts: 0 routes
- server\src\modules\participants\routes.ts: 0 routes
- server\src\modules\quality\routes.ts: 0 routes
- server\src\modules\regulatory\routes.ts: 0 routes
- **Framework:** package.json, package.json

### Database

- **Schema files:** server\src\db\schema.ts: tables users, roles, permissions, sessions, studies, sites (6 tables)
- **Migrations:** server\drizzle\0000_init.sql, server\drizzle\0001_consent_regulatory.sql, server\drizzle\0002_audit_hash_chain.sql, server\drizzle\0003_phase4_safety_coding.sql, server\drizzle\0004_phase6_quality_reporting.sql
- **Seed:** server\src\db\seed.ts

### Authentication / External Services / AI / Data Pipelines / Deployment

- **Auth:** server/src/middleware/auth.ts: authenticate + requirePermission, server/src/modules/auth/routes.ts: login/logout/me
- **External services:** CTRI scrape (AyuSphere) / Supabase (AyuTrial) / Vercel Blob (AyuSphere) / Neon (AyuSphere) — only if code found
- **AI/ML:** Not present / Not found
- **Data pipelines:** AyuSphere: CTRI scrape -> seed-real; Vedraya: demo:seed deterministic; AyuTrial: mockData -> localStorage
- **Deployment:** vercel.json, render.yaml

### Tests & Verification

- **Test configs:** playwright.config.ts, server/tests/ (Vitest)
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
