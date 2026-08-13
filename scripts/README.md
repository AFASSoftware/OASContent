# Markdown Naming Validator

This directory contains scripts for validating markdown file naming conventions and frontmatter dates in the repository.

## Files

- `markdown-naming-check.py` - Main validation script that checks if markdown files follow kebab-case naming convention and validates frontmatter dates for changed files. The script will provide suggested names for any violations found.

- `add_tags_to_markdown.py` - Script to automatically add relevant tags to markdown files in frontmatter.

- `merge_openapi_examples.py` - Script for merging OpenAPI example files from markdown into OpenAPI specification files.

- `merge_openapi_examples.md` - Documentation for the OpenAPI examples merge script

- `README.md` - This documentation file

## Naming Convention

All markdown files must follow **kebab-case** naming convention:
- All lowercase letters
- Use hyphens (-) to separate words
- Numbers are allowed
- No spaces, underscores, or capital letters
- No consecutive hyphens

### Examples
✅ **Good examples:**
- `howto-quickstart.md`
- `custom-fields.md`
- `authentication.md`
- `news-profit3.md`

❌ **Bad examples:**
- `Howto-quickstart.md` (capital letter)
- `custom_fields.md` (underscore)
- `How to quickstart.md` (spaces)
- `howto--quickstart.md` (consecutive hyphens)

### Exceptions
- `AppConnectorAuditor*.md` files are temporarily exempt from this naming convention

## Date Validation

When using the `--git` flag, the script also validates that the `date` field in the frontmatter of changed files matches the current date. This ensures that modified documents have up-to-date timestamps.  
Updating the date can be done automatically using the `--fix-dates` flag.

### Date Format
The date in frontmatter should be in ISO format without quotes:
```yaml
---
date: 2025-11-11
---
```

## Usage

### Basic Usage
```bash
# Check all files in markdownpages (naming only)
python markdown-naming-check.py

# Check only changed files in git (naming + date validation)
python markdown-naming-check.py --git
```

### Advanced Usage
```bash
# Specify a different root directory
python markdown-naming-check.py --root-path ./docs

# Focus on specific content folders with git mode
python markdown-naming-check.py --git --root-path markdownpages

# Exclude specific patterns (if needed)
python markdown-naming-check.py --exclude ".github/*" "temp/*" "draft_*.md"

# Get JSON output for integration
python markdown-naming-check.py --git --json

# Show help
python markdown-naming-check.py --help
```

## Validation Modes

### All Files Mode (default)
- Validates naming conventions for all markdown files
- Does NOT validate dates
- Use for initial repository setup or comprehensive checks

### Git Mode (`--git` flag)
- Only validates new or modified files (staged, unstaged, and untracked)
- Validates both naming conventions AND frontmatter dates
- Ensures changed files have current date
- Ideal for pre-commit hooks and CI/CD pipelines

## Validation Methods

### Automatic Validation
1. **GitHub Actions**: Runs on push/pull requests to main branches
2. **Pre-commit Hook**: Runs before each commit (installed in .git/hooks/pre-commit)

### Bypassing Validation
```bash
git commit --no-verify  # Skip pre-commit validation (not recommended)
```

## Exit Codes

- `0` - All files follow naming conventions and dates are correct (success)
- `1` - Violations found or error occurred (failure)

## Output Examples

### Successful Validation (Git Mode)
```
============================================================
Markdown File Naming Validation Report
Mode: Git changes only (new/modified files)
============================================================
Total markdown files checked: 5
Naming violations found: 0
Date violations found: 0

✅ All markdown files follow the kebab-case naming convention!
✅ All changed files have correct date (2025-11-11) in frontmatter!
✅ Validation PASSED
```

### Naming Violation Example
```
============================================================
Markdown File Naming Validation Report
Mode: All files
============================================================
Total markdown files checked: 10
Naming violations found: 1

NAMING VIOLATIONS DETECTED:
----------------------------------------
1. File: markdownpages/profit/en/Howto-Example.md
   Current name: Howto-Example.md
   Suggested name: howto-example.md

SUMMARY:
❌ Naming validation FAILED - Please rename the files above to follow kebab-case convention.
```

### Date Violation Example (Git Mode)
```
============================================================
Markdown File Naming Validation Report
Mode: Git changes only (new/modified files)
============================================================
Total markdown files checked: 3
Naming violations found: 0
Date violations found: 1

DATE VIOLATIONS DETECTED:
----------------------------------------
1. File: markdownpages/profit/nl/start.md
   Current date: 2024-02-18
   Expected date: 2025-11-11

SUMMARY:
❌ Date validation FAILED - Please update the date in frontmatter to 2025-11-11.
```

## GitHub Actions Integration

The script is automatically run by the GitHub Actions workflow defined in `.github/workflows/markdown-naming-check.yml` on:

- Push to main/develop branches (when MarkdownPages/*.md files are changed)
- Pull requests to main/develop branches (when MarkdownPages/*.md files are changed)
- Manual workflow dispatch

The validation focuses specifically on the `markdownPages` folder to ensure content files follow naming conventions.

## Troubleshooting

### Python Not Available Locally

If you don't have Python installed on your local machine:

1. **The pre-commit hook will automatically skip validation** and show a warning
2. **Validation will still run in GitHub Actions** when you push your changes
3. **To install Python**: Visit https://www.python.org/downloads/

### Disabling Local Validation

If you want to completely disable the pre-commit hook:

```bash
# On Windows (PowerShell):
.\scripts\disable-pre-commit-hook.ps1

# On Linux/Mac:
bash scripts/disable-pre-commit-hook.sh
```

### Re-enabling Local Validation

To re-enable the pre-commit hook:

```bash
# On Windows (PowerShell):
Move-Item .git/hooks/pre-commit.disabled .git/hooks/pre-commit

# On Linux/Mac:
bash scripts/enable-pre-commit-hook.sh
```

### Common Issues

1. **Python not found**: Hook will skip with warning, validation runs in GitHub Actions
2. **Validation failing**: Check output for specific files that need renaming or date updates
3. **False positives**: Verify AppConnectorAuditor files are excluded
4. **Date mismatch**: Use `--fix-dates` flag to automatically update dates
5. **Encoding errors**: Script now handles UTF-8 properly for emoji output on Windows
6. **Bypass validation**: Use `git commit --no-verify` (not recommended)

### Automatic Date Updates

If you need to update dates in frontmatter for changed files:

```bash
# Use the --fix-dates flag to updates dates
cd scripts
python markdown-naming-check.py --fix-dates
```

This will:
- Update the `date` field to the current date
- Format dates correctly without quotes (YAML date format)

### Getting Help

- Check validation output for file rename suggestions and date requirements
- Review naming convention examples above
- Use `--git` flag to validate only changed files
- Validation always runs in GitHub Actions regardless of local setup
- Contact the development team for assistance
