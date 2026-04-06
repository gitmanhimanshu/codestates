"""Code metrics calculation"""

import ast
from pathlib import Path
from dataclasses import dataclass
from typing import List


@dataclass
class FileMetrics:
    """Metrics for a single file"""
    filepath: str
    lines: int
    comments: int
    functions: int
    classes: int
    long_functions: List[str]  # Functions with >50 lines
    nested_loops: int
    imports: List[str]
    avg_function_length: float
    
    @classmethod
    def from_file(cls, filepath: Path):
        """Extract metrics from a Python file"""
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()
        
        lines = content.count('\n') + 1
        comments = sum(1 for line in content.split('\n') if line.strip().startswith('#'))
        
        try:
            tree = ast.parse(content)
        except SyntaxError:
            # If file has syntax errors, return basic metrics
            return cls(
                filepath=str(filepath),
                lines=lines,
                comments=comments,
                functions=0,
                classes=0,
                long_functions=[],
                nested_loops=0,
                imports=[],
                avg_function_length=0
            )
        
        visitor = MetricsVisitor()
        visitor.visit(tree)
        
        avg_func_len = (
            sum(visitor.function_lengths) / len(visitor.function_lengths)
            if visitor.function_lengths else 0
        )
        
        return cls(
            filepath=str(filepath),
            lines=lines,
            comments=comments,
            functions=len(visitor.function_names),
            classes=len(visitor.class_names),
            long_functions=visitor.long_functions,
            nested_loops=visitor.nested_loops,
            imports=visitor.imports,
            avg_function_length=avg_func_len
        )
    
    def to_dict(self):
        return {
            'filepath': self.filepath,
            'lines': self.lines,
            'functions': self.functions,
            'classes': self.classes
        }


class MetricsVisitor(ast.NodeVisitor):
    """AST visitor to collect code metrics"""
    
    def __init__(self):
        self.function_names = []
        self.function_lengths = []
        self.long_functions = []
        self.class_names = []
        self.nested_loops = 0
        self.imports = []
        self.current_function = None
    
    def visit_FunctionDef(self, node):
        self.function_names.append(node.name)
        
        # Calculate function length
        if node.body:
            func_lines = node.end_lineno - node.lineno + 1
            self.function_lengths.append(func_lines)
            
            if func_lines > 50:
                self.long_functions.append(f"{node.name} ({func_lines} lines)")
        
        # Check for nested loops
        self.current_function = node.name
        self._check_nested_loops(node)
        
        self.generic_visit(node)
    
    def visit_AsyncFunctionDef(self, node):
        self.visit_FunctionDef(node)
    
    def visit_ClassDef(self, node):
        self.class_names.append(node.name)
        self.generic_visit(node)
    
    def visit_Import(self, node):
        for alias in node.names:
            self.imports.append(alias.name)
        self.generic_visit(node)
    
    def visit_ImportFrom(self, node):
        if node.module:
            self.imports.append(node.module)
        self.generic_visit(node)
    
    def _check_nested_loops(self, node):
        """Check for nested loops in function"""
        for child in ast.walk(node):
            if isinstance(child, (ast.For, ast.While)):
                for nested in ast.walk(child):
                    if nested != child and isinstance(nested, (ast.For, ast.While)):
                        self.nested_loops += 1


def calculate_complexity(metrics: List[FileMetrics]) -> str:
    """Calculate overall code complexity"""
    if not metrics:
        return "Unknown"
    
    total_long_funcs = sum(len(m.long_functions) for m in metrics)
    total_nested = sum(m.nested_loops for m in metrics)
    avg_func_length = sum(m.avg_function_length for m in metrics) / len(metrics)
    
    complexity_score = 0
    
    if total_long_funcs > 5:
        complexity_score += 2
    elif total_long_funcs > 2:
        complexity_score += 1
    
    if total_nested > 3:
        complexity_score += 2
    elif total_nested > 1:
        complexity_score += 1
    
    if avg_func_length > 30:
        complexity_score += 1
    
    if complexity_score >= 4:
        return "High"
    elif complexity_score >= 2:
        return "Medium"
    else:
        return "Low"
