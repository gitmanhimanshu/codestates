# 🧪 Testing CodeStats

## Local Testing (abhi test karo)

### 1. Install in development mode
```bash
pip install -e .
```

### 2. Test on itself (khud pe test karo)
```bash
# Command line se
codestats .

# Ya Python se
python example.py
```

### 3. Create test project
```bash
mkdir test_project
cd test_project
```

Create `test_project/sample.py`:
```python
# Sample code with issues
import os
import sys  # unused

def very_long_function():
    # This function is too long
    for i in range(10):
        for j in range(10):  # nested loop
            print(i, j)
    # ... more code to make it 50+ lines
    pass

class MyClass:
    def method(self):
        return "hello"
```

Then test:
```bash
cd ..
codestats test_project/
```

### 4. Unit tests (optional but recommended)

Create `tests/test_analyzer.py`:
```python
import pytest
from codestats import analyze

def test_analyze_single_file():
    report = analyze("example.py")
    assert report.python_files >= 1
    assert report.score >= 0
    assert report.score <= 10

def test_analyze_directory():
    report = analyze(".")
    assert report.total_files > 0
    assert report.functions >= 0
```

Run tests:
```bash
pip install pytest
pytest tests/
```

## 🎯 Expected Output

```
📊 CodeStats Report
==================================================
📁 Total files: 12
🧠 Total lines: 450
🐍 Python files: 5
💬 Comments: 45
⚡ Functions: 15
📦 Classes: 3
📊 Complexity: Low
⭐ Code Score: 8.2 / 10

🔍 Code Smells Detected:
   ✅ None detected!

💡 Suggestions:
   • Code quality is good! Keep it up 🎉
==================================================
```

## ✅ Testing Checklist

- [ ] Install kiya (`pip install -e .`)
- [ ] Command line se run kiya (`codestats .`)
- [ ] Python module se use kiya (`python example.py`)
- [ ] Score 0-10 ke beech hai
- [ ] Suggestions mil rahe hain
- [ ] Different projects pe test kiya
