# Git Commit Helper

Interactive Python CLI tool for writing better git commit messages following the Conventional Commits specification.

## Features

- 🎯 **Interactive Mode**: Guided workflow for creating well-structured commits
- ⚡ **Quick Mode**: Fast commits from command line
- 📝 **Conventional Commits**: Follows industry-standard format (type, scope, description)
- ⚠️ **Breaking Changes**: Easy marking of breaking changes
- 📋 **Extended Descriptions**: Optional detailed commit body
- 🔍 **Git Status**: Quick status overview
- 📖 **Type Reference**: Built-in commit type descriptions

## Installation

1. Clone this repository:
```bash
git clone https://github.com/DonkRonk17/git-commit-helper.git
cd git-commit-helper
```

2. Make the script executable (Linux/Mac):
```bash
chmod +x commithelp.py
```

3. Optional: Add to PATH for global access

## Usage

### Interactive Mode (Default)

Run without arguments for guided commit creation:

```bash
python commithelp.py
```

The interactive mode will:
1. Let you select a commit type from a list
2. Prompt for an optional scope
3. Ask for a brief description
4. Allow extended description (optional)
5. Check if it's a breaking change
6. Show preview and confirm before committing

### Quick Mode

Create commits directly from the command line:

```bash
# Basic quick commit
python commithelp.py -q feat "Add user authentication"

# Quick commit with scope
python commithelp.py -q fix "Fix login bug" -s auth

# Other examples
python commithelp.py -q docs "Update README"
python commithelp.py -q refactor "Improve database queries" -s db
```

### Helper Commands

```bash
# Show git status
python commithelp.py --status

# List all commit types with descriptions
python commithelp.py --types
```

## Commit Types

| Type | Description |
|------|-------------|
| **feat** | A new feature |
| **fix** | A bug fix |
| **docs** | Documentation only changes |
| **style** | Code style changes (formatting, etc.) |
| **refactor** | Code change that neither fixes a bug nor adds a feature |
| **perf** | Performance improvements |
| **test** | Adding or correcting tests |
| **chore** | Build process or auxiliary tool changes |
| **build** | Build system or external dependency changes |
| **ci** | CI configuration changes |
| **revert** | Reverts a previous commit |

## Conventional Commit Format

The tool generates commits following this format:

```
<type>[optional scope][!]: <description>

[optional body]

[optional footer]
```

Examples:
- `feat: add user registration`
- `fix(auth): resolve token expiration issue`
- `feat(api)!: change authentication endpoint`
- `docs: update installation instructions`

## Why Use This Tool?

- ✅ Consistent commit message format across your team
- ✅ Better changelog generation
- ✅ Easier to understand project history
- ✅ Automated versioning support (SemVer)
- ✅ Faster code reviews
- ✅ Professional commit history

## Requirements

- Python 3.6+
- Git installed and in PATH

## License

MIT License - feel free to use and modify!

## Contributing

Contributions welcome! Please feel free to submit a Pull Request.
