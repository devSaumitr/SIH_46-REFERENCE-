#!/usr/bin/env python3
"""
SIH Problem 46 - Repo Extractor (Python version)
Cross-platform alternative to extract_repos.ps1
Usage: python scripts/extract_repos.py
"""
import os, pathlib, datetime, subprocess, collections, textwrap, shutil, zipfile

ROOT = pathlib.Path(r"E:\SIH_46")
RAW = ROOT / "repos_raw"
OUT = ROOT / "repo_extracts"
DOCS = ROOT / "docs"

SKIP_DIRS = {".git","node_modules",".venv","venv","__pycache__",".next","dist","build",".idea",".vscode"}

def tree_str(path: pathlib.Path, max_depth=8, prefix="", depth=0):
    if depth>max_depth: return ""
    try: items = sorted(path.iterdir(), key=lambda p: (not p.is_dir(), p.name.lower()))
    except: return ""
    out=""
    for i,p in enumerate(items):
        is_last = i==len(items)-1
        branch = "└── " if is_last else "├── "
        next_prefix = prefix + ("    " if is_last else "│   ")
        if p.name in SKIP_DIRS:
            out+=f"{prefix}{branch}{p.name}/ [skipped]\n"
            continue
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

def file_stats(repo: pathlib.Path):
    files=[]
    for p in repo.rglob("*"):
        if not p.is_file(): continue
        if ".git" in p.parts or "node_modules" in p.parts: continue
        files.append(p)
    total = sum(f.stat().st_size for f in files if f.exists())
    exts = collections.Counter(f.suffix or "(no ext)" for f in files)
    largest = sorted(files, key=lambda f: f.stat().st_size if f.exists() else 0, reverse=True)[:10]
    md="## File Statistics\n\n"
    md+=f"- **Total Files:** {len(files)}\n"
    md+=f"- **Total Size:** {total/1_048_576:.2f} MB\n"
    md+=f"- **Last Modified:** {datetime.datetime.fromtimestamp(repo.stat().st_mtime)}\n\n"
    md+="### Top Extensions\n\n| Extension | Count |\n|---|---|\n"
    for ext,c in exts.most_common(15): md+=f"| {ext} | {c} |\n"
    md+="\n### Largest Files (top 10)\n\n| File | Size |\n|---|---|\n"
    for f in largest:
        rel=f.relative_to(repo)
        sz=f.stat().st_size
        s=f"{sz/1_048_576:.2f} MB" if sz>1_048_576 else f"{sz/1024:.1f} KB"
        md+=f"| {rel} | {s} |\n"
    return md

def main():
    for d in [OUT, DOCS, RAW]: d.mkdir(parents=True, exist_ok=True)
    print(f"=== SIH 46 Python Extractor ===\nRaw: {RAW}\nOut: {OUT}")
    # unzip
    for z in RAW.glob("*.zip"):
        dest = RAW / z.stem
        if not dest.exists():
            print(f"Extracting {z.name} -> {dest}")
            with zipfile.ZipFile(z) as zf: zf.extractall(dest)
    # clone from urls.txt
    urls_file = RAW/"urls.txt"
    if urls_file.exists():
        for line in urls_file.read_text().splitlines():
            line=line.strip()
            if not line or line.startswith("#"): continue
            name=line.rsplit("/",1)[-1].replace(".git","").strip() or "repo"
            dest=RAW/name
            if not dest.exists():
                print(f"Cloning {line} -> {dest}")
                subprocess.run(["git","clone",line,str(dest)])
    repos=[p for p in RAW.iterdir() if p.is_dir()]
    if not repos:
        print(f"No repos in {RAW}. Place folders/zips/urls.txt there.")
        return
    rows=[]
    for repo in repos:
        name=repo.name
        print(f"\n--- {name} ---")
        ex=OUT/name; ex.mkdir(exist_ok=True)
        # 01
        tree=tree_str(repo)
        (ex/"01_STRUCTURE.md").write_text(f"# File Structure — {name}\n\n**Source:** `{repo}`\n**Generated:** {datetime.datetime.now()}\n\n```text\n{name}/\n{tree}```\n", encoding="utf-8")
        (ex/"tree.txt").write_text(f"{name}/\n{tree}", encoding="utf-8")
        # 02 readme
        readmes=list(repo.rglob("README*.md"))+list(repo.rglob("readme*.md"))
        readmes=list({r.resolve():r for r in readmes}.values())  # dedupe
        md=f"# README Inventory — {name}\n\n**Generated:** {datetime.datetime.now()}\n\n"
        if not readmes:
            md+="> ⚠️ No README.md found\n"
        else:
            md+=f"Found **{len(readmes)}** README(s):\n\n| # | Path | Size | Modified |\n|---|---|---|---|\n"
            for i,r in enumerate(readmes,1):
                rel=r.relative_to(repo)
                md+=f"| {i} | `{rel}` | {r.stat().st_size/1024:.1f} KB | {datetime.datetime.fromtimestamp(r.stat().st_mtime).date()} |\n"
            md+="\n---\n\n"
            for r in readmes:
                rel=r.relative_to(repo)
                txt=r.read_text(encoding="utf-8", errors="ignore")[:15000]
                md+=f"## File: `{rel}`\n\n```markdown\n{txt}\n```\n\n"
        other=[p for p in repo.rglob("*.md") if ".git" not in p.parts]
        if len(other)>len(readmes):
            md+="\n---\n\n## Other Markdown Docs\n\n| File | Size | Path |\n|---|---|---|\n"
            for d in other[:20]:
                if d in readmes: continue
                md+=f"| {d.name} | {d.stat().st_size/1024:.1f} KB | `{d.relative_to(repo)}` |\n"
        (ex/"02_README_CONTENT.md").write_text(md, encoding="utf-8")
        # 03 details
        stats=file_stats(repo)
        details=f"# Repo Details — {name}\n\n**Path:** `{repo}`\n\n**Generated:** {datetime.datetime.now()}\n\n{stats}\n\n"
        details+="## Tech Stack Hints\n\n| Indicator | Found |\n|---|---|\n"
        hints=[("package.json","Node.js"),("requirements.txt","Python"),("pyproject.toml","Python poetry"),("Dockerfile","Docker"),("docker-compose.yml","Compose"),("*.py","Python files"),("*.ipynb","Jupyter"),("pom.xml","Maven"),("build.gradle","Gradle"),("go.mod","Go")]
        for pat,tech in hints:
            found=any(repo.rglob(pat))
            details+=f"| {tech} (`{pat}`) | {'✅' if found else '—'} |\n"
        details+="\n## Top-Level Contents\n\n```text\n"
        for p in sorted(repo.iterdir(), key=lambda x: x.name):
            details+=f"{'DIR ' if p.is_dir() else 'FILE'}  {p.name}\n"
        details+="```\n"
        if (repo/".git").exists():
            try:
                branch=subprocess.check_output(["git","-C",str(repo),"rev-parse","--abbrev-ref","HEAD"], text=True).strip()
                log=subprocess.check_output(["git","-C",str(repo),"log","--oneline","-5"], text=True).strip()
                remote=subprocess.check_output(["git","-C",str(repo),"remote","-v"], text=True).strip()
                details+=f"\n## Git Info\n\n**Branch:** `{branch}`\n\n```text\n{remote}\n```\n\n**Last 5 commits:**\n```text\n{log}\n```\n"
            except: pass
        (ex/"03_DETAILS.md").write_text(details, encoding="utf-8")
        # 00 combined
        combined=f"# Combined Report — {name}\n\n> Auto-generated from `{repo}` on {datetime.datetime.now()}\n\n---\n\n"
        combined+=(ex/"01_STRUCTURE.md").read_text(encoding="utf-8")+"\n\n---\n\n"
        combined+=(ex/"02_README_CONTENT.md").read_text(encoding="utf-8")+"\n\n---\n\n"
        combined+=(ex/"03_DETAILS.md").read_text(encoding="utf-8")
        (ex/"00_FULL_REPORT.md").write_text(combined, encoding="utf-8")
        rows.append((name, len(list(repo.rglob('*'))), len(readmes)))
        print(f"  ✓ 01 02 03 00")
    # index
    idx="# SIH Problem 46 — Repo Extracts Index\n\n"
    idx+=f"**Generated:** {datetime.datetime.now()}\n\n**Raw:** `{RAW}`  **Extracts:** `{OUT}`\n\n## Repos\n\n| # | Repo | READMEs | Extract |\n|---|---|---|---|\n"
    for i,(n,_,r) in enumerate(rows,1):
        idx+=f"| {i} | `{n}` | {'✅' if r else '❌'} ({r}) | `repo_extracts/{n}/` |\n"
    idx+="\n## Per-Repo Files\n\nEach `repo_extracts/<repo>/` contains:\n- `00_FULL_REPORT.md` — combined\n- `01_STRUCTURE.md` — tree\n- `02_README_CONTENT.md` — README location+content\n- `03_DETAILS.md` — stats/tech/git\n- `tree.txt` — plain tree\n"
    (DOCS/"INDEX.md").write_text(idx, encoding="utf-8")
    print(f"\nDone: {len(rows)} repos -> {DOCS/'INDEX.md'}")

if __name__=="__main__": main()
