# Demo Script Analysis — nishant-uxs_vedraya

**Repository:** `nishant-uxs_vedraya`
**Generated:** 2026-09-30

**Demo files found:** 2
- `docs\DEMO_SCRIPT.md` (3.0 KB)
- `docs\DEMO_SCRIPT.md` (3.0 KB)

---

## File: `docs\DEMO_SCRIPT.md`

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

### Analysis (heuristic)

- **Opening (what shown first):** Enter Live Command Center after opening app → login admin@vedraya.demo (per vedraya docs/DEMO_SCRIPT.md:1)
- **Problem framing:** Frames SIH26046 Ministry of Ayush / AIIA problem statement
- **Workflow steps detected:** 0 numbered steps
- **Feature sequence keywords:** Regulatory, Study, KPI, SAE, Consent, AE, Participant
- **Differentiator (explicit):** GLOBAL SHA-256 hash chain re-verify (vedraya differentiator)
- **Evidence shown:** See file content above — steps with exact click paths (e.g., Go to Settings → AI Model)
- **Closing:** Unknown

---

## File: `docs\DEMO_SCRIPT.md`

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

### Analysis (heuristic)

- **Opening (what shown first):** Enter Live Command Center after opening app → login admin@vedraya.demo (per vedraya docs/DEMO_SCRIPT.md:1)
- **Problem framing:** Frames SIH26046 Ministry of Ayush / AIIA problem statement
- **Workflow steps detected:** 0 numbered steps
- **Feature sequence keywords:** Regulatory, Study, KPI, SAE, Consent, AE, Participant
- **Differentiator (explicit):** GLOBAL SHA-256 hash chain re-verify (vedraya differentiator)
- **Evidence shown:** See file content above — steps with exact click paths (e.g., Go to Settings → AI Model)
- **Closing:** Unknown

---

