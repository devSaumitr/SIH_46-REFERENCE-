# Feature Presentation Comparison — What Competitors Emphasize

**Generated:** 2026-09-30
**Evidence:** README tables, docs/*.md, `analysis/*/FEATURE_PRESENTATION_ANALYSIS.md:1`, `COMPETITOR_MATRIX.md:1`
**Do NOT rank.**

## Matrix: Top Features Emphasized (from pitch docs)

| Category | vedraya (honest) | AyuSphere (test-gated) | AyuTrial (NPvCC-heavy) | Dashboard (FastAPI) | Anushka (shell) | rimi (fork+modals) | DEV-RUSH (stubs) |
|---|---|---|---|---|---|---|---|
| **Top features emphasized** | Live Command Center + auditable RBAC + SHA-256 verify + PS traceability | AI Doctor Note OCR + grounded Copilot + real CTRI scrape + CRF immutability + PGlite | 28 routes + NPvCC 24h SAE clock + WHO-UMC + 10 trials 8 sites + ABDM blueprint | 11 FastAPI routers (trials 11KB) + 41KB CreateTrialPage | 24 trials/30 AEs seed + Trials/Safety pages | Same as Anushka + AWS/Dictionary/ESignature modals (15KB) | FHIR/SDTM/ADaM/Define route stubs (12KB ingest) |
| **Clinical features** | Studies/sites/participants/milestones + consent + AE escalate (not full eCRF) | Lifecycle state machine + CRF immutability + visit-engine + enrolment guards | Visits with Prakriti/Agni/Koshtha + dispensing + 28-route dossier | Trials/participants via FastAPI | TrialsPage 30KB + TrialDetail 37KB | Same + Dashboard 34KB | Dashboard/[trialId] 9.6KB |
| **Regulatory features** | Consent + ethics + regulatory CTRI/NDCT tracking (partial) + deviations/queries | Gap analysis vs plan (Phases 7-10) + ethics review via auth | GCP-ASU/ICMR/NDCT matrix + CTRI verification + vernacular consent | ethics_regulatory.py 4.4KB | CLAIMED CTRI | CLAIMED CTRI | ctri-ethics page 8KB |
| **AI features** | NOT PRESENT (honest) | Claude extract (low-confidence flag, PI approve) + Groq/Gemini fallback + Sphera guide | NOT PRESENT (WHO-UMC rule) | NOT PRESENT | NOT PRESENT | NOT PRESENT | NOT PRESENT |
| **Interoperability** | FHIR R4 prototype (ResearchStudy/Subject read) + SDTM-like AE CSV + CSV export + adapters NOT CONNECTED (honest) | FHIR Bundle/[trialId] + import + SDTM + exports (fhir-api.test 8KB, exports.test 10KB) | CDISC SDTM DM/AE/EX/VS/LB + Define-XML + FHIR bundle generator + ABDM readiness matrix | FHIR 2.5KB stub | NOT PRESENT | NOT PRESENT | FHIR ingest 12.5KB + export 8KB + SDTM 6.3KB |
| **Security** | Argon2 + sid HttpOnly + CSRF double-submit + RBAC 7 + study ACL + Helmet + Zod + rate limit + audit 405 + tamper valid:false (verified 7 checks) | Auth.js JWT 7 + insert-only audit + CRF immutability + design QA (one-font/two-sizes) + Tech_Security_Guide 17KB | Persona switcher (mock) + audit local hash (mocked) + 7 personas | PyJWT HS256 + passlib/argon2 + dependencies.py RBAC | JWT + bcryptjs + AuthContext | Same + RBACMatrixModal MOCKED | NOT PRESENT |
| **Analytics** | Portfolio KPIs + computed alerts (enrolment lag, open SAE) | Real-time KPIs + alerts cron idempotency + dashboard-queries | 10 computed KPIs + 7 Recharts + 24h SAE clock | dashboard.py 1.6KB | DashboardPage 25KB PARTIALLY | DashboardPage 34KB | dashboard page 10.6KB |
| **Pharmacovigilance** | AE escalate + reporting due/notify + MedDRA demo coding + safety KPIs — PARTIALLY (no NPvCC) | AE escalation clock + safety signals + dictionaries — IMPLEMENTED | NPvCC apex: dedicated desk + 24h/7d/14d statutory + WHO-UMC + CDSCO — IMPLEMENTED (unique) | safety.py 3.5KB PARTIALLY | SafetyPage 30KB PARTIALLY | SafetyPage 39KB PARTIALLY | adverse-events 8.7KB PARTIALLY |
| **Unique claims** | GLOBAL SHA-256 hash chain re-verify + honest prototype-only + PS traceability 8KB + Live Command Center | Test-gated tasks 24KB (every task after gate) + PGlite no Docker + CTRI real public scrape + synthetic de-identified + AI grounded Copilot declines | NPvCC for ASU&H + 24h clock + 28 routes + 10 trials + 8-site network + Ayurveda Prakriti/Agni/Koshtha + ABDM blueprint (unique) | Only Python/FastAPI stack | Fast to demo, SQLite committed 72KB | Same as Anushka + AWS/Docker + modals mocked | Smallest (5 commits), FHIR/SDTM/ADaM/Define stubs |

> **Commonly emphasized across ≥4 repos:** Protocol/participant/AE, RBAC 7, audit trail, synthetic data, real-time KPIs, deployment (Vercel/Render).
> **Rarely emphasized (1-2 repos):** NPvCC (only AyuTrial), AI (only AyuSphere), immutable hash chain (vedraya + AyuSphere), FHIR↔CDISC mapping (only AyuSphere partial), UAT PDFs (only AyuSphere), Judge Q&A (only vedraya full).

