"""Unit tests for codestats"""

import pytest
from pathlib import Path
from codestats import analyze


def test_analyze_current_directory():
    """Test analyzing current directory"""
    report = analyze(".")
    
    assert report.total_files > 0
    assert report.python_files > 0
    assert report.score >= 0
    assert report.score <= 10
    assert isinstance(report.suggestions, list)
    assert len(report.suggestions) > 0


def test_analyze_single_file():
    """Test analyzing a single Python file"""
    report = analyze("example.py")
    
    assert report.python_files == 1
    assert report.functions >= 0
    assert report.classes >= 0


def test_score_range():
    """Test that score is always between 0 and 10"""
    report = analyze(".")
    
    assert 0 <= report.score <= 10


def test_report_string_format():
    """Test that report can be converted to string"""
    report = analyze(".")
    report_str = str(report)
    
    assert "CodeStats Report" in report_str
    assert "Code Score" in report_str
    assert "Suggestions" in report_str


def test_invalid_path():
    """Test handling of invalid path"""
    with pytest.raises(ValueError):
        analyze("nonexistent_path_12345")


def test_metrics_types():
    """Test that all metrics have correct types"""
    report = analyze(".")
    
    assert isinstance(report.total_files, int)
    assert isinstance(report.total_lines, int)
    assert isinstance(report.python_files, int)
    assert isinstance(report.comments, int)
    assert isinstance(report.functions, int)
    assert isinstance(report.classes, int)
    assert isinstance(report.complexity, str)
    assert isinstance(report.score, float)
    assert isinstance(report.smells, list)
    assert isinstance(report.suggestions, list)
