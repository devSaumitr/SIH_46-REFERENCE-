# SIH Problem 46 - Repo Extractor
# Usage: Place repo folders/zips/git URLs in repos_raw, then run:
# powershell -ExecutionPolicy Bypass -File E:\SIH_46\scripts\extract_repos.ps1

param(
    [string]$RawDir = "E:\SIH_46\repos_raw",
    [string]$OutDir = "E:\SIH_46\repo_extracts",
    [string]$DocsDir = "E:\SIH_46\docs"
)

function Get-TreeString {
    param([string]$Path, [int]$MaxDepth = 8, [string]$Prefix = "", [int]$Depth = 0)
    if ($Depth -gt $MaxDepth) { return "" }
    $items = Get-ChildItem -LiteralPath $Path -Force -ErrorAction SilentlyContinue | Sort-Object { $_.PSIsContainer } -Descending | Sort-Object Name
    $out = ""
    for ($i=0; $i -lt $items.Count; $i++) {
        $item = $items[$i]
        $isLast = ($i -eq $items.Count - 1)
        if ($isLast) { $branch = "`-- " } else { $branch = "|-- " }
        if ($isLast) { $nextPrefix = "$Prefix    " } else { $nextPrefix = "$Prefix|   " }
        if ($item.Name -in @(".git", "node_modules", ".venv", "venv", "__pycache__", ".next", "dist", "build")) {
            $out += "$Prefix$branch$($item.Name)/ [skipped]`n"
            continue
        }
        if ($item.PSIsContainer) {
            $out += "$Prefix$branch$($item.Name)/`n"
            $out += Get-TreeString -Path $item.FullName -MaxDepth $MaxDepth -Prefix $nextPrefix -Depth ($Depth+1)
        } else {
            $size = if ($item.Length -gt 1MB) { "{0:N2} MB" -f ($item.Length/1MB) } elseif ($item.Length -gt 1KB) { "{0:N1} KB" -f ($item.Length/1KB) } else { "$($item.Length) B" }
            $out += "$Prefix$branch$($item.Name) ($size)`n"
        }
    }
    return $out
}

function Get-FileStats {
    param([string]$Path)
    $files = Get-ChildItem -LiteralPath $Path -Recurse -Force -File -ErrorAction SilentlyContinue | Where-Object { $_.FullName -notmatch "\\\.git\\" -and $_.FullName -notmatch "\\node_modules\\" -and $_.FullName -notmatch "\\\.venv\\" }
    $totalSize = ($files | Measure-Object Length -Sum).Sum
    if (-not $totalSize) { $totalSize = 0 }
    $extGroups = $files | Group-Object Extension | Sort-Object Count -Descending | Select-Object -First 15
    $stats = "## File Statistics`n`n"
    $stats += "- **Total Files:** $($files.Count)`n"
    $stats += "- **Total Size:** $([math]::Round($totalSize/1MB,2)) MB`n"
    $stats += "- **Last Modified:** $((Get-Item $Path).LastWriteTime)`n`n"
    $stats += "### Top Extensions`n`n| Extension | Count |`n|---|---|`n"
    foreach ($g in $extGroups) {
        $ext = if ($g.Name) { $g.Name } else { "(no ext)" }
        $stats += "| $ext | $($g.Count) |`n"
    }
    $stats += "`n### Largest Files (top 10)`n`n| File | Size |`n|---|---|`n"
    $largest = $files | Sort-Object Length -Descending | Select-Object -First 10
    foreach ($f in $largest) {
        $rel = $f.FullName.Replace($Path, "").TrimStart("\")
        $size = if ($f.Length -gt 1MB) { "{0:N2} MB" -f ($f.Length/1MB) } else { "{0:N1} KB" -f ($f.Length/1KB) }
        $stats += "| $rel | $size |`n"
    }
    return $stats
}

New-Item -ItemType Directory -Path $OutDir -Force | Out-Null
New-Item -ItemType Directory -Path $DocsDir -Force | Out-Null
New-Item -ItemType Directory -Path $RawDir -Force | Out-Null

Write-Host "=== SIH 46 Repo Extractor ===" -ForegroundColor Cyan
Write-Host "RawDir: $RawDir"
Write-Host "OutDir: $OutDir"

Get-ChildItem -LiteralPath $RawDir -Filter "*.zip" -Force -ErrorAction SilentlyContinue | ForEach-Object {
    $dest = Join-Path $RawDir $_.BaseName
    if (-not (Test-Path $dest)) {
        Write-Host "Extracting zip: $($_.Name) -> $dest" -ForegroundColor Yellow
        Expand-Archive -LiteralPath $_.FullName -DestinationPath $dest -Force
    }
}

$urlsFile = Join-Path $RawDir "urls.txt"
if (Test-Path $urlsFile) {
    Get-Content $urlsFile | Where-Object { $_.Trim() -ne "" -and -not $_.StartsWith("#") } | ForEach-Object {
        $url = $_.Trim()
        $name = ($url.Split("/")[-1] -replace "\.git$","").Trim()
        if (-not $name) { $name = "repo_$(Get-Random)" }
        $dest = Join-Path $RawDir $name
        if (-not (Test-Path $dest)) {
            Write-Host "Cloning $url -> $dest" -ForegroundColor Yellow
            git clone $url $dest
        } else {
            Write-Host "Skipping clone, exists: $name" -ForegroundColor Gray
        }
    }
}

$repos = Get-ChildItem -LiteralPath $RawDir -Directory -Force -ErrorAction SilentlyContinue
if (-not $repos -or $repos.Count -eq 0) {
    Write-Host "No repos found in $RawDir" -ForegroundColor Red
    Write-Host "Place repo folders, zips, or urls.txt there and re-run." -ForegroundColor Yellow
    exit 0
}

$masterRows = @()

foreach ($repo in $repos) {
    $repoName = $repo.Name
    $repoPath = $repo.FullName
    Write-Host "`n--- Processing: $repoName ---" -ForegroundColor Green

    $extractPath = Join-Path $OutDir $repoName
    New-Item -ItemType Directory -Path $extractPath -Force | Out-Null

    $tree = Get-TreeString -Path $repoPath -MaxDepth 8
    $treeMd = "# File Structure -- $repoName`n`n"
    $treeMd += "**Source:** ``$repoPath```n`n"
    $treeMd += "**Generated:** $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')`n`n"
    $treeMd += "``````text`n$repoName/`n$tree``````"
    $treeMd | Set-Content -LiteralPath (Join-Path $extractPath "01_STRUCTURE.md") -Encoding UTF8
    "$repoName/`n$tree" | Set-Content -LiteralPath (Join-Path $extractPath "tree.txt") -Encoding UTF8

    $readmes = Get-ChildItem -LiteralPath $repoPath -Recurse -Force -File -ErrorAction SilentlyContinue | Where-Object { $_.Name -like "README*.md" -or $_.Name -like "readme*.md" } | Select-Object -First 10
    $readmeMd = "# README Inventory -- $repoName`n`n"
    $readmeMd += "**Generated:** $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')`n`n"
    if (-not $readmes -or $readmes.Count -eq 0) {
        $readmeMd += "> No README.md found in this repo.`n`n"
        $readmeMd += "Searched recursively for README*.md -- none found.`n"
    } else {
        $readmeMd += "Found **$($readmes.Count)** README file(s):`n`n"
        $readmeMd += "| # | Path (relative) | Size | Modified |`n|---|---|---|---|`n"
        $idx=1
        foreach ($r in $readmes) {
            $rel = $r.FullName.Replace($repoPath,"").TrimStart("\","/")
            $readmeMd += "| $idx | ``$rel`` | $([math]::Round($r.Length/1KB,1)) KB | $($r.LastWriteTime.ToString('yyyy-MM-dd')) |`n"
            $idx++
        }
        $readmeMd += "`n---`n`n"
        foreach ($r in $readmes) {
            $rel = $r.FullName.Replace($repoPath,"").TrimStart("\","/")
            $content = Get-Content -LiteralPath $r.FullName -Raw -ErrorAction SilentlyContinue
            if ($content -and $content.Length -gt 15000) { $content = $content.Substring(0,15000) + "`n`n... [truncated]" }
            $readmeMd += "## File: ``$rel```n`n``````markdown`n$content`n`````` `n`n"
        }
    }
    $otherDocs = Get-ChildItem -LiteralPath $repoPath -Recurse -File -Force -ErrorAction SilentlyContinue | Where-Object { $_.Extension -eq ".md" -and $_.FullName -notmatch "\\\.git\\" } | Select-Object -First 20
    if ($otherDocs -and $otherDocs.Count -gt 0 -and $readmes) {
        $extra = $otherDocs | Where-Object { $_.FullName -notin $readmes.FullName }
        if ($extra.Count -gt 0) {
            $readmeMd += "`n---`n`n## Other Markdown Docs`n`n| File | Size | Path |`n|---|---|---|`n"
            foreach ($d in $extra) {
                $rel = $d.FullName.Replace($repoPath,"").TrimStart("\","/")
                $readmeMd += "| $($d.Name) | $([math]::Round($d.Length/1KB,1)) KB | ``$rel`` |`n"
            }
        }
    }
    $readmeMd | Set-Content -LiteralPath (Join-Path $extractPath "02_README_CONTENT.md") -Encoding UTF8

    $stats = Get-FileStats -Path $repoPath
    $details = "# Repo Details -- $repoName`n`n"
    $details += "**Path:** ``$repoPath```n`n"
    $details += "**Generated:** $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')`n`n"
    $details += $stats + "`n`n"
    $details += "## Tech Stack Hints`n`n| Indicator | Found |`n|---|---|`n"
    $hints = @(
        @{File="package.json"; Tech="Node.js / Frontend"},
        @{File="requirements.txt"; Tech="Python"},
        @{File="pyproject.toml"; Tech="Python (poetry)"},
        @{File="*.py"; Tech="Python files"},
        @{File="Dockerfile"; Tech="Docker"},
        @{File="docker-compose.yml"; Tech="Docker Compose"},
        @{File="*.ipynb"; Tech="Jupyter"},
        @{File="pom.xml"; Tech="Java Maven"},
        @{File="build.gradle"; Tech="Java Gradle"},
        @{File="go.mod"; Tech="Go"},
        @{File="Cargo.toml"; Tech="Rust"}
    )
    foreach ($h in $hints) {
        $found = (Get-ChildItem -LiteralPath $repoPath -Recurse -Force -ErrorAction SilentlyContinue | Where-Object { $_.Name -like $h.File }).Count -gt 0
        $icon = if ($found) { "YES" } else { "--" }
        $details += "| $($h.Tech) (``$($h.File)``) | $icon |`n"
    }
    $details += "`n## Top-Level Contents`n`n``````text`n"
    Get-ChildItem -LiteralPath $repoPath -Force | ForEach-Object {
        $type = if ($_.PSIsContainer) { "DIR " } else { "FILE" }
        $details += "$type  $($_.Name)`n"
    }
    $details += "`````` `n"
    if (Test-Path (Join-Path $repoPath ".git")) {
        try {
            $branch = git -C $repoPath rev-parse --abbrev-ref HEAD 2>$null
            $log = git -C $repoPath log --oneline -5 2>$null
            $remote = git -C $repoPath remote -v 2>$null
            $details += "`n## Git Info`n`n"
            $details += "**Branch:** ``$branch```n`n"
            if ($remote) { $details += "``````text`n$remote`n`````` `n`n" }
            if ($log) { $details += "**Last 5 commits:**`n``````text`n$log`n`````` `n" }
        } catch {}
    }
    $details | Set-Content -LiteralPath (Join-Path $extractPath "03_DETAILS.md") -Encoding UTF8

    $combined = "# Combined Report -- $repoName`n`n"
    $combined += "> Auto-generated from ``$repoPath`` on $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')`n`n"
    $combined += "---`n`n"
    $combined += (Get-Content -LiteralPath (Join-Path $extractPath "01_STRUCTURE.md") -Raw) + "`n`n---`n`n"
    $combined += (Get-Content -LiteralPath (Join-Path $extractPath "02_README_CONTENT.md") -Raw) + "`n`n---`n`n"
    $combined += (Get-Content -LiteralPath (Join-Path $extractPath "03_DETAILS.md") -Raw)
    $combined | Set-Content -LiteralPath (Join-Path $extractPath "00_FULL_REPORT.md") -Encoding UTF8

    $fileCount = (Get-ChildItem -LiteralPath $repoPath -Recurse -File -Force -ErrorAction SilentlyContinue | Where-Object { $_.FullName -notmatch "\\\.git\\" }).Count
    $hasReadme = $readmes -and $readmes.Count -gt 0
    $masterRows += [PSCustomObject]@{
        Repo = $repoName
        Files = $fileCount
        Readmes = if ($readmes) { $readmes.Count } else { 0 }
        HasReadme = if ($hasReadme) { "YES" } else { "NO" }
        Path = $repoPath
        Extract = $extractPath
    }
    Write-Host "  DONE 01_STRUCTURE.md" -ForegroundColor Gray
    Write-Host "  DONE 02_README_CONTENT.md" -ForegroundColor Gray
    Write-Host "  DONE 03_DETAILS.md" -ForegroundColor Gray
    Write-Host "  DONE 00_FULL_REPORT.md" -ForegroundColor Gray
}

$indexMd = "# SIH Problem 46 -- Repo Extracts Index`n`n"
$indexMd += "**Generated:** $(Get-Date -Format 'yyyy-MM-dd HH:mm:ss')`n`n"
$indexMd += "**Raw repos:** ``$RawDir```n**Extracts:** ``$OutDir```n`n"
$indexMd += "## Repos`n`n| # | Repo | Files | READMEs | Extract Folder |`n|---|---|---|---|---|`n"
$idx=1
foreach ($r in $masterRows) {
    $indexMd += "| $idx | ``$($r.Repo)`` | $($r.Files) | $($r.HasReadme) ($($r.Readmes)) | ``repo_extracts/$($r.Repo)/`` |`n"
    $idx++
}
$indexMd += "`n## Per-Repo Files`n`nEach ``repo_extracts/<repo>/`` contains:`n`n"
$indexMd += "- ``00_FULL_REPORT.md`` -- combined everything`n"
$indexMd += "- ``01_STRUCTURE.md`` -- full file tree`n"
$indexMd += "- ``02_README_CONTENT.md`` -- where README is + full content`n"
$indexMd += "- ``03_DETAILS.md`` -- stats, tech hints, git info`n"
$indexMd += "- ``tree.txt`` -- plain text tree`n"
$indexMd | Set-Content -LiteralPath (Join-Path $DocsDir "INDEX.md") -Encoding UTF8

Write-Host "`n=== Done: $($masterRows.Count) repos processed ===" -ForegroundColor Cyan
Write-Host "See: $DocsDir\INDEX.md"
