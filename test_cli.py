"""
Simple test to verify the CLI functionality for add and list operations.
"""

from src.cli.todo_cli import TodoCLI
from src.services.todo_service import TodoService


def test_cli_add_and_list():
    """
    Test that we can add a task and list it using the service directly.
    """
    # Create a service instance
    service = TodoService()
    
    # Add a task
    task = service.add_task("Test task", "A test description")
    print(f"Added task with ID: {task.id}, Title: {task.title}")
    
    # List tasks
    tasks = service.list_tasks()
    print(f"Total tasks: {len(tasks)}")
    
    for task in tasks:
        status = "X" if task.completed else "O"
        print(f"[{status}] {task.id}: {task.title} - {task.description}")
    
    # Add another task
    task2 = service.add_task("Second test task")
    print(f"Added task with ID: {task2.id}, Title: {task2.title}")
    
    # List tasks again
    tasks = service.list_tasks()
    print(f"Total tasks after adding second task: {len(tasks)}")
    
    for task in tasks:
        status = "X" if task.completed else "O"
        print(f"[{status}] {task.id}: {task.title}")


if __name__ == "__main__":
    test_cli_add_and_list()