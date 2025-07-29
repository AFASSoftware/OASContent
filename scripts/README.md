# Markdown Naming Validator

This directory contains scripts for validating markdown file naming conventions in the repository.

## Files

- `markdown-naming-check.py` - Main validation script that checks if markdown files follow kebab-case naming convention. The script will provide suggested names for any violations found.

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

## Usage

### Basic Usage
```bash
python markdown-naming-check.py
```

### Advanced Usage
```bash
# Specify a different root directory
python markdown-naming-check.py --root-path ./docs

# Focus on specific content folders
python markdown-naming-check.py --root-path markdownpages

# Exclude specific patterns (if needed)
python markdown-naming-check.py --exclude ".github/*" "temp/*" "draft_*.md"

# Get JSON output for integration
python markdown-naming-check.py --json

# Show help
python markdown-naming-check.py --help
```

## Validation Methods

### Automatic Validation
1. **GitHub Actions**: Runs on push/pull requests to main branches
2. **Pre-commit Hook**: Runs before each commit (installed in .git/hooks/pre-commit)

### Bypassing Validation
```bash
git commit --no-verify  # Skip pre-commit validation (not recommended)
```

## Exit Codes

- `0` - All files follow naming conventions (success)
- `1` - Violations found or error occurred (failure)

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
2. **Validation failing**: Check output for specific files that need renaming
3. **False positives**: Verify AppConnectorAuditor files are excluded
4. **Bypass validation**: Use `git commit --no-verify` (not recommended)

### Getting Help

- Check validation output for file rename suggestions
- Review naming convention examples above
- Validation always runs in GitHub Actions regardless of local setup
- Contact the development team for assistance
