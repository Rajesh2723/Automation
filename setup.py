"""
Setup configuration for Task Manager CLI Tool

This file allows the package to be installed in development mode,
ensuring proper module discovery in any environment.
"""

from setuptools import setup, find_packages

setup(
    name="task-manager-cli",
    version="1.0.0",
    description="A lightweight Python CLI automation tool for managing tasks",
    author="Learn.co",
    author_email="",
    packages=find_packages(),
    python_requires=">=3.8",
    install_requires=[
        "rich>=13.7.0",
        "requests>=2.31.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.4.3",
            "pytest-cov>=4.1.0",
        ],
    },
    entry_points={
        "console_scripts": [
            "task-manager=taks_manager:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Programming Language :: Python :: 3.14",
    ],
)
