# 📊 CodeStats

[![PyPI version](https://badge.fury.io/py/codestats-analyzer.svg)](https://pypi.org/project/codestats-analyzer/)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Python code analysis tool that gives you insights about your codebase - like GitHub insights but local!

## 🚀 Features

- 📁 **Code Metrics**: Lines, functions, classes count
- 🧠 **Complexity Analysis**: Detect long functions and nested loops
- 🔍 **Code Smell Detection**: Find unused imports, duplicate code patterns
- 💬 **Comment Analysis**: Check documentation coverage
- ⭐ **Quality Score**: Get a score from 0-10
- 💡 **Smart Suggestions**: Actionable improvement tips

## 📦 Installation

### From PyPI (Recommended):
```bash
pip install codestats-analyzer
```

### From GitHub:
```bash
pip install git+https://github.com/gitmanhimanshu/codestates.git
```

### For Development:
```bash
git clone https://github.com/gitmanhimanshu/codestates.git
cd codestates
pip install -e .
```

## 💻 Usage

### Command line:

```bash
# Analyze current directory
codestats .

# Analyze specific project
codestats myproject/

# Analyze specific file
codestats myfile.py
```

### As a Python module:

```python
from codestats import analyze

# Analyze a project
report = analyze("myproject")
print(report)

# Access specific metrics
print(f"Score: {report.score}/10")
print(f"Functions: {report.functions}")
print(f"Complexity: {report.complexity}")
```

**Full guide**: See [USER_GUIDE.md](USER_GUIDE.md) for detailed usage examples!

## 📊 Example Output

```
📊 CodeStats Report
==================================================
📁 Total files: 25
🧠 Total lines: 3200
🐍 Python files: 18
💬 Comments: 450
⚡ Functions: 60
📦 Classes: 12
📊 Complexity: Medium
⭐ Code Score: 7.5 / 10

🔍 Code Smells Detected:
   • main.py: 2 long function(s)
   • utils.py: Low comment ratio (3.2%)

💡 Suggestions:
   • Break down 2 long function(s) into smaller ones
   • Add more comments in 5 file(s)
   • Code quality is good! Keep it up 🎉
==================================================
```

## 🎯 What It Checks

- ⚠ Long functions (>50 lines)
- 🔄 Nested loops
- 📝 Comment coverage
- 🗑️ Unused imports
- 📏 File size
- 🏗️ Code organization

## 🔥 Why CodeStats?

Unlike other tools, CodeStats focuses on:
- **Simplicity**: Easy to use, clear output
- **Actionable**: Specific suggestions, not just numbers
- **Local**: No need to push to GitHub
- **Fast**: Analyzes projects in seconds

## 🔗 Links

- **PyPI**: https://pypi.org/project/codestats-analyzer/
- **GitHub**: https://github.com/gitmanhimanshu/codestates
- **Issues**: https://github.com/gitmanhimanshu/codestates/issues

## 📝 License

MIT
