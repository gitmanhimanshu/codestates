# 🤖 Automatic PyPI Deployment via GitHub

Tumne GitHub se PyPI connect kar diya hai! Ab automatic deployment setup karte hain. 🚀

## ✅ Setup (One-time - 5 minutes)

### Step 1: PyPI API Token GitHub me add karo

1. **PyPI Token copy karo**:
   - PyPI login karo: https://pypi.org/manage/account/token/
   - Token banao (agar nahi hai):
     - Name: `github-actions`
     - Scope: "Entire account"
   - Token copy karo (format: `pypi-AgEI...`)

2. **GitHub me Secret add karo**:
   - Apne repo pe jao: `https://github.com/yourusername/codestats`
   - Settings → Secrets and variables → Actions
   - "New repository secret" click karo
   - **Name**: `PYPI_API_TOKEN` (exactly ye naam)
   - **Value**: Tumhara PyPI token paste karo
   - "Add secret" click karo

### Step 2: Workflow file check karo

File already hai: `.github/workflows/publish.yml` ✅

Ye automatically PyPI pe upload karega jab tum GitHub release banao.

## 🚀 Deploy Kaise Kare (Har baar)

### Method 1: GitHub UI se (Easy)

1. **Code push karo**:
```bash
git add .
git commit -m "Ready for release v1.0.0"
git push
```

2. **GitHub pe Release banao**:
   - Repo pe jao: `https://github.com/yourusername/codestats`
   - "Releases" → "Create a new release"
   - **Tag**: `v1.0.0` (new tag banao)
   - **Title**: `v1.0.0 - Initial Release`
   - **Description**:
     ```
     🎉 First release of CodeStats!
     
     Features:
     - Code metrics analysis
     - Complexity detection
     - Quality scoring
     - Smart suggestions
     ```
   - "Publish release" click karo

3. **Automatic deployment**:
   - GitHub Actions automatically run hoga
   - 2-3 minutes me PyPI pe upload ho jayega
   - Check karo: Actions tab me

### Method 2: Command Line se (Pro)

```bash
# 1. Code commit karo
git add .
git commit -m "Release v1.0.0"

# 2. Tag banao
git tag -a v1.0.0 -m "Release version 1.0.0"

# 3. Push with tags
git push origin main --tags

# 4. GitHub pe jao aur release banao (UI se)
```

## 📊 Deployment Status Check

### GitHub Actions check karo:
1. Repo → "Actions" tab
2. Latest workflow run dekho
3. Green checkmark = Success ✅
4. Red X = Failed ❌ (logs dekho)

### PyPI check karo:
- Wait 2-3 minutes
- Check: `https://pypi.org/project/codestats-analyzer/`
- Install test: `pip install codestats-analyzer`

## 🔄 Update Version Deploy Karna

### Step 1: Version update karo
```python
# setup.py me change karo
version="1.0.1",  # 1.0.0 → 1.0.1
```

### Step 2: Commit & Release
```bash
git add setup.py
git commit -m "Bump version to 1.0.1"
git push

# GitHub pe new release banao: v1.0.1
```

### Step 3: Automatic upload
- GitHub Actions automatically run hoga
- PyPI pe v1.0.1 upload ho jayega

## 🎯 Complete Workflow Example

```bash
# 1. Code changes karo
# ... edit files ...

# 2. Version bump (setup.py)
# version="1.0.1"

# 3. Commit
git add .
git commit -m "Add new features for v1.0.1"
git push

# 4. GitHub pe jao
# Releases → New release
# Tag: v1.0.1
# Publish release

# 5. Wait 2-3 minutes
# Check: https://pypi.org/project/codestats-analyzer/

# 6. Test
pip install --upgrade codestats-analyzer
codestats .
```

## ⚠️ Troubleshooting

### Error: "PYPI_API_TOKEN not found"
**Fix**: GitHub Secrets me token add karo (Step 1 dekho)

### Error: "File already exists"
**Fix**: setup.py me version number change karo

### Error: "Invalid authentication"
**Fix**: 
- PyPI token regenerate karo
- GitHub Secret update karo

### Workflow run nahi hua
**Fix**:
- Check: Release "published" hai (draft nahi)
- Check: Tag format correct hai (`v1.0.0`)
- Check: `.github/workflows/publish.yml` file exists

## 💡 Pro Tips

### 1. Pre-release testing
```bash
# Local test pehle
pip install -e .
codestats .
pytest tests/
```

### 2. Changelog maintain karo
Create `CHANGELOG.md`:
```markdown
# Changelog

## [1.0.1] - 2026-04-06
- Fixed bug in complexity calculation
- Added new feature

## [1.0.0] - 2026-04-06
- Initial release
```

### 3. Release notes template
```markdown
## What's Changed
- Feature: Added X
- Fix: Resolved Y
- Improvement: Enhanced Z

## Installation
pip install --upgrade codestats-analyzer

## Full Changelog
https://github.com/yourusername/codestats/compare/v1.0.0...v1.0.1
```

## 🎊 Success Checklist

- [ ] PyPI token GitHub Secrets me add kiya
- [ ] `.github/workflows/publish.yml` file exists
- [ ] Code GitHub pe push kiya
- [ ] GitHub release banaya
- [ ] Actions tab me green checkmark dikha
- [ ] PyPI pe package dikha
- [ ] `pip install codestats-analyzer` working

## 📢 Next Steps

1. **README badge add karo**:
```markdown
[![PyPI version](https://badge.fury.io/py/codestats-analyzer.svg)](https://pypi.org/project/codestats-analyzer/)
[![Downloads](https://pepy.tech/badge/codestats-analyzer)](https://pepy.tech/project/codestats-analyzer)
```

2. **Social media pe share karo**:
```
🎉 Just published codestats-analyzer on PyPI!

Install: pip install codestats-analyzer

Analyze your Python code instantly!
```

3. **Documentation improve karo**:
- Examples add karo
- Screenshots add karo
- Video demo banao

## 🚀 You're All Set!

Ab har baar GitHub pe release banao, automatic PyPI pe deploy ho jayega! 🎉
