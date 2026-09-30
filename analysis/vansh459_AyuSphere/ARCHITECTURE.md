# ARCHITECTURE — vansh459_AyuSphere

**Source:** `repositories/vansh459_AyuSphere/`
**Generated:** 2026-09-30
**Evidence hierarchy:** code > config > schema > tests > docs > README

## High-Level Pattern


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


## Detailed Evidence

### Frontend

- **Entry points found:** src/app/page.tsx
- **Components/pages:** 54 files
- **State/Routing:** import type { Metadata } from "next";
import { Plus_Jakarta_Sans } from "next/font/google";
import "./globals.css";

const jakarta = Plus_Jakarta_Sans({
  variable: "--font-jakarta",
  subsets: ["lati

### Backend

- **Entry points found:** src/app/api
- **API routes discovered:** 15 groups
  - src\app\api\badges\route.ts
- src\app\api\export\route.ts
- src\app\api\guide\route.ts
- src\app\api\messages\route.ts
- src\app\api\search\route.ts
- src\app\api\messages\latest-unread\route.ts
- src\app\api\fhir\import\route.ts
- src\app\api\fhir\ResearchStudy\[id]\route.ts
- src\app\api\fhir\Bundle\[trialId]\route.ts
- src\app\api\cron\alerts\route.ts
- src\app\api\auth\[...nextauth]\route.ts
- src\app\api\alerts\latest-unread\route.ts
- **Framework:** package.json

### Database

- **Schema files:** src\db\schema.ts: tables users, trials, sites (3 tables)
- **Migrations:** drizzle\0000_brown_lenny_balinger.sql, drizzle\0001_lowly_piledriver.sql, drizzle\0002_careful_captain_america.sql, drizzle\0003_boring_songbird.sql, drizzle\0004_happy_paibok.sql
- **Seed:** tests\seed-real.test.ts, tests\seed.test.ts, src\db\seed-real.ts

### Authentication / External Services / AI / Data Pipelines / Deployment

- **Auth:** Auth.js / NextAuth (JWT)
- **External services:** CTRI scrape (AyuSphere) / Supabase (AyuTrial) / Vercel Blob (AyuSphere) / Neon (AyuSphere) — only if code found
- **AI/ML:** src/app/api/ai/* (extract, copilot, approve), Anthropic SDK found
- **Data pipelines:** AyuSphere: CTRI scrape -> seed-real; Vedraya: demo:seed deterministic; AyuTrial: mockData -> localStorage
- **Deployment:** vercel.json

### Tests & Verification

- **Test configs:** vitest.config.ts, tests/
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
