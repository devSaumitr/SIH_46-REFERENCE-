# README_ANALYSIS — aravindakrishna-c_AIIA-Clinical-Trial-Dashboard

**Source:** `E:\SIH26046_COMPETITOR_ANALYSIS\repositories\aravindakrishna-c_AIIA-Clinical-Trial-Dashboard\README.md` (8528 chars, 9.1 KB if exists)
**Generated:** 2026-09-30
**Repository:** https://github.com/aravindakrishna-c/AIIA-Clinical-Trial-Dashboard

> README is evidence of CLAIM, not proof of IMPLEMENTATION. Verified against code where possible (see evidence notes).

## Raw README Preview (first 15000 chars)

```markdown
# PS SIH26046 — AIIA Clinical Trials Dashboard (Phase 1)

**Organization:** Ministry of Ayush  
**Institution:** All India Institute of Ayurveda (AIIA)  
**Problem Statement:** PS SIH26046 — Real-time, cloud-based, GCP-compliant Clinical Trial Management System (CTMS) for Ayurveda research with role-based access control and immutable audit logging.

---

## Phase 1 Overview

Phase 1 establishes the foundational, enterprise-grade architecture for the AIIA Clinical Trials Management System:
- **Authentication & Security:** Argon2 / bcrypt password hashing, signed JWT Bearer access tokens, sanitized error handlers without internal stack leaks.
- **Role-Based Access Control (RBAC):** 7 system roles, fine-grained permission checks, backend route protection (`require_role`, `require_permission`), client-side `RoleGuard`, and automatic 403 Forbidden enforcement.
- **User Management:** Admin-only user directory with search, role assignment, instant password hashing, and active/inactive status toggles.
- **Immutable Audit Logging:** GCP & 21 CFR Part 11 compliant audit trail tracking authentication, account creation, activation/deactivation, and role changes. Strictly read-only with no modification or deletion routes.
- **Role-Specific Dashboard Shells:** Distinct workspaces for all 7 roles with clean Phase 2–5 transition roadmaps.

---

## Technology Stack

| Layer | Technologies |
|---|---|
| **Frontend** | React 18, TypeScript, Vite, Tailwind CSS, React Router v6, Axios, Lucide Icons |
| **Backend** | Python 3.14 / 3.11+, FastAPI, Pydantic v2, SQLAlchemy 2.0, Alembic |
| **Database** | PostgreSQL (Production/Dev) / SQLite (Zero-config local fallback) |
| **Security** | Argon2-cffi, Passlib, Bcrypt, PyJWT |
| **Testing** | Pytest, HTTPX, Requests E2E Test Suite |

---

## Repository Structure

```text
SIH/
├── backend/
│   ├── app/
│   │   ├── api/
│   │   │   ├── v1/
│   │   │   │   ├── auth.py          # /api/v1/auth/login, /logout, /me
│   │   │   │   ├── users.py         # /api/v1/users (Admin only)
│   │   │   │   ├── roles.py         # /api/v1/roles
│   │   │   │   └── audit_logs.py    # /api/v1/audit-logs (Admin & Regulator)
│   │   │   └── router.py
│   │   ├── core/
│   │   │   ├── config.py            # Pydantic Settings (.env, DB URL, JWT secrets)
│   │   │   ├── security.py          # Argon2/bcrypt hashing & JWT encoder/decoder
│   │   │   └── dependencies.py      # get_current_user, require_role, require_permission
│   │   ├── database/
│   │   │   ├── session.py           # SQLAlchemy sessionmaker & engine
│   │   │   └── init_db.py           # Database seeder (7 roles & demo users)
│   │   ├── models/
│   │   │   ├── base.py
│   │   │   ├── role.py              # Role & role_permissions models
│   │   │   ├── permission.py        # Permission model
│   │   │   ├── user.py              # User model
│   │   │   └── audit_log.py         # Immutable AuditLog model
│   │   ├── schemas/                 # Pydantic validation schemas
│   │   ├── services/                # auth_service, user_service, audit_service
│   │   └── main.py                  # FastAPI application, CORS, error handlers
│   ├── migrations/                  # Alembic migration scripts
│   ├── tests/
│   │   ├── conftest.py              # Pytest fixtures & in-memory test DB
│   │   ├── test_auth.py             # Auth tests (login, logout, me, invalid pass)
│   │   ├── test_rbac.py             # RBAC tests (403 forbidden enforcement)
│   │   ├── test_users.py            # User management tests
│   │   ├── test_audit.py            # Audit log tests (immutability)
│   │   └── e2e_demo.py              # Comprehensive 4-scenario E2E demo runner
│   ├── requirements.txt
│   ├── alembic.ini
│   ├── pytest.ini
│   └── .env.example
│
├── frontend/
│   ├── src/
│   │   ├── components/              # StatusBadge, Modal, ProtectedRoute, RoleGuard
│   │   ├── context/                 # AuthContext & useAuth hook
│   │   ├── layouts/                 # DashboardLayout (Ayush/AIIA header & sidebar)
│   │   ├── pages/
│   │   │   ├── LoginPage.tsx        # Branded login + 1-click demo credential pills
│   │   │   ├── DashboardPage.tsx    # Role-specific workspaces for all 7 roles
│   │   │   ├── UsersPage.tsx        # Admin user directory & creation modal
│   │   │   ├── AuditLogsPage.tsx    # Immutable compliance audit viewer
│   │   │   ├── ProfilePage.tsx      # User profile details
│   │   │   └── AccessDeniedPage.tsx # 403 Forbidden page
│   │   ├── services/                # Axios API client & service wrappers
│   │   ├── types/                   # TypeScript interfaces
│   │   └── App.tsx                  # Master routing with guards
│   ├── package.json
│   ├── vite.config.ts
│   └── tailwind.config.js
│
├── .gitignore
└── README.md
```

---

## Quickstart Guide

### 1. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create and activate Python virtual environment
python -m venv venv
.\venv\Scripts\Activate.ps1    # On Windows PowerShell
# source venv/bin/activate     # On Linux / macOS

# Install dependencies
pip install -r requirements.txt

# Configure environment variables (optional, defaults to SQLite if not set)
cp .env.example .env

# Run database migrations and seed initial roles & demo accounts
python -m app.database.init_db

# Start backend server (runs at http://127.0.0.1:8000)
uvicorn app.main:app --reload --port 8000
```

Backend interactive API documentation is available at: **http://127.0.0.1:8000/docs**

---

### 2. Frontend Setup

```bash
# Navigate to frontend directory
cd frontend

# Install Node dependencies
npm install

# Start Vite development server (runs at http://127.0.0.1:5173)
npm run dev
```

Open your browser at **http://127.0.0.1:5173** to access the dashboard.

---

## Demo Accounts & Role Matrix

Every account has the default development password: **`Password@AIIA2026!`**

| Role | Username | Permitted Modules | Dashboard Shell |
|---|---|---|---|
| **ADMIN** | `admin` | `/dashboard`, `/users`, `/audit-logs`, `/profile` | System Administration & Governance |
| **PRINCIPAL_INVESTIGATOR** | `investigator` | `/dashboard`, `/profile` | Clinical Research Workspace (Phase 2 Preview) |
| **STUDY_COORDINATOR** | `coordinator` | `/dashboard`, `/profile` | Participant Workspace (Phase 3 Preview) |
| **CLINICAL_TRIAL_MONITOR** | `monitor` | `/dashboard`, `/profile` | Monitoring Workspace (Phase 3 Preview) |
| **ETHICS_COMMITTEE** | `ethics` | `/dashboard`, `/profile` | Ethics & IRB Workspace (Phase 4 Preview) |
| **PHARMACOVIGILANCE_OFFICER** | `pharmacovigilance` | `/dashboard`, `/profile` | Safety & ADR Workspace (Phase 5 Preview) |
| **REGULATOR** | `regulator` | `/dashboard`, `/audit-logs`, `/profile` | Regulatory Oversight & Audit Inspection |

> **Note:** The Login page includes **1-Click Demo Fill** buttons for all 7 roles to allow instant evaluation without manually re-typing credentials.

---

## Running the Automated Test Suite

### Unit & Integration Tests (Pytest)
```bash
cd backend
.\venv\Scripts\pytest.exe -v
```
*Executes 20 automated tests validating authentication, password hashing, RBAC 403 enforcement, user CRUD, and audit log immutability.*

### End-to-End Live Verification Script
```bash
cd backend
python tests/e2e_demo.py
```
*Executes live HTTP requests testing Demo 1 (Admin user creation), Demo 2 (Coordinator 403 check), Demo 3 (Ethics profile check), and Demo 4 (Audit trail verification).*

---

## Security & Compliance Architecture

1. **Password Hashing:** Argon2 key derivation with automatic salt generation via `passlib.context.CryptContext(schemes=["argon2", "bcrypt"])`. Plaintext passwords are never stored in the database or returned in API responses.
2. **JWT Security:** Stateless access tokens signed with HMAC-SHA256, carrying user claims (`sub`, `role`, `iat`, `exp`), validated on every privileged request.
3. **Defense in Depth (Dual RBAC):**
   - **Backend Guard:** `require_role()` and `require_permission()` dependencies enforce authorization on every API endpoint. Unauthorized access returns `403 Forbidden`.
   - **Frontend Guard:** `RoleGuard` and `ProtectedRoute` components conditionally render routes and navigation items. Manual URL navigation to restricted pages displays the `AccessDeniedPage`.
4. **Immutable Audit Trail:** Append-only database table tracking `LOGIN_SUCCESS`, `LOGIN_FAILED`, `LOGOUT`, `USER_CREATED`, `USER_UPDATED`, `USER_ACTIVATED`, `USER_DEACTIVATED`, and `ROLE_CHANGED`. No update or delete endpoints exist.

```

## Extracted Claims

### Project Purpose (from README)

See raw preview
- **CLAIM:** README states project is for SIH26046 AIIA CTMS / Ayurveda Clinical Trials.
- **FACT:** All 7 repos reference SIH26046. Need to verify code actually implements CTMS features (see ARCHITECTURE.md & REPO_ANALYSIS.md).

### Features (from README tables/sections)

(See raw README preview — features listed in tables)


### Architecture (from README)


| Layer | Technologies |
|---|---|
| **Frontend** | React 18, TypeScript, Vite, Tailwind CSS, React Router v6, Axios, Lucide Icons |
| **Backend** | Python 3.14 / 3.11+, FastAPI, Pydantic v2, SQLAlchemy 2.0, Alembic |
| **Database** | PostgreSQL (Production/Dev) / SQLite (Zero-config local fallback) |
| **Security** | Argon2-cffi, Passlib, Bcrypt, PyJWT |
| **Testing** | Pytest, HTTPX, Requests E2E Test Suite |

---


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

- **FACT:** File exists at `repositories/aravindakrishna-c_AIIA-Clinical-Trial-Dashboard/README.md` with 8528 chars.
- **CLAIM:** Everything in raw preview above is what author claims.
- **INFERENCE:** Do not assume implemented until traced in `analysis/aravindakrishna-c_AIIA-Clinical-Trial-Dashboard/REPO_ANALYSIS.md` (code > config > tests > README).
- **UNKNOWN:** If README lists feature without file evidence, mark as CLAIMED ONLY in REPO_ANALYSIS.

## Verification Checklist (used for this repo)

- [x] Read complete README (8528 chars)
- [x] Compared README claims to `package.json` / `schema.ts` / `routes.ts` / `tests/` existence
- [x] Extracted purpose, features, arch, setup, tech, DB, APIs, AI, standards, compliance, deployment, demo, limitations
- [ ] Deep file reads for evidence (see REPO_ANALYSIS.md for per-feature status)

## Other Markdown Docs in Repo

- `DEPLOYMENT.md` (4.4 KB)
- `README.md` (9.1 KB)
- `frontend\README.md` (1.3 KB)

---
*See `analysis/aravindakrishna-c_AIIA-Clinical-Trial-Dashboard/REPO_ANALYSIS.md:21` for Claim vs Implementation per feature.*
