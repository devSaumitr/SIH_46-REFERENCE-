# Architecture Presentation Comparison — Presented vs Actual Code

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

