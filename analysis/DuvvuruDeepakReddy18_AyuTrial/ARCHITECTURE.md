# ARCHITECTURE — DuvvuruDeepakReddy18_AyuTrial

**Source:** `repositories/DuvvuruDeepakReddy18_AyuTrial/`
**Generated:** 2026-09-30
**Evidence hierarchy:** code > config > schema > tests > docs > README

## High-Level Pattern


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


## Detailed Evidence

### Frontend

- **Entry points found:** src/app/page.tsx
- **Components/pages:** 31 files
- **State/Routing:** import type { Metadata } from 'next';
import './globals.css';
import { AuthProvider } from '@/context/AuthContext';

export const metadata: Metadata = {
  title: 'AIIA Clinical Trial Management System

### Backend

- **Entry points found:** Unknown / Not found
- **API routes discovered:** 0 groups
  - Unknown / Not found
- **Framework:** package.json

### Database

- **Schema files:** Unknown / Not found
- **Migrations:** supabase\migrations\20260928000000_init_ctms.sql
- **Seed:** Unknown

### Authentication / External Services / AI / Data Pipelines / Deployment

- **Auth:** mockData.ts: persona switcher (no real auth in demo)
- **External services:** CTRI scrape (AyuSphere) / Supabase (AyuTrial) / Vercel Blob (AyuSphere) / Neon (AyuSphere) — only if code found
- **AI/ML:** Not present / Not found
- **Data pipelines:** AyuSphere: CTRI scrape -> seed-real; Vedraya: demo:seed deterministic; AyuTrial: mockData -> localStorage
- **Deployment:** supabase

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
