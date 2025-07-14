# PowerShell script to rename files using git mv based on the naming violations report
# This script reads the report.json file and renames files to start with capital letters

# Function to log messages with timestamp
function Write-Log {
    param([string]$Message, [string]$Level = "INFO")
    $timestamp = Get-Date -Format "yyyy-MM-dd HH:mm:ss"
    Write-Host "[$timestamp] [$Level] $Message"
}

# Check if we're in a git repository
if (-not (Test-Path ".git")) {
    Write-Log "Error: Not in a git repository. Please run this script from the root of your git repository." "ERROR"
    exit 1
}

# Check if report.json exists
if (-not (Test-Path "report.json")) {
    Write-Log "Error: report.json not found in current directory." "ERROR"
    exit 1
}

Write-Log "Starting file renaming process based on report.json"

try {
    # Read and parse the report.json file
    $reportContent = Get-Content "report.json" -Raw | ConvertFrom-Json
    
    Write-Log "Found $($reportContent.violations_found) violations in $($reportContent.total_files_checked) files"
    
    # Counter for successful renames
    $successCount = 0
    $errorCount = 0
    
    # Process each violation
    foreach ($violation in $reportContent.violations) {
        $currentPath = "MarkdownPages/$($violation.file_path)"
        $fileName = $violation.current_name
        $suggestedName = $violation.suggested_name
        
        # Calculate the new path by replacing the filename
        $directory = Split-Path $currentPath -Parent
        $newPath = Join-Path $directory $suggestedName
        
        Write-Log "Processing: $currentPath -> $newPath"
        
        # Check if source file exists
        if (-not (Test-Path $currentPath)) {
            Write-Log "Warning: Source file not found: $currentPath" "WARN"
            $errorCount++
            continue
        }
        
        # Check if destination already exists (case-sensitive check)
        if (Test-Path $newPath) {
            Write-Log "Warning: Destination file already exists: $newPath" "WARN"
            $errorCount++
            continue
        }
        
        try {
            # Use git mv to rename the file
            $gitMvResult = & git mv $currentPath $newPath 2>&1
            
            if ($LASTEXITCODE -eq 0) {
                Write-Log "Successfully renamed: $fileName -> $suggestedName" "SUCCESS"
                $successCount++
            } else {
                Write-Log "Git mv failed for $currentPath : $gitMvResult" "ERROR"
                $errorCount++
            }
        }
        catch {
            Write-Log "Exception during git mv for $currentPath : $($_.Exception.Message)" "ERROR"
            $errorCount++
        }
    }
    
    Write-Log "Renaming process completed!"
    Write-Log "Successfully renamed: $successCount files"
    Write-Log "Errors encountered: $errorCount files"
    
    if ($successCount -gt 0) {
        Write-Log "You can now commit the changes with: git commit -m 'Rename files to start with capital letters'"
    }
    
    if ($errorCount -gt 0) {
        Write-Log "Please review the errors above and handle them manually if needed." "WARN"
    }
}
catch {
    Write-Log "Error reading or parsing report.json: $($_.Exception.Message)" "ERROR"
    exit 1
}
