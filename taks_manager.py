"""
Task Manager CLI Tool

A lightweight command-line interface for managing tasks with file persistence.
Uses argparse for CLI handling and rich for enhanced terminal output.
"""

import argparse
import json
import os
from datetime import datetime
from pathlib import Path
from rich.console import Console
from rich.table import Table


class TaskManager:
    """Manages tasks with file persistence using JSON."""
    
    def __init__(self, tasks_file="tasks.json"):
        """Initialize TaskManager with a specified tasks file."""
        self.tasks_file = tasks_file
        self.tasks = self._load_tasks()
        self.console = Console()
    
    def _load_tasks(self):
        """Load tasks from JSON file. Create file if it doesn't exist."""
        if not os.path.exists(self.tasks_file):
            return []
        
        try:
            with open(self.tasks_file, "r") as f:
                return json.load(f)
        except (json.JSONDecodeError, IOError):
            self.console.print("[yellow]Warning: Could not load tasks file. Starting fresh.[/yellow]")
            return []
    
    def _save_tasks(self):
        """Save tasks to JSON file."""
        try:
            with open(self.tasks_file, "w") as f:
                json.dump(self.tasks, f, indent=2)
            self._log_action(f"Tasks saved to {self.tasks_file}")
        except IOError as e:
            self.console.print(f"[red]Error saving tasks: {e}[/red]")
    
    def _log_action(self, action):
        """Log action to a log file."""
        log_file = "task_manager.log"
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        with open(log_file, "a") as f:
            f.write(f"[{timestamp}] {action}\n")
    
    def add_task(self, task):
        """Add a new task to the task list."""
        new_task = {
            "id": len(self.tasks) + 1,
            "name": task,
            "completed": False,
            "created_at": datetime.now().isoformat()
        }
        self.tasks.append(new_task)
        self._save_tasks()
        self.console.print(f"[green]✓ Task added:[/green] {task}")
        self._log_action(f"Added task: {task}")
    
    def complete_task(self, task_id):
        """Mark a task as complete by ID."""
        try:
            task_id = int(task_id)
            for task in self.tasks:
                if task["id"] == task_id:
                    task["completed"] = True
                    task["completed_at"] = datetime.now().isoformat()
                    self._save_tasks()
                    self.console.print(f"[green]✓ Task completed:[/green] {task['name']}")
                    self._log_action(f"Completed task: {task['name']}")
                    return
            
            self.console.print(f"[red]✗ Task not found:[/red] ID {task_id}")
        except ValueError:
            self.console.print("[red]✗ Invalid task ID. Please use a number.[/red]")
    
    def list_tasks(self):
        """Display all tasks in a formatted table."""
        if not self.tasks:
            self.console.print("[yellow]No tasks found.[/yellow]")
            return
        
        table = Table(title="Task Manager")
        table.add_column("ID", style="cyan")
        table.add_column("Task", style="magenta")
        table.add_column("Status", style="green")
        
        for task in self.tasks:
            status = "✓ Completed" if task["completed"] else "○ Pending"
            table.add_row(str(task["id"]), task["name"], status)
        
        self.console.print(table)
        self._log_action("Listed all tasks")
    
    def get_stats(self):
        """Display task statistics."""
        total = len(self.tasks)
        completed = sum(1 for t in self.tasks if t["completed"])
        pending = total - completed
        
        self.console.print(f"\n[bold]Task Statistics[/bold]")
        self.console.print(f"  Total tasks: {total}")
        self.console.print(f"  Completed: {completed}")
        self.console.print(f"  Pending: {pending}")
        self._log_action("Displayed task statistics")


def main():
    """Main CLI entry point using argparse."""
    parser = argparse.ArgumentParser(
        description="Simple Task Manager CLI Tool",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python task_manager.py add-task "Complete project"
  python task_manager.py complete-task 1
  python task_manager.py list
  python task_manager.py stats
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
    else:
        parser.print_help()


if __name__ == "__main__":
    main()