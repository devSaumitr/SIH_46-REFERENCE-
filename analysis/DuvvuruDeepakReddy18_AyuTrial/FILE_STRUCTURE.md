# FILE_STRUCTURE — DuvvuruDeepakReddy18_AyuTrial

**Source:** `E:\SIH26046_COMPETITOR_ANALYSIS\repositories\DuvvuruDeepakReddy18_AyuTrial`
**Generated:** 2026-09-30
**Tracked files (excl .git/node_modules/.next/dist/build):** 57
**Size:** 0.78 MB

## Tree (max depth 8, skipped .git/node_modules/.venv/dist/build)

```text
DuvvuruDeepakReddy18_AyuTrial/
|-- public/
|   |-- file.svg (391 B)
|   |-- globe.svg (1.0 KB)
|   |-- next.svg (1.3 KB)
|   |-- vercel.svg (128 B)
|   `-- window.svg (385 B)
|-- src/
|   |-- app/
|   |   |-- access-denied/
|   |   |   `-- page.tsx (3.1 KB)
|   |   |-- audit-logs/
|   |   |   `-- page.tsx (10.9 KB)
|   |   |-- consent/
|   |   |   `-- page.tsx (7.4 KB)
|   |   |-- dashboard/
|   |   |   `-- page.tsx (25.3 KB)
|   |   |-- data-management/
|   |   |   `-- page.tsx (7.8 KB)
|   |   |-- deviations/
|   |   |   `-- page.tsx (15.3 KB)
|   |   |-- enrolment/
|   |   |   `-- page.tsx (8.6 KB)
|   |   |-- ethics/
|   |   |   `-- page.tsx (13.3 KB)
|   |   |-- interoperability/
|   |   |   `-- page.tsx (18.6 KB)
|   |   |-- login/
|   |   |   `-- page.tsx (8.5 KB)
|   |   |-- monitoring/
|   |   |   `-- page.tsx (16.5 KB)
|   |   |-- participants/
|   |   |   |-- [id]/
|   |   |   |   `-- page.tsx (9.1 KB)
|   |   |   `-- page.tsx (10.2 KB)
|   |   |-- pharmacovigilance/
|   |   |   |-- [id]/
|   |   |   |   `-- page.tsx (13.9 KB)
|   |   |   |-- new/
|   |   |   |   `-- page.tsx (22.6 KB)
|   |   |   `-- page.tsx (14.1 KB)
|   |   |-- regulatory/
|   |   |   `-- page.tsx (7.2 KB)
|   |   |-- reports/
|   |   |   `-- page.tsx (14.1 KB)
|   |   |-- screening/
|   |   |   `-- page.tsx (15.4 KB)
|   |   |-- settings/
|   |   |   `-- page.tsx (9.2 KB)
|   |   |-- sites/
|   |   |   `-- page.tsx (6.6 KB)
|   |   |-- studies/
|   |   |   |-- [id]/
|   |   |   |   |-- edit/
|   |   |   |   |   `-- page.tsx (7.6 KB)
|   |   |   |   `-- page.tsx (27.0 KB)
|   |   |   |-- new/
|   |   |   |   `-- page.tsx (19.3 KB)
|   |   |   `-- page.tsx (10.6 KB)
|   |   |-- users/
|   |   |   `-- page.tsx (6.5 KB)
|   |   |-- visits/
|   |   |   `-- page.tsx (9.1 KB)
|   |   |-- favicon.ico (25.3 KB)
|   |   |-- globals.css (1.3 KB)
|   |   |-- layout.tsx (989 B)
|   |   `-- page.tsx (20.6 KB)
|   |-- components/
|   |   `-- layout/
|   |       `-- AppShell.tsx (20.0 KB)
|   |-- context/
|   |   `-- AuthContext.tsx (1.8 KB)
|   |-- lib/
|   |   |-- auth.ts (5.8 KB)
|   |   |-- crypto.ts (1.6 KB)
|   |   |-- mockData.ts (58.7 KB)
|   |   `-- store.ts (16.3 KB)
|   |-- tests/
|   |   `-- workflows.test.ts (10.6 KB)
|   `-- types/
|       `-- index.ts (11.3 KB)
|-- supabase/
|   `-- migrations/
|       `-- 20260928000000_init_ctms.sql (9.1 KB)
|-- .env.example (820 B)
|-- .gitignore (547 B)
|-- AGENTS.md (687 B)
|-- ARCHITECTURE.md (5.0 KB)
|-- CLAUDE.md (12 B)
|-- eslint.config.mjs (483 B)
|-- next.config.ts (140 B)
|-- package-lock.json (257.7 KB)
|-- package.json (740 B)
|-- postcss.config.mjs (101 B)
|-- README.md (9.4 KB)
`-- tsconfig.json (704 B)

```

## Important Files (explanations, top 25)

> Focus on files affecting behavior. Skipped .git, node_modules, build artifacts.


### File: `README.md`

```text
File: README.md
Purpose: Project documentation (CLAIM vs FACT check needed)
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


### File: `src\tests\workflows.test.ts`

```text
File: src\tests\workflows.test.ts
Purpose: Test suite (tests)
Important functions/classes: export function runAllWorkflowTests, function assert
Dependencies: ../lib/auth, ../lib/mockData, ../lib/crypto, ../lib/store
Inputs: Not determined from static scan (see code)
Outputs: Not determined
```



## Note

- Do not trust README folder list if it includes .git/node_modules — those are excluded here for analysis efficiency.
- For full file list, see `repositories/DuvvuruDeepakReddy18_AyuTrial/` directly or run `tree /F` in PowerShell.
