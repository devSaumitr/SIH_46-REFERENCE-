# FILE_STRUCTURE — kalyan-2006-prog_SIH26046-DEV-RUSH-

**Source:** `E:\SIH26046_COMPETITOR_ANALYSIS\repositories\kalyan-2006-prog_SIH26046-DEV-RUSH-`
**Generated:** 2026-09-30
**Tracked files (excl .git/node_modules/.next/dist/build):** 66
**Size:** 0.57 MB

## Tree (max depth 8, skipped .git/node_modules/.venv/dist/build)

```text
kalyan-2006-prog_SIH26046-DEV-RUSH-/
|-- devrush-ctms/
|   |-- app/
|   |   |-- adverse-events/
|   |   |   |-- list/
|   |   |   |   `-- page.tsx (7.4 KB)
|   |   |   `-- page.tsx (8.7 KB)
|   |   |-- api/
|   |   |   |-- adam/
|   |   |   |   `-- export/
|   |   |   |       `-- route.ts (6.0 KB)
|   |   |   |-- audit-log/
|   |   |   |   `-- route.ts (3.1 KB)
|   |   |   |-- define/
|   |   |   |   `-- export/
|   |   |   |       `-- route.ts (9.9 KB)
|   |   |   |-- fhir/
|   |   |   |   |-- export/
|   |   |   |   |   `-- route.ts (8.0 KB)
|   |   |   |   `-- ingest/
|   |   |   |       `-- route.ts (12.5 KB)
|   |   |   `-- sdtm/
|   |   |       `-- export/
|   |   |           `-- route.ts (6.3 KB)
|   |   |-- audit-logs/
|   |   |   `-- page.tsx (3.8 KB)
|   |   |-- ctri-ethics/
|   |   |   `-- page.tsx (8.1 KB)
|   |   |-- dashboard/
|   |   |   |-- [trialId]/
|   |   |   |   `-- page.tsx (9.6 KB)
|   |   |   |-- DataExchangePanel.tsx (8.8 KB)
|   |   |   |-- page.tsx (10.6 KB)
|   |   |   `-- SaeClockPanel.tsx (7.1 KB)
|   |   |-- login/
|   |   |   `-- page.tsx (2.5 KB)
|   |   |-- participants/
|   |   |   |-- [id]/
|   |   |   |   `-- page.tsx (5.1 KB)
|   |   |   `-- page.tsx (3.1 KB)
|   |   |-- signup/
|   |   |   `-- page.tsx (2.4 KB)
|   |   |-- favicon.ico (25.3 KB)
|   |   |-- globals.css (514 B)
|   |   |-- layout.tsx (719 B)
|   |   `-- page.tsx (105 B)
|   |-- lib/
|   |   |-- alertRules.ts (4.1 KB)
|   |   |-- apiAuth.ts (2.4 KB)
|   |   |-- authHeaders.ts (419 B)
|   |   |-- firebase-admin.ts (678 B)
|   |   |-- firebase.ts (1.1 KB)
|   |   |-- postAudit.ts (1.0 KB)
|   |   |-- saeClock.ts (1.2 KB)
|   |   `-- schema.ts (13.7 KB)
|   |-- public/
|   |   |-- file.svg (391 B)
|   |   |-- globe.svg (1.0 KB)
|   |   |-- next.svg (1.3 KB)
|   |   |-- vercel.svg (128 B)
|   |   `-- window.svg (385 B)
|   |-- scripts/
|   |   |-- activate-demo-consent.ts (1.0 KB)
|   |   |-- check-audit-chain.ts (6.0 KB)
|   |   |-- clean-fhir-ingest.ts (850 B)
|   |   |-- delete-duplicate-trials.ts (2.2 KB)
|   |   |-- fix-consent.ts (1.0 KB)
|   |   |-- fix-demo-adverse-events.ts (1.5 KB)
|   |   |-- inspect-trials.ts (1.4 KB)
|   |   |-- make-sample-fhir-bundle.ts (3.9 KB)
|   |   |-- meddra-terms.ts (4.2 KB)
|   |   |-- seed-demo-sae.ts (2.3 KB)
|   |   |-- seed-meddra-terms.ts (836 B)
|   |   |-- seed-participants.ts (1.5 KB)
|   |   |-- seed-sites.ts (1019 B)
|   |   |-- seed-whodrug-terms.ts (1.9 KB)
|   |   |-- seed.ts (1.2 KB)
|   |   `-- set-demo-role.ts (1.1 KB)
|   |-- .gitignore (570 B)
|   |-- AGENTS.md (687 B)
|   |-- CLAUDE.md (12 B)
|   |-- eslint.config.mjs (483 B)
|   |-- next.config.ts (140 B)
|   |-- package-lock.json (358.9 KB)
|   |-- package.json (673 B)
|   |-- postcss.config.mjs (101 B)
|   |-- README.md (1.5 KB)
|   |-- seed_output.txt (0 B)
|   `-- tsconfig.json (700 B)
|-- .DS_Store (6.0 KB)
|-- .gitignore (12 B)
|-- index.js (27 B)
`-- package.json (564 B)

```

## Important Files (explanations, top 25)

> Focus on files affecting behavior. Skipped .git, node_modules, build artifacts.


### File: `devrush-ctms\README.md`

```text
File: devrush-ctms\README.md
Purpose: Project documentation (CLAIM vs FACT check needed)
Important functions/classes: Not extracted
Dependencies: Unknown
Inputs: Not determined from static scan (see code)
Outputs: Not determined
```


### File: `devrush-ctms\lib\schema.ts`

```text
File: devrush-ctms\lib\schema.ts
Purpose: Database schema (Drizzle / tables)
Important functions/classes: Not extracted
Dependencies: firebase/firestore
Inputs: Not determined from static scan (see code)
Outputs: Not determined
```


### File: `devrush-ctms\package.json`

```text
File: devrush-ctms\package.json
Purpose: Node dependencies & scripts
Important functions/classes: Not extracted
Dependencies: Unknown
Inputs: Not determined from static scan (see code)
Outputs: Not determined
```


### File: `package.json`

```text
File: package.json
Purpose: Node dependencies & scripts
Important functions/classes: Not extracted
Dependencies: Unknown
Inputs: Not determined from static scan (see code)
Outputs: Not determined
```



## Note

- Do not trust README folder list if it includes .git/node_modules — those are excluded here for analysis efficiency.
- For full file list, see `repositories/kalyan-2006-prog_SIH26046-DEV-RUSH-/` directly or run `tree /F` in PowerShell.
