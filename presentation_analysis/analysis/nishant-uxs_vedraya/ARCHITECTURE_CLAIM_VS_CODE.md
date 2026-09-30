# Architecture Claim vs Code — nishant-uxs_vedraya

**Repository:** `nishant-uxs_vedraya`
**Generated:** 2026-09-30

## Presented Architecture — File: `docs\ARCHITECTURE.md` (5.5 KB)

```markdown
# VEDRAYA Architecture

> SIH26046 AIIA Clinical Trials Dashboard / CTMS  
> Status: Phase 0 forensics + target architecture  
> Last updated: 2026-09-29

## 1. Current system (as-built)

### Stack

| Layer | Technology | Notes |
|-------|------------|-------|
| Frontend | Vite 8 + React 19 + TypeScript | SPA only |
| Motion | GSAP, Lenis, Framer Motion | Landing cinematic |
| Theme | `data-theme` + CSS tokens | Light/dark |
| Backend | **None** | — |
| Database | **None** | — |
| Auth | **None** | Theme in `localStorage` only |
| Tests | **None** | — |

### Frontend topology

```
App.tsx
├── Navbar (hash links)
├── Hero + VedrayaScrollSequence (frame scrub)
├── FragmentedData (#platform)
├── TrialLifecycle
├── RiskIntelligence (#intelligence)
├── SafetyIntelligence (#safety)
├── ComplianceMatrix (#compliance)
├── InteropPipeline (#interop)
├── AuditTimeline
├── CopilotPanel (#copilot)
├── RoleSwitcher
├── CommandCenter (#command-center) → DashboardPreview
├── FinalCTA
└── SiteFooter
```

- **No React Router.** Navigation is hash anchors on one page.
- **No API client.** All domain data is inline `const` arrays.
- **Command Center** is a visual mock (`DashboardPreview`), not an application shell.

### Fake / hardcoded data sources

| Source | File | Claims |
|--------|------|--------|
| `STUDIES`, `ALERTS` | `DashboardPreview.tsx` | Live portfolio / alerts |
| `STAGES` | `TrialLifecycle.tsx` | Lifecycle ops |
| `FACTORS` | `RiskIntelligence.tsx` | Risk scoring |
| `HIERARCHY`, `WORKFLOW` | `SafetyIntelligence.tsx` | PV workflow |
| `MATRIX` | `ComplianceMatrix.tsx` | Regulatory checks |
| `PIPE`, `TRANSFORM` | `InteropPipeline.tsx` | FHIR/CDISC/ABDM |
| `EVENTS` | `AuditTimeline.tsx` | ALCOA+ audit |
| `ROLE_MODULES` | `RoleSwitcher.tsx` | RBAC |
| `RESPONSE_LINES` | `CopilotPanel.tsx` | AI / grounded query |
| Telemetry string | `DashboardPreview.tsx` | Latency / federated / immutable |

### What must be preserved

- Landing cinematic experience (hero frames, GSAP sections)
- Design tokens (`tokens.css`), theme toggle, typography
- Visual language of Command Center (layout/CSS), but fed by APIs
- `design.md` principles where they do not conflict with CTMS ops UX

---

## 2. Target system

### Modular monolith

```
Browser (React)
    │  cookie session
    ▼
Express API  /api/v1/*
    │
    ├── Auth / Users / RBAC
    ├── Studies / Sites / Investigators / Participants
    ├── Milestones / Regulatory / Consents
    ├── Adverse Events / Safety
    ├── Audit (append-only)
    ├── Exports (CSV prototype)
    └── Interop (FHIR-shaped read MVP)
    │
    ▼
PostgreSQL (Drizzle ORM)
```

### Repository layout (target)

```
/
├── src/                    # Existing Vite frontend (preserved)
├── server/                 # New Node + Express + Drizzle API
│   ├── src/
│   │   ├── config/
│   │   ├── db/
│   │   ├── middleware/
│   │   ├── modules/
│   │   ├── routes/
│   │   ├── app.ts
│   │   └── index.ts
│   ├── drizzle/
│   └── package.json        # or workspace root scripts
├── docs/
└── package.json            # frontend + workspace scripts
```

### API conventions

- Base path: `/api/v1`
- JSON only
- Zod validation on inputs
- Errors: `{ error: { code, message, details? } }`
- Auth: HTTP-only session cookie (`vedraya_sid`) preferred
- Authorization: permission strings checked **server-side**

### Frontend integration strategy

1. Keep landing page as marketing story (can still use static educational props where labeled DEMO).
2. Grow Command Center into the **authenticated app surface** (routes under `#/app` or `/app` via React Router added surgically).
3. Replace `DashboardPreview` data with `GET /api/v1/studies`, `/alerts`, `/kpis`.
4. Never invent fake `/api` responses in Vite middleware.

### Environment

| Variable | Purpose |
|----------|---------|
| `DATABASE_URL` | PostgreSQL connection |
| `SESSION_SECRET` | Session signing |
| `NODE_ENV` | development / production |
| `CORS_ORIGIN` | Frontend origin |
| `VITE_API_BASE` | Frontend API base (default `/api/v1`) |

Vite will proxy `/api` → `http://localhost:4000` in development.

---

## 3. Security baseline

- Passwords: Argon2id (or bcrypt if Argon2 packaging blocked)
- Sessions: HTTP-only, Secure in prod, SameSite=Lax
- CSRF: SameSite cookie + same-origin SPA; document residual risk
- No secrets in git; `.env.example` only
- Audit events written only by server on mutations
- Normal roles cannot PATCH/DELETE audit rows

---

## 4. Honesty / compliance labeling

| Claim | Allowed when |
|-------|----------------|
| ALCOA+ | Only after append-only audit + documented integrity limits |
| FHIR R4 | Only for resources actually returned; say "FHIR-shaped MVP" |
| CDISC | Only for documented CSV mapping prototype |
| DPDP | Privacy-by-design foundations only; no legal compliance claim |
| RBAC | Only when API returns 403 for unauthorized roles |

---

## 5. Staged delivery (aligned to PS)

1. **MVP A:** Auth + RBAC + Studies + Sites + Investigators + KPIs + Audit  
2. **MVP B:** Participants + Lifecycle transitions + Milestones + Alerts  
3. **MVP C:** AE/SAE workflow + Consent MVP + Regulatory records  
4. **MVP D:** FHIR-shaped reads + CSV export + Docs + Tests + Demo script  

```

- **Frontend:** found — `Frontend | Vite 8 + React 19 + TypeScript | SPA only |`
- **Backend:** found — `Backend | **None** | — |`
- **Database:** found — `Database | **None** | — |`
- **AI:** found — `AIIA Clinical Trials Dashboard / CTMS  `
- **External APIs:** not mentioned in presented doc
- **Cloud:** not mentioned in presented doc
- **Authentication:** not mentioned in presented doc
- **Data flow:** not mentioned in presented doc
- **Integration:** found — `integration strategy`


## Actual Code Architecture (verified)

See `analysis/nishant-uxs_vedraya/ARCHITECTURE.md:1` (diagram with evidence: `server/src/modules/*/routes.ts:1`, `schema.ts`, `package.json`).

## Comparison — Presented vs Actual

| Layer | Presented (from ARCHITECTURE.md) | Actual (from code) | Difference |
|---|---|---|---|
| Frontend | Yes (presented) | No code | Check if presented matches Vite/Next vs code |
| Backend | Yes | Yes | See ARCHITECTURE.md |
| Database | Mentioned | Yes | Verify schema.ts |
| AI | Mentioned | Not present (most) | Only AyuSphere has code |
| Cloud | Mentioned if vercel/render in doc | See deployment (vercel.json/render.yaml) |
| Authentication | Mentioned | See REPO_ANALYSIS 7. Auth |
| Data flow | Mentioned | See ARCHITECTURE.md diagram |

> **Rule:** If presented says ABDM integrated but code search `ABDM` 0 hits → CLAIMED ONLY vs NOT PRESENT.

