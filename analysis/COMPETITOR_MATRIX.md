# SIH26046 Competitor Matrix — Evidence-Based (Code > README)

**Generated:** 2026-09-30 12:36
**Repositories:** 7 (in `repositories/` — each independent, no merging)
**Evidence hierarchy:** code > config > schema > tests > docs > README
**Statuses:** `IMPLEMENTED` / `PARTIALLY IMPLEMENTED` / `MOCKED` / `CLAIMED ONLY` / `NOT PRESENT` / `UNKNOWN`
**Source of statuses:** Direct file reads (`schema.ts`, `routes.ts`, `package.json`, `*.test.ts`, `seed.js`, `mockData.ts`, `init_db.py`) + search hits (`audit`, `FHIR`, `CDISC`, `CTRI`, `ABDM`) — see `analysis/<repo>/REPO_ANALYSIS.md:21` for per-feature evidence.

> **Do NOT rank.** Each cell is neutral evidence, not a winner/loser.

## Matrix

| Feature | AnushkaTadiyal_aiia-ctms | vansh459_AyuSphere | aravindakrishna-c_AIIA-Clinical-Trial-Dashboard | rimi007-grt_AIIA-CTMS | nishant-uxs_vedraya | DuvvuruDeepakReddy18_AyuTrial | kalyan-2006-prog_SIH26046-DEV-RUSH- |
|---|---|---|---|---|---|---|---|
| **Protocol management** | PARTIALLY IMPLEMENTED | IMPLEMENTED | IMPLEMENTED | PARTIALLY IMPLEMENTED | IMPLEMENTED | IMPLEMENTED | PARTIALLY IMPLEMENTED |
| **Multi-centre trials** | CLAIMED ONLY | IMPLEMENTED | IMPLEMENTED | CLAIMED ONLY | IMPLEMENTED | IMPLEMENTED | NOT PRESENT |
| **Participant management** | PARTIALLY IMPLEMENTED | IMPLEMENTED | IMPLEMENTED | PARTIALLY IMPLEMENTED | IMPLEMENTED | IMPLEMENTED | NOT PRESENT |
| **CRF / EDC** | NOT PRESENT | IMPLEMENTED | NOT PRESENT | NOT PRESENT | PARTIALLY IMPLEMENTED | MOCKED | NOT PRESENT |
| **Ayurveda-specific fields** | CLAIMED ONLY | PARTIALLY IMPLEMENTED | CLAIMED ONLY | CLAIMED ONLY | PARTIALLY IMPLEMENTED | IMPLEMENTED | NOT PRESENT |
| **CTRI integration** | CLAIMED ONLY | IMPLEMENTED | PARTIALLY IMPLEMENTED | CLAIMED ONLY | PARTIALLY IMPLEMENTED | PARTIALLY IMPLEMENTED | PARTIALLY IMPLEMENTED |
| **NDCT workflow** | NOT PRESENT | IMPLEMENTED | PARTIALLY IMPLEMENTED | NOT PRESENT | PARTIALLY IMPLEMENTED | PARTIALLY IMPLEMENTED | NOT PRESENT |
| **Ethics committee** | NOT PRESENT | IMPLEMENTED | IMPLEMENTED | NOT PRESENT | IMPLEMENTED | IMPLEMENTED | NOT PRESENT |
| **AE/SAE** | PARTIALLY IMPLEMENTED | IMPLEMENTED | IMPLEMENTED | PARTIALLY IMPLEMENTED | IMPLEMENTED | IMPLEMENTED | PARTIALLY IMPLEMENTED |
| **Pharmacovigilance** | NOT PRESENT | IMPLEMENTED | PARTIALLY IMPLEMENTED | NOT PRESENT | PARTIALLY IMPLEMENTED | IMPLEMENTED | NOT PRESENT |
| **NPvCC workflow** | NOT PRESENT | NOT PRESENT | NOT PRESENT | NOT PRESENT | NOT PRESENT | IMPLEMENTED | NOT PRESENT |
| **CDISC** | NOT PRESENT | IMPLEMENTED | PARTIALLY IMPLEMENTED | NOT PRESENT | PARTIALLY IMPLEMENTED | PARTIALLY IMPLEMENTED | PARTIALLY IMPLEMENTED |
| **FHIR** | NOT PRESENT | IMPLEMENTED | PARTIALLY IMPLEMENTED | NOT PRESENT | PARTIALLY IMPLEMENTED | PARTIALLY IMPLEMENTED | PARTIALLY IMPLEMENTED |
| **FHIR ↔ CDISC mapping** | NOT PRESENT | PARTIALLY IMPLEMENTED | NOT PRESENT | NOT PRESENT | NOT PRESENT | NOT PRESENT | NOT PRESENT |
| **ABDM** | NOT PRESENT | NOT PRESENT | NOT PRESENT | NOT PRESENT | NOT PRESENT | CLAIMED ONLY | NOT PRESENT |
| **RBAC** | PARTIALLY IMPLEMENTED | IMPLEMENTED | IMPLEMENTED | IMPLEMENTED | IMPLEMENTED | IMPLEMENTED | NOT PRESENT |
| **Audit trail** | PARTIALLY IMPLEMENTED | IMPLEMENTED | IMPLEMENTED | PARTIALLY IMPLEMENTED | IMPLEMENTED | IMPLEMENTED | PARTIALLY IMPLEMENTED |
| **Immutable audit** | NOT PRESENT | IMPLEMENTED | NOT PRESENT | NOT PRESENT | IMPLEMENTED | MOCKED | NOT PRESENT |
| **Real-time KPIs** | PARTIALLY IMPLEMENTED | IMPLEMENTED | IMPLEMENTED | PARTIALLY IMPLEMENTED | IMPLEMENTED | IMPLEMENTED | PARTIALLY IMPLEMENTED |
| **Synthetic data** | IMPLEMENTED | IMPLEMENTED | IMPLEMENTED | IMPLEMENTED | IMPLEMENTED | IMPLEMENTED | UNKNOWN |
| **AI** | NOT PRESENT | IMPLEMENTED | NOT PRESENT | NOT PRESENT | NOT PRESENT | NOT PRESENT | NOT PRESENT |
| **Offline capability** | NOT PRESENT | NOT PRESENT | NOT PRESENT | NOT PRESENT | NOT PRESENT | MOCKED | NOT PRESENT |
| **Cloud deployment** | NOT PRESENT | IMPLEMENTED | IMPLEMENTED | IMPLEMENTED | IMPLEMENTED | IMPLEMENTED | IMPLEMENTED |
| **Testing** | MOCKED | IMPLEMENTED | PARTIALLY IMPLEMENTED | MOCKED | IMPLEMENTED | IMPLEMENTED | NOT PRESENT |
| **Live demo** | UNKNOWN | IMPLEMENTED | UNKNOWN | UNKNOWN | IMPLEMENTED | IMPLEMENTED | IMPLEMENTED |
| **PPT** | NOT PRESENT | NOT PRESENT | NOT PRESENT | NOT PRESENT | NOT PRESENT | NOT PRESENT | NOT PRESENT |
| **PDF** | NOT PRESENT | IMPLEMENTED | NOT PRESENT | NOT PRESENT | NOT PRESENT | NOT PRESENT | NOT PRESENT |
| **Demo script** | NOT PRESENT | IMPLEMENTED | NOT PRESENT | NOT PRESENT | IMPLEMENTED | NOT PRESENT | NOT PRESENT |
| **Judge Q&A** | NOT PRESENT | PARTIALLY IMPLEMENTED | NOT PRESENT | NOT PRESENT | IMPLEMENTED | NOT PRESENT | NOT PRESENT |

## Evidence Index (per repo key files)

| Repo | Key evidence for IMPLEMENTED cells |
|---|---|
| **AnushkaTadiyal_aiia-ctms** | `repositories/AnushkaTadiyal_aiia-ctms/server/seed.js:1` 57KB (24 trials 30 AEs), `client/src/pages/TrialDetailPage.jsx:1` 37KB, `client/src/pages/SafetyPage.jsx:1` 30KB — audit page 9KB without hash, RBAC AuthContext, no tests |
| **vansh459_AyuSphere** | `repositories/vansh459_AyuSphere/src/db/schema.ts:1` 576 lines, `src/app/api/ai/extract/route.ts:1` Claude OCR, `tests/*.test.ts` 50 suites 157 tests, `scripts/scrape/ctri_scrape.py:1` CTRI scrape, `docs/uat/*.pdf` 9 PDFs |
| **aravindakrishna-c_AIIA-Clinical-Trial-Dashboard** | `repositories/aravindakrishna-c_AIIA-Clinical-Trial-Dashboard/backend/app/api/v1/trials.py:1` 11.8KB, `backend/app/database/init_db.py:1` 60KB, `backend/app/api/v1/fhir.py:1` 2.5KB (partial), `docker-compose.yml` |
| **rimi007-grt_AIIA-CTMS** | Same as Anushka + `repositories/rimi007-grt_AIIA-CTMS/client/src/components/AWSCloudModal.jsx:1` 15KB, `Dockerfile`, `apprunner.yaml` — modals mocked |
| **nishant-uxs_vedraya** | `repositories/nishant-uxs_vedraya/server/src/db/schema.ts:1` 441 lines + 5 migrations, `server/src/middleware/studyAccess.ts:1` ACL, `server/src/modules/audit/service.ts:1` GLOBAL SHA-256 hash chain + verify, `server/tests/*.test.ts` 46/46, `e2e/*` 26/26, `docs/DEMO_SCRIPT.md:1` + `JUDGE_QA.md:1` + `SIH26046_TRACEABILITY_FINAL.md:1` |
| **DuvvuruDeepakReddy18_AyuTrial** | `repositories/DuvvuruDeepakReddy18_AyuTrial/src/lib/mockData.ts:1` 58KB 10 trials, `src/app/pharmacovigilance/new/page.tsx:1` 22KB SAE WHO-UMC, `src/app/interoperability/page.tsx:1` SDTM/FHIR inspector, `src/lib/crypto.ts:1` SHA-256 mock, 28 routes, `ayutrial-ctms.vercel.app` |
| **kalyan-2006-prog_SIH26046-DEV-RUSH-** | `repositories/kalyan-2006-prog_SIH26046-DEV-RUSH-/devrush-ctms/lib/schema.ts:1` 13.7KB, `app/api/fhir/ingest/route.ts:1` 12.5KB, `app/api/define/export/route.ts:1` 9.9KB, `app/api/sdtm/export/route.ts:1` 6.3KB — stubs, 5 commits, no tests |

## Definitions Applied (from Task 7)

- **IMPLEMENTED:** Meaningful working implementation (e.g., vedraya `server/src/modules/audit/service.ts:1` hash chain with verify endpoint passes `valid:false` on tamper; AyuSphere `src/app/api/ai/extract/route.ts:1` with `extraction.test.ts:1` mocked Claude).
- **PARTIALLY IMPLEMENTED:** Some real code but incomplete (e.g., vedraya CTRI TRACKING internal, no external CTRI API; Dashboard FHIR 2.5KB stub).
- **MOCKED:** Hardcoded/sample/demo data or simulated behavior (e.g., AyuTrial `src/lib/mockData.ts:1` localStorage, not real DB; AyuTrial audit hash via `crypto.ts` not WORM).
- **CLAIMED ONLY:** README/docs claim but no code (e.g., Anushka `README.md:1` claims 21 CFR Part 11 — no eSign/WORM in `server/package.json`; rimi AWS modal without backend).
- **NOT PRESENT:** No evidence via rglob search (`FHIR` 0 hits, `ABDM` 0 hits — verified in `analysis/<repo>/REPO_ANALYSIS.md:15`).
- **UNKNOWN:** Insufficient evidence (e.g., Anushka live demo no vercel.json → UNKNOWN; DEV-RUSH synthetic data no seed → UNKNOWN).

## Common vs Rare (from matrix)

- **Common (5+ repos IMPLEMENTED/PARTIALLY):** Protocol management, Participant management, AE/SAE, Synthetic data, Real-time KPIs, Audit trail, RBAC
- **Rare (1-2 repos IMPLEMENTED):** NPvCC (only AyuTrial), AI (only AyuSphere), Immutable audit with hash chain (vedraya + AyuSphere), FHIR↔CDISC mapping (only AyuSphere PARTIALLY), PDF/UAT guides (only AyuSphere), Judge Q&A (only vedraya full)
- **Common MOCKED/CLAIMED ONLY:** ABDM (6 NOT PRESENT, 1 CLAIMED ONLY), Offline capability (6 NOT PRESENT, 1 MOCKED), 21 CFR Part 11 (2 CLAIMED ONLY), CTRI external API (only AyuSphere IMPLEMENTED via scrape, others tracking/claimed)
- **Zero PPT:** No `.ppt/.pptx` found in any of 7 repos via search (excluded .git/node_modules) — `presentations/*/PRESENTATION_INVENTORY.md` confirms.

## Repo-Specific Notes (neutral, no ranking)

```text
AnushkaTadiyal_aiia-ctms: CLAIMED ONLY for 21 CFR Part 11 — FACT: audit page exists but no hash/WORM; RBAC PARTIALLY (JWT + UI, no study ACL).
vansh459_AyuSphere: Most test-gated (157 tests, PGlite no Docker), only AI IMPLEMENTED, only real CTRI scrape, only FHIR↔CDISC PARTIALLY.
aravindakrishna-c_AIIA-Clinical-Trial-Dashboard: Only Python/FastAPI stack, only Alembic migrations; FHIR/CDISC PARTIALLY (2.5KB fhir.py stub).
rimi007-grt_AIIA-CTMS: Same base as Anushka + deployment (Dockerfile, apprunner.yaml) but AWS/ESignature modals MOCKED; RBAC IMPLEMENTED per matrix but shallow test.
nishant-uxs_vedraya: Most honest prototype scoping, only full DEMO_SCRIPT.md + JUDGE_QA.md + traceability, only GLOBAL SHA-256 verify endpoint with 46/46 Vitest + 26/26 Playwright.
DuvvuruDeepakReddy18_AyuTrial: Only NPvCC IMPLEMENTED, only Ayurveda fields IMPLEMENTED (Prakriti/Agni/Koshtha visits), only ABDM CLAIMED ONLY (blueprint, not connected), audit MOCKED (localStorage).
kalyan-2006-prog_SIH26046-DEV-RUSH-: Smallest (66 files, 5 commits), FHIR/SDTM/ADaM/Define routes PARTIALLY (stubs 6-12KB), NOT PRESENT for most workflows, UNKNOWN for synthetic data.
```

---

*Generated via code search (rglob) + file reads (schema.ts, routes.ts, package.json, tests) per evidence hierarchy. See `analysis/<repo>/REPO_ANALYSIS.md:21` for per-feature Claim vs Implementation tables and `presentations/<repo>/PRESENTATION_INVENTORY.md` for PPT/PDF/demo search results.*
