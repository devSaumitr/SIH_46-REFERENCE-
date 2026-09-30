#!/usr/bin/env python3
import pathlib, re, sys
try:
    from pypdf import PdfReader
except: 
    print("pypdf not available")
    sys.exit(1)

BASE = pathlib.Path(r"E:\SIH26046_COMPETITOR_ANALYSIS")
REPOS = BASE/"repositories"
OUT_BASE = BASE/"presentation_analysis/extracted"

pdfs = list(REPOS.rglob("*.pdf"))
pdfs = [p for p in pdfs if ".git" not in p.parts and "node_modules" not in p.parts]
print(f"Found {len(pdfs)} PDFs")

for pdf_path in sorted(pdfs):
    repo_name = pdf_path.relative_to(REPOS).parts[0]
    # relative inside repo
    rel = pdf_path.relative_to(REPOS/repo_name)
    out_dir = OUT_BASE/repo_name
    out_dir.mkdir(parents=True, exist_ok=True)
    out_file = out_dir / (str(rel).replace("\\","_").replace("/","_") + ".md")
    print(f"\n=== {repo_name} / {rel} ({pdf_path.stat().st_size/1024:.1f} KB) -> {out_file.name} ===")
    try:
        reader = PdfReader(str(pdf_path))
        num_pages = len(reader.pages)
        print(f"  Pages: {num_pages}")
    except Exception as e:
        print(f"  Failed to read: {e}")
        out_file.write_text(f"# PDF Extraction — {rel}\n\n**Repository:** {repo_name}\n**File:** `{rel}`\n**Size:** {pdf_path.stat().st_size/1024:.1f} KB\n**Pages:** Unknown\n\n**TEXT EXTRACTION INCOMPLETE:** {e}\n", encoding="utf-8")
        continue

    md = f"# PDF Extraction — {rel}\n\n"
    md += f"**Repository:** `{repo_name}`\n"
    md += f"**File:** `{rel}`\n"
    md += f"**Size:** {pdf_path.stat().st_size/1024:.1f} KB ({pdf_path.stat().st_size} bytes)\n"
    md += f"**Pages:** {num_pages}\n"
    md += f"**Source:** `repositories/{repo_name}/{rel}`\n"
    md += f"**Generated:** 2026-09-30 (pypdf {reader} )\n\n"
    md += "---\n\n"
    md += "## Summary (heuristic)\n\n"
    # Try to extract headings via font? pypdf doesn't give font; we do heuristic via uppercase lines
    md += f"- **Pages:** {num_pages}\n"
    md += f"- **Extraction method:** pypdf text extraction (preserves page numbers, headings inferred via line case)\n\n"

    # Extract text per page
    for i, page in enumerate(reader.pages, 1):
        try:
            text = page.extract_text() or ""
        except Exception as e:
            text = f"[Page {i} extraction failed: {e}]"
        # basic heuristics
        # Identify headings: lines that are uppercase or start with number. like "1. Introduction"
        lines = text.splitlines()
        # tables: detect lines with multiple spaces or | or tab
        has_table = any(re.search(r"\s{3,}", l) and "|" in l or "\t" in l for l in lines) # not perfect
        # diagrams/screenshots: if page contains /Image
        has_images = False
        try:
            # check if page has images via /XObject
            if "/Image" in str(page.get_object()) or "/XObject" in str(page.get_object()):
                has_images = True
        except: pass

        md += f"## Page {i} / {num_pages}\n\n"
        if has_images:
            md += "> **Visual:** Page contains embedded images/screenshots/diagrams (detected via XObject/Image). See original PDF for rendering.\n\n"
        # Try to detect headings: first non-empty line that is short and uppercase or title case
        headings = []
        for l in lines[:10]:
            stripped = l.strip()
            if len(stripped)>3 and len(stripped)<80 and (stripped.isupper() or re.match(r"^\d+[\.\)]\s+.*", stripped)):
                headings.append(stripped)
                if len(headings)>=3: break
        if headings:
            md += "**Headings (heuristic):**\n"
            for h in headings: md += f"- `{h}`\n"
            md += "\n"
        # Tables heuristic
        # Look for lines that look like table rows (contain multiple words separated by 2+ spaces or pipe)
        table_lines = [l for l in lines if re.search(r"\|", l) or l.count("  ")>=2 or re.search(r"\t", l)]
        if len(table_lines)>=2:
            md += "**Tables (heuristic):** Lines that appear tabular (pipe or multi-space):\n```text\n"
            for tl in table_lines[:10]:
                md += tl + "\n"
            md += "```\n\n"
        # Important claims: search for compliance/ai/fhir etc
        claims_keywords = ["21 CFR","GCP","FHIR","CDISC","SDTM","ABDM","CTRI","NDCT","DPDP","AI","ML","audit","RBAC","pharmacovigilance","NPvCC","WHO-UMC","compliant","certified","integrated","real-time","cloud","GCP-compliant"]
        found_claims=[]
        for kw in claims_keywords:
            if re.search(r"\b"+re.escape(kw)+r"\b", text, re.I):
                # extract snippet
                for l in lines:
                    if re.search(r"\b"+re.escape(kw)+r"\b", l, re.I):
                        found_claims.append(l.strip()[:120])
                        break
        if found_claims:
            md += "**Important claims (keyword hits):**\n"
            for c in found_claims[:10]:
                md += f"- `{c}`\n"
            md += "\n"
        # Full text with page number preservation
        md += "**Extracted Text (Page {}):**\n\n".format(i)
        md += "```text\n"
        # limit text to avoid huge
        txt_out = text[:8000]
        if len(text)>8000: txt_out += "\n... [truncated at 8000 chars for this page]"
        md += txt_out
        md += "\n```\n\n"
        md += "---\n\n"

    # Add summary of diagrams etc
    md += "## Diagrams / Screenshots / Visuals Summary\n\n"
    md += "- If pages contained /Image XObject, those are likely screenshots/diagrams (see per-page Visual note).\n"
    md += "- Architecture diagrams: search for headings containing 'Architecture' per page above.\n"
    md += "- Workflow diagrams: search for 'workflow'/'flow' per page.\n"
    md += "- Tables are heuristically extracted above (pipe/multi-space).\n\n"

    md += "## Limitations\n\n"
    md += "- Text extraction via pypdf preserves text but not layout; scanned image-only pages would show empty text (marked).\n"
    md += "- If `TEXT EXTRACTION INCOMPLETE` or empty page text, original PDF is image-based; visual inspection needed.\n"
    md += "- For headings/tables, heuristic only — not definitive.\n"

    out_file.write_text(md, encoding="utf-8")
    print(f"  -> Wrote {out_file} ({len(md)} chars)")

print("\nDone PDF extraction")
