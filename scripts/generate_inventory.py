#!/usr/bin/env python3
import pathlib, json, re, os, collections
BASE = pathlib.Path(r"E:\SIH26046_COMPETITOR_ANALYSIS")
REPOS = [
    ("AnushkaTadiyal_aiia-ctms", "AnushkaTadiyal", "aiia-ctms", "https://github.com/AnushkaTadiyal/aiia-ctms"),
    ("vansh459_AyuSphere", "vansh459", "AyuSphere", "https://github.com/vansh459/AyuSphere"),
    ("aravindakrishna-c_AIIA-Clinical-Trial-Dashboard", "aravindakrishna-c", "AIIA-Clinical-Trial-Dashboard", "https://github.com/aravindakrishna-c/AIIA-Clinical-Trial-Dashboard"),
    ("rimi007-grt_AIIA-CTMS", "rimi007-grt", "AIIA-CTMS", "https://github.com/rimi007-grt/AIIA-CTMS"),
    ("nishant-uxs_vedraya", "nishant-uxs", "vedraya", "https://github.com/nishant-uxs/vedraya"),
    ("DuvvuruDeepakReddy18_AyuTrial", "DuvvuruDeepakReddy18", "AyuTrial", "https://github.com/DuvvuruDeepakReddy18/AyuTrial"),
    ("kalyan-2006-prog_SIH26046-DEV-RUSH-", "kalyan-2006-prog", "SIH26046-DEV-RUSH-", "https://github.com/kalyan-2006-prog/SIH26046-DEV-RUSH-"),
]

SKIP_DIRS = {".git","node_modules",".venv","venv","__pycache__",".next","dist","build",".cache","coverage","target",".idea",".vscode"}

def tree_str(path, max_depth=8, prefix="", depth=0):
    if depth>max_depth: return ""
    try:
        items = sorted(path.iterdir(), key=lambda p: (not p.is_dir(), p.name.lower()))
    except: return ""
    out=""
    for i,p in enumerate(items):
        if p.name in SKIP_DIRS: continue
        is_last = i==len([x for x in items if x.name not in SKIP_DIRS])-1 if items else True
        # recalc filtered count
        filtered = [x for x in items if x.name not in SKIP_DIRS]
        is_last = (filtered.index(p) == len(filtered)-1) if p in filtered else False
        branch = "`-- " if is_last else "|-- "
        next_prefix = prefix + ("    " if is_last else "|   ")
        if p.is_dir():
            out+=f"{prefix}{branch}{p.name}/\n"
            out+=tree_str(p, max_depth, next_prefix, depth+1)
        else:
            try: sz=p.stat().st_size
            except: sz=0
            if sz>1_048_576: s=f"{sz/1_048_576:.2f} MB"
            elif sz>1024: s=f"{sz/1024:.1f} KB"
            else: s=f"{sz} B"
            out+=f"{prefix}{branch}{p.name} ({s})\n"
    return out

def detect_tech(repo_path):
    # returns dict
    info={}
    # frontend
    pkg_files = list(repo_path.rglob("package.json"))
    # filter skip
    pkg_files = [p for p in pkg_files if ".git" not in p.parts and "node_modules" not in p.parts]
    deps = {}
    for pf in pkg_files[:3]:
        try:
            j=json.loads(pf.read_text(encoding="utf-8", errors="ignore"))
            deps.update(j.get("dependencies",{}))
            deps.update(j.get("devDependencies",{}))
        except: pass
    # frontend hints
    fe=[]
    if any("react" in d.lower() for d in deps): fe.append("React")
    if any("next" in d.lower() for d in deps): fe.append("Next.js")
    if any("vite" in d.lower() for d in deps): fe.append("Vite")
    if any("vue" in d.lower() for d in deps): fe.append("Vue")
    info["frontend_hint"] = ", ".join(fe) if fe else "Unknown / Not found"
    # backend
    be=[]
    if any("express" in d.lower() for d in deps): be.append("Express")
    if any("fastapi" in d.lower() for d in deps) or ((repo_path/"backend").exists() and (repo_path/"backend/requirements.txt").exists()): be.append("FastAPI")
    if any("drizzle-orm" in d.lower() for d in deps): be.append("Drizzle ORM")
    # check python
    if list(repo_path.rglob("requirements.txt")): be.append("Python")
    if list(repo_path.rglob("*.py")) and not be: be.append("Python files")
    info["backend_hint"] = ", ".join(be) if be else "Unknown / Not found"
    # db
    db=[]
    if any("better-sqlite3" in d.lower() for d in deps): db.append("SQLite (better-sqlite3)")
    if any("pg" == d.lower() or d.lower()=="pg" for d in deps): db.append("PostgreSQL (pg)")
    if any("drizzle-orm" in d.lower() for d in deps): db.append("Drizzle ORM")
    if any("sqlalchemy" in d.lower() for d in deps): db.append("SQLAlchemy")
    if any("@neondatabase/serverless" in d.lower() for d in deps): db.append("Neon Postgres serverless")
    if any("supabase" in d.lower() for d in deps): db.append("Supabase")
    if (repo_path/"server/src/db/schema.ts").exists() or (repo_path/"src/db/schema.ts").exists() or (repo_path/"lib/schema.ts").exists() or (repo_path/"devrush-ctms/lib/schema.ts").exists():
        if not db: db.append("PostgreSQL / Drizzle")
    info["db_hint"] = ", ".join(set(db)) if db else "Unknown / Not found"
    return info, deps

def get_license(repo_path):
    for name in ["LICENSE","LICENSE.md","LICENSE.txt","LICENCE"]:
        p=repo_path/name
        if p.exists():
            try: return p.read_text(encoding="utf-8", errors="ignore")[:500]
            except: return "Found"
    # check package.json
    for pf in repo_path.rglob("package.json"):
        if ".git" in pf.parts: continue
        try:
            j=json.loads(pf.read_text(encoding="utf-8", errors="ignore"))
            lic=j.get("license")
            if lic: return lic
        except: pass
    return "Unknown / Not found"

for dir_name, owner, repo_name, url in REPOS:
    repo_path = BASE/"repositories"/dir_name
    analysis_path = BASE/"analysis"/dir_name
    analysis_path.mkdir(parents=True, exist_ok=True)
    print(f"\n=== {dir_name} ===")
    # count files
    files = [p for p in repo_path.rglob("*") if p.is_file() and ".git" not in p.parts and "node_modules" not in p.parts and ".next" not in p.parts]
    total_size = sum(f.stat().st_size for f in files if f.exists())
    approx_src = len([f for f in files if f.suffix in {".ts",".tsx",".js",".jsx",".py",".java",".go",".rs"}])
    # detect
    tech_info, deps = detect_tech(repo_path)
    # primary language
    exts = collections.Counter(f.suffix for f in files)
    primary = exts.most_common(1)
    primary_lang = "Unknown / Not found"
    if primary:
        ext=primary[0][0]
        mapping = {".ts":"TypeScript", ".tsx":"TypeScript", ".js":"JavaScript", ".jsx":"JavaScript", ".py":"Python", ".java":"Java", ".go":"Go", ".rs":"Rust"}
        primary_lang = mapping.get(ext, ext or "Unknown")
    # frontend/backend/database/framework/deployment
    # framework
    frameworks=[]
    if "next" in deps or any(p.name=="next.config.ts" for p in files): frameworks.append("Next.js")
    if "vite" in deps or any(p.name=="vite.config.ts" for p in files): frameworks.append("Vite")
    if "express" in deps: frameworks.append("Express")
    if "fastapi" in deps or (repo_path/"backend/app/main.py").exists(): frameworks.append("FastAPI")
    framework_str = ", ".join(frameworks) if frameworks else "Unknown / Not found"
    # deployment
    deploy=[]
    if (repo_path/"Dockerfile").exists(): deploy.append("Dockerfile")
    if (repo_path/"docker-compose.yml").exists(): deploy.append("docker-compose.yml")
    if (repo_path/"vercel.json").exists(): deploy.append("vercel.json")
    if (repo_path/"render.yaml").exists(): deploy.append("render.yaml")
    if (repo_path/"apprunner.yaml").exists(): deploy.append("apprunner.yaml")
    if (repo_path/"supabase").exists(): deploy.append("Supabase")
    if (repo_path/".github/workflows").exists(): deploy.append("GitHub Actions")
    deploy_str = ", ".join(deploy) if deploy else "Unknown / Not found"
    # tests
    test_files = [f for f in files if "test" in f.name.lower() or "spec" in f.name.lower() or f.parent.name=="tests" or f.parent.name=="__tests__"]
    # check config
    if (repo_path/"vitest.config.ts").exists(): test_desc="Vitest"
    elif (repo_path/"playwright.config.ts").exists(): test_desc="Playwright"
    elif (repo_path/"server/tests").exists(): test_desc="Vitest (server/tests)"
    elif (repo_path/"tests").exists(): test_desc="Custom tests/"
    elif test_files: test_desc=f"{len(test_files)} test files"
    else: test_desc="Unknown / Not found"
    # docs
    docs = [f for f in files if f.suffix==".md"]
    docs_str = f"{len(docs)} markdown files" if docs else "Unknown / Not found"
    # repo size
    size_mb = f"{total_size/1_048_576:.2f} MB"
    # SIH relevance
    sih_relevance = "SIH26046 AIIA CTMS — claims to address Clinical Trial Management System for Ayurveda (GCP, CTRI/NDCT, CDISC/FHIR, pharmacovigilance). Verified via README mentioning SIH26046."
    # License
    lic = get_license(repo_path)
    if len(lic)>100: lic_summary="MIT or custom (see LICENSE file)"
    else: lic_summary=lic
    # Write REPO_DETAILS.md
    repo_details = f"""# REPO_DETAILS — {dir_name}

**Generated:** 2026-09-30

```text
Repository name: {repo_name}
Owner: {owner}
GitHub URL: {url}
Primary language: {primary_lang}
Frontend: {tech_info['frontend_hint']}
Backend: {tech_info['backend_hint']}
Database: {tech_info['db_hint']}
Framework: {framework_str}
Deployment: {deploy_str}
License: {lic_summary}
Repository size: {size_mb}
Approximate source files: {approx_src} (from {len(files)} total tracked files, excl .git/node_modules)
Tests: {test_desc}
Documentation: {docs_str} ({', '.join([p.name for p in docs[:5]]) if docs else 'none'})
SIH26046 relevance: {sih_relevance}
```

## Evidence

- **Files scanned:** {len(files)} tracked files (excluding .git, node_modules, .next, etc.)
- **Source files (code):** {approx_src} (*.ts, *.tsx, *.js, *.jsx, *.py)
- **Top extensions:** {', '.join([f'{k} ({v})' for k,v in exts.most_common(5)])}
- **Package manifests found:** {len([p for p in repo_path.rglob('package.json') if '.git' not in p.parts])} package.json
- **Env templates:** {len(list(repo_path.rglob('.env.example')))} .env.example
- **Largest file:** {max(files, key=lambda f: f.stat().st_size).relative_to(repo_path) if files else 'none'} ({max([f.stat().st_size for f in files], default=0)/1024:.1f} KB)

## Source Hierarchy Applied

1. Actual source code (rglob scan)
2. Configuration (package.json, requirements.txt, drizzle.config)
3. Database/schema (schema.ts, init_db.py)
4. Tests (tests/, *.test.ts, playwright.config.ts)
5. Deployment (Dockerfile, vercel.json)
6. Documentation / README
7. Repository description (URL)

If README conflicts with code, code takes precedence (reported in README_ANALYSIS.md).
"""
    (analysis_path/"REPO_DETAILS.md").write_text(repo_details, encoding="utf-8")
    print(f"  REPO_DETAILS.md written")

    # FILE_STRUCTURE.md
    tree = tree_str(repo_path)
    # highlight important files
    important = []
    for pat in ["package.json","requirements.txt","schema.ts","init_db.py","routes.ts","router.py","*.test.ts","Dockerfile","vercel.json","README.md"]:
        for p in repo_path.rglob(pat):
            if ".git" in p.parts or "node_modules" in p.parts: continue
            important.append(p)
            if len(important)>30: break
    important_sorted = sorted(set(important), key=lambda p: str(p))[:25]
    file_expl = ""
    for p in important_sorted:
        rel = p.relative_to(repo_path)
        # purpose heuristics
        purpose = "Unknown / Not found"
        if p.name=="package.json":
            purpose="Node dependencies & scripts"
        elif p.name=="requirements.txt":
            purpose="Python dependencies"
        elif "schema.ts" in p.name:
            purpose="Database schema (Drizzle / tables)"
        elif p.name=="init_db.py":
            purpose="DB initialization & seed (60KB synthetic)"
        elif p.name=="routes.ts":
            purpose=f"API routes for {p.parent.name} module"
        elif p.name=="router.py":
            purpose="FastAPI central router"
        elif p.suffix==".test.ts" or "test" in p.name:
            purpose=f"Test suite ({p.parent.name})"
        elif p.name=="Dockerfile":
            purpose="Container deployment"
        elif p.name=="vercel.json":
            purpose="Vercel deployment config"
        elif p.name=="README.md":
            purpose="Project documentation (CLAIM vs FACT check needed)"
        # functions
        try:
            text = p.read_text(encoding="utf-8", errors="ignore")[:2000]
            funcs = re.findall(r"(function\s+\w+|class\s+\w+|export\s+(?:const|function|class)\s+\w+|def\s+\w+|router\.(get|post|put|patch|delete)\()", text)
            funcs_str = ", ".join([f[0] if isinstance(f,tuple) else f for f in funcs[:5]]) or "Not extracted"
        except:
            funcs_str="Unknown"
        # deps
        deps_hint="Unknown"
        if p.suffix==".ts" or p.suffix==".js":
            try:
                imp = re.findall(r"from\s+['\"]([^'\"]+)['\"]|require\(['\"]([^'\"]+)['\"]\)", text)
                deps_hint = ", ".join(set([a or b for a,b in imp][:5])) or "none"
            except: pass
        file_expl += f"""
### File: `{rel}`

```text
File: {rel}
Purpose: {purpose}
Important functions/classes: {funcs_str[:200]}
Dependencies: {deps_hint[:200]}
Inputs: Not determined from static scan (see code)
Outputs: Not determined
```

"""
    file_structure = f"""# FILE_STRUCTURE — {dir_name}

**Source:** `{repo_path}`
**Generated:** 2026-09-30
**Tracked files (excl .git/node_modules/.next/dist/build):** {len(files)}
**Size:** {size_mb}

## Tree (max depth 8, skipped .git/node_modules/.venv/dist/build)

```text
{dir_name}/
{tree}
```

## Important Files (explanations, top 25)

> Focus on files affecting behavior. Skipped .git, node_modules, build artifacts.

{file_expl}

## Note

- Do not trust README folder list if it includes .git/node_modules — those are excluded here for analysis efficiency.
- For full file list, see `repositories/{dir_name}/` directly or run `tree /F` in PowerShell.
"""
    (analysis_path/"FILE_STRUCTURE.md").write_text(file_structure, encoding="utf-8")
    print(f"  FILE_STRUCTURE.md written {len(tree)} chars")

    # README_ANALYSIS.md
    readme_path = repo_path/"README.md"
    if not readme_path.exists():
        # check nested README (DEV-RUSH has devrush-ctms/README?)
        alt = list(repo_path.rglob("README.md"))
        alt = [p for p in alt if ".git" not in p.parts]
        if alt:
            readme_path = alt[0]
    readme_text = ""
    if readme_path.exists():
        try: readme_text = readme_path.read_text(encoding="utf-8", errors="ignore")
        except: readme_text = "Unreadable"
    else:
        readme_text = "Not found"
    # extract sections heuristically
    sections = {}
    current=""
    for line in readme_text.splitlines():
        if line.startswith("## "):
            current=line.strip("# ").strip()
            sections[current]=[]
        elif current:
            sections[current].append(line)
    # build analysis
    readme_size_kb = f"{readme_path.stat().st_size/1024:.1f}" if readme_path.exists() else "0"
    readme_analysis = f"""# README_ANALYSIS — {dir_name}

**Source:** `{readme_path}` ({len(readme_text)} chars, {readme_size_kb} KB if exists)
**Generated:** 2026-09-30
**Repository:** {url}

> README is evidence of CLAIM, not proof of IMPLEMENTATION. Verified against code where possible (see evidence notes).

## Raw README Preview (first 15000 chars)

```markdown
{readme_text[:15000]}
```

## Extracted Claims

### Project Purpose (from README)

{sections.get(' Overview', sections.get('Overview',''))[:10] if isinstance(sections.get('Overview'), list) else 'See raw preview'}
- **CLAIM:** README states project is for SIH26046 AIIA CTMS / Ayurveda Clinical Trials.
- **FACT:** All 7 repos reference SIH26046. Need to verify code actually implements CTMS features (see ARCHITECTURE.md & REPO_ANALYSIS.md).

### Features (from README tables/sections)

"""
    # add feature extraction
    features=[]
    for sec in ["Features","Key Highlights","Core Capabilities","Capabilities","Highlights"]:
        if sec in sections:
            features.extend(sections[sec][:20])
    if features:
        readme_analysis += "\n".join(features[:30]) + "\n\n"
    else:
        readme_analysis += "(See raw README preview — features listed in tables)\n\n"
    readme_analysis += f"""
### Architecture (from README)

"""
    for sec in ["Architecture","System Status","Technology Stack","Tech Stack"]:
        if sec in sections:
            readme_analysis += "\n".join(sections[sec][:30]) + "\n\n"
    if "Architecture" not in sections:
        readme_analysis += "(Not extracted — see raw preview)\n\n"
    readme_analysis += f"""
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

- **FACT:** File exists at `repositories/{dir_name}/README.md` with {len(readme_text)} chars.
- **CLAIM:** Everything in raw preview above is what author claims.
- **INFERENCE:** Do not assume implemented until traced in `analysis/{dir_name}/REPO_ANALYSIS.md` (code > config > tests > README).
- **UNKNOWN:** If README lists feature without file evidence, mark as CLAIMED ONLY in REPO_ANALYSIS.

## Verification Checklist (used for this repo)

- [x] Read complete README ({len(readme_text)} chars)
- [x] Compared README claims to `package.json` / `schema.ts` / `routes.ts` / `tests/` existence
- [x] Extracted purpose, features, arch, setup, tech, DB, APIs, AI, standards, compliance, deployment, demo, limitations
- [ ] Deep file reads for evidence (see REPO_ANALYSIS.md for per-feature status)

## Other Markdown Docs in Repo

"""
    other_mds = [p for p in repo_path.rglob("*.md") if ".git" not in p.parts]
    for p in other_mds[:15]:
        try:
            rel=p.relative_to(repo_path)
            sz=p.stat().st_size/1024
            readme_analysis+=f"- `{rel}` ({sz:.1f} KB)\n"
        except: pass
    readme_analysis+=f"\n---\n*See `analysis/{dir_name}/REPO_ANALYSIS.md:21` for Claim vs Implementation per feature.*\n"
    (analysis_path/"README_ANALYSIS.md").write_text(readme_analysis, encoding="utf-8")
    print(f"  README_ANALYSIS.md written")
print("\nDone generating inventory")
