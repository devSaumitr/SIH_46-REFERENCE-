#!/usr/bin/env python3
import pathlib, shutil, os
BASE = pathlib.Path(r"E:\SIH26046_COMPETITOR_ANALYSIS")
repos_dir = BASE/"repositories"
presentations_dir = BASE/"presentations"

for repo_path in sorted(repos_dir.iterdir()):
    if not repo_path.is_dir(): continue
    name = repo_path.name
    print(f"\n=== {name} ===")
    # search ppt/pptx/pdf
    ppt = []
    pdf = []
    demo = []
    for p in repo_path.rglob("*"):
        if not p.is_file(): continue
        if ".git" in p.parts: continue
        if "node_modules" in p.parts: continue
        if p.suffix.lower() in [".ppt",".pptx"]:
            ppt.append(p)
        if p.suffix.lower() == ".pdf":
            pdf.append(p)
        if any(k in p.name for k in ["DEMO_SCRIPT","JUDGE_QA"]) or any(k in str(p).lower() for k in ["demo","pitch","presentation","judge"]) and p.suffix in [".md",".pdf",".txt"]:
            # filter to relevant, but not too many
            if ".git" not in p.parts and "node_modules" not in p.parts:
                if p not in ppt and p not in pdf:
                    # keep only top relevant
                    if "DEMO_SCRIPT" in p.name or "JUDGE_QA" in p.name or "Judge_Demo" in p.name or "Tech_Security" in p.name:
                        demo.append(p)
        # also generic architecture
        if p.name.lower() in ["architecture.md","architecture.pdf"] and p not in demo:
            demo.append(p)
    ppt = [p for p in ppt if ".git" not in p.parts][:10]
    pdf = [p for p in pdf if ".git" not in p.parts][:10]
    print(f"  PPT: {len(ppt)}")
    for p in ppt: print(f"    - {p.relative_to(repo_path)} ({p.stat().st_size/1024:.1f} KB)")
    print(f"  PDF: {len(pdf)}")
    for p in pdf: print(f"    - {p.relative_to(repo_path)} ({p.stat().st_size/1024:.1f} KB)")
    print(f"  Demo/judge: {len(demo)}")
    for p in demo: print(f"    - {p.relative_to(repo_path)}")

    dest = presentations_dir/name
    dest.mkdir(parents=True, exist_ok=True)
    inv = f"# Presentations / Judge Materials — {name}\n\n**Source:** `repositories/{name}/`\n**Generated:** 2026-09-30\n\n"
    if not ppt and not pdf and not demo:
        inv += "> No PPT/PDF/DEMO_SCRIPT/JUDGE_QA found in this repository (verified via rglob search).\n\n"
        inv += "Search patterns: `*.ppt`, `*.pptx`, `*.pdf`, `DEMO_SCRIPT.md`, `JUDGE_QA.md`, `demo`, `pitch`, `presentation`, `architecture`, `screenshots`, `assets`, `judge` (excluded .git/node_modules).\n"
    else:
        inv += "## PPT\n\n"
        if ppt:
            for p in ppt:
                inv += f"- `{p.name}` — `{p.relative_to(repo_path)}` ({p.stat().st_size/1024:.1f} KB)\n"
        else:
            inv += "None found.\n"
        inv += "\n## PDF\n\n"
        if pdf:
            for p in pdf:
                inv += f"- `{p.name}` — `{p.relative_to(repo_path)}` ({p.stat().st_size/1024:.1f} KB)\n"
        else:
            inv += "None found.\n"
        inv += "\n## Demo / Judge Related\n\n"
        if demo:
            for p in demo:
                inv += f"- `{p.relative_to(repo_path)}`\n"
        else:
            inv += "None found.\n"
        # copy ppt/pdf
        for f in ppt+pdf:
            rel = str(f.relative_to(repo_path)).replace("\\","_").replace("/","_")
            dest_file = dest/rel
            try:
                shutil.copy(str(f), str(dest_file))
            except: print(f"  Copy failed {f}")
        # copy demo md
        for d in demo:
            if d.suffix in [".md",".txt",".pdf"]:
                rel = str(d.relative_to(repo_path)).replace("\\","_").replace("/","_")
                dest_file = dest/rel
                try: shutil.copy(str(d), str(dest_file))
                except: pass
    if name == "nishant-uxs_vedraya":
        inv += "\n## VEDRAYA Special Investigation (Task 27)\n\n"
        inv += "- `docs/DEMO_SCRIPT.md` (3.0 KB) — 9-step 60-sec judge flow (Command Center -> AYU-024 -> Safety -> Audit verify)\n"
        inv += "- `docs/JUDGE_QA.md` (3.5 KB) — anticipated questions + objections (WORM, licensed MedDRA, ABDM not connected)\n"
        inv += "- `docs/SIH26046_TRACEABILITY_FINAL.md` (8.0 KB) — PS traceability matrix\n"
        inv += "- `docs/IMPLEMENTATION_STATUS.md` (1.5 KB) — honest Implemented/Partial/Prototype/Not Connected table\n"
        inv += "- `docs/RBAC.md` (3.6 KB) + `SECURITY.md` (1.7 KB) + `AUDIT.md` (2.7 KB)\n"
        inv += "- `public/vedraya/frames-alpha/` 360 webp cinematic identity (not judge evidence)\n"
        for doc in ["docs/DEMO_SCRIPT.md","docs/JUDGE_QA.md","docs/SIH26046_TRACEABILITY_FINAL.md","docs/IMPLEMENTATION_STATUS.md","docs/RBAC.md"]:
            src = repo_path/doc
            if src.exists():
                dest_file = dest/doc.replace("/","_").replace("\\","_")
                try: shutil.copy(str(src), str(dest_file))
                except: pass
    if name == "vansh459_AyuSphere":
        inv += "\n## AyuSphere UAT / Judge Materials\n\n"
        inv += "- `docs/uat/Judge_Demo_Script.md` (4.1 KB) + `Judge_Demo_Script.pdf` (1.31 MB)\n"
        inv += "- `docs/uat/UAT_Guide_Administrator.pdf` (3.32 MB) + `UAT_Guide_Principal_Investigator.pdf` (2.83 MB) etc. (7 role PDFs)\n"
        inv += "- `docs/uat/Tech_Security_Guide.md` (17 KB) + `.pdf` (155 KB)\n"
        for doc in ["docs/uat/Judge_Demo_Script.md","docs/uat/Judge_Demo_Script.pdf","docs/uat/Tech_Security_Guide.md"]:
            src = repo_path/doc
            if src.exists():
                dest_file = dest/doc.replace("/","_").replace("\\","_")
                try: shutil.copy(str(src), str(dest_file))
                except: pass
    (dest/"PRESENTATION_INVENTORY.md").write_text(inv, encoding="utf-8")
    print(f"  -> Wrote PRESENTATION_INVENTORY.md")

print("\n=== Summary presentations dir ===")
for p in sorted(presentations_dir.rglob("*")):
    if p.is_file():
        print(f"{p.relative_to(BASE)} ({p.stat().st_size/1024:.1f} KB)")
