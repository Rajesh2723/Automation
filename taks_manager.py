"""
Task Manager CLI Tool

Main entry point for the Task Manager automation tool.
Uses the lib module for core functionality.
"""

import argparse
from lib.task_manager import TaskManager
from lib.generate_log import generate_log


def main():
    """Main CLI entry point using argparse."""
    parser = argparse.ArgumentParser(
        description="Task Manager CLI Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python taks_manager.py add-task "Complete project"
  python taks_manager.py complete-task 1
  python taks_manager.py list
  python taks_manager.py stats
  python taks_manager.py generate-log
        """
    )
    
    subparsers = parser.add_subparsers(dest="command", help="Available commands")
    
    # Add task command
    add_parser = subparsers.add_parser("add-task", help="Add a new task")
    add_parser.add_argument("task", help="Task description")
    
    # Complete task command
    complete_parser = subparsers.add_parser("complete-task", help="Mark a task as complete")
    complete_parser.add_argument("task_id", help="Task ID to complete")
    
    # List tasks command
    subparsers.add_parser("list", help="List all tasks")
    
    # Statistics command
    subparsers.add_parser("stats", help="Show task statistics")
    
    # Generate log command
    subparsers.add_parser("generate-log", help="Generate a timestamped log file")
    
    args = parser.parse_args()
    
    manager = TaskManager()
    
    if args.command == "add-task":
        manager.add_task(args.task)
    elif args.command == "complete-task":
        manager.complete_task(args.task_id)
    elif args.command == "list":
        manager.list_tasks()
    elif args.command == "stats":
        manager.get_stats()
    elif args.command == "generate-log":
        log_data = [
            "Task Manager initialized",
            "User accessed task list",
            "New task created successfully",
            "Task marked as complete"
        ]
        generate_log(log_data)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
