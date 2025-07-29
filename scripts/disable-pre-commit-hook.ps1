# PowerShell script to disable the pre-commit hook
# Use this if you don't have Python installed locally

Write-Host "Disabling pre-commit hook..." -ForegroundColor Yellow

$preCommitPath = ".git/hooks/pre-commit"
$disabledPath = ".git/hooks/pre-commit.disabled"

if (Test-Path $preCommitPath) {
    Move-Item $preCommitPath $disabledPath
    Write-Host "✅ Pre-commit hook disabled successfully" -ForegroundColor Green
    Write-Host "   The hook has been renamed to 'pre-commit.disabled'" -ForegroundColor Gray
    Write-Host "   Validation will still run in GitHub Actions when you push" -ForegroundColor Gray
} else {
    Write-Host "ℹ️  No pre-commit hook found to disable" -ForegroundColor Blue
}

Write-Host ""
Write-Host "To re-enable the hook later:" -ForegroundColor Cyan
Write-Host "  Move-Item .git/hooks/pre-commit.disabled .git/hooks/pre-commit" -ForegroundColor Gray
