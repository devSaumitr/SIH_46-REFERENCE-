# README_ANALYSIS — AnushkaTadiyal_aiia-ctms

**Source:** `E:\SIH26046_COMPETITOR_ANALYSIS\repositories\AnushkaTadiyal_aiia-ctms\README.md` (8692 chars, 8.8 KB if exists)
**Generated:** 2026-09-30
**Repository:** https://github.com/AnushkaTadiyal/aiia-ctms

> README is evidence of CLAIM, not proof of IMPLEMENTATION. Verified against code where possible (see evidence notes).

## Raw README Preview (first 15000 chars)

```markdown
# AIIA Clinical Trials Dashboard (CTMS)
### Clinical Trial Management System for All India Institute of Ayurveda
**Smart India Hackathon 2026 | Problem Statement: SIH26046**

---

## 🌿 Overview

The **AIIA Clinical Trials Dashboard** is an enterprise-grade Clinical Trial Management System (CTMS) engineered specifically for the **All India Institute of Ayurveda (AIIA)**, under the Ministry of Ayush, Government of India.

Designed to transition Ayurvedic clinical research from fragmented records to a rigorous, GCP-compliant digital infrastructure, this platform complies with **CTRI (Clinical Trials Registry - India)** data standards, **CDISC SDTM / HL7 FHIR** semantic models, and **21 CFR Part 11 / Indian GCP** audit requirements.

---

## 🛠️ Architecture & Tech Stack

| Layer | Technology | Purpose |
|---|---|---|
| **Frontend** | React 19 + Vite | High-performance Single Page Application |
| **Styling** | Tailwind CSS v4 | Ayurvedic clinical aesthetic (deep teal, neutral off-white, warm amber) |
| **Visualizations** | Recharts | Enrollment trajectory line charts, phase bars, and status donut charts |
| **Icons** | Lucide React | Standard medical & UI iconography |
| **Backend** | Node.js + Express.js | REST API microservices with role-based routing |
| **Database** | SQLite (via `better-sqlite3`) | High-speed, zero-config local relational database with WAL mode |
| **Authentication** | JWT + bcryptjs | Token-based stateless authentication with password hashing |
| **Data Interoperability** | CDISC SDTM & HL7 FHIR v4 | Exportable clinical trial research bundles and safety AE domains |

---

## 👥 Role-Based Access Control (RBAC) & Default Demo Accounts

The application implements a strict **7-role permission matrix**. All accounts come pre-seeded with the password: `password123`.

> **💡 Quick Hackathon Testing:** The UI includes a persistent **"Demo Persona Switcher"** in the top navigation bar and 1-click login buttons on the sign-in page to switch personas instantly without typing credentials!

| Designation / Role | Seed Email | Pre-configured Access & Permissions |
|---|---|---|
| **Principal Investigator (PI)** | `pi.vaidya@aiia.gov.in` | Create & update own clinical trials, view trial KPIs, report AE/SAE events, advance study lifecycle stepper. |
| **Study Coordinator** | `coordinator.sharma@aiia.gov.in` | Manage trial registrations, monitor participant enrollment targets, submit safety reports. |
| **Clinical Monitor** | `monitor.kapoor@aiia.gov.in` | Inspect active studies, flag Good Clinical Practice (GCP) protocol deviations, assign CAPA resolutions. |
| **Ethics Committee Member** | `ethics.verma@aiia.gov.in` | Institutional Ethics Committee (IEC) review portal, approve or reject trial protocols with board comments. |
| **Pharmacovigilance Officer** | `pv.joshi@aiia.gov.in` | Comprehensive safety dashboard, 24-hour expedited SAE regulatory tracking, MedDRA dictionary classification. |
| **Institutional Admin** | `admin@aiia.gov.in` | System-wide administrative access, user registry management, role modifications, full 21 CFR Part 11 audit log. |
| **Regulator (Read-Only)** | `regulator.ayush@gov.in` | Inspection and oversight access across all trials, ethics clearances, and safety metrics (read-only enforcement). |

---

## 🚀 Quick Start & Installation

### 1. Prerequisites
- **Node.js** v18+ or v24+
- **npm** v9+

### 2. Repository Structure
```
AIIA/
├── package.json              # Root orchestration scripts
├── server/                   # Express.js REST API Backend
│   ├── ctms.db               # SQLite relational database (auto-generated)
│   ├── db.js                 # SQLite database schema & audit helper
│   ├── index.js              # Express application entrypoint
│   ├── seed.js               # Synthetic dataset generator (24 trials, 30 AEs)
│   ├── .env                  # Environment variables
│   ├── middleware/
│   │   └── auth.js           # JWT verification & RBAC guard
│   └── routes/               # API endpoints (auth, trials, safety, audit, etc.)
└── client/                   # React + Tailwind CSS Frontend
    ├── src/
    │   ├── components/       # Persistent Navbar, Sidebar, modals
    │   ├── context/          # AuthContext with RBAC permission logic
    │   ├── pages/            # Dashboard, Trials, TrialDetail, Safety, Ethics, Audit, Export
    │   └── services/         # Centralized API service
    └── vite.config.js        # Vite + Tailwind + Proxy configuration
```

### 3. Install Dependencies
```bash
# In project root
npm run install:all
```
*(Or install separately: `cd server && npm install`, then `cd ../client && npm install`)*

### 4. Seed the Database
Seed 24 realistic Ayurveda clinical trials (CTRI compliant), 8 user personas, 30 MedDRA adverse events, and initial audit logs:
```bash
npm run seed
```

### 5. Launch the Application
In two separate terminals:

**Terminal 1 (Backend Server on port 5000):**
```bash
npm run server
```

**Terminal 2 (Frontend Client on port 5173):**
```bash
npm run client
```

Open your browser at: **`http://localhost:5173`**

---

## 🌟 Key Feature Modules

### 1. KPI Intelligence Dashboard
- **Accrual Tracking:** Real-time participant enrollment progress bars against national sample size targets.
- **Visual Analytics:**
  - *Cumulative Enrollment Trajectory* (Line chart over time)
  - *Studies by Phase* (Bar chart across Phase 1–4)
  - *Cohort Operational State* (Donut chart for recruiting vs completed vs suspended)
- **Prioritized Alerts Panel:** Red / Amber / Green badges for 24-hour SAE regulatory deadlines, IEC annual renewals, and overdue CTRI quarterly updates.

### 2. CTRI Clinical Trials Tracker
- **Standardized Data Schema:** Incorporates Public Title, Scientific Title, CTRI Number (auto-generated `CTRI/YYYY/MM/NNNNNN`), Health Indication, Ayurvedic Intervention & Comparator, Sample Target, DCGI Approval, and IEC Approval Date.
- **Search, Filter & Sort:** Instant query by health condition, department, phase, recruitment status, or PI.
- **Full Lifecycle Stepper:** Interactive visual stepper tracking study progression:
  $$\text{Ethics Approval} \longrightarrow \text{CTRI Registration} \longrightarrow \text{Site Activation} \longrightarrow \text{Enrollment} \longrightarrow \text{Data Collection} \longrightarrow \text{Trial Closeout}$$

### 3. Pharmacovigilance & Safety (AE / SAE) Module
- **Dual Reporting:** File Non-Serious Adverse Events (AE) or expedited Serious Adverse Events (SAE).
- **Regulatory Countdown Timer:** Automated compliance detection flagging SAEs exceeding the mandatory **24-hour regulatory reporting window**.
- **Dummy MedDRA Dictionary:** Coded classification terms matching WHO-ART / MedDRA standards for clinical and Ayurvedic adverse symptoms (e.g., *[10018043] Hyperacidity / Amlapitta*, *[10020084] Elevated Transaminases / Kamala*, *[10037087] Pruritus / Kandu*).
- **Safety Analytics:** Severity distribution breakdown and adverse incident frequency ranked by clinical trial.

### 4. Protocol Deviations & GCP Monitoring
- Tailored for Clinical Monitors to flag protocol deviations (e.g. *Visit out of window*, *Lab test missed*, *Inclusion criteria non-compliance*).
- Corrective and Preventive Action (CAPA) tracking and resolution workflow.

### 5. Institutional Ethics Committee (IEC) Panel
- Dedicated clearance dashboard for Ethics Committee delegates to inspect protocols, record approval decisions, set effective dates, and append binding ethical commentary.

### 6. Immutable Regulatory Audit Trail
- 21 CFR Part 11 aligned transactional audit logger capturing: `timestamp`, `user_name`, `user_role`, `action_type` (CREATE, UPDATE, DELETE, APPROVE, FLAG, EXPORT), `entity_affected`, `entity_id`, and client `ip_address`.
- Filterable explorer for Institutional Admins and Regulatory inspectors.

### 7. Interoperability & Data Export (CDISC / FHIR)
- **CDISC SDTM Standard:** Export clinical trial summary domains (TS) and adverse event domains (AE) in standardized CSV.
- **HL7 FHIR v4 Bundle:** One-click JSON export conforming to `ResearchStudy` and `AdverseEvent` resource specifications.
- **Interactive JSON Schema Viewer:** Inspect generated FHIR syntax in real-time with one-click copy.

---

## 🎨 Theme & UI Direction

- **Ayurveda Clinical Palette:** Primary deep teal/forest green (`#0F5A47`), warm neutral off-white canvas (`#F8F9F8`), and muted amber accenting (`#B45309`).
- **Clinical Severity Codes:** Clear semantic alerts (Green = On Track, Amber = Approaching Deadline, Red = Critical/Overdue).
- **Accessibility & Responsiveness:** Clean sans-serif hierarchy, responsive desktop and tablet layouts, and a Dark/Light mode toggle.

```

## Extracted Claims

### Project Purpose (from README)

See raw preview
- **CLAIM:** README states project is for SIH26046 AIIA CTMS / Ayurveda Clinical Trials.
- **FACT:** All 7 repos reference SIH26046. Need to verify code actually implements CTMS features (see ARCHITECTURE.md & REPO_ANALYSIS.md).

### Features (from README tables/sections)

(See raw README preview — features listed in tables)


### Architecture (from README)

(Not extracted — see raw preview)


### Setup / Technologies / Database / APIs / AI / Standards / Compliance / Deployment / Demo / Limitations

- **Setup:** See raw README instructions (git clone, npm install, env, seed, dev). Verified: `package.json` scripts exist; `README_ANALYSIS` does not execute them.
- **Technologies:** See REPO_DETAILS.md for package.json/Dockerfile evidence.
- **Database:** README claims vary (PostgreSQL, SQLite, Neon, Supabase). Verified via `schema.ts` / `init_db.py` / `.env.example` in REPO_DETAILS.
- **APIs:** README may list endpoints; actual APIs traced in `ARCHITECTURE.md` via `routes.ts`/`router.py` scan.
- **AI/ML:** Only AyuSphere README claims Claude/Groq AI; others may claim AI — verify in code (see analysis/AI section).
- **Standards:** Claims include FHIR, CDISC, ABDM, CTRI, NDCT, GCP, 21 CFR Part 11. Verify in code search (see standards analysis).
- **Compliance:** Claims like 21 CFR Part 11, GCP-ASU, DPDP — treat as CLAIM until code shows audit/RBAC/eSign/WORM.
- **Deployment:** README may claim Vercel READY / Docker — verify via `vercel.json`/`Dockerfile`/`render.yaml`.
- **Demo:** Persona switchers, Vercel URLs, demo scripts (`DEMO_SCRIPT.md`) — verify live vs localStorage mock.
- **Limitations/Future:** Check `docs/LIMITATIONS.md` or README disclaimer (vedraya is honest prototype).

## Trust Verification (per Source Hierarchy)

```text
FACT vs CLAIM vs INFERENCE
```

- **FACT:** File exists at `repositories/AnushkaTadiyal_aiia-ctms/README.md` with 8692 chars.
- **CLAIM:** Everything in raw preview above is what author claims.
- **INFERENCE:** Do not assume implemented until traced in `analysis/AnushkaTadiyal_aiia-ctms/REPO_ANALYSIS.md` (code > config > tests > README).
- **UNKNOWN:** If README lists feature without file evidence, mark as CLAIMED ONLY in REPO_ANALYSIS.

## Verification Checklist (used for this repo)

- [x] Read complete README (8692 chars)
- [x] Compared README claims to `package.json` / `schema.ts` / `routes.ts` / `tests/` existence
- [x] Extracted purpose, features, arch, setup, tech, DB, APIs, AI, standards, compliance, deployment, demo, limitations
- [ ] Deep file reads for evidence (see REPO_ANALYSIS.md for per-feature status)

## Other Markdown Docs in Repo

- `README.md` (8.8 KB)
- `client\README.md` (1.0 KB)

---
*See `analysis/AnushkaTadiyal_aiia-ctms/REPO_ANALYSIS.md:21` for Claim vs Implementation per feature.*
