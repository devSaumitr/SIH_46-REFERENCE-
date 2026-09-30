# FILE_STRUCTURE — aravindakrishna-c_AIIA-Clinical-Trial-Dashboard

**Source:** `E:\SIH26046_COMPETITOR_ANALYSIS\repositories\aravindakrishna-c_AIIA-Clinical-Trial-Dashboard`
**Generated:** 2026-09-30
**Tracked files (excl .git/node_modules/.next/dist/build):** 153
**Size:** 0.98 MB

## Tree (max depth 8, skipped .git/node_modules/.venv/dist/build)

```text
aravindakrishna-c_AIIA-Clinical-Trial-Dashboard/
|-- backend/
|   |-- app/
|   |   |-- api/
|   |   |   |-- v1/
|   |   |   |   |-- audit_logs.py (1.3 KB)
|   |   |   |   |-- auth.py (2.2 KB)
|   |   |   |   |-- dashboard.py (1.6 KB)
|   |   |   |   |-- ethics_regulatory.py (4.4 KB)
|   |   |   |   |-- export.py (1.7 KB)
|   |   |   |   |-- fhir.py (2.5 KB)
|   |   |   |   |-- participants.py (7.3 KB)
|   |   |   |   |-- roles.py (1.0 KB)
|   |   |   |   |-- safety.py (3.5 KB)
|   |   |   |   |-- trials.py (11.8 KB)
|   |   |   |   `-- users.py (2.8 KB)
|   |   |   `-- router.py (670 B)
|   |   |-- core/
|   |   |   |-- config.py (1.2 KB)
|   |   |   |-- dependencies.py (3.5 KB)
|   |   |   `-- security.py (1.7 KB)
|   |   |-- database/
|   |   |   |-- init_db.py (60.0 KB)
|   |   |   `-- session.py (748 B)
|   |   |-- models/
|   |   |   |-- __init__.py (1.0 KB)
|   |   |   |-- adverse_event.py (5.1 KB)
|   |   |   |-- audit_log.py (1.5 KB)
|   |   |   |-- base.py (185 B)
|   |   |   |-- clinical_trial.py (6.9 KB)
|   |   |   |-- ctri_regulatory.py (3.8 KB)
|   |   |   |-- ethics_submission.py (2.8 KB)
|   |   |   |-- participant.py (4.4 KB)
|   |   |   |-- participant_visit.py (2.9 KB)
|   |   |   |-- permission.py (1.3 KB)
|   |   |   |-- role.py (1.0 KB)
|   |   |   |-- trial_milestone.py (1.6 KB)
|   |   |   |-- trial_protocol_version.py (1.7 KB)
|   |   |   |-- trial_site.py (2.7 KB)
|   |   |   `-- user.py (1.6 KB)
|   |   |-- schemas/
|   |   |   |-- adverse_event.py (2.5 KB)
|   |   |   |-- audit_log.py (517 B)
|   |   |   |-- auth.py (643 B)
|   |   |   |-- clinical_trial.py (6.4 KB)
|   |   |   |-- dashboard_kpi.py (2.2 KB)
|   |   |   |-- ethics_regulatory.py (3.5 KB)
|   |   |   |-- fhir_cdisc.py (385 B)
|   |   |   |-- participant.py (3.3 KB)
|   |   |   |-- participant_visit.py (1.5 KB)
|   |   |   |-- role.py (606 B)
|   |   |   |-- trial_milestone.py (982 B)
|   |   |   |-- trial_protocol.py (757 B)
|   |   |   |-- trial_site.py (1.9 KB)
|   |   |   `-- user.py (1.0 KB)
|   |   |-- services/
|   |   |   |-- audit_service.py (2.1 KB)
|   |   |   |-- auth_service.py (3.2 KB)
|   |   |   |-- cdisc_service.py (5.0 KB)
|   |   |   |-- dashboard_service.py (15.7 KB)
|   |   |   |-- fhir_service.py (11.2 KB)
|   |   |   |-- participant_service.py (20.9 KB)
|   |   |   |-- regulatory_service.py (9.4 KB)
|   |   |   |-- safety_service.py (9.7 KB)
|   |   |   |-- trial_service.py (24.9 KB)
|   |   |   `-- user_service.py (7.1 KB)
|   |   `-- main.py (5.1 KB)
|   |-- migrations/
|   |   |-- versions/
|   |   |   `-- 001_initial_schema.py (4.9 KB)
|   |   |-- env.py (1.6 KB)
|   |   `-- script.py.mako (661 B)
|   |-- tests/
|   |   |-- conftest.py (3.3 KB)
|   |   |-- e2e_demo.py (6.9 KB)
|   |   |-- test_audit.py (2.5 KB)
|   |   |-- test_auth.py (2.0 KB)
|   |   |-- test_dashboard_kpis.py (1.4 KB)
|   |   |-- test_e2e_full_lifecycle.py (10.3 KB)
|   |   |-- test_ethics_regulatory.py (2.6 KB)
|   |   |-- test_fhir_cdisc.py (2.2 KB)
|   |   |-- test_participants.py (4.2 KB)
|   |   |-- test_rbac.py (1.7 KB)
|   |   |-- test_safety.py (2.8 KB)
|   |   |-- test_trial_rbac.py (3.5 KB)
|   |   |-- test_trial_sites.py (3.7 KB)
|   |   |-- test_trial_workflow.py (4.1 KB)
|   |   |-- test_trials.py (6.4 KB)
|   |   `-- test_users.py (3.3 KB)
|   |-- .env.example (1.1 KB)
|   |-- alembic.ini (1.7 KB)
|   |-- pytest.ini (45 B)
|   `-- requirements.txt (286 B)
|-- frontend/
|   |-- public/
|   |   |-- favicon.svg (9.3 KB)
|   |   `-- icons.svg (4.9 KB)
|   |-- src/
|   |   |-- assets/
|   |   |   |-- hero.png (12.8 KB)
|   |   |   |-- react.svg (4.0 KB)
|   |   |   `-- vite.svg (8.5 KB)
|   |   |-- components/
|   |   |   |-- modals/
|   |   |   |   |-- EthicsDecisionModal.tsx (8.0 KB)
|   |   |   |   |-- RandomizationModal.tsx (7.3 KB)
|   |   |   |   |-- SafetyReportModal.tsx (14.0 KB)
|   |   |   |   `-- VisitModal.tsx (5.7 KB)
|   |   |   |-- MilestoneTimeline.tsx (17.3 KB)
|   |   |   |-- Modal.tsx (1.6 KB)
|   |   |   |-- ProtectedRoute.tsx (899 B)
|   |   |   |-- ProtocolVersionModal.tsx (5.8 KB)
|   |   |   |-- RoleGuard.tsx (674 B)
|   |   |   |-- SiteModal.tsx (12.1 KB)
|   |   |   |-- SiteStatusModal.tsx (5.7 KB)
|   |   |   |-- StatusBadge.tsx (8.4 KB)
|   |   |   `-- StatusTransitionModal.tsx (6.8 KB)
|   |   |-- context/
|   |   |   `-- AuthContext.tsx (3.1 KB)
|   |   |-- layouts/
|   |   |   `-- DashboardLayout.tsx (14.4 KB)
|   |   |-- pages/
|   |   |   |-- AccessDeniedPage.tsx (2.8 KB)
|   |   |   |-- AuditLogsPage.tsx (7.7 KB)
|   |   |   |-- CreateTrialPage.tsx (41.2 KB)
|   |   |   |-- DashboardPage.tsx (27.4 KB)
|   |   |   |-- EditTrialPage.tsx (20.4 KB)
|   |   |   |-- EthicsRegulatoryPage.tsx (40.5 KB)
|   |   |   |-- InteroperabilityPage.tsx (12.2 KB)
|   |   |   |-- LoginPage.tsx (8.3 KB)
|   |   |   |-- ParticipantDetailPage.tsx (28.9 KB)
|   |   |   |-- ParticipantScreeningPage.tsx (17.8 KB)
|   |   |   |-- ParticipantsPage.tsx (20.5 KB)
|   |   |   |-- ProfilePage.tsx (4.3 KB)
|   |   |   |-- SafetyDetailPage.tsx (21.0 KB)
|   |   |   |-- SafetyPage.tsx (20.9 KB)
|   |   |   |-- TrialDetailPage.tsx (34.1 KB)
|   |   |   |-- TrialsPage.tsx (19.2 KB)
|   |   |   `-- UsersPage.tsx (14.7 KB)
|   |   |-- services/
|   |   |   |-- api.ts (1.2 KB)
|   |   |   |-- authService.ts (714 B)
|   |   |   |-- dashboardService.ts (627 B)
|   |   |   |-- interopService.ts (878 B)
|   |   |   |-- participantService.ts (3.3 KB)
|   |   |   |-- regulatoryService.ts (2.2 KB)
|   |   |   |-- safetyService.ts (1.6 KB)
|   |   |   |-- trialService.ts (5.0 KB)
|   |   |   `-- userService.ts (1.6 KB)
|   |   |-- types/
|   |   |   `-- index.ts (15.3 KB)
|   |   |-- App.css (3.0 KB)
|   |   |-- App.tsx (4.9 KB)
|   |   |-- index.css (744 B)
|   |   `-- main.tsx (240 B)
|   |-- .env.example (153 B)
|   |-- .gitignore (277 B)
|   |-- .oxlintrc.json (253 B)
|   |-- index.html (373 B)
|   |-- package-lock.json (93.1 KB)
|   |-- package.json (735 B)
|   |-- postcss.config.js (86 B)
|   |-- README.md (1.3 KB)
|   |-- tailwind.config.js (998 B)
|   |-- tsconfig.app.json (681 B)
|   |-- tsconfig.json (126 B)
|   |-- tsconfig.node.json (581 B)
|   |-- vercel.json (104 B)
|   `-- vite.config.ts (347 B)
|-- .gitignore (463 B)
|-- DEPLOYMENT.md (4.4 KB)
|-- docker-compose.yml (374 B)
|-- Dockerfile (1015 B)
|-- README.md (9.1 KB)
|-- render.yaml (643 B)
|-- run_localhost.bat (1.1 KB)
`-- vercel.json (209 B)

```

## Important Files (explanations, top 25)

> Focus on files affecting behavior. Skipped .git, node_modules, build artifacts.


### File: `Dockerfile`

```text
File: Dockerfile
Purpose: Container deployment
Important functions/classes: Not extracted
Dependencies: Unknown
Inputs: Not determined from static scan (see code)
Outputs: Not determined
```


### File: `README.md`

```text
File: README.md
Purpose: Project documentation (CLAIM vs FACT check needed)
Important functions/classes: Not extracted
Dependencies: Unknown
Inputs: Not determined from static scan (see code)
Outputs: Not determined
```


### File: `backend\app\api\router.py`

```text
File: backend\app\api\router.py
Purpose: FastAPI central router
Important functions/classes: Not extracted
Dependencies: Unknown
Inputs: Not determined from static scan (see code)
Outputs: Not determined
```


### File: `backend\app\database\init_db.py`

```text
File: backend\app\database\init_db.py
Purpose: DB initialization & seed (60KB synthetic)
Important functions/classes: Not extracted
Dependencies: Unknown
Inputs: Not determined from static scan (see code)
Outputs: Not determined
```


### File: `backend\requirements.txt`

```text
File: backend\requirements.txt
Purpose: Python dependencies
Important functions/classes: Not extracted
Dependencies: Unknown
Inputs: Not determined from static scan (see code)
Outputs: Not determined
```


### File: `frontend\README.md`

```text
File: frontend\README.md
Purpose: Project documentation (CLAIM vs FACT check needed)
Important functions/classes: Not extracted
Dependencies: Unknown
Inputs: Not determined from static scan (see code)
Outputs: Not determined
```


### File: `frontend\package.json`

```text
File: frontend\package.json
Purpose: Node dependencies & scripts
Important functions/classes: Not extracted
Dependencies: Unknown
Inputs: Not determined from static scan (see code)
Outputs: Not determined
```


### File: `frontend\vercel.json`

```text
File: frontend\vercel.json
Purpose: Vercel deployment config
Important functions/classes: Not extracted
Dependencies: Unknown
Inputs: Not determined from static scan (see code)
Outputs: Not determined
```


### File: `vercel.json`

```text
File: vercel.json
Purpose: Vercel deployment config
Important functions/classes: Not extracted
Dependencies: Unknown
Inputs: Not determined from static scan (see code)
Outputs: Not determined
```



## Note

- Do not trust README folder list if it includes .git/node_modules — those are excluded here for analysis efficiency.
- For full file list, see `repositories/aravindakrishna-c_AIIA-Clinical-Trial-Dashboard/` directly or run `tree /F` in PowerShell.
