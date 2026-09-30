# FILE_STRUCTURE — vansh459_AyuSphere

**Source:** `E:\SIH26046_COMPETITOR_ANALYSIS\repositories\vansh459_AyuSphere`
**Generated:** 2026-09-30
**Tracked files (excl .git/node_modules/.next/dist/build):** 282
**Size:** 14.38 MB

## Tree (max depth 8, skipped .git/node_modules/.venv/dist/build)

```text
vansh459_AyuSphere/
|-- docs/
|   |-- uat/
|   |   |-- Judge_Demo_Script.md (4.1 KB)
|   |   |-- Judge_Demo_Script.pdf (1.31 MB)
|   |   |-- Tech_Security_Guide.md (17.0 KB)
|   |   |-- Tech_Security_Guide.pdf (155.6 KB)
|   |   |-- UAT_Guide_Administrator.pdf (3.32 MB)
|   |   |-- UAT_Guide_Ethics_Committee.pdf (466.0 KB)
|   |   |-- UAT_Guide_Monitor.pdf (667.3 KB)
|   |   |-- UAT_Guide_Pharmacovigilance.pdf (1.25 MB)
|   |   |-- UAT_Guide_Principal_Investigator.pdf (2.83 MB)
|   |   |-- UAT_Guide_Regulator.pdf (529.0 KB)
|   |   `-- UAT_Guide_Study_Coordinator.pdf (1.86 MB)
|   |-- architecture.md (17.4 KB)
|   |-- decisions.md (29.6 KB)
|   |-- development-plan.md (9.1 KB)
|   |-- gap-analysis.md (13.0 KB)
|   |-- gap-plan.md (16.4 KB)
|   |-- loading-skeletons.md (6.2 KB)
|   |-- performance-audit.md (5.1 KB)
|   |-- tasks.md (24.4 KB)
|   |-- technology.md (10.4 KB)
|   |-- ui-audit.md (5.8 KB)
|   `-- workflow.md (14.5 KB)
|-- drizzle/
|   |-- meta/
|   |   |-- 0000_snapshot.json (42.0 KB)
|   |   |-- 0001_snapshot.json (43.0 KB)
|   |   |-- 0002_snapshot.json (44.8 KB)
|   |   |-- 0003_snapshot.json (46.5 KB)
|   |   |-- 0004_snapshot.json (48.8 KB)
|   |   |-- 0005_snapshot.json (52.0 KB)
|   |   |-- 0006_snapshot.json (56.2 KB)
|   |   |-- 0007_snapshot.json (56.3 KB)
|   |   |-- 0008_snapshot.json (59.4 KB)
|   |   |-- 0009_snapshot.json (61.6 KB)
|   |   `-- _journal.json (1.5 KB)
|   |-- 0000_brown_lenny_balinger.sql (12.2 KB)
|   |-- 0001_lowly_piledriver.sql (180 B)
|   |-- 0002_careful_captain_america.sql (365 B)
|   |-- 0003_boring_songbird.sql (358 B)
|   |-- 0004_happy_paibok.sql (654 B)
|   |-- 0005_superb_the_executioner.sql (773 B)
|   |-- 0006_lowly_blink.sql (1.2 KB)
|   |-- 0007_curved_domino.sql (74 B)
|   |-- 0008_lively_james_howlett.sql (899 B)
|   `-- 0009_legal_toad_men.sql (495 B)
|-- public/
|   |-- apple-touch-icon.png (5.6 KB)
|   |-- favicon.ico (3.1 KB)
|   |-- file.svg (391 B)
|   |-- globe.svg (1.0 KB)
|   |-- icon-192.png (6.1 KB)
|   |-- icon-512.png (20.4 KB)
|   |-- icon.svg (499 B)
|   |-- next.svg (1.3 KB)
|   |-- vercel.svg (128 B)
|   `-- window.svg (385 B)
|-- scripts/
|   |-- scrape/
|   |   |-- ctri_repair.py (2.5 KB)
|   |   |-- ctri_scrape.py (13.3 KB)
|   |   `-- ctri_trials.json (16.7 KB)
|   |-- backfill-templates.ts (3.4 KB)
|   |-- build-tech-guide.ts (36.7 KB)
|   |-- build-uat-guides.ts (24.2 KB)
|   |-- check-trial.ts (1.1 KB)
|   |-- cleanup-demo-data.ts (2.9 KB)
|   |-- db-migrate.ts (2.3 KB)
|   |-- debug-trials-query.ts (570 B)
|   |-- e2e-live-guide.ts (5.9 KB)
|   |-- e2e-messages-unread.ts (6.1 KB)
|   |-- e2e-ui-sweep.ts (5.8 KB)
|   |-- get-admin-id.ts (800 B)
|   `-- set-guide-key.ts (1.3 KB)
|-- src/
|   |-- app/
|   |   |-- (app)/
|   |   |   |-- adverse-events/
|   |   |   |   |-- [id]/
|   |   |   |   |   `-- report/
|   |   |   |   |       `-- page.tsx (7.5 KB)
|   |   |   |   |-- dsmb/
|   |   |   |   |   `-- page.tsx (6.4 KB)
|   |   |   |   `-- page.tsx (27.3 KB)
|   |   |   |-- alerts/
|   |   |   |   |-- actions.ts (445 B)
|   |   |   |   `-- page.tsx (1.4 KB)
|   |   |   |-- audit/
|   |   |   |   `-- page.tsx (4.5 KB)
|   |   |   |-- copilot/
|   |   |   |   |-- copilot-client.tsx (3.8 KB)
|   |   |   |   `-- page.tsx (760 B)
|   |   |   |-- dashboard/
|   |   |   |   |-- loading.tsx (1.5 KB)
|   |   |   |   `-- page.tsx (27.0 KB)
|   |   |   |-- doctor-note/
|   |   |   |   |-- doctor-note-client.tsx (13.1 KB)
|   |   |   |   `-- page.tsx (2.0 KB)
|   |   |   |-- documents/
|   |   |   |   `-- page.tsx (6.7 KB)
|   |   |   |-- ethics/
|   |   |   |   `-- page.tsx (8.1 KB)
|   |   |   |-- exports/
|   |   |   |   `-- page.tsx (4.7 KB)
|   |   |   |-- extractions/
|   |   |   |   `-- page.tsx (4.0 KB)
|   |   |   |-- messages/
|   |   |   |   |-- messages-client.tsx (15.5 KB)
|   |   |   |   `-- page.tsx (1.3 KB)
|   |   |   |-- monitoring/
|   |   |   |   `-- page.tsx (18.0 KB)
|   |   |   |-- participants/
|   |   |   |   `-- page.tsx (10.3 KB)
|   |   |   |-- settings/
|   |   |   |   `-- page.tsx (16.6 KB)
|   |   |   |-- sites/
|   |   |   |   `-- page.tsx (7.6 KB)
|   |   |   |-- trials/
|   |   |   |   |-- [id]/
|   |   |   |   |   `-- page.tsx (15.7 KB)
|   |   |   |   |-- new/
|   |   |   |   |   `-- page.tsx (6.2 KB)
|   |   |   |   `-- page.tsx (3.2 KB)
|   |   |   |-- visits/
|   |   |   |   |-- [id]/
|   |   |   |   |   `-- page.tsx (12.1 KB)
|   |   |   |   `-- page.tsx (3.1 KB)
|   |   |   |-- layout.tsx (4.4 KB)
|   |   |   `-- loading.tsx (922 B)
|   |   |-- (auth)/
|   |   |   `-- login/
|   |   |       |-- actions.ts (638 B)
|   |   |       |-- login-form.tsx (1.6 KB)
|   |   |       `-- page.tsx (824 B)
|   |   |-- api/
|   |   |   |-- ai/
|   |   |   |   |-- approve/
|   |   |   |   |   `-- route.ts (2.0 KB)
|   |   |   |   |-- copilot/
|   |   |   |   |   `-- route.ts (1.9 KB)
|   |   |   |   `-- extract/
|   |   |   |       `-- route.ts (2.7 KB)
|   |   |   |-- alerts/
|   |   |   |   `-- latest-unread/
|   |   |   |       `-- route.ts (1.5 KB)
|   |   |   |-- auth/
|   |   |   |   `-- [...nextauth]/
|   |   |   |       `-- route.ts (82 B)
|   |   |   |-- badges/
|   |   |   |   `-- route.ts (1.2 KB)
|   |   |   |-- cron/
|   |   |   |   `-- alerts/
|   |   |   |       `-- route.ts (825 B)
|   |   |   |-- export/
|   |   |   |   `-- route.ts (3.1 KB)
|   |   |   |-- fhir/
|   |   |   |   |-- Bundle/
|   |   |   |   |   `-- [trialId]/
|   |   |   |   |       `-- route.ts (1.6 KB)
|   |   |   |   |-- import/
|   |   |   |   |   `-- route.ts (2.0 KB)
|   |   |   |   `-- ResearchStudy/
|   |   |   |       `-- [id]/
|   |   |   |           `-- route.ts (1.6 KB)
|   |   |   |-- guide/
|   |   |   |   `-- route.ts (4.8 KB)
|   |   |   |-- messages/
|   |   |   |   |-- latest-unread/
|   |   |   |   |   `-- route.ts (1.6 KB)
|   |   |   |   `-- route.ts (3.7 KB)
|   |   |   `-- search/
|   |   |       `-- route.ts (1.3 KB)
|   |   |-- apple-icon.png (5.6 KB)
|   |   |-- favicon.ico (3.1 KB)
|   |   |-- globals.css (3.9 KB)
|   |   |-- icon.png (1022 B)
|   |   |-- icon.svg (499 B)
|   |   |-- layout.tsx (923 B)
|   |   |-- manifest.ts (1.1 KB)
|   |   `-- page.tsx (111 B)
|   |-- components/
|   |   |-- app/
|   |   |   |-- alerts-list.tsx (4.9 KB)
|   |   |   |-- assistant-panel.tsx (11.7 KB)
|   |   |   |-- dashboard-charts.tsx (5.2 KB)
|   |   |   |-- doc-preview.tsx (5.8 KB)
|   |   |   |-- escalation-clock.tsx (2.5 KB)
|   |   |   |-- guide-widget.tsx (12.4 KB)
|   |   |   |-- install-banner.tsx (3.7 KB)
|   |   |   |-- live-badges.tsx (2.5 KB)
|   |   |   |-- live-clock.tsx (1.2 KB)
|   |   |   |-- message-toast.tsx (16.5 KB)
|   |   |   |-- mobile-nav.tsx (3.5 KB)
|   |   |   |-- nav-list.tsx (3.0 KB)
|   |   |   |-- print-button.tsx (405 B)
|   |   |   |-- quick-search.tsx (4.0 KB)
|   |   |   |-- shared.tsx (3.5 KB)
|   |   |   |-- sidebar.tsx (6.5 KB)
|   |   |   |-- skeleton.tsx (1.2 KB)
|   |   |   `-- term-picker.tsx (5.0 KB)
|   |   `-- ui/
|   |       |-- badge.tsx (808 B)
|   |       |-- button.tsx (1.5 KB)
|   |       |-- card.tsx (820 B)
|   |       `-- input.tsx (672 B)
|   |-- db/
|   |   |-- data/
|   |   |   `-- ctri_trials.json (16.7 KB)
|   |   |-- index.ts (1.4 KB)
|   |   |-- run-seed-real.ts (1.4 KB)
|   |   |-- run-seed.ts (393 B)
|   |   |-- schema.ts (20.3 KB)
|   |   |-- seed-real.ts (11.4 KB)
|   |   `-- seed.ts (12.8 KB)
|   |-- lib/
|   |   |-- ai/
|   |   |   |-- claude-text.ts (679 B)
|   |   |   |-- claude.ts (1.6 KB)
|   |   |   |-- gemini.ts (2.8 KB)
|   |   |   |-- prompts.ts (2.5 KB)
|   |   |   |-- provider.ts (2.6 KB)
|   |   |   `-- types.ts (2.0 KB)
|   |   |-- dictionaries/
|   |   |   |-- meddra-subset.ts (10.1 KB)
|   |   |   `-- whodrug-subset.ts (5.6 KB)
|   |   |-- guide/
|   |   |   |-- graph.ts (2.0 KB)
|   |   |   |-- knowledge.ts (19.2 KB)
|   |   |   |-- model.ts (720 B)
|   |   |   `-- prompt.ts (3.7 KB)
|   |   |-- rules/
|   |   |   |-- data-quality.ts (3.1 KB)
|   |   |   |-- deadlines.ts (1.9 KB)
|   |   |   |-- lifecycle.ts (2.8 KB)
|   |   |   |-- randomization.ts (3.1 KB)
|   |   |   |-- recruitment.ts (3.2 KB)
|   |   |   `-- visits.ts (1.8 KB)
|   |   |-- actor.ts (757 B)
|   |   |-- audit.ts (1.4 KB)
|   |   |-- auth-core.ts (1.5 KB)
|   |   |-- auth.ts (1.9 KB)
|   |   |-- crf.ts (3.5 KB)
|   |   |-- dashboard-variants.ts (3.5 KB)
|   |   |-- dates.ts (1.4 KB)
|   |   |-- device.ts (2.5 KB)
|   |   |-- errors.ts (1.8 KB)
|   |   |-- image.ts (2.5 KB)
|   |   |-- motion.ts (1.8 KB)
|   |   |-- nav.ts (3.7 KB)
|   |   |-- rbac.ts (3.4 KB)
|   |   |-- ttl-cache.ts (2.5 KB)
|   |   `-- utils.ts (175 B)
|   `-- services/
|       |-- export/
|       |   |-- adam.ts (1.9 KB)
|       |   |-- fhir.ts (4.7 KB)
|       |   `-- sdtm.ts (14.2 KB)
|       |-- adr.ts (4.0 KB)
|       |-- adverse-events.ts (5.9 KB)
|       |-- ae-report.ts (4.3 KB)
|       |-- alerts.ts (10.7 KB)
|       |-- amendments.ts (7.0 KB)
|       |-- audit-browser.ts (1.1 KB)
|       |-- badges.ts (2.7 KB)
|       |-- copilot.ts (5.3 KB)
|       |-- crf.ts (7.0 KB)
|       |-- dashboard.ts (14.0 KB)
|       |-- data-quality.ts (2.3 KB)
|       |-- data-queries.ts (7.6 KB)
|       |-- documents.ts (1.5 KB)
|       |-- extractions.ts (11.4 KB)
|       |-- fhir-import.ts (6.2 KB)
|       |-- guide-chat.ts (7.0 KB)
|       |-- kpi.ts (4.3 KB)
|       |-- messages.ts (4.7 KB)
|       |-- monitoring.ts (5.4 KB)
|       |-- participants.ts (11.0 KB)
|       |-- safety-signals.ts (7.7 KB)
|       |-- search.ts (3.0 KB)
|       |-- settings.ts (9.8 KB)
|       |-- signatures.ts (4.4 KB)
|       |-- sites.ts (3.1 KB)
|       |-- trials.ts (6.9 KB)
|       |-- users.ts (2.0 KB)
|       `-- visits.ts (2.5 KB)
|-- tests/
|   |-- helpers/
|   |   `-- db.ts (683 B)
|   |-- adr-intake.test.ts (5.9 KB)
|   |-- ae-report.test.ts (6.1 KB)
|   |-- ae-service.test.ts (5.0 KB)
|   |-- ai-provider.test.ts (7.1 KB)
|   |-- alert-config.test.ts (8.9 KB)
|   |-- alerts.test.ts (5.1 KB)
|   |-- amendments.test.ts (6.8 KB)
|   |-- auth-rbac.test.ts (3.5 KB)
|   |-- badges.test.ts (2.5 KB)
|   |-- consent.test.ts (6.5 KB)
|   |-- copilot.test.ts (4.2 KB)
|   |-- crf.test.ts (7.0 KB)
|   |-- dashboard-queries.test.ts (3.9 KB)
|   |-- dashboard-variants.test.ts (3.6 KB)
|   |-- data-quality.test.ts (2.8 KB)
|   |-- data-queries.test.ts (7.3 KB)
|   |-- dates.test.ts (1.6 KB)
|   |-- deadlines.test.ts (2.2 KB)
|   |-- design-qa.test.ts (4.1 KB)
|   |-- design-tokens.test.ts (2.8 KB)
|   |-- device.test.ts (3.7 KB)
|   |-- dictionaries.test.ts (6.0 KB)
|   |-- doc-preview.test.ts (1.3 KB)
|   |-- error-format.test.ts (2.5 KB)
|   |-- exports.test.ts (10.7 KB)
|   |-- extraction.test.ts (10.9 KB)
|   |-- fhir-api.test.ts (8.2 KB)
|   |-- guide-chat.test.ts (9.0 KB)
|   |-- guide.test.ts (6.4 KB)
|   |-- image.test.ts (1.6 KB)
|   |-- kpi.test.ts (2.4 KB)
|   |-- lifecycle.test.ts (2.9 KB)
|   |-- messages.test.ts (6.9 KB)
|   |-- monitoring.test.ts (7.6 KB)
|   |-- nav.test.ts (3.4 KB)
|   |-- participant-service.test.ts (6.8 KB)
|   |-- randomization.test.ts (7.1 KB)
|   |-- recruitment.test.ts (3.0 KB)
|   |-- regulator.test.ts (5.4 KB)
|   |-- safety-signals.test.ts (6.6 KB)
|   |-- sanity.test.ts (350 B)
|   |-- schema.test.ts (3.9 KB)
|   |-- search.test.ts (3.8 KB)
|   |-- seed-real.test.ts (6.0 KB)
|   |-- seed.test.ts (2.8 KB)
|   |-- signatures.test.ts (9.4 KB)
|   |-- site-service.test.ts (3.4 KB)
|   |-- trial-service.test.ts (7.6 KB)
|   |-- ttl-cache.test.ts (2.5 KB)
|   `-- visit-engine.test.ts (4.1 KB)
|-- .env.example (778 B)
|-- .gitignore (697 B)
|-- AGENTS.md (687 B)
|-- CLAUDE.md (12 B)
|-- CONTRIBUTING.md (3.4 KB)
|-- drizzle.config.ts (338 B)
|-- eslint.config.mjs (483 B)
|-- next.config.ts (140 B)
|-- package.json (1.7 KB)
|-- pnpm-lock.yaml (221.5 KB)
|-- postcss.config.mjs (101 B)
|-- README.md (2.8 KB)
|-- tsconfig.json (704 B)
|-- vercel.json (138 B)
`-- vitest.config.ts (706 B)

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


### File: `src\db\schema.ts`

```text
File: src\db\schema.ts
Purpose: Database schema (Drizzle / tables)
Important functions/classes: export const roleEnum, export const trialStatusEnum, export const studyTypeEnum, export const activationStatusEnum, export const screeningStatusEnum
Dependencies: drizzle-orm, drizzle-orm/pg-core
Inputs: Not determined from static scan (see code)
Outputs: Not determined
```


### File: `tests\adr-intake.test.ts`

```text
File: tests\adr-intake.test.ts
Purpose: Test suite (tests)
Important functions/classes: Not extracted
Dependencies: @/db/schema, ./helpers/db, drizzle-orm, vitest, @/lib/audit
Inputs: Not determined from static scan (see code)
Outputs: Not determined
```


### File: `tests\ae-report.test.ts`

```text
File: tests\ae-report.test.ts
Purpose: Test suite (tests)
Important functions/classes: Not extracted
Dependencies: @/db/schema, ./helpers/db, drizzle-orm, vitest, @/lib/audit
Inputs: Not determined from static scan (see code)
Outputs: Not determined
```


### File: `tests\ae-service.test.ts`

```text
File: tests\ae-service.test.ts
Purpose: Test suite (tests)
Important functions/classes: Not extracted
Dependencies: @/db/schema, ./helpers/db, drizzle-orm, vitest, @/lib/audit
Inputs: Not determined from static scan (see code)
Outputs: Not determined
```


### File: `tests\ai-provider.test.ts`

```text
File: tests\ai-provider.test.ts
Purpose: Test suite (tests)
Important functions/classes: Not extracted
Dependencies: @/db/schema, ./helpers/db, drizzle-orm, vitest, @/lib/audit
Inputs: Not determined from static scan (see code)
Outputs: Not determined
```


### File: `tests\alert-config.test.ts`

```text
File: tests\alert-config.test.ts
Purpose: Test suite (tests)
Important functions/classes: Not extracted
Dependencies: @/db/schema, ./helpers/db, drizzle-orm, vitest, @/lib/audit
Inputs: Not determined from static scan (see code)
Outputs: Not determined
```


### File: `tests\alerts.test.ts`

```text
File: tests\alerts.test.ts
Purpose: Test suite (tests)
Important functions/classes: Not extracted
Dependencies: @/db/schema, @/db/seed, ./helpers/db, drizzle-orm, vitest
Inputs: Not determined from static scan (see code)
Outputs: Not determined
```


### File: `tests\amendments.test.ts`

```text
File: tests\amendments.test.ts
Purpose: Test suite (tests)
Important functions/classes: Not extracted
Dependencies: @/db/schema, ./helpers/db, drizzle-orm, vitest, @/lib/audit
Inputs: Not determined from static scan (see code)
Outputs: Not determined
```


### File: `tests\auth-rbac.test.ts`

```text
File: tests\auth-rbac.test.ts
Purpose: Test suite (tests)
Important functions/classes: Not extracted
Dependencies: @/db/schema, @/lib/rbac, ./helpers/db, @/lib/auth-core, vitest
Inputs: Not determined from static scan (see code)
Outputs: Not determined
```


### File: `tests\badges.test.ts`

```text
File: tests\badges.test.ts
Purpose: Test suite (tests)
Important functions/classes: Not extracted
Dependencies: @/services/badges, @/db/schema, ./helpers/db, vitest, @/lib/audit
Inputs: Not determined from static scan (see code)
Outputs: Not determined
```


### File: `tests\consent.test.ts`

```text
File: tests\consent.test.ts
Purpose: Test suite (tests)
Important functions/classes: Not extracted
Dependencies: @/db/schema, ./helpers/db, drizzle-orm, vitest, @/lib/audit
Inputs: Not determined from static scan (see code)
Outputs: Not determined
```


### File: `tests\copilot.test.ts`

```text
File: tests\copilot.test.ts
Purpose: Test suite (tests)
Important functions/classes: function mockLlm
Dependencies: @/db/schema, @/db/seed, ./helpers/db, drizzle-orm, vitest
Inputs: Not determined from static scan (see code)
Outputs: Not determined
```


### File: `tests\crf.test.ts`

```text
File: tests\crf.test.ts
Purpose: Test suite (tests)
Important functions/classes: Not extracted
Dependencies: @/db/schema, ./helpers/db, drizzle-orm, vitest, @/lib/audit
Inputs: Not determined from static scan (see code)
Outputs: Not determined
```


### File: `tests\dashboard-queries.test.ts`

```text
File: tests\dashboard-queries.test.ts
Purpose: Test suite (tests)
Important functions/classes: Not extracted
Dependencies: @/db/schema, @/db/seed, ./helpers/db, drizzle-orm, vitest
Inputs: Not determined from static scan (see code)
Outputs: Not determined
```


### File: `tests\dashboard-variants.test.ts`

```text
File: tests\dashboard-variants.test.ts
Purpose: Test suite (tests)
Important functions/classes: Not extracted
Dependencies: @/lib/dashboard-variants, vitest, @/lib/rbac
Inputs: Not determined from static scan (see code)
Outputs: Not determined
```


### File: `tests\data-quality.test.ts`

```text
File: tests\data-quality.test.ts
Purpose: Test suite (tests)
Important functions/classes: Not extracted
Dependencies: @/lib/rules/data-quality, vitest
Inputs: Not determined from static scan (see code)
Outputs: Not determined
```


### File: `tests\data-queries.test.ts`

```text
File: tests\data-queries.test.ts
Purpose: Test suite (tests)
Important functions/classes: Not extracted
Dependencies: @/db/schema, ./helpers/db, drizzle-orm, vitest, @/lib/audit
Inputs: Not determined from static scan (see code)
Outputs: Not determined
```


### File: `tests\dates.test.ts`

```text
File: tests\dates.test.ts
Purpose: Test suite (tests)
Important functions/classes: Not extracted
Dependencies: vitest, @/lib/dates
Inputs: Not determined from static scan (see code)
Outputs: Not determined
```


### File: `tests\deadlines.test.ts`

```text
File: tests\deadlines.test.ts
Purpose: Test suite (tests)
Important functions/classes: Not extracted
Dependencies: @/lib/rules/deadlines, vitest
Inputs: Not determined from static scan (see code)
Outputs: Not determined
```


### File: `tests\design-qa.test.ts`

```text
File: tests\design-qa.test.ts
Purpose: Test suite (tests)
Important functions/classes: function walk
Dependencies: node:path, vitest, node:fs
Inputs: Not determined from static scan (see code)
Outputs: Not determined
```


### File: `tests\design-tokens.test.ts`

```text
File: tests\design-tokens.test.ts
Purpose: Test suite (tests)
Important functions/classes: Not extracted
Dependencies: node:path, vitest, node:fs, @/lib/motion
Inputs: Not determined from static scan (see code)
Outputs: Not determined
```


### File: `tests\device.test.ts`

```text
File: tests\device.test.ts
Purpose: Test suite (tests)
Important functions/classes: Not extracted
Dependencies: vitest, @/lib/device
Inputs: Not determined from static scan (see code)
Outputs: Not determined
```


### File: `tests\dictionaries.test.ts`

```text
File: tests\dictionaries.test.ts
Purpose: Test suite (tests)
Important functions/classes: Not extracted
Dependencies: @/lib/dictionaries/meddra-subset, @/db/schema, ./helpers/db, vitest, @/lib/audit
Inputs: Not determined from static scan (see code)
Outputs: Not determined
```



## Note

- Do not trust README folder list if it includes .git/node_modules — those are excluded here for analysis efficiency.
- For full file list, see `repositories/vansh459_AyuSphere/` directly or run `tree /F` in PowerShell.
