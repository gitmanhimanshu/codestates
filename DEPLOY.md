# 🚀 PyPI Deployment Guide

## Prerequisites

```bash
# Install required tools
pip install build twine
```

## Step-by-Step Deployment

### 1. PyPI Account Setup

1. **Create account**: https://pypi.org/account/register/
2. **Verify email**
3. **Enable 2FA** (recommended)
4. **Create API token**:
   - Go to: https://pypi.org/manage/account/token/
   - Create token with scope: "Entire account"
   - Save token securely (dikhega sirf ek baar)

### 2. Update setup.py (important fields)

```python
setup(
    name="codestats-analyzer",  # Unique name (check on PyPI)
    version="1.0.0",
    description="Python code analysis tool with insights",
    long_description=open('README.md').read(),
    long_description_content_type="text/markdown",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/codestats",
    packages=find_packages(),
    python_requires=">=3.7",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    entry_points={
        'console_scripts': [
            'codestats=codestats.cli:main',
        ],
    },
)
```

### 3. Create LICENSE file

```bash
# MIT License (recommended)
# Copy from: https://opensource.org/licenses/MIT
```

### 4. Build the package

```bash
# Clean previous builds
rm -rf build/ dist/ *.egg-info

# Build
python -m build
```

Ye create karega:
- `dist/codestats-analyzer-1.0.0.tar.gz`
- `dist/codestats_analyzer-1.0.0-py3-none-any.whl`

### 5. Test on TestPyPI (optional but recommended)

```bash
# Upload to TestPyPI
python -m twine upload --repository testpypi dist/*

# Username: __token__
# Password: <your-testpypi-token>

# Test install
pip install --index-url https://test.pypi.org/simple/ codestats-analyzer
```

### 6. Upload to PyPI (final deployment)

```bash
# Upload
python -m twine upload dist/*

# Username: __token__
# Password: <your-pypi-token>
```

### 7. Verify deployment

```bash
# Install from PyPI
pip install codestats-analyzer

# Test
codestats .
```

## 🔄 Update karne ke liye (new version)

1. **Update version** in `setup.py`:
   ```python
   version="1.0.1",  # Increment version
   ```

2. **Update CHANGELOG** (optional):
   ```markdown
   ## [1.0.1] - 2026-04-06
   - Fixed bug in complexity calculation
   - Added new feature
   ```

3. **Rebuild and upload**:
   ```bash
   rm -rf dist/
   python -m build
   python -m twine upload dist/*
   ```

## 📝 .pypirc Configuration (optional - easier uploads)

Create `~/.pypirc`:
```ini
[pypi]
username = __token__
password = pypi-your-token-here

[testpypi]
username = __token__
password = pypi-your-testpypi-token-here
```

Then upload without entering credentials:
```bash
python -m twine upload dist/*
```

## ⚠️ Important Notes

1. **Name must be unique** on PyPI
   - Check: https://pypi.org/project/codestats-analyzer/
   - If taken, use different name like `codestats-py`, `py-codestats`

2. **Version cannot be reused**
   - Once uploaded, version 1.0.0 cannot be uploaded again
   - Always increment version for updates

3. **README.md** becomes your PyPI page
   - Make it attractive with emojis and examples
   - Include installation and usage

4. **Test locally first**
   - Always test before uploading
   - Use TestPyPI for practice

## 🎯 Quick Commands Summary

```bash
# One-time setup
pip install build twine

# Every deployment
rm -rf dist/
python -m build
python -m twine upload dist/*

# Test install
pip install codestats-analyzer
codestats .
```

## 🔗 Useful Links

- PyPI: https://pypi.org/
- TestPyPI: https://test.pypi.org/
- Packaging Guide: https://packaging.python.org/
- Twine Docs: https://twine.readthedocs.io/
