#!/usr/bin/env python3
"""
Markdown File Naming Validator

This script validates that all markdown files in the repository follow kebab-case naming convention,
except for AppConnectorAuditor* files which are allowed to be named differently.
It recursively scans for *.md files and reports any violations.

Author: GitHub Copilot
Date: 2025-07-29
"""

import os
import sys
import argparse
import json
from pathlib import Path
from typing import List, Dict, Tuple
import re


class MarkdownNamingValidator:
    """Validates markdown file naming conventions."""
    
    def __init__(self, root_path: str = ".", exclusions: List[str] = None, json_output: bool = False):
        """
        Initialize the validator.
        
        Args:
            root_path: Root directory to start scanning from
            exclusions: List of patterns to exclude from validation
            json_output: Whether to output results in JSON format
        """
        self.root_path = Path(root_path).resolve()
        self.exclusions = exclusions or []
        self.json_output = json_output
        self.violations = []
        self.total_files = 0
        
    def is_excluded(self, file_path: Path) -> bool:
        """
        Check if a file should be excluded from validation.
        
        Args:
            file_path: Path to the file to check
            
        Returns:
            True if the file should be excluded, False otherwise
        """
        relative_path = str(file_path.relative_to(self.root_path)).replace('\\', '/')
        filename = file_path.name
        
        for pattern in self.exclusions:
            # Convert glob pattern to regex
            regex_pattern = pattern.replace('*', '.*').replace('?', '.')
            if regex_pattern.endswith('/'):
                regex_pattern = regex_pattern[:-1] + '/.*'
            
            # Match the pattern against both relative path and filename
            if (re.match(regex_pattern, relative_path) or 
                re.match(regex_pattern, filename) or
                relative_path.startswith(pattern.rstrip('*')) or
                filename.startswith(pattern.rstrip('*'))):
                return True
        return False
    
    def validate_filename(self, file_path: Path) -> Tuple[bool, str]:
        """
        Validate that a markdown filename follows kebab-case convention.
        
        Args:
            file_path: Path to the markdown file
            
        Returns:
            Tuple of (is_valid, suggested_name)
        """
        filename = file_path.name
        basename = file_path.stem  # filename without .md extension
        
        # Check if filename follows kebab-case convention:
        # - All lowercase letters, numbers, hyphens, underscores, and dots
        # - No spaces
        # - No consecutive hyphens
        # - Doesn't start or end with hyphen
        kebab_pattern = r'^[a-z0-9]+([a-z0-9._-]*[a-z0-9])?$'
        
        if re.match(kebab_pattern, basename) and '--' not in basename and not basename.startswith('-') and not basename.endswith('-'):
            return True, filename
        
        # Generate suggested correction (convert to kebab-case)
        suggested_basename = self.to_kebab_case(basename)
        suggested_filename = suggested_basename + '.md'
        
        return False, suggested_filename
    
    def to_kebab_case(self, text: str) -> str:
        """
        Convert text to kebab-case.
        
        Args:
            text: Input text to convert
            
        Returns:
            kebab-case version of the text
        """
        # Replace spaces with hyphens
        text = re.sub(r'\s+', '-', text)
        
        # Insert hyphens before capital letters (for PascalCase/camelCase)
        text = re.sub(r'([a-z])([A-Z])', r'\1-\2', text)
        
        # Convert to lowercase
        text = text.lower()
        
        # Clean up multiple hyphens
        text = re.sub(r'-+', '-', text)
        
        # Remove leading/trailing hyphens
        text = text.strip('-')
        
        return text
    
    def scan_directory(self) -> None:
        """Recursively scan directory for markdown files and validate naming."""
        
        # Find all markdown files recursively
        markdown_files = list(self.root_path.rglob("*.md"))
        self.total_files = len(markdown_files)
        
        for file_path in markdown_files:
            # Skip excluded files
            if self.is_excluded(file_path):
                self.total_files -= 1
                continue
                
            # Validate filename
            is_valid, suggested_name = self.validate_filename(file_path)
            
            if not is_valid:
                relative_path = str(file_path.relative_to(self.root_path))
                violation = {
                    "file_path": relative_path,
                    "current_name": file_path.name,
                    "suggested_name": suggested_name,
                    "full_path": str(file_path)
                }
                self.violations.append(violation)
    
    def generate_report(self) -> Dict:
        """
        Generate a validation report.
        
        Returns:
            Dictionary containing validation results
        """
        return {
            "total_files_checked": self.total_files,
            "violations_found": len(self.violations),
            "violations": self.violations,
            "success": len(self.violations) == 0
        }
    
    def print_report(self) -> None:
        """Print the validation report to stdout."""
        
        if self.json_output:
            # JSON output for integration with other tools
            report = self.generate_report()
            print(json.dumps(report, indent=2))
        else:
            # Human-readable output
            print("=" * 60)
            print("Markdown File Naming Validation Report")
            print("=" * 60)
            print(f"Total markdown files checked: {self.total_files}")
            print(f"Violations found: {len(self.violations)}")
            print()
            
            if self.violations:
                print("VIOLATIONS DETECTED:")
                print("-" * 40)
                for i, violation in enumerate(self.violations, 1):
                    print(f"{i}. File: {violation['file_path']}")
                    print(f"   Current name: {violation['current_name']}")
                    print(f"   Suggested name: {violation['suggested_name']}")
                    print()
                
                print("SUMMARY:")
                print("❌ Validation FAILED - Please rename the files above to follow kebab-case convention.")
            else:
                print("✅ All markdown files follow the kebab-case naming convention!")
                print("✅ Validation PASSED")
    
    def validate(self) -> bool:
        """
        Run the validation process.
        
        Returns:
            True if validation passes, False if violations are found
        """
        try:
            self.scan_directory()
            self.print_report()
            return len(self.violations) == 0
        except Exception as e:
            if self.json_output:
                error_report = {
                    "error": str(e),
                    "success": False,
                    "total_files_checked": 0,
                    "violations_found": 0,
                    "violations": []
                }
                print(json.dumps(error_report, indent=2))
            else:
                print(f"❌ Error during validation: {e}", file=sys.stderr)
            return False


def main():
    """Main entry point for the script."""
    
    parser = argparse.ArgumentParser(
        description="Validate markdown file naming conventions (kebab-case)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
This script validates that markdown files follow kebab-case naming convention.

Examples:
  python markdown-naming-check.py
  python markdown-naming-check.py --root-path ./docs
  python markdown-naming-check.py --json
  python markdown-naming-check.py --exclude "temp/*" "draft_*.md"
        """
    )
    
    parser.add_argument(
        "--root-path",
        default=".",
        help="Root directory to start scanning from (default: current directory)"
    )
    
    parser.add_argument(
        "--exclude",
        nargs="*",
        default=["AppConnectorAuditor*.md"],
        help="Patterns to exclude from validation (glob-style)"
    )
    
    parser.add_argument(
        "--json",
        action="store_true",
        help="Output results in JSON format"
    )
    
    parser.add_argument(
        "--version",
        action="version",
        version="1.0.0"
    )
    
    args = parser.parse_args()
    
    # Create validator instance
    validator = MarkdownNamingValidator(
        root_path=args.root_path,
        exclusions=args.exclude,
        json_output=args.json
    )
    
    # Run validation
    success = validator.validate()
    
    # Exit with appropriate code for CI integration
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()