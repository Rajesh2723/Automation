# Task Manager CLI Tool

A lightweight, modular Python command-line interface (CLI) automation tool for managing tasks efficiently. This project demonstrates best practices in Python scripting, pip package management, OOP design, and testing.

## Features

- ✅ **Add Tasks**: Quickly add new tasks from the command line
- ✅ **Mark Complete**: Track task completion with task IDs
- ✅ **List Tasks**: Display all tasks in a formatted table
- ✅ **View Statistics**: Get an overview of task completion status
- ✅ **File Persistence**: All tasks are saved to a JSON file automatically
- ✅ **Activity Logging**: All actions are logged to `task_manager.log`
- ✅ **Log Generation**: Generate timestamped log files via API
- ✅ **Rich Terminal Output**: Enhanced CLI with colored output and formatted tables
- ✅ **Comprehensive Tests**: Full test suite using pytest

## Project Structure

```
Task Manager/
├── lib/                          # Core library modules
│   ├── __init__.py              # Package initialization
│   ├── task_manager.py          # TaskManager class with core logic
│   └── generate_log.py          # Log file generation function
├── testing/                      # Test suite
│   ├── __init__.py              # Test package initialization
│   └── test_generate_log.py     # Tests for log generation module
├── taks_manager.py              # Main CLI entry point
├── pytest.ini                   # Pytest configuration
├── requirements.txt             # Project dependencies
├── .gitignore                   # Git ignore file
└── README.md                    # This file
```

## Prerequisites

- Python 3.8 or higher
- pip package manager

## Setup Instructions

### 1. Verify Python and pip

```bash
python --version
pip --version
```

**Expected Output:**
```
Python 3.14.5
pip 26.1.1
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- **rich** (13.7.0): For enhanced terminal output with colors and tables
- **requests** (2.31.0): For HTTP functionality and potential API integration
- **pytest** (7.4.3): For running the test suite
- **pytest-cov** (4.1.0): For test coverage reporting

### 3. Verify Installation

```bash
python taks_manager.py --help
```

## Usage

### Add a Task

```bash
python taks_manager.py add-task "Buy groceries"
python taks_manager.py add-task "Complete project report"
```

**Output:**
```
✓ Task added: Buy groceries
✓ Task added: Complete project report
```

### List All Tasks

```bash
python taks_manager.py list
```

**Output:**
```
┏━━━━┳━━━━━━━━━━━━━━━━━━━━━┳━━━━━━━━━━━━━┓
┃ ID ┃ Task                ┃ Status      ┃
┡━━━━╇━━━━━━━━━━━━━━━━━━━━━╇━━━━━━━━━━━━━┩
│ 1  │ Buy groceries       │ ○ Pending   │
│ 2  │ Complete project... │ ○ Pending   │
└────┴─────────────────────┴─────────────┘
```

### Mark a Task as Complete

```bash
python taks_manager.py complete-task 1
```

**Output:**
```
✓ Task completed: Buy groceries
```

### View Task Statistics

```bash
python taks_manager.py stats
```

**Output:**
```
Task Statistics
  Total tasks: 2
  Completed: 1
  Pending: 1
```

### Generate a Timestamped Log File

```bash
python taks_manager.py generate-log
```

**Output:**
```
Log written to log_20250610.txt
```

This creates a file like `log_20250610.txt` containing:
```
Task Manager initialized
User accessed task list
New task created successfully
Task marked as complete
```

### Get Help

```bash
python taks_manager.py --help
```

## Testing

The project includes comprehensive unit tests for the log generation module.

### Run All Tests

```bash
pytest
```

**Output:**
```
testing/test_generate_log.py::test_log_file_created PASSED      [ 16%]
testing/test_generate_log.py::test_log_file_name_format PASSED  [ 33%]
testing/test_generate_log.py::test_log_file_content_matches_input PASSED [ 50%]
testing/test_generate_log.py::test_generate_log_raises_error_on_invalid_input PASSED [ 66%]
testing/test_generate_log.py::test_empty_log_list_creates_empty_file PASSED [ 83%]
testing/test_generate_log.py::test_generate_log_with_special_characters PASSED [100%]
```

### Run Specific Test

```bash
pytest testing/test_generate_log.py::test_log_file_created -v
```

### Generate Coverage Report

```bash
pytest --cov=lib testing/
```

## Technical Details

### Architecture

The project follows **Object-Oriented Programming (OOP)** and **modular design** principles:

#### `lib/generate_log.py`
- `generate_log(data)`: Main function for log file generation
  - Validates input (must be a list)
  - Creates timestamped filename
  - Writes entries to file using File I/O
  - Returns the created filename
  - Raises `ValueError` for invalid input

#### `lib/task_manager.py`
- `TaskManager` class: Core task management
  - `add_task()`: Add new tasks
  - `complete_task()`: Mark tasks as complete
  - `list_tasks()`: Display all tasks in formatted table
  - `get_stats()`: Show task statistics
  - `_load_tasks()`: Persist data (JSON)
  - `_save_tasks()`: Persist data (JSON)
  - `_log_action()`: Log activities

### File Persistence

Tasks are automatically saved to `tasks.json` after each operation:

```json
[
  {
    "id": 1,
    "name": "Buy groceries",
    "completed": true,
    "created_at": "2024-06-10T14:30:00",
    "completed_at": "2024-06-10T14:35:00"
  },
  {
    "id": 2,
    "name": "Complete project",
    "completed": false,
    "created_at": "2024-06-10T14:31:00"
  }
]
```

### Activity Logging

All operations are logged to `task_manager.log`:

```
[2024-06-10 14:30:00] Added task: Buy groceries
[2024-06-10 14:35:00] Completed task: Buy groceries
[2024-06-10 14:35:15] Listed all tasks
```

### Log File Generation

The `generate_log()` function creates timestamped log files:

```python
from lib.generate_log import generate_log

log_data = ["User logged in", "Report exported"]
filename = generate_log(log_data)  # Returns: "log_20250610.txt"
```

### CLI Implementation

The main script uses Python's built-in `argparse` module:

```python
if __name__ == "__main__":
    main()
```

This pattern allows:
- Direct execution from command line
- Import as a module in other projects
- Independent testing of components

## Dependencies

| Package    | Version | Purpose                                  |
|-----------|---------|------------------------------------------|
| rich      | 13.7.0  | Enhanced terminal output                 |
| requests  | 2.31.0  | HTTP client for API features             |
| pytest    | 7.4.3   | Testing framework                        |
| pytest-cov| 4.1.0   | Test coverage reporting                  |

## Best Practices Applied

✅ **Modular Design**: Separate concerns using `lib/` package structure  
✅ **Virtual Environments**: `requirements.txt` for reproducibility  
✅ **Error Handling**: Graceful handling of missing files and invalid input  
✅ **Documentation**: Comprehensive docstrings and comments  
✅ **File I/O**: Persistent storage using JSON  
✅ **Logging**: Track all user actions for auditing  
✅ **CLI Design**: Intuitive command structure with argparse  
✅ **Main Guard**: Code wrapped in `if __name__ == "__main__":`  
✅ **Testing**: Comprehensive pytest suite with fixtures  
✅ **Type Hints**: Function documentation for clarity  

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'lib'"

**Solution:** Ensure you're running the script from the project root directory:
```bash
cd d:\Python Projects\Task Manager
python taks_manager.py --help
```

### Issue: "ModuleNotFoundError: No module named 'rich'"

**Solution:** Install dependencies:
```bash
pip install -r requirements.txt
```

### Issue: "ERROR collecting test_file.py - ModuleNotFoundError: No module named 'lib'"

**Solution:** Make sure you're running pytest from the project root:
```bash
cd d:\Python Projects\Task Manager
pytest
```

## Git Workflow (if applicable)

```bash
# Create a feature branch
git checkout -b feature-automation-tool

# Make changes and commit
git add .
git commit -m "Add task manager with logging and tests"

# Push to remote
git push origin feature-automation-tool

# Merge after review
git checkout main
git merge feature-automation-tool
git push origin main
```

## Future Enhancements

- Add task priority levels
- Implement task categories/tags
- Add due dates and reminders
- Create a REST API version
- Add more comprehensive test coverage
- Implement task search functionality
- Add data export to CSV
- Create a web-based dashboard

## License

This project is part of the Learn.co curriculum for demonstrating pip, PyPI, and Python scripting best practices.

## Author

Created as part of the Python Automation Lab - demonstrating CLI architecture, OOP principles, dependency management, and testing best practices.

