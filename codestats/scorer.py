"""Code quality scoring and suggestions"""

from typing import List
from pathlib import Path
from .metrics import FileMetrics


def calculate_score(metrics: List[FileMetrics], smells: List[str]) -> float:
    """Calculate overall code quality score (0-10)"""
    if not metrics:
        return 0.0
    
    score = 10.0
    
    # Deduct for code smells
    score -= min(len(smells) * 0.5, 3.0)
    
    # Deduct for long functions
    total_long = sum(len(m.long_functions) for m in metrics)
    score -= min(total_long * 0.3, 2.0)
    
    # Deduct for low comments
    total_lines = sum(m.lines for m in metrics)
    total_comments = sum(m.comments for m in metrics)
    if total_lines > 0:
        comment_ratio = total_comments / total_lines
        if comment_ratio < 0.1:
            score -= 1.0
        elif comment_ratio < 0.05:
            score -= 2.0
    
    # Deduct for nested loops
    total_nested = sum(m.nested_loops for m in metrics)
    score -= min(total_nested * 0.4, 1.5)
    
    # Bonus for good structure
    total_funcs = sum(m.functions for m in metrics)
    total_classes = sum(m.classes for m in metrics)
    if total_funcs > 0 and total_classes > 0:
        score += 0.5
    
    return max(0.0, min(10.0, score))


def generate_suggestions(metrics: List[FileMetrics], smells: List[str], score: float) -> List[str]:
    """Generate improvement suggestions"""
    suggestions = []
    
    # Check for long functions
    total_long = sum(len(m.long_functions) for m in metrics)
    if total_long > 0:
        suggestions.append(f"Break down {total_long} long function(s) into smaller ones")
    
    # Check for comments
    total_lines = sum(m.lines for m in metrics)
    total_comments = sum(m.comments for m in metrics)
    if total_lines > 0:
        comment_ratio = total_comments / total_lines
        if comment_ratio < 0.1:
            low_comment_files = sum(1 for m in metrics if m.lines > 20 and m.comments / m.lines < 0.1)
            suggestions.append(f"Add more comments in {low_comment_files} file(s)")
    
    # Check for nested loops
    total_nested = sum(m.nested_loops for m in metrics)
    if total_nested > 2:
        suggestions.append("Refactor nested loops to improve readability")
    
    # Check for code organization
    total_funcs = sum(m.functions for m in metrics)
    total_classes = sum(m.classes for m in metrics)
    if total_funcs > 20 and total_classes == 0:
        suggestions.append("Consider organizing functions into classes")
    
    # Score-based suggestions
    if score < 5:
        suggestions.append("Code quality needs significant improvement")
    elif score < 7:
        suggestions.append("Code quality is acceptable but can be improved")
    else:
        suggestions.append("Code quality is good! Keep it up 🎉")
    
    # Check for very long files
    for m in metrics:
        if m.lines > 500:
            suggestions.append(f"Consider splitting large file: {Path(m.filepath).name}")
            break
    
    return suggestions[:5]  # Limit to top 5 suggestions
