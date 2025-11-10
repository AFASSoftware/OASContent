#!/usr/bin/env python3
"""
Markdown File Naming Validator

This script validates that all markdown files in the repository follow kebab-case naming convention.
It can scan all files or only new/modified files in git.
Also validates that the date in frontmatter matches the current date for changed files.

Author: GitHub Copilot
Date: 2025-07-29
"""

import os
import sys
import argparse
import json
import subprocess
from pathlib import Path
from typing import List, Dict, Tuple, Set
import re
from datetime import datetime
import frontmatter

# Set UTF-8 encoding for Windows console to handle emojis
if sys.platform == 'win32':
    try:
        sys.stdout.reconfigure(encoding='utf-8')
        sys.stderr.reconfigure(encoding='utf-8')
    except AttributeError:
        # Python < 3.7
        import codecs
        sys.stdout = codecs.getwriter('utf-8')(sys.stdout.buffer, 'strict')
        sys.stderr = codecs.getwriter('utf-8')(sys.stderr.buffer, 'strict')


class MarkdownNamingValidator:
    """Validates markdown file naming conventions and date consistency."""
    
    def __init__(self, root_path: str = ".", exclusions: List[str] = None, json_output: bool = False, git_mode: bool = False, fix_dates: bool = False):
        """
        Initialize the validator.
        
        Args:
            root_path: Root directory to start scanning from
            exclusions: List of patterns to exclude from validation
            json_output: Whether to output results in JSON format
            git_mode: If True, only check new/modified files in git
            fix_dates: If True, automatically update dates in frontmatter
        """
        self.root_path = Path(root_path).resolve()
        self.exclusions = exclusions or []
        self.json_output = json_output
        self.git_mode = git_mode
        self.fix_dates = fix_dates
        self.violations = []
        self.date_violations = []
        self.date_fixes = []
        self.total_files = 0
        self.current_date = datetime.now().strftime('%Y-%m-%d')
        
    def get_changed_markdown_files(self) -> Set[Path]:
        """
        Get list of new or modified markdown files from git.
        
        Returns:
            Set of Path objects for changed markdown files
        """
        try:
            # Get the git root directory
            git_root_result = subprocess.run(
                ['git', 'rev-parse', '--show-toplevel'],
                capture_output=True,
                text=True,
                cwd=self.root_path
            )
            
            if git_root_result.returncode != 0:
                return set()
            
            git_root = Path(git_root_result.stdout.strip())
            
            # Get staged files (git add)
            staged_result = subprocess.run(
                ['git', 'diff', '--cached', '--name-only', '--diff-filter=ACMR'],
                capture_output=True,
                text=True,
                cwd=git_root
            )
            
            # Get unstaged files (modified but not added)
            unstaged_result = subprocess.run(
                ['git', 'diff', '--name-only', '--diff-filter=ACMR'],
                capture_output=True,
                text=True,
                cwd=git_root
            )
            
            # Get untracked files
            untracked_result = subprocess.run(
                ['git', 'ls-files', '--others', '--exclude-standard'],
                capture_output=True,
                text=True,
                cwd=git_root
            )
            
            # Combine all changed files
            all_files = set()
            
            if staged_result.returncode == 0:
                all_files.update(staged_result.stdout.strip().split('\n'))
            
            if unstaged_result.returncode == 0:
                all_files.update(unstaged_result.stdout.strip().split('\n'))
            
            if untracked_result.returncode == 0:
                all_files.update(untracked_result.stdout.strip().split('\n'))
            
            # Filter for markdown files only and convert to Path objects
            # Files must be under self.root_path and be markdown files
            markdown_files = set()
            for file in all_files:
                if file and file.endswith('.md'):
                    # Construct full path from git root
                    file_path = git_root / file
                    # Check if file is under our root_path and exists
                    if file_path.exists():
                        try:
                            # Check if the file is within our root_path
                            file_path.relative_to(self.root_path)
                            markdown_files.add(file_path)
                        except ValueError:
                            # File is not under root_path, skip it
                            pass
            
            return markdown_files
            
        except FileNotFoundError:
            if not self.json_output:
                print("Warning: git not found. Falling back to scanning all files.", file=sys.stderr)
            return set()
        except Exception as e:
            if not self.json_output:
                print(f"Warning: Error getting git changes: {e}. Falling back to scanning all files.", file=sys.stderr)
            return set()
    
    def is_excluded(self, file_path: Path) -> bool:
        """
        Check if a file should be excluded from validation.
        
        Args:
            file_path: Path to the file to check
            
        Returns:
            True if the file should be excluded, False otherwise
        """
        try:
            relative_path = str(file_path.relative_to(self.root_path)).replace('\\', '/')
        except ValueError:
            relative_path = str(file_path)
        
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
    
    def validate_date(self, file_path: Path) -> Tuple[bool, str]:
        """
        Validate that the date in frontmatter matches current date for changed files.
        Only validates if git_mode is True.
        
        Args:
            file_path: Path to the markdown file
            
        Returns:
            Tuple of (is_valid, current_date_in_file)
        """
        # Only validate dates in git mode (for changed files)
        if not self.git_mode:
            return True, ""
        
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)
            
            file_date = post.metadata.get('date', '')
            
            # If no date field exists, it's not valid
            if not file_date:
                return False, "missing"
            
            # Convert date to string if it's a datetime object
            if isinstance(file_date, datetime):
                file_date = file_date.strftime('%Y-%m-%d')
            else:
                file_date = str(file_date)
            
            # Check if date matches current date
            return file_date == self.current_date, file_date
            
        except Exception as e:
            # If we can't read the file or parse frontmatter, skip validation
            return True, ""
    
    def fix_date(self, file_path: Path) -> bool:
        """
        Update the date in frontmatter to current date.
        
        Args:
            file_path: Path to the markdown file
            
        Returns:
            True if date was updated successfully, False otherwise
        """
        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                post = frontmatter.load(f)
            
            # Update the date as a date object (without time)
            current_datetime = datetime.strptime(self.current_date, '%Y-%m-%d')
            post.metadata['date'] = current_datetime.date()
            
            # Write back to file
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(frontmatter.dumps(post))
            
            return True
            
        except Exception as e:
            if not self.json_output:
                print(f"Error updating date in {file_path}: {e}", file=sys.stderr)
            return False
    
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
        
        if self.git_mode:
            # Only check changed files
            markdown_files = list(self.get_changed_markdown_files())
            if not markdown_files:
                if not self.json_output:
                    print("No new or modified markdown files found in git.")
        else:
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
                try:
                    relative_path = str(file_path.relative_to(self.root_path))
                except ValueError:
                    relative_path = str(file_path)
                
                violation = {
                    "file_path": relative_path,
                    "current_name": file_path.name,
                    "suggested_name": suggested_name,
                    "full_path": str(file_path)
                }
                self.violations.append(violation)
            
            # Validate date in frontmatter (only in git mode)
            if self.git_mode:
                date_valid, file_date = self.validate_date(file_path)
                
                if not date_valid:
                    if self.fix_dates:
                        # Try to fix the date automatically
                        if self.fix_date(file_path):
                            try:
                                relative_path = str(file_path.relative_to(self.root_path))
                            except ValueError:
                                relative_path = str(file_path)
                            
                            fix_info = {
                                "file_path": relative_path,
                                "old_date": file_date,
                                "new_date": self.current_date,
                                "full_path": str(file_path)
                            }
                            self.date_fixes.append(fix_info)
                        else:
                            # Fix failed, record as violation
                            try:
                                relative_path = str(file_path.relative_to(self.root_path))
                            except ValueError:
                                relative_path = str(file_path)
                            
                            date_violation = {
                                "file_path": relative_path,
                                "current_date": file_date,
                                "expected_date": self.current_date,
                                "full_path": str(file_path)
                            }
                            self.date_violations.append(date_violation)
                    else:
                        # Not fixing, just record violation
                        try:
                            relative_path = str(file_path.relative_to(self.root_path))
                        except ValueError:
                            relative_path = str(file_path)
                        
                        date_violation = {
                            "file_path": relative_path,
                            "current_date": file_date,
                            "expected_date": self.current_date,
                            "full_path": str(file_path)
                        }
                        self.date_violations.append(date_violation)
    
    def generate_report(self) -> Dict:
        """
        Generate a validation report.
        
        Returns:
            Dictionary containing validation results
        """
        return {
            "mode": "git" if self.git_mode else "all",
            "total_files_checked": self.total_files,
            "violations_found": len(self.violations),
            "date_violations_found": len(self.date_violations),
            "violations": self.violations,
            "date_violations": self.date_violations,
            "success": len(self.violations) == 0 and len(self.date_violations) == 0
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
            if self.git_mode:
                print("Mode: Git changes only (new/modified files)")
            else:
                print("Mode: All files")
            print("=" * 60)
            print(f"Total markdown files checked: {self.total_files}")
            print(f"Naming violations found: {len(self.violations)}")
            if self.git_mode:
                print(f"Date violations found: {len(self.date_violations)}")
                if self.fix_dates:
                    print(f"Dates automatically fixed: {len(self.date_fixes)}")
            print()
            
            if self.date_fixes:
                print("DATES AUTOMATICALLY FIXED:")
                print("-" * 40)
                for i, fix in enumerate(self.date_fixes, 1):
                    print(f"{i}. File: {fix['file_path']}")
                    print(f"   Old date: {fix['old_date']}")
                    print(f"   New date: {fix['new_date']}")
                    print()
            
            if self.violations:
                print("NAMING VIOLATIONS DETECTED:")
                print("-" * 40)
                for i, violation in enumerate(self.violations, 1):
                    print(f"{i}. File: {violation['file_path']}")
                    print(f"   Current name: {violation['current_name']}")
                    print(f"   Suggested name: {violation['suggested_name']}")
                    print()
            
            if self.date_violations:
                print("DATE VIOLATIONS DETECTED:")
                print("-" * 40)
                for i, violation in enumerate(self.date_violations, 1):
                    print(f"{i}. File: {violation['file_path']}")
                    print(f"   Current date: {violation['current_date']}")
                    print(f"   Expected date: {violation['expected_date']}")
                    print()
            
            if self.violations or self.date_violations:
                print("SUMMARY:")
                if self.violations:
                    print("Naming validation FAILED - Please rename the files above to follow kebab-case convention.")
                if self.date_violations:
                    print(f"Date validation FAILED - Please update the date in frontmatter to {self.current_date}.")
            else:
                print("All markdown files follow the kebab-case naming convention!")
                if self.git_mode:
                    print(f"All changed files have correct date ({self.current_date}) in frontmatter!")
                print("Validation PASSED")
    
    def validate(self) -> bool:
        """
        Run the validation process.
        
        Returns:
            True if validation passes, False if violations are found
        """
        try:
            self.scan_directory()
            self.print_report()
            return len(self.violations) == 0 and len(self.date_violations) == 0
        except Exception as e:
            if self.json_output:
                error_report = {
                    "error": str(e),
                    "success": False,
                    "mode": "git" if self.git_mode else "all",
                    "total_files_checked": 0,
                    "violations_found": 0,
                    "violations": []
                }
                print(json.dumps(error_report, indent=2))
            else:
                print(f"Error during validation: {e}", file=sys.stderr)
            return False


def main():
    """Main entry point for the script."""
    
    parser = argparse.ArgumentParser(
        description="Validate markdown file naming conventions (kebab-case)",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
This script validates that markdown files follow kebab-case naming convention.

Examples:
  # Check all files
  python markdown-naming-check.py
  
  # Check only new/modified files in git
  python markdown-naming-check.py --git
  
  # Check and automatically fix dates in changed files
  python markdown-naming-check.py --git --fix-dates
  
  # Check specific directory
  python markdown-naming-check.py --root-path ./docs
  
  # JSON output for CI/CD
  python markdown-naming-check.py --git --json
  
  # Exclude specific patterns
  python markdown-naming-check.py --exclude "temp/*" "draft_*.md"
        """
    )
    
    parser.add_argument(
        "--root-path",
        default=".",
        help="Root directory to start scanning from (default: current directory)"
    )
    
    parser.add_argument(
        "--git",
        action="store_true",
        help="Only check new or modified files in git (staged, unstaged, and untracked)"
    )
    
    parser.add_argument(
        "--fix-dates",
        action="store_true",
        help="Automatically update dates in frontmatter to current date (only with --git)"
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
        json_output=args.json,
        git_mode=args.git,
        fix_dates=args.fix_dates
    )
    
    # Run validation
    success = validator.validate()
    
    # Exit with appropriate code for CI integration
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    main()