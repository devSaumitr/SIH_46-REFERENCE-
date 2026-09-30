# PDF Extraction — docs\uat\Judge_Demo_Script.pdf

**Repository:** `vansh459_AyuSphere`
**File:** `docs\uat\Judge_Demo_Script.pdf`
**Size:** 1343.6 KB (1375869 bytes)
**Pages:** 10
**Source:** `repositories/vansh459_AyuSphere/docs\uat\Judge_Demo_Script.pdf`
**Generated:** 2026-09-30 (pypdf <pypdf._reader.PdfReader object at 0x0000022A2D9C96A0> )

---

## Summary (heuristic)

- **Pages:** 10
- **Extraction method:** pypdf text extraction (preserves page numbers, headings inferred via line case)

## Page 1 / 10

> **Visual:** Page contains embedded images/screenshots/diagrams (detected via XObject/Image). See original PDF for rendering.

**Important claims (keyword hits):**
- `data is synthetic/de-identified; trials are real public CTRI registry records.`
- `AyuSphere — AI-assisted Clinical Research Intelligence Platform for Ayurveda (SIH26046). All participant`
- `reporting · interoperability conformance · access-control & audit completeness`

**Extracted Text (Page 1):**

```text
AyuSphere · Judge Demo Script
The 8-minute storyline — mapped to the four evaluation axes
AyuSphere — AI-assisted Clinical Research Intelligence Platform for Ayurveda (SIH26046). All participant
data is synthetic/de-identified; trials are real public CTRI registry records.
Problem statement SIH26046 · evaluated on: data accuracy & integrity · timeliness of safety & regulatory
reporting · interoperability conformance · access-control & audit completeness
Live demo: https://ayusphere-three.vercel.app  · every role signs in with password
Demo@1234
pi@ · coordinator@ · monitor@ · ethics@ · pv@ · admin@ · regulator@ — all aiia.demo
Generated 14 September 2026. Each step names the login, the exact clicks, the line to say, and the axis it
scores.
```

---

## Page 2 / 10

> **Visual:** Page contains embedded images/screenshots/diagrams (detected via XObject/Image). See original PDF for rendering.

**Important claims (keyword hits):**
- `2. Enter your password and click Sign & approve — a GCP electronic signature: password re-verified, SHA-`
- `Say: Approval is not a click — it is a signature. The hash lands in the immutable audit trail.`

**Extracted Text (Page 2):**

```text
0:00 — PI  Axis 4 · access control
1. Sign in as pi@aiia.demo — the dashboard is role-tailored: signing queue, open data queries, due visits
2. Click the leaf orb — Sphera greets by name and role (it remembers past conversations)
Say: Seven enforced roles, each with its own dashboard. Even the in-app guide only knows THIS role's screens.
PI — live screen
1:00 — PI  Axis 1 · data integrity
1. Visit Schedule → open a due visit → fill the e-CRF (ranges enforced) → Save & submit for approval
2. Enter your password and click Sign & approve — a GCP electronic signature: password re-verified, SHA-
256 hash of the record stored
Say: Approval is not a click — it is a signature. The hash lands in the immutable audit trail.
```

---

## Page 3 / 10

> **Visual:** Page contains embedded images/screenshots/diagrams (detected via XObject/Image). See original PDF for rendering.

**Important claims (keyword hits):**
- `Say: Coded to MedDRA and WHODrug demo dictionaries; the NDCT-style deadline clock starts at capture —`

**Extracted Text (Page 3):**

```text
PI — live screen
2:30 — PI  Axis 2 · safety timeliness
1. Adverse Events → Capture tab → pick the participant, type 'Nausea' (MedDRA picker auto-codes it),
suspected formulation 'Ashwagandha churna' (WHODrug picker), seriousness SAE → Capture
2. The Open AEs tab shows the new SAE with its escalation clock already counting down
Say: Coded to MedDRA and WHODrug demo dictionaries; the NDCT-style deadline clock starts at capture —
and the rules are admin-configurable, not hard-coded.
```

---

## Page 4 / 10

> **Visual:** Page contains embedded images/screenshots/diagrams (detected via XObject/Image). See original PDF for rendering.

**Headings (heuristic):**
- `1. Switch to pv@aiia.demo — the safety dashboard sorts by deadline proximity`

**Important claims (keyword hits):**
- `Say: AIIA hosts the National Pharmacovigilance Coordination Centre — this is that role, end to end, with`
- `the NPvCC ADRs tab takes spontaneous reports`

**Extracted Text (Page 4):**

```text
PI — live screen
3:30 — PV  Axis 2 · safety timeliness
1. Switch to pv@aiia.demo — the safety dashboard sorts by deadline proximity
2. Start PV review → Sign & mark reported (another e-signature) → Generate regulatory report — the
printable CIOMS-style summary with the full escalation timeline and deadline compliance
3. Safety Signals tab → term×trial disproportionality flags → Full DSMB summary (printable board pack);
the NPvCC ADRs tab takes spontaneous reports
Say: AIIA hosts the National Pharmacovigilance Coordination Centre — this is that role, end to end, with
artifacts a regulator can hold.
```

---

## Page 5 / 10

> **Visual:** Page contains embedded images/screenshots/diagrams (detected via XObject/Image). See original PDF for rendering.

**Important claims (keyword hits):**
- `1. Reports & Exports → download the FHIR R4 Bundle, SDTM DM/AE, ADaM ADSL and Define-XML`
- `Say: CDISC and FHIR are not slideware here — every artifact opens, and the API is live and audited.`
- `1. Reports & Exports → download the FHIR R4 Bundle, SDTM DM/AE, ADaM ADSL and Define-XML`

**Extracted Text (Page 5):**

```text
PV — live screen
5:00 — PI  Axis 3 · interoperability
1. Reports & Exports → download the FHIR R4 Bundle, SDTM DM/AE, ADaM ADSL and Define-XML
(real variable-level metadata)
2. Show the live API: GET /api/fhir/Bundle/[trialId] returns application/fhir+json; inbound Observation
bundles land as DRAFT CRFs — nothing imported auto-commits
Say: CDISC and FHIR are not slideware here — every artifact opens, and the API is live and audited.
```

---

## Page 6 / 10

> **Visual:** Page contains embedded images/screenshots/diagrams (detected via XObject/Image). See original PDF for rendering.

**Extracted Text (Page 6):**

```text
PI — live screen
6:00 — Ethics  Axis 4 · access control
1. Switch to ethics@aiia.demo — the amendment queue lists protocol changes awaiting IEC decision
2. Return one (a comment is REQUIRED) or Approve — running-trial protocol changes stay blocked until
approval
Say: IEC oversight covers amendments, not just first approval — the protocol version bumps only through this
gate.
```

---

## Page 7 / 10

> **Visual:** Page contains embedded images/screenshots/diagrams (detected via XObject/Image). See original PDF for rendering.

**Headings (heuristic):**
- `1. Switch to regulator@aiia.demo — read-only everywhere, three screens only`

**Important claims (keyword hits):**
- `7:00 — Regulator  Axis 4 · audit completeness`

**Extracted Text (Page 7):**

```text
Ethics — live screen
7:00 — Regulator  Axis 4 · audit completeness
1. Switch to regulator@aiia.demo — read-only everywhere, three screens only
2. Audit Trail → filter to the CRF entry approved in minute 1 — the row shows the approver, before/after,
timestamp AND the e-signature hash
Say: ALCOA+ made literal: append-only at the database, every approval attributable and hash-sealed.
```

---

## Page 8 / 10

> **Visual:** Page contains embedded images/screenshots/diagrams (detected via XObject/Image). See original PDF for rendering.

**Important claims (keyword hits):**
- `1. Closers: quick-search 'CTRI' jumps to a real registry trial; the app works on a phone (drawer navigation);`
- `Say: Real CTRI trials, synthetic participants only — DPDP by schema. Everything you saw is test-gated: 297`

**Extracted Text (Page 8):**

```text
Regulator — live screen
7:45 — Any  All axes
1. Closers: quick-search 'CTRI' jumps to a real registry trial; the app works on a phone (drawer navigation);
ask Sphera "what did I ask you earlier?" — it remembers
Say: Real CTRI trials, synthetic participants only — DPDP by schema. Everything you saw is test-gated: 297
automated tests.
```

---

## Page 9 / 10

> **Visual:** Page contains embedded images/screenshots/diagrams (detected via XObject/Image). See original PDF for rendering.

**Extracted Text (Page 9):**

```text

```

---

## Page 10 / 10

> **Visual:** Page contains embedded images/screenshots/diagrams (detected via XObject/Image). See original PDF for rendering.

**Extracted Text (Page 10):**

```text
Any — live screen
AyuSphere · SIH26046 · Judge demo script · generated 14 September 2026.
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
