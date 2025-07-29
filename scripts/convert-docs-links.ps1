#!/usr/bin/env pwsh
<#
.SYNOPSIS
    Convert absolute docs.afas.help URLs to relative paths in markdown files
.DESCRIPTION
    This script finds all docs.afas.help URLs in markdown files and converts them to 
    appropriate relative paths for internal navigation within the documentation structure.
.PARAMETER DryRun
    Show what would be changed without actually modifying files
.PARAMETER Path
    Root path to search for markdown files (defaults to markdownpages directory)
#>

param(
    [switch]$DryRun,
    [string]$Path = "markdownpages"
)

# Color output functions
function Write-Success($message) { Write-Host $message -ForegroundColor Green }
function Write-Warning($message) { Write-Host $message -ForegroundColor Yellow }
function Write-Error($message) { Write-Host $message -ForegroundColor Red }
function Write-Info($message) { Write-Host $message -ForegroundColor Cyan }

# Get the absolute path
$markdownPath = if ([System.IO.Path]::IsPathRooted($Path)) { 
    $Path 
} else { 
    Join-Path (Get-Location) $Path 
}

# Normalize path and ensure it's a directory
if (Test-Path $markdownPath -PathType Leaf) {
    # Single file specified
    $markdownFiles = @(Get-Item $markdownPath)
    $markdownPath = Split-Path $markdownPath -Parent
    $basePath = Split-Path $markdownPath -Parent  # Go up one more for relative calculations
} else {
    # Directory specified
    if (-not (Test-Path $markdownPath)) {
        Write-Error "Path not found: $markdownPath"
        exit 1
    }
    $markdownFiles = Get-ChildItem -Path $markdownPath -Recurse -Filter "*.md" | Where-Object { -not $_.PSIsContainer }
    $basePath = $markdownPath
}

Write-Info "Scanning for docs.afas.help links in: $markdownPath"
if ($DryRun) {
    Write-Warning "DRY RUN MODE - No files will be modified"
}

Write-Info "Found $($markdownFiles.Count) markdown files to process"

$totalReplacements = 0
$filesModified = 0

# URL mapping patterns for conversion
$urlMappings = @{
    # API documentation - most common pattern
    'https://docs\.afas\.help/apidoc/([a-z]{2})/([^)#\s\]]+)' = '../../api-specs/$1/$2'
    'https://docs\.afas\.help/apidoc/sb/([a-z]{2})/latest([^)#\s\]]*)' = '../../api-specs/sb/$1/latest$2'
    
    # SB root links - simple cases
    'https://docs\.afas\.help/sb(?:/en)?/?$' = {
        # Get current file context
        $currentPath = $relativePath
        $pathParts = $currentPath.Split('/')
        
        if ($pathParts.Length -gt 0 -and $pathParts[0] -eq 'sb') {
            # Already in SB directory
            return "./"
        } else {
            # From outside SB
            return "../sb/en/"
        }
    }
    
    'https://docs\.afas\.help/sb/?$' = {
        # Get current file context
        $currentPath = $relativePath
        $pathParts = $currentPath.Split('/')
        
        if ($pathParts.Length -gt 0 -and $pathParts[0] -eq 'sb') {
            # Already in SB directory - link to parent SB
            return "../"
        } else {
            # From outside SB
            return "../sb/"
        }
    }
    
    # SB conceptual documentation - same language
    'https://docs\.afas\.help/sb/([a-z]{2})/([^)#\s\]]+)' = {
        param($targetLang, $page)
        
        # Get current file context
        $currentPath = $relativePath
        $pathParts = $currentPath.Split('/')
        
        if ($pathParts.Length -gt 1 -and $pathParts[0] -eq 'sb' -and $pathParts[1] -eq $targetLang) {
            # Same language within SB - use relative path
            return "./$page"
        } elseif ($pathParts.Length -gt 0 -and $pathParts[0] -eq 'sb') {
            # Different language within SB
            return "../$targetLang/$page"
        } else {
            # From outside SB to SB
            return "../sb/$targetLang/$page"
        }
    }
    
    # Profit conceptual documentation
    'https://docs\.afas\.help/[Pp]rofit/([a-z]{2})/([^)#\s\]]+)' = {
        param($targetLang, $page)
        
        # Get current file context
        $currentPath = $relativePath
        $pathParts = $currentPath.Split('/')
        
        if ($pathParts.Length -gt 1 -and $pathParts[0] -eq 'profit' -and $pathParts[1] -eq $targetLang) {
            # Same language within Profit
            return "./$page"
        } elseif ($pathParts.Length -gt 0 -and $pathParts[0] -eq 'profit') {
            # Different language within Profit
            return "../$targetLang/$page"
        } else {
            # From outside Profit to Profit
            return "../profit/$targetLang/$page"
        }
    }
}

foreach ($file in $markdownFiles) {
    # Calculate relative path safely
    $fileFullPath = $file.FullName
    $relativePath = if ($fileFullPath.Length -gt $basePath.Length) {
        $fileFullPath.Substring($basePath.Length + 1).Replace('\', '/')
    } else {
        $file.Name
    }
    
    Write-Host "Processing: " -NoNewline
    Write-Host $relativePath -ForegroundColor Gray
    
    $content = Get-Content $file.FullName -Raw -Encoding UTF8
    $originalContent = $content
    $fileReplacements = 0
    
    # Get the current file's context for relative path calculation
    $pathParts = $relativePath.Split('/')
    $currentLang = if ($pathParts.Length -gt 1) { $pathParts[1] } else { 'en' }
    
    # Apply URL mappings
    foreach ($pattern in $urlMappings.Keys) {
        $replacement = $urlMappings[$pattern]
        
        if ($replacement -is [scriptblock]) {
            # Dynamic replacement using script block - pass current context
            $currentRelativePath = $relativePath
            $content = [regex]::Replace($content, $pattern, {
                param($match)
                $groups = $match.Groups
                
                # Extract capture groups
                $captureGroups = @()
                for ($i = 1; $i -lt $groups.Count; $i++) {
                    $captureGroups += $groups[$i].Value
                }
                
                # Create a new scope with the context variables
                $scriptWithContext = [ScriptBlock]::Create("
                    `$relativePath = '$currentRelativePath'
                    & {$($replacement.ToString())} @args
                ")
                
                # Execute the script block with captured groups
                $result = & $scriptWithContext @captureGroups
                return $result
            })
        } else {
            # Simple regex replacement
            $beforeCount = ([regex]::Matches($content, $pattern)).Count
            $content = [regex]::Replace($content, $pattern, $replacement)
            $afterCount = ([regex]::Matches($content, $pattern)).Count
            $replacementsMade = $beforeCount - $afterCount
            $fileReplacements += $replacementsMade
        }
    }
    
    # Count total changes by comparing with original
    $docsAfasHelpCount = ([regex]::Matches($originalContent, 'https://docs\.afas\.help')).Count
    $newDocsAfasHelpCount = ([regex]::Matches($content, 'https://docs\.afas\.help')).Count
    $actualReplacements = $docsAfasHelpCount - $newDocsAfasHelpCount
    
    if ($actualReplacements -gt 0) {
        $filesModified++
        $totalReplacements += $actualReplacements
        
        Write-Success "  → Converted $actualReplacements docs.afas.help URLs"
        
        if (-not $DryRun) {
            Set-Content -Path $file.FullName -Value $content -Encoding UTF8 -NoNewline
        }
        
        # Show some examples of what was changed
        if ($DryRun) {
            $lines = $content -split "`n"
            $changedLines = for ($i = 0; $i -lt $lines.Length; $i++) {
                $originalLine = ($originalContent -split "`n")[$i]
                if ($lines[$i] -ne $originalLine -and $originalLine -match 'docs\.afas\.help') {
                    "    Line $($i + 1): $($originalLine.Trim())"
                    "    →         $($lines[$i].Trim())"
                }
            }
            if ($changedLines) {
                Write-Host ($changedLines | Select-Object -First 4 | Out-String) -ForegroundColor DarkGray
                if ($changedLines.Count -gt 4) {
                    Write-Host "    ... and $($changedLines.Count - 4) more changes" -ForegroundColor DarkGray
                }
            }
        }
    }
}

Write-Host "`n" -NoNewline
Write-Success "Summary:"
Write-Host "  Files processed: $($markdownFiles.Count)"
Write-Host "  Files modified: $filesModified" 
Write-Host "  Total URLs converted: $totalReplacements"

if ($DryRun) {
    Write-Warning "`nDRY RUN COMPLETE - No files were actually modified."
    Write-Host "Run without -DryRun to apply changes."
} else {
    Write-Success "`nConversion complete!"
}

# Show remaining docs.afas.help URLs if any
$remainingUrls = $markdownFiles | 
    ForEach-Object { 
        $content = Get-Content $_.FullName -Raw 
        $urlMatches = [regex]::Matches($content, 'https://docs\.afas\.help[^\s\)\]]+')
        foreach ($match in $urlMatches) {
            $fileFullPath = $_.FullName
            $fileRelativePath = if ($fileFullPath.Length -gt $basePath.Length) {
                $fileFullPath.Substring($basePath.Length + 1)
            } else {
                $_.Name
            }
            [PSCustomObject]@{
                File = $fileRelativePath
                URL = $match.Value
            }
        }
    }

if ($remainingUrls) {
    Write-Warning "`nRemaining docs.afas.help URLs that may need manual review:"
    $remainingUrls | Format-Table -AutoSize
} else {
    Write-Success "`nAll docs.afas.help URLs have been successfully converted!"
}
