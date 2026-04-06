"""Command-line interface for codestats"""

import sys
from pathlib import Path
from .analyzer import analyze


def main():
    """Main CLI entry point"""
    if len(sys.argv) < 2:
        print("Usage: codestats <path>")
        print("Example: codestats .")
        print("         codestats myproject/")
        sys.exit(1)
    
    path = sys.argv[1]
    
    try:
        print(f"🔍 Analyzing: {path}\n")
        report = analyze(path)
        print(report)
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
