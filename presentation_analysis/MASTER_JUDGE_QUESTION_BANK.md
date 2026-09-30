# Master Judge Question Bank — SIH26046

**Generated:** 2026-09-30
**Repositories scanned:** 7 (nishant-uxs_vedraya, vansh459_AyuSphere primary judge material; others via README/analysis)
**Total questions combined (deduped):** 36
**Sources:** `nishant-uxs_vedraya/docs/JUDGE_QA.md:1` (3.5KB), `vansh459_AyuSphere/docs/uat/Tech_Security_Guide.md:1` (17KB), `analysis/*/JUDGE_QA_ANALYSIS.md:1` + traceability/limitations, `COMPETITOR_MATRIX.md:1` claim vs code.

> Do not confuse PDF UAT guides with PowerPoint — PPT/PPTX FOUND: 0.

## AI

1. **Q:** Does Copilot hallucinate? How is grounding enforced? Does it decline on empty retrieval?  
   **Source:** `vansh459_AyuSphere/tests/copilot.test.ts:1`
2. **Q:** How does AI work? Claude vs Gemini vs Groq? Mocked or real API?  
   **Source:** `vansh459_AyuSphere/src/app/api/ai/extract/route.ts:1 + tests/extraction.test.ts mocked`

## Architecture

1. **Q:** How scalable is architecture? Monolith vs microservices? Why not microservices?  
   **Source:** `nishant-uxs_vedraya docs/ARCHITECTURE.md:1 modular monolith vs AyuSphere Next.js`

## Clinical

1. **Q:** How are adverse events coded? MedDRA/WHODrug pickers?  
   **Source:** `nishant-uxs_vedraya coding/routes.ts MEDDRA_DEMO vs AyuSphere dictionaries.test.ts`
2. **Q:** What is the NPvCC workflow? 24h SAE clock? WHO-UMC causality?  
   **Source:** `DuvvuruDeepakReddy18_AyuTrial src/app/pharmacovigilance/new/page.tsx:1 24h clock`

## Data

1. **Q:** Are participants real patient data or synthetic? DPDP compliant?  
   **Source:** `All repos synthetic/de-identified per README + schema no identifier cols (AyuSphere)`
2. **Q:** How is data quality assured? CRF immutability? Versioned corrections?  
   **Source:** `vansh459_AyuSphere crf.test.ts + design-qa.test.ts`
3. **Q:** Is CTRI data real or synthetic? How often updated?  
   **Source:** `vansh459_AyuSphere docs/uat: trials real CTRI public, participants synthetic`

## Demo

1. **Q:** Can you show audit re-verify live? Show before/after tamper?  
   **Source:** `nishant-uxs_vedraya docs/DEMO_SCRIPT.md:1 step 6 Audit → Re-verify SHA-256`
2. **Q:** Is live demo actually live or localStorage mock? Supabase vs demo mode?  
   **Source:** `DuvvuruDeepakReddy18_AyuTrial .env.example NEXT_PUBLIC_APP_ENV=demo vs Supabase`

## Deployment

1. **Q:** What is the deployment? Vercel only? Where is Postgres? Docker?  
   **Source:** `nishant-uxs_vedraya README Vercel SPA only + render.yaml vs vansh459 Vercel+Neon`

## Implementation

1. **Q:** What are the limitations? What is not implemented vs prototype?  
   **Source:** `nishant-uxs_vedraya docs/LIMITATIONS.md:1 + docs/IMPLEMENTATION_STATUS.md:1 vs others sparse`

## Innovation

1. **Q:** What differentiates your solution vs other CTMS prototypes?  
   **Source:** `All repos pitch differentiators per README — vedraya hash chain, AyuSphere test-gated AI, AyuTrial NPvCC`

## Interoperability

1. **Q:** Is ABDM/HIS/EDC actually connected? ABHA verification?  
   **Source:** `nishant-uxs_vedraya/docs/JUDGE_QA.md:1 + README NOT CONNECTED`
2. **Q:** Is CDISC SDTM certified? Define-XML present?  
   **Source:** `nishant-uxs_vedraya/docs/JUDGE_QA.md:1 + docs/IMPLEMENTATION_STATUS.md:1`
3. **Q:** Is FHIR R4 certified integration or prototype?  
   **Source:** `nishant-uxs_vedraya/docs/JUDGE_QA.md:1 + vansh459_AyuSphere fhir-api.test.ts`

## Regulatory

1. **Q:** How is CTRI integrated? Real API or tracking/scrape?  
   **Source:** `vansh459_AyuSphere/scripts/scrape/ctri_scrape.py:1 vs vedraya regulatory/routes.ts tracking`
2. **Q:** Is 21 CFR Part 11 compliant? eSignature, WORM, audit?  
   **Source:** `AnushkaTadiyal_aiia-ctms README claim vs no code + vedraya honest NOT CLAIMED`
3. **Q:** Is MedDRA/WHODrug licensed or demo dictionary?  
   **Source:** `nishant-uxs_vedraya/docs/JUDGE_QA.md:1 + docs/LIMITATIONS.md:1`

## Scalability

1. **Q:** Can system work offline in rural sites? IndexedDB sync?  
   **Source:** `All repos NOT PRESENT except AyuTrial MOCKED localStorage — gap`

## Security

1. **Q:** How is study membership ACL enforced? Can monitor access only AYU-024?  
   **Source:** `nishant-uxs_vedraya/docs/JUDGE_QA.md:1 + server/src/middleware/studyAccess.ts:1`
2. **Q:** Is audit trail immutable? WORM storage? Can admin delete logs?  
   **Source:** `nishant-uxs_vedraya/docs/JUDGE_QA.md:1 + docs/LIMITATIONS.md:1 + vansh459_AyuSphere audit insert-only`
3. **Q:** What happens if audit log is tampered in DB? Does verify detect it?  
   **Source:** `nishant-uxs_vedraya/docs/JUDGE_QA.md:1 + server/tests/api.audit.integrity.test.ts:1`

## Technical

1. **Q:** ## 1. Is MedDRA official?  
   **Source:** `nishant-uxs_vedraya/docs/JUDGE_QA.md:1 (extracted)`
2. **Q:** ## 10. What happens to unauthorized API requests?  
   **Source:** `nishant-uxs_vedraya/docs/JUDGE_QA.md:1 (extracted)`
3. **Q:** ## 2. Is WHODrug official?  
   **Source:** `nishant-uxs_vedraya/docs/JUDGE_QA.md:1 (extracted)`
4. **Q:** ## 3. Is this CDISC compliant?  
   **Source:** `nishant-uxs_vedraya/docs/JUDGE_QA.md:1 (extracted)`
5. **Q:** ## 4. Is ABDM connected?  
   **Source:** `nishant-uxs_vedraya/docs/JUDGE_QA.md:1 (extracted)`
6. **Q:** ## 5. Is CTRI integrated?  
   **Source:** `nishant-uxs_vedraya/docs/JUDGE_QA.md:1 (extracted)`
7. **Q:** ## 6. Is the audit WORM?  
   **Source:** `nishant-uxs_vedraya/docs/JUDGE_QA.md:1 (extracted)`
8. **Q:** ## 7. Is this ALCOA+ compliant?  
   **Source:** `nishant-uxs_vedraya/docs/JUDGE_QA.md:1 (extracted)`
9. **Q:** ## 8. How does RBAC work?  
   **Source:** `nishant-uxs_vedraya/docs/JUDGE_QA.md:1 (extracted)`
10. **Q:** ## 9. How is study-level isolation enforced?  
   **Source:** `nishant-uxs_vedraya/docs/JUDGE_QA.md:1 (extracted)`
11. **Q:** How are KPIs computed? Real-time derived vs hardcoded?  
   **Source:** `nishant-uxs_vedraya server/src/modules/alerts/routes.ts vs AyuSphere alerts cron`
12. **Q:** How does authentication and RBAC work? Is it 7 roles?  
   **Source:** `nishant-uxs_vedraya/docs/JUDGE_QA.md:1 + vansh459_AyuSphere/docs/uat/Tech_Security_Guide.md:1`
13. **Q:** What tests exist? Coverage? E2E?  
   **Source:** `vedraya 46/46 Vitest + 26/26 Playwright vs AyuSphere 157 PGlite vs AyuTrial 21 tsx`

---

## Evidence Index for Questions

- Technical/RBAC/audit questions → verify via `analysis/nishant-uxs_vedraya/REPO_ANALYSIS.md:7` (Auth/RBAC) + `analysis/vansh459_AyuSphere/REPO_ANALYSIS.md:7`
- Regulatory/21 CFR → `analysis/AnushkaTadiyal_aiia-ctms/CLAIM_VS_EVIDENCE.md:1` (CLAIMED ONLY) vs `nishant-uxs_vedraya/docs/LIMITATIONS.md:1` (honest)
- AI → `vansh459_AyuSphere/src/app/api/ai/extract/route.ts:1` + `tests/extraction.test.ts:1`
- FHIR/CDISC/ABDM → `analysis/*/REPO_ANALYSIS.md:11-14` (search hits FHIR 0-5, CDISC 0-3, ABDM 0-1)
- Data/DPDP → `src/db/schema.ts:1` (AyuSphere no identifier cols), `server/src/db/seed.ts:1` synthetic
