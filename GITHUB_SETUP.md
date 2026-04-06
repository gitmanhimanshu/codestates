# 🚀 GitHub Setup & pip Install Guide

## Step 1: GitHub pe Push karo

### 1.1 Git Initialize karo
```bash
git init
git add .
git commit -m "Initial commit: CodeStats analyzer"
```

### 1.2 GitHub pe repo banao
1. GitHub.com pe jao
2. New repository banao: `codestats`
3. Public rakho (important for pip install)
4. README.md mat banao (already hai)

### 1.3 Push karo
```bash
# Replace 'yourusername' with your GitHub username
git remote add origin https://github.com/yourusername/codestats.git
git branch -M main
git push -u origin main
```

## Step 2: GitHub se Direct Install (pip)

### Method 1: Direct GitHub Install (sabse easy)
```bash
# Install directly from GitHub
pip install git+https://github.com/yourusername/codestats.git

# Use karo
codestats .
```

### Method 2: Specific branch/tag se install
```bash
# Main branch se
pip install git+https://github.com/yourusername/codestats.git@main

# Specific tag se (v1.0.0)
pip install git+https://github.com/yourusername/codestats.git@v1.0.0
```

### Method 3: requirements.txt mein add karo
```txt
# requirements.txt
git+https://github.com/yourusername/codestats.git
```

Then:
```bash
pip install -r requirements.txt
```

## Step 3: Release banao (recommended)

### 3.1 Tag create karo
```bash
git tag -a v1.0.0 -m "Release version 1.0.0"
git push origin v1.0.0
```

### 3.2 GitHub Release banao
1. GitHub repo pe jao
2. "Releases" → "Create a new release"
3. Tag select karo: `v1.0.0`
4. Title: "CodeStats v1.0.0"
5. Description add karo
6. "Publish release"

### 3.3 Install from release
```bash
pip install git+https://github.com/yourusername/codestats.git@v1.0.0
```

## Step 4: PyPI se Link (optional - best method)

Agar chahte ho ki log sirf `pip install codestats-analyzer` se install karein:

### 4.1 PyPI pe upload karo
```bash
pip install build twine
python -m build
python -m twine upload dist/*
```

### 4.2 setup.py mein GitHub link already hai
```python
url="https://github.com/yourusername/codestats",
project_urls={
    'Source': 'https://github.com/yourusername/codestats',
}
```

### 4.3 Install from PyPI
```bash
pip install codestats-analyzer
```

## 🎯 Quick Commands Summary

```bash
# GitHub setup
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/yourusername/codestats.git
git push -u origin main

# Install from GitHub
pip install git+https://github.com/yourusername/codestats.git

# Test
codestats .
```

## 📝 Update karne ke liye

```bash
# Code change karo
git add .
git commit -m "Updated features"
git push

# New version tag
git tag -a v1.0.1 -m "Version 1.0.1"
git push origin v1.0.1

# Users ko update
pip install --upgrade git+https://github.com/yourusername/codestats.git
```

## ⚠️ Important Notes

1. **Repo PUBLIC hona chahiye** - private se pip install nahi hoga
2. **setup.py must be in root** - already hai ✅
3. **GitHub URL correct ho** - apna username daalo
4. **Tag versioning** - semantic versioning use karo (v1.0.0, v1.0.1)

## 🔗 Installation Methods Comparison

| Method | Command | Best For |
|--------|---------|----------|
| GitHub Direct | `pip install git+https://...` | Development, testing |
| GitHub Release | `pip install git+https://...@v1.0.0` | Stable versions |
| PyPI | `pip install codestats-analyzer` | Public distribution |

## 🎉 Share karo

Apne README.md mein add karo:

```markdown
## Installation

```bash
pip install git+https://github.com/yourusername/codestats.git
```

Or from PyPI:

```bash
pip install codestats-analyzer
```
```

## 🐛 Troubleshooting

**Error: Repository not found**
- Check if repo public hai
- GitHub URL correct hai

**Error: No module named 'codestats'**
- setup.py check karo
- `pip install -e .` locally test karo

**Error: Permission denied**
- GitHub authentication check karo
- SSH key setup karo ya HTTPS use karo
