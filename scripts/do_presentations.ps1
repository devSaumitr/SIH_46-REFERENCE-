$base = "E:\SIH26046_COMPETITOR_ANALYSIS"
$repos = Get-ChildItem -LiteralPath "$base\repositories" -Directory
foreach ($repo in $repos) {
  $name = $repo.Name
  Write-Host "`n=== $name ==="
  $ppt = Get-ChildItem -LiteralPath $repo.FullName -Recurse -Include "*.ppt","*.pptx" -Force -ErrorAction SilentlyContinue | Where-Object { $_.FullName -notmatch "\\\.git\\" }
  $pdf = Get-ChildItem -LiteralPath $repo.FullName -Recurse -Include "*.pdf" -Force -ErrorAction SilentlyContinue | Where-Object { $_.FullName -notmatch "\\\.git\\" }
  $demo = Get-ChildItem -LiteralPath $repo.FullName -Recurse -Force -ErrorAction SilentlyContinue | Where-Object { $_.Name -match "DEMO_SCRIPT|JUDGE_QA|demo|pitch|presentation|architecture|screenshots|assets|judge" -and $_.FullName -notmatch "\\\.git\\" -and $_.FullName -notmatch "\\node_modules\\" } | Select-Object -First 20
  Write-Host "  PPT: $($ppt.Count) files"
  $ppt | ForEach-Object { Write-Host "    - $($_.FullName.Replace($repo.FullName,'')) ($([math]::Round($_.Length/1KB,1)) KB)" }
  Write-Host "  PDF: $($pdf.Count) files"
  $pdf | ForEach-Object { Write-Host "    - $($_.FullName.Replace($repo.FullName,'')) ($([math]::Round($_.Length/1KB,1)) KB)" }
  Write-Host "  Demo/judge: $($demo.Count) files"
  $demo | ForEach-Object { Write-Host "    - $($_.FullName.Replace($repo.FullName,''))" }
  $dest = Join-Path $base "presentations\$name"
  New-Item -ItemType Directory -Path $dest -Force | Out-Null
  $inv = "# Presentations / Judge Materials — $name`n`n**Source:** repositories/$name/`n**Generated:** 2026-09-30`n`n"
  if ($ppt.Count -eq 0 -and $pdf.Count -eq 0 -and $demo.Count -eq 0) {
    $inv += "> No PPT/PDF/DEMO_SCRIPT/JUDGE_QA found in this repository (verified via rglob search).`n`n"
    $inv += "Search patterns: *.ppt, *.pptx, *.pdf, DEMO_SCRIPT.md, JUDGE_QA.md, demo, pitch, presentation, architecture, screenshots, assets, judge (excluded .git/node_modules).`n"
  } else {
    $inv += "## PPT`n`n"
    if ($ppt) { $ppt | ForEach-Object { $inv += "- " + $_.Name + " — " + $_.FullName.Replace($repo.FullName,'') + " (" + [math]::Round($_.Length/1KB,1) + " KB)`n" } } else { $inv += "None found.`n" }
    $inv += "`n## PDF`n`n"
    if ($pdf) { $pdf | ForEach-Object { $inv += "- " + $_.Name + " — " + $_.FullName.Replace($repo.FullName,'') + " (" + [math]::Round($_.Length/1KB,1) + " KB)`n" } } else { $inv += "None found.`n" }
    $inv += "`n## Demo / Judge Related`n`n"
    if ($demo) { $demo | ForEach-Object { $inv += "- " + $_.FullName.Replace($repo.FullName,'') + "`n" } } else { $inv += "None found.`n" }
    foreach ($f in @($ppt + $pdf)) {
      if ($f -and $f.FullName -notmatch "\\\.git\\") {
        $rel = $f.FullName.Replace($repo.FullName, "").TrimStart("\","/")
        $destFile = Join-Path $dest ($rel -replace "[\\\/]", "_")
        try { Copy-Item -LiteralPath $f.FullName -Destination $destFile -Force } catch { Write-Host "  Copy failed $($f.FullName)" }
      }
    }
    foreach ($d in $demo) {
      if ($d.PSIsContainer) { continue }
      if ($d.Extension -in @(".md",".txt",".pdf") -and $d.Name -match "DEMO_SCRIPT|JUDGE_QA|Judge_Demo") {
        $rel = $d.FullName.Replace($repo.FullName, "").TrimStart("\","/")
        $destFile = Join-Path $dest ($rel -replace "[\\\/]", "_")
        try { Copy-Item -LiteralPath $d.FullName -Destination $destFile -Force } catch {}
      }
    }
  }
  if ($name -eq "nishant-uxs_vedraya") {
    $inv += "`n## VEDRAYA Special Investigation (Task 27)`n`n"
    $inv += "- docs/DEMO_SCRIPT.md (3.0 KB) — 9-step 60-sec judge flow (Command Center -> AYU-024 -> Safety -> Audit verify)`n"
    $inv += "- docs/JUDGE_QA.md (3.5 KB) — anticipated questions + objections (WORM, licensed MedDRA, ABDM not connected)`n"
    $inv += "- docs/SIH26046_TRACEABILITY_FINAL.md (8.0 KB) — PS traceability matrix`n"
    $inv += "- docs/IMPLEMENTATION_STATUS.md (1.5 KB) — honest Implemented/Partial/Prototype/Not Connected table`n"
    $inv += "- docs/RBAC.md (3.6 KB) + SECURITY.md (1.7 KB) + AUDIT.md (2.7 KB)`n"
    $inv += "- public/vedraya/frames-alpha/ 360 webp cinematic identity (not judge evidence)`n"
    # also copy those docs to presentations
    foreach ($doc in @("docs/DEMO_SCRIPT.md","docs/JUDGE_QA.md","docs/SIH26046_TRACEABILITY_FINAL.md","docs/IMPLEMENTATION_STATUS.md","docs/RBAC.md")) {
      $src = Join-Path $repo.FullName $doc
      if (Test-Path $src) { Copy-Item -LiteralPath $src -Destination (Join-Path $dest ($doc -replace "[\\\/]", "_")) -Force }
    }
  }
  if ($name -eq "vansh459_AyuSphere") {
    $inv += "`n## AyuSphere UAT / Judge Materials`n`n"
    $inv += "- docs/uat/Judge_Demo_Script.md (4.1 KB) + Judge_Demo_Script.pdf (1.31 MB)`n"
    $inv += "- docs/uat/UAT_Guide_Administrator.pdf (3.32 MB) + UAT_Guide_Principal_Investigator.pdf (2.83 MB) etc. (7 role PDFs)`n"
    $inv += "- docs/uat/Tech_Security_Guide.md (17 KB) + .pdf (155 KB)`n"
    foreach ($doc in @("docs/uat/Judge_Demo_Script.md","docs/uat/Judge_Demo_Script.pdf","docs/uat/Tech_Security_Guide.md")) {
      $src = Join-Path $repo.FullName $doc
      if (Test-Path $src) {
        $destFile = Join-Path $dest ($doc -replace "[\\\/]", "_")
        try { Copy-Item -LiteralPath $src -Destination $destFile -Force } catch {}
      }
    }
  }
  $inv | Set-Content -LiteralPath (Join-Path $dest "PRESENTATION_INVENTORY.md") -Encoding UTF8
  Write-Host "  -> Wrote PRESENTATION_INVENTORY.md"
}
Write-Host "`n=== Summary presentations dir ==="
Get-ChildItem -LiteralPath "$base\presentations" -Recurse | Format-Table FullName, Length -AutoSize
