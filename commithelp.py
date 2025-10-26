#!/usr/bin/env python3
"""
Git Commit Helper - Interactive tool for writing better commit messages
Follows conventional commit format and best practices
"""

import argparse
import subprocess
import sys
from typing import List, Optional

# Conventional commit types
COMMIT_TYPES = {
    'feat': 'A new feature',
    'fix': 'A bug fix',
    'docs': 'Documentation only changes',
    'style': 'Changes that do not affect the meaning of the code',
    'refactor': 'A code change that neither fixes a bug nor adds a feature',
    'perf': 'A code change that improves performance',
    'test': 'Adding missing tests or correcting existing tests',
    'chore': 'Changes to the build process or auxiliary tools',
    'build': 'Changes that affect the build system or external dependencies',
    'ci': 'Changes to CI configuration files and scripts',
    'revert': 'Reverts a previous commit'
}

class CommitHelper:
    """Helper class for creating conventional commits"""
    
    def __init__(self):
        self.type = ""
        self.scope = ""
        self.description = ""
        self.body = ""
        self.breaking = False
        
    def select_type(self) -> str:
        """Interactive type selection"""
        print("\n📝 Select commit type:")
        types = list(COMMIT_TYPES.keys())
        for i, commit_type in enumerate(types, 1):
            print(f"  {i}. {commit_type:12} - {COMMIT_TYPES[commit_type]}")
        
        while True:
            try:
                choice = input("\nEnter number (1-{}): ".format(len(types))).strip()
                idx = int(choice) - 1
                if 0 <= idx < len(types):
                    return types[idx]
                print("❌ Invalid selection. Try again.")
            except (ValueError, KeyboardInterrupt):
                print("\n❌ Cancelled.")
                sys.exit(1)
    
    def get_scope(self) -> str:
        """Get optional scope"""
        scope = input("\n🎯 Scope (optional, press Enter to skip): ").strip()
        return scope
    
    def get_description(self) -> str:
        """Get commit description"""
        while True:
            desc = input("\n📋 Brief description (required): ").strip()
            if desc:
                if len(desc) > 72:
                    print("⚠️  Warning: Description is quite long. Consider shortening.")
                    confirm = input("Continue anyway? (y/n): ").strip().lower()
                    if confirm == 'y':
                        return desc
                else:
                    return desc
            print("❌ Description is required.")
    
    def get_body(self) -> str:
        """Get optional commit body"""
        print("\n📄 Extended description (optional, press Enter to skip):")
        print("   (Enter a blank line when done)")
        lines = []
        while True:
            line = input()
            if not line:
                break
            lines.append(line)
        return "\n".join(lines)
    
    def check_breaking(self) -> bool:
        """Check if this is a breaking change"""
        response = input("\n⚠️  Is this a BREAKING CHANGE? (y/n): ").strip().lower()
        return response == 'y'
    
    def build_message(self) -> str:
        """Build the complete commit message"""
        # Build header
        header = self.type
        if self.scope:
            header += f"({self.scope})"
        if self.breaking:
            header += "!"
        header += f": {self.description}"
        
        # Build full message
        parts = [header]
        
        if self.body:
            parts.append("")  # Blank line
            parts.append(self.body)
        
        if self.breaking:
            parts.append("")  # Blank line
            parts.append("BREAKING CHANGE: This commit introduces breaking changes.")
        
        return "\n".join(parts)
    
    def interactive_commit(self):
        """Interactive commit creation"""
        print("\n" + "="*60)
        print("🚀 Git Commit Helper - Interactive Mode")
        print("="*60)
        
        self.type = self.select_type()
        self.scope = self.get_scope()
        self.description = self.get_description()
        self.body = self.get_body()
        self.breaking = self.check_breaking()
        
        message = self.build_message()
        
        print("\n" + "="*60)
        print("📨 Generated commit message:")
        print("="*60)
        print(message)
        print("="*60)
        
        confirm = input("\n✅ Commit with this message? (y/n): ").strip().lower()
        if confirm == 'y':
            return self.execute_commit(message)
        else:
            print("❌ Commit cancelled.")
            return False
    
    def execute_commit(self, message: str) -> bool:
        """Execute the git commit"""
        try:
            subprocess.run(['git', 'commit', '-m', message], check=True)
            print("\n✅ Commit successful!")
            return True
        except subprocess.CalledProcessError as e:
            print(f"\n❌ Commit failed: {e}")
            return False
        except FileNotFoundError:
            print("\n❌ Git not found. Make sure git is installed and in PATH.")
            return False

def quick_commit(commit_type: str, description: str, scope: Optional[str] = None):
    """Quick commit without interaction"""
    helper = CommitHelper()
    helper.type = commit_type
    helper.scope = scope or ""
    helper.description = description
    
    message = helper.build_message()
    return helper.execute_commit(message)

def show_status():
    """Show git status"""
    try:
        subprocess.run(['git', 'status', '--short'], check=True)
    except subprocess.CalledProcessError:
        print("❌ Failed to get git status")
    except FileNotFoundError:
        print("❌ Git not found")

def show_types():
    """Display all commit types"""
    print("\n📝 Conventional Commit Types:")
    print("="*60)
    for commit_type, description in COMMIT_TYPES.items():
        print(f"  {commit_type:12} - {description}")
    print("="*60)

def main():
    parser = argparse.ArgumentParser(
        description='Git Commit Helper - Write better commit messages',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  commithelp.py                           # Interactive mode
  commithelp.py -q feat "Add user login"  # Quick commit
  commithelp.py -q fix "Fix null pointer" -s auth  # With scope
  commithelp.py --status                  # Show git status
  commithelp.py --types                   # List commit types
        """
    )
    
    parser.add_argument('-q', '--quick', nargs=2, metavar=('TYPE', 'DESC'),
                        help='Quick commit: TYPE and DESCRIPTION')
    parser.add_argument('-s', '--scope', help='Scope for quick commit')
    parser.add_argument('--status', action='store_true',
                        help='Show git status')
    parser.add_argument('--types', action='store_true',
                        help='List all commit types')
    
    args = parser.parse_args()
    
    # Handle flags
    if args.status:
        show_status()
        return
    
    if args.types:
        show_types()
        return
    
    # Quick commit mode
    if args.quick:
        commit_type, description = args.quick
        if commit_type not in COMMIT_TYPES:
            print(f"❌ Invalid commit type: {commit_type}")
            print(f"Valid types: {', '.join(COMMIT_TYPES.keys())}")
            sys.exit(1)
        
        if quick_commit(commit_type, description, args.scope):
            sys.exit(0)
        else:
            sys.exit(1)
    
    # Interactive mode (default)
    helper = CommitHelper()
    if helper.interactive_commit():
        sys.exit(0)
    else:
        sys.exit(1)

if __name__ == '__main__':
    main()
