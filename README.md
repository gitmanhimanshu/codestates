# 📊 CodeStats

[![PyPI version](https://badge.fury.io/py/codestats-analyzer.svg)](https://pypi.org/project/codestats-analyzer/)
[![Python 3.7+](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**CodeStats** is a powerful Python code analysis tool that provides instant insights into your codebase quality - like GitHub Insights but runs locally on your machine!

## 🎯 What is CodeStats?

CodeStats analyzes your Python projects and provides:
- **Code Quality Metrics**: Lines of code, functions, classes, comments
- **Complexity Analysis**: Identifies long functions, nested loops, and code smells
- **Quality Score**: 0-10 rating based on best practices
- **Actionable Suggestions**: Specific recommendations to improve your code

Perfect for developers who want to maintain high code quality without complex setup!

## 🚀 Features

- 📁 **Code Metrics**: Lines, functions, classes count
- 🧠 **Complexity Analysis**: Detect long functions and nested loops
- 🔍 **Code Smell Detection**: Find unused imports, duplicate code patterns
- 💬 **Comment Analysis**: Check documentation coverage
- ⭐ **Quality Score**: Get a score from 0-10
- 💡 **Smart Suggestions**: Actionable improvement tips

## 🌐 Supported Languages

### ✅ Fully Supported:
- **Python** (.py) - Complete analysis with AST parsing

### 🚧 Coming Soon (v2.0):
- **JavaScript/TypeScript** (.js, .ts, .jsx, .tsx)
- **Java** (.java)
- **C/C++** (.c, .cpp, .h, .hpp)
- **Go** (.go)
- **Ruby** (.rb)
- **PHP** (.php)

**Note**: Currently optimized for Python projects. Multi-language support is planned for future releases!

## 📦 Installation

### Quick Install (Recommended):
```bash
pip install codestats-analyzer
```

### From GitHub (Latest):
```bash
pip install git+https://github.com/gitmanhimanshu/codestates.git
```

### For Development:
```bash
git clone https://github.com/gitmanhimanshu/codestates.git
cd codestates
pip install -e .
```

**Requirements**: Python 3.7 or higher

## 💻 Usage

### Command Line (Easiest):

```bash
# Analyze current directory
codestats .

# Analyze specific project
codestats /path/to/myproject

# Analyze specific file
codestats myfile.py
```

### As a Python Module:

```python
from codestats import analyze

# Analyze a project
report = analyze("myproject")

# Print full report
print(report)

# Access specific metrics
print(f"Quality Score: {report.score}/10")
print(f"Total Functions: {report.functions}")
print(f"Code Complexity: {report.complexity}")
print(f"Python Files: {report.python_files}")

# Get suggestions
for suggestion in report.suggestions:
    print(f"💡 {suggestion}")

# Check code smells
for smell in report.smells:
    print(f"⚠️  {smell}")
```

**Full documentation**: See [USER_GUIDE.md](USER_GUIDE.md) for detailed examples and use cases!

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

### Understanding the Metrics:

- **Code Score (0-10)**: Overall quality rating
  - 8-10: Excellent ✨
  - 6-8: Good 👍
  - 4-6: Needs improvement ⚠️
  - 0-4: Significant work needed 🔧

- **Complexity**: Code maintainability level
  - Low: Easy to maintain
  - Medium: Moderate complexity
  - High: Needs refactoring

- **Code Smells**: Potential issues detected
  - Long functions (>50 lines)
  - Nested loops
  - Low comment coverage
  - Unused imports

## 🎯 Use Cases

### 1. Pre-Commit Quality Check
```bash
# Check code quality before committing
codestats . && git commit -m "Your message"
```

### 2. CI/CD Integration
```yaml
# .github/workflows/code-quality.yml
- name: Check Code Quality
  run: |
    pip install codestats-analyzer
    codestats .
```

### 3. Project Health Monitoring
```python
from codestats import analyze

report = analyze(".")
if report.score < 7:
    print("⚠️ Code quality below threshold!")
    exit(1)
```

### 4. Code Review Assistant
```bash
# Analyze specific branch or PR
codestats feature-branch/
```

### 5. Learning & Improvement
- Track code quality improvements over time
- Identify areas needing refactoring
- Learn best practices through suggestions

## 🔥 Why CodeStats?

Unlike other tools, CodeStats focuses on:
- **Simplicity**: Easy to use, clear output
- **Actionable**: Specific suggestions, not just numbers
- **Local**: No need to push to GitHub
- **Fast**: Analyzes projects in seconds

## 🔗 Links

- **PyPI Package**: https://pypi.org/project/codestats-analyzer/
- **GitHub Repository**: https://github.com/gitmanhimanshu/codestates
- **Issue Tracker**: https://github.com/gitmanhimanshu/codestates/issues
- **Documentation**: [USER_GUIDE.md](USER_GUIDE.md)

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

MIT License - see [LICENSE](LICENSE) file for details

## 👨‍💻 Author

**Himanshu Tadav**
- GitHub: [@gitmanhimanshu](https://github.com/gitmanhimanshu)
- Email: himanshuyada70@gmail.com

## 🙏 Acknowledgments

- Built with Python's AST module for accurate code parsing
- Inspired by tools like pylint, flake8, and radon
- Thanks to the Python community for feedback and support

---

**Made with ❤️ for Python developers who care about code quality**
