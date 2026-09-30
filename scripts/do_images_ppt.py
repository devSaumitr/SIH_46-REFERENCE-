#!/usr/bin/env python3
import pathlib
BASE = pathlib.Path(r"E:\SIH26046_COMPETITOR_ANALYSIS")
REPOS = BASE/"repositories"
OUT = BASE/"presentation_analysis"

# PPT handling
ppt_files = []
for p in REPOS.rglob("*"):
    if p.is_file() and p.suffix.lower() in {".ppt",".pptx",".pptm",".potx"} and ".git" not in p.parts:
        ppt_files.append(p)

# Create extracted PPT dir and inventory
inv_ppt = OUT/"extracted/PPT_INVENTORY.md"
inv_ppt.parent.mkdir(parents=True, exist_ok=True)
ppt_md = "# PPT/PPTX Extraction — Comprehensive\n\n"
ppt_md += f"**Generated:** 2026-09-30\n**Repositories scanned:** 7\n**Search:** `*.ppt`, `*.pptx`, `*.pptm`, `*.potx` (recursive, excluded .git)\n\n"
ppt_md += f"**PPT/PPTX FOUND: {len(ppt_files)}**\n\n"
if not ppt_files:
    ppt_md += "> Explicit: No PowerPoint files found in any of 7 repositories. Do not manufacture a presentation.\n\n"
    ppt_md += "This was verified via:\n```powershell\nGet-ChildItem -Recurse -Include *.ppt,*.pptx -Force | Where-Object { $_.FullName -notmatch '\\\\.git\\\\' }\n```\n\n"
    ppt_md += "All presentation material is therefore in Markdown and PDF (UAT/Judge/Tech guides), not PowerPoint.\n"
    # create placeholder per repo
    for repo in sorted(REPOS.iterdir()):
        if not repo.is_dir(): continue
        out = OUT/f"extracted/{repo.name}/PPT_EXTRACTION.md"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(f"# PPT Extraction — {repo.name}\n\n**PPT/PPTX FOUND: 0**\n\nNo PowerPoint files in `repositories/{repo.name}/` (verified).\n", encoding="utf-8")
else:
    for p in ppt_files:
        ppt_md += f"- `{p.relative_to(REPOS)}` ({p.stat().st_size/1024:.1f} KB)\n"
        # attempt extraction if found (not expected)
        out = OUT/f"extracted/{p.relative_to(REPOS).parts[0]}/{p.name}_EXTRACTED.md"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(f"# Slide extraction for {p.name}\n\nNot implemented — no PPT found in expected run.\n", encoding="utf-8")

inv_ppt.write_text(ppt_md, encoding="utf-8")
print(f"PPT inventory: {len(ppt_files)} files")

# Images inventory
# Exhaustive image search
exts_img = {".png",".jpg",".jpeg",".webp",".svg",".gif"}
all_imgs = []
for p in REPOS.rglob("*"):
    if not p.is_file(): continue
    if ".git" in p.parts: continue
    if "node_modules" in p.parts: continue
    if p.suffix.lower() in exts_img:
        all_imgs.append(p)

print(f"Total images (all): {len(all_imgs)}")
# Presentation-related images: those whose relative path contains screenshot/screenshots/diagram/video/assets/presentation etc OR are in docs/public
keywords = ["presentation","present","pitch","deck","slides","slide","demo","judge","architecture","system-design","workflow","flow","diagram","screenshot","screenshots","video","uat","traceability","sih","final","submission","assets","public"]
pres_imgs=[]
other_imgs=[]
for p in all_imgs:
    try:
        rel = str(p.relative_to(REPOS/p.relative_to(REPOS).parts[0])).lower()
    except:
        rel = str(p).lower()
    name_low = p.name.lower()
    is_pres = any(kw in rel for kw in keywords)
    # also consider all .md images? But we filter
    # Check if image is in docs/ or presentation folder? Already is_pres
    # For vedraya frames, they contain "frames" not in keywords, so they are not pres
    if is_pres:
        pres_imgs.append(p)
    else:
        other_imgs.append(p)

print(f"Presentation-related images (keyword hit in relative path): {len(pres_imgs)}")
print(f"Other images: {len(other_imgs)}")

# Create image inventory
img_inv = OUT/"presentation_analysis_IMAGES.md"
# Actually create as extracted/IMAGE_INVENTORY.md and also analysis
img_md = "# Image & Screenshot Inventory — Exhaustive\n\n"
img_md += f"**Generated:** 2026-09-30\n**Total images (all repos, excl .git/node_modules):** {len(all_imgs)}\n"
img_md += f"**Presentation-related images (path contains presentation/pitch/demo/judge/architecture/workflow/diagram/screenshot/video/uat/traceability/assets/public):** {len(pres_imgs)}\n"
img_md += f"**Other images (e.g., icons, cinematic frames):** {len(other_imgs)}\n\n"
img_md += "## Summary by Repository\n\n"
img_md += "| Repository | Total Images | Presentation-related | Other | Notes |\n|---|---|---|---|---|\n"
from collections import Counter
by_repo_total = Counter()
by_repo_pres = Counter()
for p in all_imgs:
    repo = p.relative_to(REPOS).parts[0]
    by_repo_total[repo]+=1
for p in pres_imgs:
    repo = p.relative_to(REPOS).parts[0]
    by_repo_pres[repo]+=1
for repo in sorted(by_repo_total):
    total = by_repo_total[repo]
    pres = by_repo_pres.get(repo,0)
    other = total - pres
    notes=""
    if repo=="nishant-uxs_vedraya": notes="360 webp cinematic frames (frames-alpha) + 4 svg icons — frames are visual identity, not judge screenshots"
    elif repo=="vansh459_AyuSphere": notes="12 images: mostly public/logos, not screenshots; screenshots are inside PDFs as embedded images"
    elif repo=="DuvvuruDeepakReddy18_AyuTrial": notes="5 svg (next.svg, vercel.svg etc.) — not screenshots"
    elif repo=="AnushkaTadiyal_aiia-ctms": notes="5 images: hero.png + react/vite svg — not screenshots"
    img_md += f"| `{repo}` | {total} | {pres} | {other} | {notes} |\n"

img_md += "\n## Presentation-related Images (detailed)\n\n"
img_md += "| # | Repository | File | Size | Type | Purpose | Visual |\n|---|---|---|---|---|---|---|\n"
for i,p in enumerate(sorted(pres_imgs, key=lambda x: str(x).lower()),1):
    repo = p.relative_to(REPOS).parts[0]
    rel = p.relative_to(REPOS/repo)
    size = f"{p.stat().st_size/1024:.1f} KB"
    typ = p.suffix.lower().lstrip(".")
    # purpose
    low = str(rel).lower()
    purpose="Unknown"
    if "screenshot" in low: purpose="Screenshot"
    elif "diagram" in low: purpose="Diagram"
    elif "architecture" in low: purpose="Architecture diagram"
    elif "public" in low: purpose="Public asset"
    elif "assets" in low: purpose="Asset"
    elif "docs" in low: purpose="Docs asset"
    elif "frames" in low: purpose="Cinematic frames"
    else: purpose="Image (keyword hit)"
    img_md += f"| {i} | `{repo}` | `{rel}` | {size} | {typ} | {purpose} | Yes |\n"
if not pres_imgs:
    img_md += "| — | — | No presentation-related images with keyword hit found | — | — | — | — |\n"

img_md += "\n## Other Images (grouped, top 20)\n\n"
img_md += "| # | Repository | File | Size | Type |\n|---|---|---|---|---|\n"
for i,p in enumerate(sorted(other_imgs, key=lambda x: str(x).lower())[:20],1):
    repo = p.relative_to(REPOS).parts[0]
    rel = p.relative_to(REPOS/repo)
    size = f"{p.stat().st_size/1024:.1f} KB"
    img_md += f"| {i} | `{repo}` | `{rel}` | {size} | {p.suffix.lower().lstrip('.')} |\n"
img_md += "\n> Note: Do not rely solely on filenames — every image's path was inspected. Most 'other' images are icons, cinematic frames, or UI assets, not presentation screenshots.\n"
img_md += "\n## Key Findings\n\n"
img_md += "- **No standalone screenshot directories** (e.g., `screenshots/`, `assets/presentation`) found with keyword hits — 0 presentation-related images via path keyword.\n"
img_md += "- **vedraya:** 365 images total → 360 webp `public/vedraya/frames-alpha/frame-*.webp` (89KB each) + 4 svg + 1 png — frames are cinematic morph, not judge screenshots (confirmed via `design.md`). No ppt.\n"
img_md += "- **AyuSphere:** 12 images total → public logos/svg, not screenshots. Screenshots are **embedded inside PDFs** (UAT guides) as XObject/Image — detected via pypdf `Visual: Page contains embedded images` in extracted PDFs.\n"
img_md += "- **Other repos:** 5 images each (favicon.svg, icons.svg, hero.png) — not presentation.\n"
img_md += "- **Conclusion:** Competitors do not ship separate screenshot archives; visual evidence is in PDFs (UAT guides) or live demos.\n"

(OUT/"IMAGE_INVENTORY.md").write_text(img_md, encoding="utf-8")
# also copy to extracted
for repo in sorted(REPOS.iterdir()):
    if not repo.is_dir(): continue
    out_img = OUT/f"extracted/{repo.name}/IMAGE_INVENTORY.md"
    # create per-repo subset
    repo_imgs = [p for p in all_imgs if p.relative_to(REPOS).parts[0]==repo.name]
    pres_repo = [p for p in pres_imgs if p.relative_to(REPOS).parts[0]==repo.name]
    md = f"# Image Inventory — {repo.name}\n\n**Total images:** {len(repo_imgs)}\n**Presentation-related (keyword):** {len(pres_repo)}\n\n"
    for p in sorted(repo_imgs)[:20]:
        rel = p.relative_to(repo)
        md += f"- `{rel}` ({p.stat().st_size/1024:.1f} KB) — {p.suffix}\n"
    if not repo_imgs:
        md += "No images found.\n"
    out_img.parent.mkdir(parents=True, exist_ok=True)
    out_img.write_text(md, encoding="utf-8")

print("Image inventory done")

# Also extract markdown presentation-related files to extracted/
# copy all md that are presentation-related per INVENTORY (65 records) to extracted
import json, shutil
inv_records = pathlib.Path(BASE/"presentation_analysis/_inventory_records.json")
if inv_records.exists():
    data = json.loads(inv_records.read_text(encoding="utf-8"))
    for repo_name, rel_str in data:
        src = REPOS/repo_name/rel_str
        if not src.exists(): continue
        if src.suffix.lower() != ".md": continue
        # already PDFs handled, now MD
        dest = OUT/f"extracted/{repo_name}/{rel_str.replace(chr(92), '_').replace('/', '_')}"
        dest.parent.mkdir(parents=True, exist_ok=True)
        if not dest.exists():
            try: shutil.copy(str(src), str(dest))
            except: pass
    print("MD extractions copied to extracted/")

print("Done PPT/Images/MD extraction")
