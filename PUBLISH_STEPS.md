# 🚀 PyPI Publish - Step by Step

## ✅ Pre-requisites Check

```bash
# 1. Test locally pehle
pip install -e .
codestats .

# 2. Sab kuch working hai?
python example.py
```

## 📝 Step 1: PyPI Account Setup (5 min)

### 1.1 Account banao
1. **PyPI**: https://pypi.org/account/register/
2. Email verify karo
3. 2FA enable karo (recommended)

### 1.2 API Token banao
1. Login karo PyPI pe
2. Account Settings → API tokens
3. "Add API token"
   - Token name: `codestats-upload`
   - Scope: "Entire account" (pehli baar ke liye)
4. **Token copy karo** (sirf ek baar dikhega!)
   - Format: `pypi-AgEIcHlwaS5vcmc...` (long string)
5. Safe jagah save karo

## 🔧 Step 2: Tools Install

```bash
pip install --upgrade build twine
```

## 📦 Step 3: Package Name Check (IMPORTANT!)

```bash
# Check if name available hai
# Browser me jao: https://pypi.org/project/codestats-analyzer/
```

**Agar already exists:**
- `setup.py` me name change karo
- Try: `codestats-py`, `py-codestats`, `codestats-tool`

## 🏗️ Step 4: Build Package

```bash
# Clean previous builds
rm -rf build/ dist/ *.egg-info/

# Build
python -m build
```

**Output dikhega:**
```
Successfully built codestats_analyzer-1.0.0.tar.gz
Successfully built codestats_analyzer-1.0.0-py3-none-any.whl
```

## 🧪 Step 5: Test on TestPyPI (Optional but Recommended)

### 5.1 TestPyPI account banao
- https://test.pypi.org/account/register/
- API token banao (same process)

### 5.2 Upload to TestPyPI
```bash
python -m twine upload --repository testpypi dist/*
```

**Prompts:**
```
Enter your username: __token__
Enter your password: pypi-AgEIcHlwaS5vcmc...  (paste token)
```

### 5.3 Test install
```bash
pip install --index-url https://test.pypi.org/simple/ codestats-analyzer
codestats .
```

## 🎉 Step 6: Upload to PyPI (FINAL!)

```bash
python -m twine upload dist/*
```

**Prompts:**
```
Enter your username: __token__
Enter your password: pypi-AgEIcHlwaS5vcmc...  (paste your REAL PyPI token)
```

**Success message:**
```
Uploading distributions to https://upload.pypi.org/legacy/
Uploading codestats_analyzer-1.0.0-py3-none-any.whl
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 
Uploading codestats_analyzer-1.0.0.tar.gz
100% ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

View at:
https://pypi.org/project/codestats-analyzer/1.0.0/
```

## ✅ Step 7: Verify & Test

```bash
# Wait 1-2 minutes for PyPI to process

# Install from PyPI
pip install codestats-analyzer

# Test
codestats .
```

## 🎯 Quick Commands (Copy-Paste)

```bash
# Install tools
pip install --upgrade build twine

# Build
rm -rf build/ dist/ *.egg-info/
python -m build

# Upload to PyPI
python -m twine upload dist/*
# Username: __token__
# Password: <your-pypi-token>

# Test
pip install codestats-analyzer
codestats .
```

## 🔄 Update Version (Future)

### Update karne ke liye:

1. **setup.py me version change karo:**
```python
version="1.0.1",  # 1.0.0 → 1.0.1
```

2. **Rebuild & upload:**
```bash
rm -rf build/ dist/ *.egg-info/
python -m build
python -m twine upload dist/*
```

## 💡 Pro Tips

### Save credentials (optional)
Create `~/.pypirc`:
```ini
[pypi]
username = __token__
password = pypi-your-token-here
```

Then upload without typing:
```bash
python -m twine upload dist/*
```

### Version naming
- Bug fix: `1.0.0` → `1.0.1`
- New feature: `1.0.0` → `1.1.0`
- Breaking change: `1.0.0` → `2.0.0`

## ⚠️ Common Errors

### Error: "File already exists"
- Version already uploaded
- Change version in setup.py

### Error: "Invalid or non-existent authentication"
- Token galat hai
- Username `__token__` hai (with underscores)

### Error: "The name is too similar to an existing project"
- Name change karo setup.py me
- Try different name

## 🎊 Success!

Tumhara package ab live hai:
- **PyPI**: https://pypi.org/project/codestats-analyzer/
- **Install**: `pip install codestats-analyzer`
- **Share karo**: Twitter, LinkedIn, Reddit!

## 📢 Share karne ke liye

```markdown
🎉 Just published my first Python package!

📦 codestats-analyzer - Python code analysis tool

Install:
pip install codestats-analyzer

Features:
✅ Code metrics
✅ Complexity analysis  
✅ Quality score
✅ Smart suggestions

Try it: codestats .

#Python #OpenSource #PyPI
```
