# Python Installation & Package Management Guide

A comprehensive guide to modern Python version and package management on macOS.

## Table of Contents

- [Overview](#overview)
- [Understanding the Landscape](#understanding-the-landscape)
- [Traditional Approach: pyenv + pip + venv](#traditional-approach-pyenv--pip--venv)
  - [Checking Your Current Python](#checking-your-current-python)
  - [Installing Python Versions with pyenv](#installing-python-versions-with-pyenv)
  - [Switching Python Versions](#switching-python-versions)
  - [Virtual Environments](#virtual-environments)
- [Modern Approach: UV](#modern-approach-uv)
  - [Why UV?](#why-uv)
  - [Installation](#installation)
  - [Basic Workflow](#basic-workflow)
- [Comparison Table](#comparison-table)
- [Recommendations](#recommendations)
- [Additional Resources](#additional-resources)

---

## Overview

Python development requires managing multiple Python versions and package dependencies across different projects. This guide covers both traditional and modern approaches to Python installation and package management on macOS.

**TL;DR:**
- **Learning/Legacy projects**: Use traditional `pyenv` + `venv` approach
- **New projects (2024+)**: Use modern `uv` tool (10-100x faster)

---

## Understanding the Landscape

### Multiple Python Installations

Your macOS system may have multiple Python installations:

1. **System Python** - macOS default (don't use for development)
2. **Homebrew Python** - Installed via `brew install python`
3. **pyenv-managed Pythons** - Installed via `pyenv install`
4. **uv-managed Pythons** - Installed via `uv python install`

### Checking Active Python

To see which Python is currently active:

```bash
# Check Python 3 location and version
which python3 && python3 --version

# Check Python location and version
which python && python --version

# Example output:
# /Users/username/.pyenv/shims/python3
# Python 3.12.0
```

### Package Installation Location

When you run `pip install <package>`, it installs to the **currently active Python** version:

```bash
# List installed packages for current Python
python3 -m pip list
```

#### Installation Scopes

| Command | Installation Location |
|---------|----------------------|
| `pip install <package>` | Python's site-packages directory |
| `pip install --user <package>` | `~/.local/lib/python3.x/site-packages/` |

---

## Traditional Approach: pyenv + pip + venv

The tried-and-tested method that has been the standard for years.

### Installing Python Versions with pyenv

#### Setup pyenv

```bash
# Install pyenv via Homebrew
brew install pyenv

# Add to shell configuration (~/.zshrc or ~/.bash_profile)
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshrc
echo 'eval "$(pyenv init -)"' >> ~/.zshrc

# Reload shell
source ~/.zshrc
```

#### Install Python Versions

```bash
# List available Python versions
pyenv install --list

# Install specific version
pyenv install 3.12.0
pyenv install 3.7.17

# Set global default
pyenv global 3.12.0
```

### Switching Python Versions

```bash
# Set Python for current directory (creates .python-version file)
pyenv local 3.7.17

# Set for current shell session only
pyenv shell 3.11.0

# Set system-wide default
pyenv global 3.12.0
```

### Virtual Environments

#### The Problem: Dependency Conflicts

Imagine you're working on multiple Python projects:

**Project A** - A legacy web application that requires:
- `Django==2.2.0` (released in 2019)
- `requests==2.20.0`

**Project B** - A modern data analysis tool that requires:
- `Django==5.0.0` (latest version)
- `requests==2.31.0`

**Without virtual environments**, when you install packages, they go into your system-wide Python installation:

```bash
# Working on Project A
pip install Django==2.2.0    # Installs globally

# Switch to Project B
pip install Django==5.0.0    # Overwrites Django 2.2.0!

# Go back to Project A
python manage.py runserver   # ❌ BREAKS! Project A needs Django 2.2.0
```

**The core problem:**
- All packages share the same installation directory
- Installing/upgrading a package for one project affects all projects
- You can only have **one version** of each package at a time
- Breaking changes in new versions cause existing projects to fail

**Real-world scenario:**

You have:
- **E-commerce Site** (production): Uses `stripe==2.48.0` for payment processing
- **New Microservice** (development): Needs `stripe==8.0.0` with new features

Without isolation:
```bash
pip install stripe==8.0.0  # Upgrade for new project
# ❌ E-commerce site suddenly breaks in production!
# Old API methods were removed in stripe 8.0.0
```

#### The Solution: Virtual Environments

Virtual environments create **isolated Python installations** for each project. Each environment has its own:
- Package installation directory
- Independent package versions
- Separate dependency tree

Think of it as having multiple "Python sandboxes" - changes in one don't affect others.

#### Option 1: Standard Python venv (Built-in)

Creates a local virtual environment in your project directory.

```bash
cd /path/to/your/project

# Create virtual environment
python -m venv myenv

# Activate (must do every time you work on this project)
source myenv/bin/activate

# Now pip installs packages only in THIS environment
pip install requests==2.20.0

# Your terminal prompt shows you're in the venv:
# (myenv) user@machine:~/project$

# Deactivate when done
deactivate
```

**How it works:**
```bash
# Before activation
which python
# /usr/local/bin/python

pip list
# [System-wide packages]

# After activation
source myenv/bin/activate

which python
# /path/to/project/myenv/bin/python  ← Different Python!

pip list
# [Only packages in THIS virtual environment]
```

**Directory structure:**
```
your-project/
├── myenv/                    ← Virtual environment
│   ├── bin/
│   │   ├── python           ← Isolated Python
│   │   ├── pip              ← Isolated pip
│   │   └── activate         ← Activation script
│   ├── lib/
│   │   └── python3.12/
│   │       └── site-packages/  ← Packages install here
│   └── ...
├── app.py
└── requirements.txt
```

**Characteristics:**
- ✅ No additional tools needed
- ✅ Environment lives with project
- ✅ Complete isolation per project
- ❌ Must manually activate each time
- ❌ Not centrally managed
- ❌ Takes up disk space per project

#### Option 2: pyenv virtualenv (Plugin)

Creates a **named** virtual environment managed centrally by pyenv.

```bash
# Install pyenv-virtualenv plugin first
brew install pyenv-virtualenv

# Add to ~/.zshrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc
source ~/.zshrc

# Create named environment (can be reused across projects)
pyenv virtualenv 3.7.17 company-xyz-env

# Activate manually
pyenv activate company-xyz-env

# OR set for project directory (auto-activates on cd)
cd /path/to/your/project
pyenv local company-xyz-env

# Now whenever you cd into this directory, company-xyz-env auto-activates!
```

**Use case for named environments:**

You work at a company with three related microservices that share dependencies:
```bash
# Create shared environment
pyenv virtualenv 3.11.0 company-backend-env
pyenv activate company-backend-env

# Install common dependencies once
pip install fastapi==0.104.0 sqlalchemy==2.0.0 pydantic==2.5.0

# Use in multiple projects
cd ~/projects/user-service
pyenv local company-backend-env

cd ~/projects/order-service
pyenv local company-backend-env

cd ~/projects/notification-service
pyenv local company-backend-env

# All three services use the same environment and dependency versions!
```

**Characteristics:**
- ✅ Named environments (reusable)
- ✅ Centrally managed in `~/.pyenv/versions/3.7.17/envs/`
- ✅ Auto-activation with `pyenv local`
- ✅ Works across multiple projects with same dependencies
- ✅ Saves disk space (one environment for multiple projects)
- ❌ Requires `pyenv-virtualenv` plugin

#### Comparison: venv vs pyenv virtualenv

| Feature | python venv | pyenv virtualenv |
|---------|-------------|------------------|
| **Location** | Project directory (`./myenv/`) | `~/.pyenv/versions/X.X.X/envs/` |
| **Activation** | `source myenv/bin/activate` | `pyenv activate env-name` |
| **Auto-activate** | No | Yes (with `pyenv local`) |
| **Naming** | Path-based | Named environments |
| **Reusability** | Per-project only | Can share across projects |
| **Setup** | Built-in | Requires plugin |
| **Disk usage** | Duplicated per project | Shared across projects |

#### Which Virtual Environment Should You Use?

**Use `python venv` when:**
- You want maximum isolation (each project completely independent)
- You're learning Python (simpler to understand)
- Different projects need conflicting dependency versions
- You want to keep everything together with the project

**Use `pyenv virtualenv` when:**
- You manage many related projects with similar dependencies
- You want centralized environment management
- You want auto-activation on `cd`
- Disk space is a concern

---

## Modern Approach: UV

**UV** is the next-generation Python package and project manager created by Astral (makers of `ruff`).

Official Documentation: https://docs.astral.sh/uv/

### Why UV?

UV is the **2024/2025 trend** in Python development because it:

| Feature | Benefit |
|---------|---------|
| ⚡ **10-100x faster** | Rust-powered performance vs pip |
| 🔄 **Manages Python versions** | Replaces pyenv |
| 📦 **Manages packages** | Replaces pip |
| 🌐 **Manages virtual environments** | Replaces venv/virtualenv |
| 🔒 **Lock files** | Like poetry/pipenv |
| 🎯 **Single tool** | One tool for everything |
| 📝 **Compatible** | Works with pip/requirements.txt |

### Installation

```bash
# Install UV
curl -LsSf https://astral.sh/uv/install.sh | sh
```

**Output:**
```
downloading uv 0.9.9 aarch64-apple-darwin
no checksums to verify
installing to ~/.local/bin
  uv
  uvx
everything's installed!
```

### Basic Workflow

#### 1. Check Available Python Versions

```bash
# List both installed and available Python versions
uv python list

# Check current Python in use
uv python find

# Check if specific version exists
uv python find 3.12.0
```

#### 2. Install Python (if needed)

```bash
# Install specific Python version
uv python install 3.12.0
uv python install 3.7.17
```

#### 3. Set Up Your Project

```bash
cd /path/to/your/project

# Pin Python version (creates .python-version file)
uv python pin 3.12.0

# This file tells uv to automatically use Python 3.12.0 in this directory
```

#### 4. Create Virtual Environment

```bash
# Create venv with pinned Python version
uv venv

# Or specify Python version explicitly
uv venv --python 3.12.0

# Automatically activates! Verify:
which python
python --version
```

#### 5. Install Packages

```bash
# Install packages (goes to project's venv)
uv pip install requests
uv pip install pandas numpy

# Install from requirements.txt
uv pip install -r requirements.txt

# Install with specific Python version
uv pip install --python 3.12 requests
```

#### 6. Run Your Code

```bash
# Run Python script
uv run python script.py

# Run installed CLI tools
uv add pytest  # Install pytest
uv run pytest  # Run tests

# Interactive Python REPL
uv run python
```

### Complete Example Workflow

```bash
# Navigate to project
cd ~/my-project

# Pin Python version
uv python pin 3.12.0

# Create virtual environment
uv venv

# Install dependencies
uv pip install fastapi uvicorn pytest

# Run your application
uv run python main.py

# Run tests
uv run pytest
```

---

## Comparison Table

### Tool Comparison

| Tool | Python Versions | Package Management | Virtual Environments | Speed | Status |
|------|----------------|--------------------|--------------------|-------|--------|
| **uv** | ✅ | ✅ | ✅ | 🚀🚀🚀 | **2024+ Standard** |
| pyenv + pip | ✅ | ✅ | Manual (venv) | 🐌 | Traditional |
| Poetry | ❌ | ✅ | ✅ | 🐌 | Popular Alternative |
| Conda | ✅ | ✅ | ✅ | 🐌🐌 | Data Science Focus |

### When to Use Each Approach

| Scenario | Recommended Tool | Reason |
|----------|------------------|--------|
| **New project (2024+)** | UV | Modern, fast, all-in-one |
| **Learning Python** | pyenv + venv | Industry standard, widely documented |
| **Legacy project** | pyenv + venv | Matches existing setup |
| **Data science** | Conda/Miniconda | Non-Python dependencies (CUDA, etc.) |
| **Publishing packages** | Poetry or UV | Built-in dependency resolution |
| **Team with existing workflow** | Match team standard | Consistency |

---

## Recommendations

### For Beginners
Start with **pyenv + venv**:
- Widely documented
- Separate tools = clear mental model
- Transferable skills across teams

### For New Projects (2024+)
Use **UV**:
- Fastest growing adoption
- Best performance
- Single tool to learn
- Future-proof

### For Existing Projects
Stick with **current tooling**:
- Don't fix what isn't broken
- Team consistency matters
- Migration has a cost

### Quick Start Commands

**Traditional Approach:**
```bash
# One-time setup
brew install pyenv
pyenv install 3.12.0

# Per project
cd my-project
pyenv local 3.12.0
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

**Modern Approach:**
```bash
# One-time setup
curl -LsSf https://astral.sh/uv/install.sh | sh

# Per project
cd my-project
uv python pin 3.12.0
uv venv
uv pip install -r requirements.txt
uv run python main.py
```

---

## Additional Resources

### Official Documentation
- **UV**: https://docs.astral.sh/uv/
- **pyenv**: https://github.com/pyenv/pyenv
- **Python venv**: https://docs.python.org/3/library/venv.html
- **pip**: https://pip.pypa.io/

### Related Tools
- **ruff**: Modern Python linter/formatter (https://github.com/astral-sh/ruff)
- **Poetry**: Alternative package manager (https://python-poetry.org/)
- **pipx**: Install CLI tools globally (https://pipx.pypa.io/)

### Community
- UV GitHub: https://github.com/astral-sh/uv
- Python Packaging User Guide: https://packaging.python.org/

---

**Last Updated:** November 2024

**Author:** Based on practical experience and community best practices

