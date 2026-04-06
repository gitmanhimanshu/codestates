"""Example usage of codestats"""

from codestats import analyze

# Analyze current directory
report = analyze(".")

# Print the report
print(report)

# Access specific metrics
print(f"\n📊 Quick Stats:")
print(f"Score: {report.score:.1f}/10")
print(f"Python files: {report.python_files}")
print(f"Total functions: {report.functions}")
