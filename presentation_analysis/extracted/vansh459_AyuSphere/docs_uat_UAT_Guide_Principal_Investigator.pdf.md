# PDF Extraction — docs\uat\UAT_Guide_Principal_Investigator.pdf

**Repository:** `vansh459_AyuSphere`
**File:** `docs\uat\UAT_Guide_Principal_Investigator.pdf`
**Size:** 2894.5 KB (2963941 bytes)
**Pages:** 13
**Source:** `repositories/vansh459_AyuSphere/docs\uat\UAT_Guide_Principal_Investigator.pdf`
**Generated:** 2026-09-30 (pypdf <pypdf._reader.PdfReader object at 0x0000022A30BE6BE0> )

---

## Summary (heuristic)

- **Pages:** 13
- **Extraction method:** pypdf text extraction (preserves page numbers, headings inferred via line case)

## Page 1 / 13

> **Visual:** Page contains embedded images/screenshots/diagrams (detected via XObject/Image). See original PDF for rendering.

**Important claims (keyword hits):**
- `data is synthetic/de-identified; trials are real public CTRI registry records.`
- `AyuSphere — AI-assisted Clinical Research Intelligence Platform for Ayurveda (SIH26046). All participant`

**Extracted Text (Page 1):**

```text
AyuSphere · UAT Guide
Principal Investigator
AyuSphere — AI-assisted Clinical Research Intelligence Platform for Ayurveda (SIH26046). All participant
data is synthetic/de-identified; trials are real public CTRI registry records.
Problem statement SIH26046 · Ministry of Ayush · All India Institute of Ayurveda
Live demo: https://ayusphere-three.vercel.app
Sign in as: pi@aiia.demo  · password Demo@1234
Generated 14 September 2026 from the application's living knowledge base — click paths in this guide are
the exact labels in the product and are drift-guard tested against the navigation and permission matrix.
```

---

## Page 2 / 13

> **Visual:** Page contains embedded images/screenshots/diagrams (detected via XObject/Image). See original PDF for rendering.

**Headings (heuristic):**
- `OVERVIEW`
- `STUDY CONDUCT`

**Important claims (keyword hits):**
- `AI Assistant · Reports & Exports`

**Extracted Text (Page 2):**

```text
1 · Your workspace
The dark green sidebar on the left lists every screen your role can access, grouped into sections (Overview,
Study Conduct, Data Capture, Safety & Quality, Intelligence, System) when the list is long. On phones, the
sidebar becomes a menu button ( ☰ ) in the top bar that opens the same navigation as a drawer. The top bar
also has a quick search (type 2+ letters to jump to a screen, a trial by protocol code, or a participant by
subject code — Enter opens the first match), a bell icon showing open alerts (click it to open Alerts if your
role has it), and your profile chip.
OVERVIEW
Dashboard · Messages
STUDY CONDUCT
Clinical Trials · Participants · Site Management · Visit Schedule
DATA CAPTURE
Data Entry (eCRF) · Extractions · Documents
SAFETY & QUALITY
Adverse Events · Alerts
INTELLIGENCE
AI Assistant · Reports & Exports
Dashboard
2 · What you can and cannot do
```

---

## Page 3 / 13

> **Visual:** Page contains embedded images/screenshots/diagrams (detected via XObject/Image). See original PDF for rendering.

**Important claims (keyword hits):**
- `5. After approval, enter the CTRI number and click Record CTRI registration, attach & activate a site under`
- `capture adverse events and use the AI Copilot`
- `delete or edit audit-trail entries — the audit`
- `run the pharmacovigilance review walk (mark`

**Extracted Text (Page 3):**

```text
You can
create/edit trials and run lifecycle steps
(except the ethics decision itself)
manage sites, participants, visits and
documents
enter CRFs and APPROVE CRF entries and
note extractions
capture adverse events and use the AI Copilot
and exports
You cannot
approve or return an ethics review — only the
Ethics Committee (or Admin) decides that
run the pharmacovigilance review walk (mark
AEs reported/closed) — that's the
Pharmacovigilance role (or Admin)
manage user accounts or the AI model
settings — Admin only
delete or edit audit-trail entries — the audit
log is append-only for everyone, including
admins
3 · Core workflows (exact click paths)
Create a new trial and take it through the lifecycle
1. Go to Clinical Trials, click New Trial
2. Fill protocol code, title, intervention, target enrolment and at least one visit-plan row, then click Create
trial
3. Upload the protocol first: Documents → pick the trial → Kind Protocol → choose file → Upload (ethics
submission is gated on this)
4. On the trial page click Submit for ethics review — the Ethics Committee approves it on their side
5. After approval, enter the CTRI number and click Record CTRI registration, attach & activate a site under
Site Management, then click Activate trial
Enrol a participant
1. Go to Participants, choose the active trial · site, click Add (code auto-generated) — the subject code is
created for you, no personal data is entered
2. On the new row click Pass screening, then Record consent — consent binds the trial's current consent-
form version (a trial with no consent form on file refuses consent)
3. Click Enrol & randomize — the arm is assigned by permuted-block randomization (no manual choice)
and the protocol visit schedule is generated automatically
Amend an active protocol (IEC oversight)
1. Open the trial page — the Protocol amendments card shows the current protocol version
2. Describe the change in Amendment summary and click Submit to Ethics; the Ethics Committee
approves or returns it with a comment
3. Once approved, the protocol change (visit plan / arms) can be applied — it consumes the amendment
and bumps the protocol version
Answer a monitor's data query
1. Open the visit under Visit Schedule — an entry with an open query shows the monitor's question and
"approval is blocked until this query is answered"
```

---

## Page 4 / 13

> **Visual:** Page contains embedded images/screenshots/diagrams (detected via XObject/Image). See original PDF for rendering.

**Headings (heuristic):**
- `1. Go to Visit Schedule, click the participant's visit`

**Important claims (keyword hits):**
- `1. Go to Reports & Exports, pick a trial, download FHIR R4 Bundle, SDTM DM (CSV), SDTM AE (CSV),`
- `1. Go to Reports & Exports, pick a trial, download FHIR R4 Bundle, SDTM DM (CSV), SDTM AE (CSV),`
- `Scan a doctor note into the CRF (AI OCR)`
- `ADaM ADSL (CSV) or Define-XML (variable-level metadata) — every export is recorded in the audit`

**Extracted Text (Page 4):**

```text
2. Type the answer and click Answer; approval unlocks once answered, and the monitor closes the query
on their side
Capture a visit CRF manually
1. Go to Visit Schedule, click the participant's visit
2. Fill the e-CRF fields (plausible ranges are shown under each field) and click Save & submit for approval
3. On the submitted entry, enter your password and click Sign & approve — approval is an electronic
signature (your password is re-verified and a SHA-256 hash of the record is stored); then Mark visit
completed
Scan a doctor note into the CRF (AI OCR)
1. Go to Data Entry (eCRF), choose the participant visit, click Note photo and pick the photo (large phone
photos are auto-compressed)
2. Click Extract to CRF draft — the AI (Gemini) reads the note and shows every field with a confidence
badge next to the original image
3. Fields marked confirm (low confidence or contradicting an earlier approved record) must be
clicked/edited before approval unlocks
4. Click Approve as record — an official CRF entry is created with full provenance; see it under the visit's
Entries and in Extractions
Watch safety deadlines
1. Adverse Events → the Open AEs tab lists open AE/SAE sorted by reporting deadline with a live
countdown clock (amber under 24h, red under 6h)
2. To record a new event, switch to the Capture tab and use the MedDRA/WHODrug pickers; the Safety
Signals tab shows term×trial clusters and the DSMB summary link
3. Open Alerts to acknowledge deadline, enrolment-lag, overdue-visit and deviation alerts
Ask the clinical AI Copilot
1. Go to AI Assistant, ask e.g. "Which sites are behind target?" — every answer cites the underlying
records; with no supporting records it declines rather than guessing
Export submission-ready data
1. Go to Reports & Exports, pick a trial, download FHIR R4 Bundle, SDTM DM (CSV), SDTM AE (CSV),
ADaM ADSL (CSV) or Define-XML (variable-level metadata) — every export is recorded in the audit
trail
2. Systems can also pull live FHIR from the API (audited), and inbound Observation bundles land as DRAFT
CRF entries — nothing imported auto-commits
4 · Screens
```

---

## Page 5 / 13

> **Visual:** Page contains embedded images/screenshots/diagrams (detected via XObject/Image). See original PDF for rendering.

**Extracted Text (Page 5):**

```text
Messages
Clinical Trials
```

---

## Page 6 / 13

> **Visual:** Page contains embedded images/screenshots/diagrams (detected via XObject/Image). See original PDF for rendering.

**Extracted Text (Page 6):**

```text
Participants
Site Management
```

---

## Page 7 / 13

> **Visual:** Page contains embedded images/screenshots/diagrams (detected via XObject/Image). See original PDF for rendering.

**Extracted Text (Page 7):**

```text
Visit Schedule
Data Entry (eCRF)
```

---

## Page 8 / 13

> **Visual:** Page contains embedded images/screenshots/diagrams (detected via XObject/Image). See original PDF for rendering.

**Extracted Text (Page 8):**

```text
Extractions
Documents
```

---

## Page 9 / 13

> **Visual:** Page contains embedded images/screenshots/diagrams (detected via XObject/Image). See original PDF for rendering.

**Extracted Text (Page 9):**

```text
Adverse Events
Alerts
```

---

## Page 10 / 13

> **Visual:** Page contains embedded images/screenshots/diagrams (detected via XObject/Image). See original PDF for rendering.

**Important claims (keyword hits):**
- `AI Assistant`

**Extracted Text (Page 10):**

```text
AI Assistant
Reports & Exports
```

---

## Page 11 / 13

> **Visual:** Page contains embedded images/screenshots/diagrams (detected via XObject/Image). See original PDF for rendering.

**Extracted Text (Page 11):**

```text
Adverse Events — Capture tab (MedDRA/WHODrug pickers)
Quick search — jump to any screen, trial or participant
```

---

## Page 12 / 13

> **Visual:** Page contains embedded images/screenshots/diagrams (detected via XObject/Image). See original PDF for rendering.

**Extracted Text (Page 12):**

```text
Trial detail — lifecycle, KPIs, consent register, protocol amendments
Sphera — the role-aware guide (persistent memory across sessions)
```

---

## Page 13 / 13

> **Visual:** Page contains embedded images/screenshots/diagrams (detected via XObject/Image). See original PDF for rendering.

**Important claims (keyword hits):**
- `stores a SHA-256 hash of the record (GCP e-sign)`
- `Exports grew — real Define-XML (variable-level metadata), ADaM ADSL, and a live audited FHIR API`
- `are public CTRI registry records.`
- `AyuSphere · SIH26046 · Principal Investigator UAT guide · generated 14 September 2026 · all participant data synthetic (`

**Extracted Text (Page 13):**

```text
5 · New in this build
Electronic signatures — approving a CRF, an extraction, or a correction re-verifies your password and
stores a SHA-256 hash of the record (GCP e-sign)
Enrol & randomize — arms are assigned by permuted-block randomization; manual arm choice is gone
Protocol amendments — changing a running trial's visit plan/arms now requires an IEC-approved
amendment (trial page card)
Consent register — consent binds the consent-form version signed; a new form version flags re-
consent per participant
Data queries — a monitor's open query blocks entry approval until you answer it on the visit page
Adverse Events tabs — Open AEs / Capture (MedDRA & WHODrug pickers) / Safety Signals / and the
DSMB summary
Exports grew — real Define-XML (variable-level metadata), ADaM ADSL, and a live audited FHIR API
Tailored dashboard — your signing queue, open queries and visits lead the page
Sphera guide with memory — the leaf orb remembers your conversation across refreshes and devices
Grouped sidebar sections, working quick-search, mobile navigation drawer, live unread badges
How this role scores in evaluation: Axis 1 (data accuracy & integrity): template-validated CRFs,
signed approvals, versioned corrections. Axis 3 (interoperability): the exports you run.
AyuSphere · SIH26046 · Principal Investigator UAT guide · generated 14 September 2026 · all participant data synthetic (DPDP), trials
are public CTRI registry records.
```

---

## Diagrams / Screenshots / Visuals Summary

- If pages contained /Image XObject, those are likely screenshots/diagrams (see per-page Visual note).
- Architecture diagrams: search for headings containing 'Architecture' per page above.
- Workflow diagrams: search for 'workflow'/'flow' per page.
- Tables are heuristically extracted above (pipe/multi-space).

## Limitations

- Text extraction via pypdf preserves text but not layout; scanned image-only pages would show empty text (marked).
- If `TEXT EXTRACTION INCOMPLETE` or empty page text, original PDF is image-based; visual inspection needed.
- For headings/tables, heuristic only — not definitive.
