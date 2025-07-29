#!/bin/sh
#
# This script re-enables the pre-commit hook
#

echo "Re-enabling pre-commit hook..."

if [ -f ".git/hooks/pre-commit.disabled" ]; then
    mv ".git/hooks/pre-commit.disabled" ".git/hooks/pre-commit"
    echo "✅ Pre-commit hook re-enabled successfully"
    echo "   The hook will now run before each commit"
else
    echo "ℹ️  No disabled pre-commit hook found"
    if [ -f ".git/hooks/pre-commit" ]; then
        echo "   Pre-commit hook is already active"
    fi
fi
