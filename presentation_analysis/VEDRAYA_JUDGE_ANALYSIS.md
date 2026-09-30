# VEDRAYA Special Extraction — Judge Intelligence

**Repository:** `nishant-uxs_vedraya` (`https://github.com/nishant-uxs/vedraya`)
**Generated:** 2026-09-30
**Files analyzed:** `docs/DEMO_SCRIPT.md` (3.0 KB), `docs/JUDGE_QA.md` (3.5 KB), `docs/SIH26046_TRACEABILITY_FINAL.md` (8.0 KB), `docs/ARCHITECTURE.md` (5.5 KB), `docs/` (14 md), `README.md` (16.3 KB)

## 1. Demo Sequence (from DEMO_SCRIPT.md)

```markdown
# DEMO SCRIPT — SIH26046 (3–5 minutes)

**Before the round:** `npm run demo:seed`  
Password (all accounts): `Vedraya!Demo1`  
Primary surface: **Live Command Center** (`#command-center`)

| Time | Action | What to show | What to say | Expected result |
|------|--------|--------------|-------------|-----------------|
| 00:00–00:20 | Open app → click **Enter Live Command Center** → login `admin@vedraya.demo` | Badge **Command Center · Live PostgreSQL** | “Marketing sections above are conceptual. This panel is live PostgreSQL.” | KPIs non-zero; SOURCE postgresql |
| 00:20–00:50 | Overview → Studies → select **AYU-024** | Study code, phase, enrolment, risk | “Portfolio and per-study drill-down from the database.” | AYU-024 visible with DB fields |
| 00:50–01:10 | Sites → Investigators → Participants | Assigned sites/PI/subjects | “Site activation and enrolment/screening statuses are persisted.” | Lists load; no empty crash |
| 01:10–01:50 | Safety → open AE → DEMO MedDRA code → escalate SAE → show report due / notify | Coding label + status transitions | “MedDRA-compatible coding prototype — demo dictionary, not licensed MedDRA. SAE reporting timeline is tracked here.” | Coding applied; SAE escalated; timeline fields visible |
| 01:50–02:15 | Consents → Regulatory | Consent status; IEC / **CTRI TRACKING** / NDCT | “CTRI TRACKING only — not an external CTRI integration.” | Records load; note visible |
| 02:15–02:35 | Quality | Deviations + data queries | “Operational quality tracking — partial vs full CAPA/EDC.” | Seeded PD/DQ or create one |
| 02:35–02:50 | Overview alerts | Enrolment lag / SAE reporting overdue / deviation | “Alerts are computed from DB rules, not a fake static list.” | Meaningful alert rows |
| 02:50–03:20 | Audit → **Re-verify SHA-256 chain** | VERIFIED · GLOBAL · event count | “Append-only audit with SHA-256 hash-chain integrity verification — tamper detection, not WORM.” | AUDIT CHAIN: VERIFIED |
| 03:20–03:40 | Exports → FHIR Interop | CSV / SDTM-like AE; ResearchStudy JSON; adapters | “SDTM-like AE prototype. FHIR R4 ResearchStudy/Subject prototype. ABDM/HIS/EDC are NOT CONNECTED.” | Honest labels; load succeeds |
| 03:40–04:10 | Logout → `monitor@vedraya.demo` | Studies = **AYU-024** only | “Study membership ACL — monitor is scoped.” | totalStudies 1 |
| 04:10–04:30 | Logout → `regulator@vedraya.demo` → attempt create (UI absent) / note API 403 | Read-only regulator | “Regulator can view portfolio; mutations return 403 from the API.” | No create study UI |
| 04:30–05:00 | Close | Limitations slide / LIMITATIONS.md | “Prototype boundaries are intentional for SIH staging.” | Clear honesty |

## Optional API proof (terminal)

```bash
# regulator create → 403
# monitor GET non-AYU-024 study → 403
# GET /api/v1/audit-events/verify → valid: true
```

## After Playwright / experiments

Always re-run `npm run demo:seed` so `E2E-ST-*` studies do not appear in the judge demo.

```

**Analysis:**
- **What shown first:** Open app → Enter Live Command Center → login `admin@vedraya.demo` (password `Vedraya!Demo1`) → confirm badge **Command Center · Live PostgreSQL** → open study **AYU-024** → Sites/Investigators/Participants → Safety AE → DEMO MedDRA coding → escalate SAE → reporting due / notify → Consents + Regulatory (IEC / CTRI TRACKING / NDCT) → Quality + alerts → Audit **Re-verify SHA-256 chain** → `AUDIT CHAIN: VERIFIED` → Exports/Interop (SDTM-like, FHIR prototype, adapters NOT CONNECTED) → logout → `monitor@vedraya.demo` (AYU-024 only) → `regulator@vedraya.demo` (no create UI, API 403)
- **Prerequisite:** `npm run demo:seed` (clears E2E-ST-* pollution, restores AYU-* portfolio)
- **Timing:** 9 steps, 60-second judge flow (README Judge in 60 seconds + docs/DEMO_SCRIPT.md)
- **Evidence shown:** Live PostgreSQL numbers after sign-in (README notes marketing landing is conceptual, live numbers from PG), deterministic seed.

## 2. Judge Questions Anticipated (from JUDGE_QA.md)

```markdown
# Judge Q&A — VEDRAYA / SIH26046

Answers match the **current** implementation. Do not improvise beyond this sheet.

## 1. Is MedDRA official?

**No.** We use `MEDDRA_DEMO` — a MedDRA-compatible coding prototype with a synthetic demo dictionary. Not licensed MedDRA.

## 2. Is WHODrug official?

**No.** `WHODRUG_DEMO` only — WHODrug-compatible coding prototype. Not licensed WHODrug.

## 3. Is this CDISC compliant?

**No certification claim.** We provide an **SDTM-like AE transformation prototype** and CSV exports. CDASH, full SDTM, ADaM datasets, and Define-XML are not implemented.

## 4. Is ABDM connected?

**No.** Adapter status is **NOT CONNECTED**.

## 5. Is CTRI integrated?

**No external CTRI API.** We implement **CTRI TRACKING** (internal regulatory status records). Same honesty for NDCT tracking.

## 6. Is the audit WORM?

**No.** Application-level **append-only** audit trail with **GLOBAL SHA-256 hash-chain integrity verification** (tamper detection). Direct DB mutation is not prevented by WORM storage; verify can detect hash mismatches.

## 7. Is this ALCOA+ compliant?

**We do not claim legal ALCOA+ compliance.** The audit supports attributable, contemporaneous, original-ish snapshots and integrity checks as a prototype foundation.

## 8. How does RBAC work?

Seven seeded roles (PI, coordinator, monitor, ethics, PV, administration, regulator) with permission keys enforced by server middleware `requirePermission`. UI hiding is not authorization.

## 9. How is study-level isolation enforced?

Table `study_memberships`. Administration and regulator: unrestricted study scope. Other roles: only membership studies. **Zero memberships → empty study list (deny).** Enforced in API handlers via `resolveStudyScope` / `assertStudyAccess`.

## 10. What happens to unauthorized API requests?

- No session → **401**
- Session without permission → **403**
- Session without study membership for that resource → **403**
- Sessioned mutation without CSRF → **403**

## 11. Where is the data stored?

**PostgreSQL** via Drizzle ORM. Command Center shows `SOURCE postgresql` when live.

## 12. Does refresh preserve changes?

**Yes** for persisted mutations (studies, AE, consent, etc.). After create/update, refresh or re-login and data remains. Demo seed is restored with `npm run demo:seed`.

## 13. How does SAE reporting work?

AE workflow with status transitions; serious/escalated cases get a `reportingDueAt` clock (demo 24h). `authorityNotifiedAt` records notification. Overdue cases surface in computed alerts. **Not** a certified NDCT jurisdictional filing integration.

## 14. How are alerts generated?

Server computes alerts from DB state (overdue milestones, high risk, open SAE, pending consent/ethics, enrolment lag, SAE reporting overdue, open deviations/queries). Fixed rules in code — **not** end-user configurable yet.

## 15. What is currently prototype-only?

MedDRA/WHODrug demo coding; SDTM-like AE; ADaM placeholder; FHIR R4 ResearchStudy/Subject; quality deviations/queries (partial); interop adapters NOT_CONNECTED; landing cinematic narrative (MOCK/conceptual).

## 16. What would be required for production deployment?

Licensed dictionaries; full CDISC + Define-XML; real EDC/HIS/ABDM integration; external CTRI; WORM/attested audit; e-signature; hardened hosting (ISO27001/CERT-In); DPDP operational controls; user-configurable alerts; IWRS/randomization; full visit/eCRF; penetration testing and compliance assessment. Staged delivery is aligned with the PS.

```

**Categories extracted (heuristic):**
- Technical: WORM? → NOT WORM but hash-chain verify; Auth: Argon2 + sid + CSRF; RBAC 7 + ACL
- Security: Audit tamper → valid:false test; Rate limiting pluggable
- Regulatory: Licensed MedDRA? → DEMO dictionary MEDDRA_DEMO, not licensed; CDISC certified? → SDTM-like prototype, not certified
- Architecture: ABDM/HIS/EDC connected? → NOT CONNECTED (`/interop/adapters`)
- Data: Real patient? → Synthetic only, de-identified
- Compliance: GCP-ASU/DPDP certified? → Process support, not certified (LIMITATIONS.md)
- Deployment: Where hosted? → Vercel SPA only (API + Postgres separate per README)
- See `analysis/nishant-uxs_vedraya/JUDGE_QA_ANALYSIS.md:1` for per-question categories.

## 3. PS Mapping (from SIH26046_TRACEABILITY_FINAL.md)

```markdown
# SIH26046 — Final Requirements Traceability

**Source of truth:** Official SIH Problem Statement ID **26046** (Ministry of Ayush / AIIA), as provided in the Phase 6 workspace brief.

**Product:** VEDRAYA CTMS prototype  
**Last updated:** 2026-09-29 (Phase 6)

Statuses: `IMPLEMENTED` | `PARTIAL` | `PROTOTYPE` | `MOCKED` | `NOT IMPLEMENTED` | `NOT APPLICABLE`

`IMPLEMENTED` requires (where applicable): UI → API → auth → RBAC/ACL → validation → business logic → PostgreSQL → audit → automated test. Missing layers → `PARTIAL` / `PROTOTYPE`.

---

## Exact PS requirements extracted

### Functional / product
1. Real-time, cloud-based CTMS + monitoring dashboard  
2. Single role-based, auditable portfolio view  
3. Per-study lifecycle: protocol & IEC approval, CTRI registration, site activation, screening, enrolment & randomization against target, visit & protocol-deviation compliance, data-query & data-quality status, milestones/timelines, close-out  
4. Real-time KPIs with configurable alerts (e.g. enrolment lag, ethics/CTRI due, overdue monitoring visit)  
5. Pharmacovigilance: ADR/AE/SAE capture & routing against regulatory reporting timelines; MedDRA & WHODrug coding; aggregate safety signals for DSMB / leadership  
6. CDISC: CDASH (collection), SDTM (tabulation), ADaM (analysis); Define-XML export  
7. HL7 FHIR R4 interoperability with EDC, HIS, ABDM building blocks  
8. ALCOA+ data integrity + immutable time-stamped audit trail  
9. Strict RBAC: PI, study coordinator, monitor, Ethics Committee, pharmacovigilance, administration, read-only regulator  
10. Informed-consent management  
11. Electronic-signature and data-integrity controls consistent with GCP  
12. Export submission-ready SDTM / ADaM / Define-XML  
13. Tailored dashboards: Investigators, Ethics Committee, PV, institutional leadership  
14. Hosting: data-resident cloud, ISO/IEC 27001 & CERT-In norms  

### Compliance / legal (claims vs implementation)
15. GCP-ASU compliance  
16. ICMR National Ethical Guidelines alignment  
17. NDCT Rules 2019 where applicable  
18. CTRI requirements  
19. DPDP Act 2023 & 2025 Rules (consent, minimisation, encryption, residency)  

### Data / evaluation
20. Synthetic / de-identified development data  
21. Evaluable on: data accuracy & integrity; timeliness of safety & regulatory reporting; interoperability conformance; access-control & audit completeness  

### Delivery note from PS
22. Staged build is acceptable: core study-tracking + KPI MVP → EDC/FHIR + PV → full CDISC submission export & advanced analytics  

---

## Traceability matrix

| PS Requirement | VEDRAYA Implementation | Status | Evidence | Gap | Priority |
|---|---|---|---|---|---|
| Real-time cloud CTMS dashboard | Command Center + Express/Postgres API | **IMPLEMENTED** | CC UI, `/api/v1/*`, seed | Cloud hosting / CERT-In not productized | P2 |
| Role-based auditable portfolio | Studies list + KPIs + RBAC + audit | **IMPLEMENTED** | roles seed, ACL, audit | Zero-membership fixed Phase 6 | P0 |
| Protocol / IEC approval tracking | Milestones + regulatory IEC submissions | **PARTIAL** | milestones `ethics_approval`, regulatory kind IEC | No separate protocol-document workflow | P1 |
| CTRI registration tracking | Regulatory CTRI TRACKING + milestone | **PARTIAL** | `/regulatory/.../ctri` | No external CTRI API | P1 |
| Site activation | Sites + study_sites activatedAt | **IMPLEMENTED** | sites/studySites APIs | — | — |
| Screening / enrolment | Participants statuses screened/enrolled | **IMPLEMENTED** | participants module | Randomization not modeled | P1 |
| Randomization against target | Enrollment current vs target only | **PARTIAL** | studies.enrollment* | No randomization arm/IWRS | P1 |
| Visit compliance | Milestone type monitoring_visit | **PARTIAL** | milestones + overdue alerts | No visit schedule / eCRF visits | P1 |
| Protocol-deviation compliance | protocol_deviations table + Quality module | **PARTIAL** | Phase 6 API/UI | Not full CAPA | P1 |
| Data-query / data-quality | data_queries table + Quality module | **PARTIAL** | Phase 6 API/UI | Not full CDMS query mgmt | P1 |
| Study milestones / timelines / close-out | Milestones + study status → completed/archived | **IMPLEMENTED** | milestones, study transitions | — | — |
| Real-time KPIs | DB aggregations (studies/AE/consent/reg) | **IMPLEMENTED** | `/studies/kpis` etc. | — | — |
| Configurable alerts | Computed alerts (rules fixed in code) | **PARTIAL** | `/alerts` | Not user-configurable rule engine | P1 |
| Enrolment-lag alert | Computed when enroll << target & recruiting | **IMPLEMENTED** | alerts Phase 6 | — | — |
| Ethics / CTRI due alerts | Pending ethics + overdue regulatory | **IMPLEMENTED** | alerts | — | — |
| Overdue monitoring visit alert | Milestone overdue | **IMPLEMENTED** | alerts | — | — |
| AE/ADR/SAE capture & route | AE workflow + escalate | **IMPLEMENTED** | AE module | ADR label alias only | — |
| Regulatory reporting timelines | reportingDueAt / authorityNotifiedAt | **PARTIAL** | AE fields + overdue alert | Not jurisdiction-specific NDCT clocks | P1 |
| MedDRA coding | MEDDRA_DEMO dictionary | **PROTOTYPE** | coding module | Official MedDRA unavailable | — |
| WHODrug coding | WHODRUG_DEMO dictionary | **PROTOTYPE** | coding module | Official WHODrug unavailable | — |
| Aggregate safety signals (DSMB/leadership) | AE KPIs + overdue reporting counts | **PARTIAL** | AE kpis | No DSMB workspace | P2 |
| CDASH | — | **NOT IMPLEMENTED** | — | Collection standard | P2 |
| SDTM | SDTM-like AE CSV transform | **PROTOTYPE** | `/exports/sdtm/ae` | Not CDISC certified | — |
| ADaM | Interface/docs only | **PROTOTYPE** | docs | No analysis dataset | — |
| Define-XML | — | **NOT IMPLEMENTED** | — | Submission package | P2 |
| FHIR R4 | ResearchStudy / ResearchSubject reads | **PROTOTYPE** | `/fhir/R4/*` | Limited resources | — |
| EDC / HIS / ABDM interop | Adapter status NOT_CONNECTED | **NOT IMPLEMENTED** | `/interop/adapters` | External systems | — |
```

**Heuristic extraction:** Table rows with SIH requirement → Claimed implementation → Actual evidence. Example rows (first 5):
# SIH26046 — Final Requirements Traceability

**Source of truth:** Official SIH Problem Statement ID **26046** (Ministry of Ayush / AIIA), as provided in the Phase 6 workspace brief.

**Product:** VEDRAYA CTMS prototype  
**Last updated:** 2026-09-29 (Phase 6)

Statuses: `IMPLEMENTED` | `PARTIAL` | `PROTOTYPE` | `MOCKED` | `NOT IMPLEMENTED` | `NOT APPLICABLE`

`IMPLEMENTED` requires (where applicable): UI → API → auth → RBAC/ACL → validation → business logic → PostgreSQL → audit → automated test. Missing layers → `PARTIAL` / `PROTOTYPE`.

---

## Exact PS requirements extracted

### Functional / product
1. Real-time, cloud-based CTMS + monitoring dashboard  
2. Single role-based, auditable portfolio view  
3. Per-study lifecycle: protocol & IEC approval, CTRI registration, site activation, screening, enrolment & randomization against target, visit & protocol-deviation compliance, data-query & data-quality status, milestones/timelines, close-out  
4. Real-time KPIs with configurable alerts (e.g. enrolment lag, ethics/CTRI due, overdue monitoring visit)  

**Evidence vs claim per task 21:** Use `analysis/nishant-uxs_vedraya/TRACEABILITY_ANALYSIS.md:1` + `REPO_ANALYSIS.md:21` matrix. Honest Implemented/Partial/Prototype/Not Connected table in `docs/IMPLEMENTATION_STATUS.md:1` 1.5KB lists what has code vs not.

## 4. Claimed Differentiators (from README)

- **Stated differentiator:** Auditable RBAC + study membership ACL (monitor AYU-024 only) + GLOBAL SHA-256 hash chain re-verify (not WORM) + honest prototype-only scope + PS traceability.
- **Architecture differentiator:** Modular monolith (not microservices), 14 domain modules, 5 Drizzle migrations, separate Vercel SPA vs Render API.

## 5. Evidence (what actually demonstrated)

- **Implemented (code):** Auth (Argon2, sid), RBAC 7 (`ROLE_DEFS`), ACL (`studyAccess.ts`), studies/sites/participants/milestones, KPIs, consent, audit chain verified (`api.audit.integrity.test.ts:1` tamper → valid:false, seed → valid:true), Command Center UI (`src/components/sections/CommandCenter.tsx`)
- **Partial:** Regulatory/CTRI/NDCT tracking internal, no external CTRI API
- **Prototype:** MedDRA_DEMO/WHODRUG_DEMO (not licensed), SDTM-like AE CSV, FHIR R4 ResearchStudy/Subject
- **Not Connected:** ABDM/HIS/EDC adapters
- **Not Implemented:** Licensed dictionaries, full CDISC, Define-XML, WORM, eSign, IWRS (per LIMITATIONS.md:1)
- **Tests:** Vitest 46/46 + Playwright 26/26 (most credible)

## 6. Technical/Security/Compliance Claims

- **Security claims:** Argon2, sid HttpOnly, CSRF double-submit, Helmet, Zod, rate limiting, RBAC, ACL — **IMPLEMENTED** (tested `api.auth.rbac.test.ts:1`)
- **Compliance claims:** Not claimed certified — explicitly says prototype only, needs validation (`README.md:1` disclaimer). **FACT vs CLAIM:** Do not conclude compliant.
- **Screenshots:** No standalone screenshots folder; 360 webp `public/vedraya/frames-alpha/` are cinematic landing frames (visual identity, not dashboard screenshots). Dashboard screenshots are seen live in Command Center after login, not as static assets.

## 7. What is Actually Demonstrated (60-sec)

Proves: login → RBAC (monitor/regulator ACL) → study dossier → AE escalate → audit verify → exports. Does not demonstrate: ABDM, licensed MedDRA, WORM, offline.

**Source files:** `docs/DEMO_SCRIPT.md:1`, `docs/JUDGE_QA.md:1`, `docs/SIH26046_TRACEABILITY_FINAL.md:1`, `docs/IMPLEMENTATION_STATUS.md:1`, `docs/RBAC.md:1` 3.6KB, `docs/SECURITY.md:1`, `e2e/ctms-critical-path.spec.ts:1` 11KB.
