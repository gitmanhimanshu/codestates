# 🔄 Version Update Guide

## Quick Steps (3 files update karo)

### 1️⃣ pyproject.toml
```toml
[project]
name = "codestats-analyzer"
version = "1.0.1"  # ← Yahan change karo
```

### 2️⃣ codestats/__init__.py
```python
__version__ = "1.0.1"  # ← Yahan change karo
```

### 3️⃣ Build & Upload
```bash
# Clean old builds
Remove-Item -Path dist -Recurse -Force
Remove-Item -Path build -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path codestats_analyzer.egg-info -Recurse -Force -ErrorAction SilentlyContinue

# Build new version
python -m build

# Upload to PyPI
python -m twine upload dist/*
```

## 📋 Version Numbering (Semantic Versioning)

Format: `MAJOR.MINOR.PATCH` (e.g., 1.0.1)

### MAJOR (1.x.x)
- Breaking changes
- API changes that break backward compatibility
- Example: `1.0.0` → `2.0.0`

### MINOR (x.1.x)
- New features
- Backward compatible changes
- Example: `1.0.0` → `1.1.0`

### PATCH (x.x.1)
- Bug fixes
- Small improvements
- Example: `1.0.0` → `1.0.1`

## 🎯 Complete Update Process

### Step 1: Update Version Numbers
```bash
# Edit these 2 files:
# 1. pyproject.toml → version = "1.0.1"
# 2. codestats/__init__.py → __version__ = "1.0.1"
```

### Step 2: Commit Changes
```bash
git add .
git commit -m "Bump version to 1.0.1"
git push
```

### Step 3: Create Git Tag
```bash
git tag -a v1.0.1 -m "Release version 1.0.1"
git push origin v1.0.1
```

### Step 4: Build & Upload
```bash
# Clean
Remove-Item -Path dist -Recurse -Force
Remove-Item -Path build -Recurse -Force -ErrorAction SilentlyContinue
Remove-Item -Path codestats_analyzer.egg-info -Recurse -Force -ErrorAction SilentlyContinue

# Build
python -m build

# Upload
python -m twine upload dist/*
```

### Step 5: Create GitHub Release (Optional)
1. GitHub repo pe jao
2. Releases → Create new release
3. Tag: `v1.0.1`
4. Title: `v1.0.1 - Bug fixes`
5. Description:
   ```
   ## What's Changed
   - Fixed bug in complexity calculation
   - Improved performance
   
   ## Installation
   pip install --upgrade codestats-analyzer
   ```
6. Publish release

## 🤖 Automatic Deployment (GitHub Actions)

Agar tumne GitHub Secret add kiya hai (`PYPI_API_TOKEN`), to:

1. **Version update karo** (pyproject.toml + __init__.py)
2. **Commit & push karo**
3. **GitHub release banao** → Automatic PyPI upload! 🎉

## 📝 Example: Bug Fix Update

```bash
# 1. Update version
# pyproject.toml: version = "1.0.1"
# codestats/__init__.py: __version__ = "1.0.1"

# 2. Commit
git add .
git commit -m "Fix: Resolved complexity calculation bug"
git push

# 3. Tag
git tag -a v1.0.1 -m "Bug fix release"
git push origin v1.0.1

# 4. Build & Upload
Remove-Item -Path dist -Recurse -Force
python -m build
python -m twine upload dist/*
```

## 📝 Example: New Feature Update

```bash
# 1. Update version
# pyproject.toml: version = "1.1.0"
# codestats/__init__.py: __version__ = "1.1.0"

# 2. Commit
git add .
git commit -m "Feature: Added code duplication detection"
git push

# 3. Tag
git tag -a v1.1.0 -m "New feature release"
git push origin v1.1.0

# 4. Build & Upload
Remove-Item -Path dist -Recurse -Force
python -m build
python -m twine upload dist/*
```

## ⚠️ Important Notes

1. **Version cannot be reused** on PyPI
   - Agar 1.0.1 upload kar diya, dobara 1.0.1 nahi kar sakte
   - Always increment version

2. **Test locally first**
   ```bash
   pip install -e .
   codestats .
   pytest tests/
   ```

3. **Update CHANGELOG** (optional but recommended)
   ```markdown
   # Changelog
   
   ## [1.0.1] - 2026-04-06
   ### Fixed
   - Bug in complexity calculation
   - Import detection issue
   
   ## [1.0.0] - 2026-04-06
   - Initial release
   ```

4. **Users ko update batao**
   ```bash
   pip install --upgrade codestats-analyzer
   ```

## 🎯 Quick Commands (Copy-Paste)

```bash
# Update version in files first, then:

# Clean, build, upload
Remove-Item -Path dist -Recurse -Force; Remove-Item -Path build -Recurse -Force -ErrorAction SilentlyContinue; Remove-Item -Path codestats_analyzer.egg-info -Recurse -Force -ErrorAction SilentlyContinue; python -m build; python -m twine upload dist/*

# Git tag
git tag -a v1.0.1 -m "Release v1.0.1"
git push origin v1.0.1
```

## 🔍 Check Current Version

```bash
# Installed version
pip show codestats-analyzer

# Latest on PyPI
pip index versions codestats-analyzer
```
