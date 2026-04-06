"""Code smell detector"""

import ast
from pathlib import Path
from typing import List
from .metrics import FileMetrics


def detect_code_smells(filepath: Path, metrics: FileMetrics) -> List[str]:
    """Detect code smells in a file"""
    smells = []
    
    # Check for long functions
    if metrics.long_functions:
        smells.append(f"⚠ {filepath.name}: {len(metrics.long_functions)} long function(s)")
    
    # Check for nested loops
    if metrics.nested_loops > 0:
        smells.append(f"⚠ {filepath.name}: {metrics.nested_loops} nested loop(s) detected")
    
    # Check for unused imports (basic check)
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        tree = ast.parse(content)
        unused = _find_unused_imports(tree, content)
        if unused:
            smells.append(f"⚠ {filepath.name}: {len(unused)} potentially unused import(s)")
    except:
        pass
    
    # Check for low comment ratio
    if metrics.lines > 50:
        comment_ratio = metrics.comments / metrics.lines
        if comment_ratio < 0.05:  # Less than 5% comments
            smells.append(f"⚠ {filepath.name}: Low comment ratio ({comment_ratio*100:.1f}%)")
    
    # Check for duplicate code patterns (basic)
    if metrics.functions > 10 and metrics.avg_function_length < 5:
        smells.append(f"⚠ {filepath.name}: Many small functions - possible code duplication")
    
    return smells


def _find_unused_imports(tree: ast.AST, content: str) -> List[str]:
    """Find potentially unused imports (basic heuristic)"""
    imports = []
    used_names = set()
    
    # Collect imports
    for node in ast.walk(tree):
        if isinstance(node, ast.Import):
            for alias in node.names:
                name = alias.asname if alias.asname else alias.name.split('.')[0]
                imports.append(name)
        elif isinstance(node, ast.ImportFrom):
            for alias in node.names:
                name = alias.asname if alias.asname else alias.name
                imports.append(name)
    
    # Collect used names (simple check)
    for node in ast.walk(tree):
        if isinstance(node, ast.Name):
            used_names.add(node.id)
    
    # Find unused (basic check - may have false positives)
    unused = []
    for imp in imports:
        if imp not in used_names and imp not in content:
            unused.append(imp)
    
    return unused[:3]  # Limit to avoid false positives
