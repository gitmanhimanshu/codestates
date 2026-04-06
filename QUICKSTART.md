# ⚡ Quick Start Guide

## 🧪 Testing (Local)

### Step 1: Install
```bash
pip install -e .
```

### Step 2: Test it
```bash
# Test on current project
codestats .

# Or use Python
python example.py
```

### Step 3: Run tests (optional)
```bash
pip install pytest
pytest tests/
```

## 🚀 Deploy to PyPI

### Step 1: Setup
```bash
# Install tools
pip install build twine

# Create PyPI account
# Go to: https://pypi.org/account/register/
```

### Step 2: Update setup.py
- Change `name` to unique name (check PyPI first)
- Add your email and GitHub URL
- Update author name

### Step 3: Build
```bash
python -m build
```

### Step 4: Upload
```bash
# Get API token from: https://pypi.org/manage/account/token/
python -m twine upload dist/*

# Username: __token__
# Password: <paste-your-token>
```

### Step 5: Install from PyPI
```bash
pip install codestats-analyzer
codestats .
```

## 🎯 That's it!

Detailed guides:
- Testing: See `TEST.md`
- Deployment: See `DEPLOY.md`
