"""
Pytest configuration file

Ensures that the lib module is properly discoverable when running tests.
This file is automatically loaded by pytest and helps configure the test environment.
"""

import sys
from pathlib import Path

# Add the project root to the Python path so lib can be imported
project_root = Path(__file__).parent
sys.path.insert(0, str(project_root))
