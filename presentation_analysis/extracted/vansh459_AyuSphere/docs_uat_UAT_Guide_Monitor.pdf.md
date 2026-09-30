# PDF Extraction — docs\uat\UAT_Guide_Monitor.pdf

**Repository:** `vansh459_AyuSphere`
**File:** `docs\uat\UAT_Guide_Monitor.pdf`
**Size:** 667.3 KB (683346 bytes)
**Pages:** 5
**Source:** `repositories/vansh459_AyuSphere/docs\uat\UAT_Guide_Monitor.pdf`
**Generated:** 2026-09-30 (pypdf <pypdf._reader.PdfReader object at 0x0000022A30BBE9E0> )

---

## Summary (heuristic)

- **Pages:** 5
- **Extraction method:** pypdf text extraction (preserves page numbers, headings inferred via line case)

## Page 1 / 5

> **Visual:** Page contains embedded images/screenshots/diagrams (detected via XObject/Image). See original PDF for rendering.

**Important claims (keyword hits):**
- `data is synthetic/de-identified; trials are real public CTRI registry records.`
- `AyuSphere — AI-assisted Clinical Research Intelligence Platform for Ayurveda (SIH26046). All participant`

**Extracted Text (Page 1):**

```text
AyuSphere · UAT Guide
Monitor
AyuSphere — AI-assisted Clinical Research Intelligence Platform for Ayurveda (SIH26046). All participant
data is synthetic/de-identified; trials are real public CTRI registry records.
Problem statement SIH26046 · Ministry of Ayush · All India Institute of Ayurveda
Live demo: https://ayusphere-three.vercel.app
Sign in as: monitor@aiia.demo  · password Demo@1234
Generated 14 September 2026 from the application's living knowledge base — click paths in this guide are
the exact labels in the product and are drift-guard tested against the navigation and permission matrix.
```

---

## Page 2 / 5

> **Visual:** Page contains embedded images/screenshots/diagrams (detected via XObject/Image). See original PDF for rendering.

**Important claims (keyword hits):**
- `use the AI Copilot or exports`
- `delete or edit audit-trail entries — the audit`

**Extracted Text (Page 2):**

```text
1 · Your workspace
The dark green sidebar on the left lists every screen your role can access, grouped into sections (Overview,
Study Conduct, Data Capture, Safety & Quality, Intelligence, System) when the list is long. On phones, the
sidebar becomes a menu button ( ☰ ) in the top bar that opens the same navigation as a drawer. The top bar
also has a quick search (type 2+ letters to jump to a screen, a trial by protocol code, or a participant by
subject code — Enter opens the first match), a bell icon showing open alerts (click it to open Alerts if your
role has it), and your profile chip.
Dashboard · Messages · Monitoring · Alerts
Dashboard
2 · What you can and cannot do
You can
schedule and complete monitoring visits (the
due-date cadence is admin-configurable)
raise and close data queries on CRF entries —
an open query blocks approval
view monitoring analytics and data-quality
findings
acknowledge alerts
You cannot
enter or approve CRFs, answer data queries,
enrol participants, or edit trials — those
belong to the PI/Coordinator
use the AI Copilot or exports
delete or edit audit-trail entries — the audit
log is append-only for everyone, including
admins
```

---

## Page 3 / 5

> **Visual:** Page contains embedded images/screenshots/diagrams (detected via XObject/Image). See original PDF for rendering.

**Extracted Text (Page 3):**

```text
message any user
3 · Core workflows (exact click paths)
Log a monitoring visit
1. Go to Monitoring — the 'Monitoring visits' card lists every activated trial-site with its due date
2. Pick the trial site and a date, click Schedule monitoring visit; after the visit, fill the summary (and
findings, one per line) and click Complete visit — the site's next due date advances by the configured
cadence and any overdue alert auto-resolves
Raise and close data queries
1. On Monitoring, the 'Data queries' card shows open/answered/closed counts and median cycle time
2. Pick the CRF entry, type the question and click Raise query — the entry CANNOT be approved until the
data-entry team answers it
3. Once answered, click Close query (optionally with a resolution note)
Review site performance and data quality
1. Monitoring also shows, per active trial: per-site recruitment bars, open data-quality findings (duplicates,
impossible values, missing assessments) and deviation alerts
Work the alert queue
1. Go to Alerts, review overdue-visit / deviation / data-quality / monitoring-overdue items and click
Acknowledge on the ones you own
4 · Screens
```

---

## Page 4 / 5

> **Visual:** Page contains embedded images/screenshots/diagrams (detected via XObject/Image). See original PDF for rendering.

**Extracted Text (Page 4):**

```text
Messages
Monitoring
```

---

## Page 5 / 5

> **Visual:** Page contains embedded images/screenshots/diagrams (detected via XObject/Image). See original PDF for rendering.

**Important claims (keyword hits):**
- `CTRI registry records.`
- `AyuSphere · SIH26046 · Monitor UAT guide · generated 14 September 2026 · all participant data synthetic (DPDP), trials a`

**Extracted Text (Page 5):**

```text
Alerts
5 · New in this build
Monitoring visits — schedule and complete site visits; the due date advances by the configured
cadence and overdue sites raise alerts
Data queries — raise a query on any CRF entry (blocks its approval), close it when resolved; cycle-time
stats on the page
Tailored dashboard — site due dates and open queries lead the page
Sphera guide with memory, quick-search, mobile drawer, live badges
How this role scores in evaluation: Axis 1 (data accuracy & integrity): data queries + quality findings.
Axis 4: monitoring oversight trail.
AyuSphere · SIH26046 · Monitor UAT guide · generated 14 September 2026 · all participant data synthetic (DPDP), trials are public
CTRI registry records.
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
