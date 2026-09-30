# README_ANALYSIS — vansh459_AyuSphere

**Source:** `E:\SIH26046_COMPETITOR_ANALYSIS\repositories\vansh459_AyuSphere\README.md` (2749 chars, 2.8 KB if exists)
**Generated:** 2026-09-30
**Repository:** https://github.com/vansh459/AyuSphere

> README is evidence of CLAIM, not proof of IMPLEMENTATION. Verified against code where possible (see evidence notes).

## Raw README Preview (first 15000 chars)

```markdown
# AyuSphere

AI-assisted Clinical Research Intelligence Platform for Ayurveda — SIH26046
(AIIA Clinical Trials Dashboard). Team **Bob The Builder**.

Full documentation lives in [`docs/`](docs/): development plan,
architecture, technology, application workflows, ADR decision log, the
test-gated task board, and the [PS gap analysis](docs/gap-analysis.md) with
its [gap-fill plan](docs/gap-plan.md) (Phases 7–10).

## Stack

Next.js 16 (App Router) + TypeScript · Neon Postgres + Drizzle · Auth.js v5
(7 roles, JWT) · Claude API (Doctor Note OCR/extraction + grounded Copilot) ·
Tailwind v4 + hand-owned shadcn-style components · Framer Motion ·
Vitest + **PGlite** (in-process Postgres — **no Docker anywhere**, D-019).

## Quickstart

```bash
pnpm install
cp .env.example .env.local   # fill DATABASE_URL (Neon), AUTH_SECRET, ANTHROPIC_API_KEY
pnpm db:migrate              # apply migrations to Neon
pnpm db:seed                 # deterministic synthetic demo data (D-016)
pnpm dev
```

Demo logins (password `Demo@1234`): `pi@aiia.demo`, `coordinator@aiia.demo`,
`monitor@aiia.demo`, `ethics@aiia.demo`, `pv@aiia.demo`, `admin@aiia.demo`,
`regulator@aiia.demo` (read-only).

## Tests (the task gates)

```bash
pnpm verify      # runs typecheck and full vitest suite
pnpm test        # 157 tests: domain rules + services on PGlite + static design QA
pnpm typecheck
pnpm build
```

See [CONTRIBUTING.md](CONTRIBUTING.md) for contribution guidelines, architecture conventions, and development setup.

Every task in [`docs/tasks.md`](docs/tasks.md) shipped only after its
test gate passed. Key suites: lifecycle state machine, ALCOA+ audit atomicity,
enrolment guards, visit windows, CRF immutability + versioned corrections,
AE escalation clock, alert idempotency/auto-resolve, the full Doctor Note
extraction pipeline (mocked Claude), Copilot grounding (declines on empty
retrieval), FHIR/SDTM exports, regulator read-only, and the
one-font/two-sizes design rule enforced statically.

## Notes

- Trial-level metadata can be REAL public CTRI registry records (titles, CTRI
  numbers, interventions, sponsors, sites/states) scraped politely by
  `scripts/scrape/ctri_scrape.py` (crawl4ai, pip-only — no Docker) and seeded
  via `pnpm db:seed:real` (idempotent; see D-021). **All participant-level
  data is synthetic** (`src/db/seed.ts` / `src/db/seed-real.ts`, fixed faker
  seed). No real personal data may enter any environment.
- The participants table has **no identifier columns** — de-identification by
  schema.
- `audit_events` is insert-only; every mutation commits inside `withAudit()`.
- Doctor Note drafts never auto-commit: low-confidence and flagged fields must
  be explicitly confirmed, and only the PI can approve into the record.

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

- **FACT:** File exists at `repositories/vansh459_AyuSphere/README.md` with 2749 chars.
- **CLAIM:** Everything in raw preview above is what author claims.
- **INFERENCE:** Do not assume implemented until traced in `analysis/vansh459_AyuSphere/REPO_ANALYSIS.md` (code > config > tests > README).
- **UNKNOWN:** If README lists feature without file evidence, mark as CLAIMED ONLY in REPO_ANALYSIS.

## Verification Checklist (used for this repo)

- [x] Read complete README (2749 chars)
- [x] Compared README claims to `package.json` / `schema.ts` / `routes.ts` / `tests/` existence
- [x] Extracted purpose, features, arch, setup, tech, DB, APIs, AI, standards, compliance, deployment, demo, limitations
- [ ] Deep file reads for evidence (see REPO_ANALYSIS.md for per-feature status)

## Other Markdown Docs in Repo

- `AGENTS.md` (0.7 KB)
- `CLAUDE.md` (0.0 KB)
- `CONTRIBUTING.md` (3.4 KB)
- `README.md` (2.8 KB)
- `docs\architecture.md` (17.4 KB)
- `docs\decisions.md` (29.6 KB)
- `docs\development-plan.md` (9.1 KB)
- `docs\gap-analysis.md` (13.0 KB)
- `docs\gap-plan.md` (16.4 KB)
- `docs\loading-skeletons.md` (6.2 KB)
- `docs\performance-audit.md` (5.1 KB)
- `docs\tasks.md` (24.4 KB)
- `docs\technology.md` (10.4 KB)
- `docs\ui-audit.md` (5.8 KB)
- `docs\workflow.md` (14.5 KB)

---
*See `analysis/vansh459_AyuSphere/REPO_ANALYSIS.md:21` for Claim vs Implementation per feature.*
