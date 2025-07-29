#!/bin/sh
#
# This script disables the pre-commit hook by renaming it
# Use this if you don't have Python installed locally
#

echo "Disabling pre-commit hook..."

if [ -f ".git/hooks/pre-commit" ]; then
    mv ".git/hooks/pre-commit" ".git/hooks/pre-commit.disabled"
    echo "✅ Pre-commit hook disabled successfully"
    echo "   The hook has been renamed to 'pre-commit.disabled'"
    echo "   Validation will still run in GitHub Actions when you push"
else
    echo "ℹ️  No pre-commit hook found to disable"
fi

echo ""
echo "To re-enable the hook later:"
echo "  mv .git/hooks/pre-commit.disabled .git/hooks/pre-commit"
