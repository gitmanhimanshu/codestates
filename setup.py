"""Setup script for codestats"""

from setuptools import setup, find_packages
from pathlib import Path

# Read README for long description
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text(encoding='utf-8')

setup(
    name="codestats-analyzer",  # Change this to unique name on PyPI
    version="1.0.0",
    description="Python code analysis tool with insights - like GitHub insights but local",
    long_description=long_description,
    long_description_content_type="text/markdown",
    author="Himanshu Tadav",
    author_email="your.email@example.com",
    url="https://github.com/yourusername/codestats",  # Your GitHub repo
    packages=find_packages(),
    python_requires=">=3.7",
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Quality Assurance",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ],
    keywords="code analysis metrics quality complexity linting",
    entry_points={
        'console_scripts': [
            'codestats=codestats.cli:main',
        ],
    },
    project_urls={
        'Bug Reports': 'https://github.com/yourusername/codestats/issues',
        'Source': 'https://github.com/yourusername/codestats',
    },
)
