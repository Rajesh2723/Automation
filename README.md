# Task Manager CLI Tool

A lightweight Python command-line interface (CLI) tool for managing tasks efficiently. This project demonstrates best practices in Python scripting, pip package management, and object-oriented design.

## Features

- ✅ **Add Tasks**: Quickly add new tasks from the command line
- ✅ **Mark Complete**: Track task completion with task IDs
- ✅ **List Tasks**: Display all tasks in a formatted table
- ✅ **View Statistics**: Get an overview of task completion status
- ✅ **File Persistence**: All tasks are saved to a JSON file automatically
- ✅ **Activity Logging**: All actions are logged to `task_manager.log`
- ✅ **Rich Terminal Output**: Enhanced CLI with colored output and formatted tables

## Project Structure

```
.
├── taks_manager.py      # Main CLI script
├── tasks.json           # Task data file (auto-generated)
├── task_manager.log     # Activity log file (auto-generated)
├── requirements.txt     # Project dependencies
└── README.md           # This file
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

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

This will install:
- **rich** (13.7.0): For enhanced terminal output with colors and tables
- **requests** (2.31.0): For potential API integration in future features

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

### Get Help

```bash
python taks_manager.py --help
```

## Technical Details

### Architecture

The tool follows **Object-Oriented Programming (OOP)** principles:

- **TaskManager Class**: Core logic for task operations
  - `add_task()`: Add new tasks
  - `complete_task()`: Mark tasks as complete
  - `list_tasks()`: Display all tasks
  - `get_stats()`: Show statistics
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

### CLI Implementation

The tool uses Python's built-in `argparse` module to handle commands:

```python
if __name__ == "__main__":
    main()
```

This pattern allows the script to be:
- Executed directly from the command line
- Imported as a module in other projects
- Tested independently

## Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| rich    | 13.7.0  | Enhanced terminal output with colors and tables |
| requests| 2.31.0  | HTTP client for potential API features |

## Best Practices Applied

✅ **Virtual Environments**: Use `requirements.txt` to ensure reproducibility across environments
✅ **Modular Code**: Separate concerns using classes and methods
✅ **Error Handling**: Graceful handling of missing files and invalid input
✅ **Documentation**: Comprehensive comments and docstrings
✅ **File I/O**: Persistent storage using JSON
✅ **Logging**: Track all user actions for auditing
✅ **CLI Design**: Intuitive command structure with help documentation
✅ **Main Guard**: Code wrapped in `if __name__ == "__main__":` for modularity

## Future Enhancements

- Add task priority levels
- Implement task categories/tags
- Add due dates and reminders
- Create a REST API version
- Add unit tests
- Implement task search functionality
- Add data export to CSV

## Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'rich'"

**Solution:** Ensure you've installed dependencies:
```bash
pip install -r requirements.txt
```

### Issue: "FileNotFoundError" on Windows

**Solution:** Use forward slashes or `pathlib.Path` for cross-platform compatibility (already done in this script).

### Issue: No output when running commands

**Solution:** Ensure you're using the correct command format:
```bash
python taks_manager.py <command> <arguments>
```

## License

This project is part of the Learn.co curriculum for demonstrating pip, PyPI, and Python scripting best practices.

## Author

Created as part of the Python Automation Lab - demonstrating CLI architecture, OOP principles, and dependency management.
