# Demo Comparison — Across 7 Competitors

**Generated:** 2026-09-30
**Evidence:** `presentation_analysis/analysis/*/DEMO_ANALYSIS.md:1` + `docs/DEMO_SCRIPT.md` raw, not README claim alone.
**Do NOT rank.**

## Matrix

| Stage | nishant-uxs_vedraya | vansh459_AyuSphere | DuvvuruDeepakReddy18_AyuTrial | aravindakrishna-c_AIIA-Clinical-Trial-Dashboard | AnushkaTadiyal_aiia-ctms | rimi007-grt_AIIA-CTMS | kalyan-2006-prog_SIH26046-DEV-RUSH- |
|---|---|---|---|---|---|---|---|
| **Opening** | Open app → Enter Live Command Center → login admin@vedraya.demo (Vedraya!Demo1) → badge Live PostgreSQL | Live demo https://ayusphere-three.vercel.app → sign in as pi@aiia.demo (Demo@1234) | Landing page Ministry of Ayush branding → 1-click persona launcher (no password) → login page | No demo script — README only — Unknown | No demo script — Unknown | No demo script — Unknown | No demo script — Unknown |
| **Problem framing** | SIH26046 Ministry of Ayush / AIIA + traceability matrix docs/SIH26046_TRACEABILITY_FINAL.md 8KB | SIH26046 Ministry of Ayush · AIIA + gap-analysis.md 13KB / gap-plan.md 16KB | SIH26046 Organization Ministry of Ayush, Institution AIIA, Domain CTMS + NPvCC | README SIH26046 (sparse) | README SIH26046, keywords ctms | README Aayu-Setu CTMS Ministry of Ayush | No problem framing doc — minimal README 1.5KB |
| **Login/RBAC** | 7 roles demo via admin login, then monitor@vedraya.demo (AYU-024 only) → regulator@vedraya.demo (403) — ACL tested | 7 roles via Auth.js JWT (pi, coordinator, monitor, ethics, pv, admin, regulator read-only) — Tested regulator.test.ts | 7 personas via 1-click switcher (admin.ctms@aiia.gov.in etc.) no password — demo persona, not real auth | Login page (frontend) + FastAPI JWT — no judge persona docs | AuthPage.jsx JWT — no demo persona doc | Same as Anushka + test_rbac_matrix.js | No demo script — seed-demo scripts (activate-demo-consent.ts etc.) |
| **Trial creation** | Study AYU-024 lifecycle transitions (studies/routes.ts) | Clinical Trials → trial lifecycle state machine (lifecycle.test.ts) | /studies + /studies/new GCP-ASU form + 10-stage pipeline /studies/[id] 27KB | trials.py POST /trials (11KB) + frontend CreateTrialPage 41KB | TrialsPage 30KB + TrialDetail 37KB — basic CRUD | Same | Dashboard/[trialId] page 9.6KB — stub |
| **Protocol** | Milestones per study (milestones/routes.ts) | Amendments (`amendments.test.ts`) + lifecycle | Milestone tracker tabbed dossiers | trials.py includes protocol fields | No protocol differentiator | No | No |
| **Participant** | Participants CRUD (participants/routes.ts) screened/enrolled | Participants de-identified by schema (no identifier cols) | Synthetic participants registry DEMO-0001 + participant dossier | participants.py 7.3KB | basic | basic | NOT PRESENT |
| **Clinical data / CRF** | Participants + AE (no full eCRF) — PARTIALLY | CRF immutability + versioned corrections (crf.test.ts) IMPLEMENTED | Scheduled visit adherence matrix + Ayush exams (Prakriti/Agni/Koshtha) — MOCKED | NOT PRESENT | NOT PRESENT | NOT PRESENT | NOT PRESENT |
| **AE/SAE** | Safety → AE → DEMO MedDRA coding → escalate SAE → reporting due / notify | AE escalation clock (ae-service.test.ts) + safety signals | pharmacovigilance NPvCC + 24h SAE countdown + WHO-UMC (pharmacovigilance/new 22KB) | safety.py 3.5KB | SafetyPage 30KB | SafetyPage 39KB | adverse-events page 8.7KB |
| **Ethics** | Ethics committees via regulatory routes | Ethics Review (ethics@ role) | Institutional Ethics Committee workflow (Prof Joshi) | ethics_regulatory.py 4.4KB | EthicsPage 12KB | EthicsPage | NOT PRESENT |
| **Regulatory** | Regulatory / CTRI TRACKING / NDCT (tracking) | CTRI real scrape + regulatory workflow | Statutory compliance matrix GCP-ASU/ICMR/NDCT + CTRI verification | ethics_regulatory.py | CLAIMED ONLY | CLAIMED ONLY | ctri-ethics page 8KB |
| **Pharmacovigilance** | PARTIALLY (no NPvCC) | PV officer + signals | NPvCC apex IMPLEMENTED (dedicated) + CDSCO | PARTIALLY | NOT PRESENT | NOT PRESENT | NOT PRESENT |
| **Analytics** | Portfolio KPIs + computed alerts (enrolment lag, open SAE) | Real-time KPIs + alerts cron idempotency | 10 computed KPIs + 7 Recharts + 24h SAE clock | dashboard.py 1.6KB | DashboardPage 25KB PARTIALLY | DashboardPage 34KB | dashboard page 10.6KB |
| **AI** | NOT PRESENT (honest) | Doctor Note OCR + grounded Copilot (declines on empty) — IMPLEMENTED | NOT PRESENT (WHO-UMC rule) | NOT PRESENT | NOT PRESENT | NOT PRESENT | NOT PRESENT |
| **FHIR/CDISC** | Exports/Interop → SDTM-like AE · FHIR R4 prototype · adapters NOT CONNECTED | FHIR Bundle + SDTM exports (fhir-api.test.ts, exports.test.ts) | CDISC SDTM DM/AE/EX/VS/LB + FHIR R4 bundle inspector + ABDM blueprint NOT CONNECTED | FHIR 2.5KB stub | NOT PRESENT | NOT PRESENT | FHIR ingest 12.5KB / SDTM stubs |
| **Audit** | Audit → Re-verify SHA-256 chain → AUDIT CHAIN: VERIFIED (audit/service.ts GLOBAL) | Audit Trail append-only (withAudit) — admin cannot delete | Audit-logs ALCOA+ ledger + SHA-256 local hash (mocked) | audit_logs.py | AuditPage 9KB | AuditPage 33KB | audit-log route 3.1KB |
| **Closing** | Logout → monitor/regulator ACL demo, then verdict (see VEDRAYA_JUDGE_ANALYSIS) | Role scores evaluation axes (Administrator guide: All four axes) | Settings regulatory deadline rules editor | Unknown | Unknown | Unknown | Unknown |
| **Evidence demo exists** | YES (DEMO_SCRIPT.md 3KB + Judge in 60 seconds README + e2e critical path 11KB) | YES (Judge_Demo_Script.md 4.1KB + pdf 1.31MB + 7 UAT guides) | No explicit demo script — README is pitch, 28 routes + mockData is demo | No demo script | No demo script | No demo script | No demo script (scripts/activate-demo* are data scripts) |

> **Common:** All with demo emphasize trial creation → participants → AE/SAE → audit. Only vedraya + AyuSphere have detailed judge-grade demo scripts with exact click paths drift-guard tested; AyuTrial emphasizes NPvCC 24h clock.

