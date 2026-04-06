"""Main analyzer module"""

import os
import ast
from pathlib import Path
from dataclasses import dataclass
from typing import List, Dict
from .metrics import FileMetrics, calculate_complexity
from .detector import detect_code_smells
from .scorer import calculate_score, generate_suggestions


@dataclass
class CodeReport:
    """Code analysis report"""
    total_files: int
    total_lines: int
    python_files: int
    comments: int
    functions: int
    classes: int
    complexity: str
    score: float
    smells: List[str]
    suggestions: List[str]
    file_details: List[Dict]
    
    def __str__(self):
        return f"""
📊 CodeStats Report
{'='*50}
📁 Total files: {self.total_files}
🧠 Total lines: {self.total_lines}
🐍 Python files: {self.python_files}
💬 Comments: {self.comments}
⚡ Functions: {self.functions}
📦 Classes: {self.classes}
📊 Complexity: {self.complexity}
⭐ Code Score: {self.score:.1f} / 10

🔍 Code Smells Detected:
{self._format_list(self.smells) if self.smells else '   ✅ None detected!'}

💡 Suggestions:
{self._format_list(self.suggestions)}
{'='*50}
"""
    
    def _format_list(self, items):
        return '\n'.join(f'   • {item}' for item in items)


def analyze(path: str) -> CodeReport:
    """Analyze Python project and return report"""
    path = Path(path)
    
    if not path.exists():
        raise ValueError(f"Path does not exist: {path}")
    
    # Collect all Python files
    py_files = []
    if path.is_file() and path.suffix == '.py':
        py_files = [path]
    else:
        py_files = list(path.rglob('*.py'))
    
    # Analyze each file
    file_metrics = []
    total_lines = 0
    total_comments = 0
    total_functions = 0
    total_classes = 0
    all_smells = []
    
    for py_file in py_files:
        try:
            metrics = FileMetrics.from_file(py_file)
            file_metrics.append(metrics)
            total_lines += metrics.lines
            total_comments += metrics.comments
            total_functions += metrics.functions
            total_classes += metrics.classes
            
            # Detect code smells
            smells = detect_code_smells(py_file, metrics)
            all_smells.extend(smells)
        except Exception as e:
            print(f"⚠ Warning: Could not analyze {py_file}: {e}")
    
    # Calculate overall complexity
    complexity = calculate_complexity(file_metrics)
    
    # Calculate score
    score = calculate_score(file_metrics, all_smells)
    
    # Generate suggestions
    suggestions = generate_suggestions(file_metrics, all_smells, score)
    
    # Count all files (not just Python)
    if path.is_file():
        total_files = 1
    else:
        total_files = sum(1 for _ in path.rglob('*') if _.is_file())
    
    return CodeReport(
        total_files=total_files,
        total_lines=total_lines,
        python_files=len(py_files),
        comments=total_comments,
        functions=total_functions,
        classes=total_classes,
        complexity=complexity,
        score=score,
        smells=all_smells,
        suggestions=suggestions,
        file_details=[m.to_dict() for m in file_metrics]
    )
