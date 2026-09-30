# ARCHITECTURE — kalyan-2006-prog_SIH26046-DEV-RUSH-

**Source:** `repositories/kalyan-2006-prog_SIH26046-DEV-RUSH-/`
**Generated:** 2026-09-30
**Evidence hierarchy:** code > config > schema > tests > docs > README

## High-Level Pattern


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


## Detailed Evidence

### Frontend

- **Entry points found:** Unknown / Not found
- **Components/pages:** Not scanned files
- **State/Routing:** Unknown

### Backend

- **Entry points found:** devrush-ctms/app/api
- **API routes discovered:** 6 groups
  - devrush-ctms\app\api\audit-log\route.ts
- devrush-ctms\app\api\sdtm\export\route.ts
- devrush-ctms\app\api\fhir\export\route.ts
- devrush-ctms\app\api\fhir\ingest\route.ts
- devrush-ctms\app\api\define\export\route.ts
- devrush-ctms\app\api\adam\export\route.ts
- **Framework:** package.json, package.json

### Database

- **Schema files:** devrush-ctms\lib\schema.ts: tables not parsed (0 tables)
- **Migrations:** Unknown / Not found
- **Seed:** devrush-ctms\seed_output.txt, devrush-ctms\scripts\seed-demo-sae.ts, devrush-ctms\scripts\seed-meddra-terms.ts

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
