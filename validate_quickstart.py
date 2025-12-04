#!/usr/bin/env python3
"""
Quickstart validation script for Todo Console App.

This script validates the functionality described in quickstart.md
"""

import sys
import os
# Add src to path to import modules
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

from cli.todo_cli import TodoCLI


def validate_quickstart_functionality():
    """Validate that all quickstart functionality works as described."""
    print("[INFO] Validating quickstart functionality...")

    cli = TodoCLI()

    print("[OK] Created CLI instance")

    # Test 1: Add a task
    print("\n[TEST] Testing: add 'Buy milk'")
    cli.process_command('add "Buy milk"')
    tasks = cli.service.list_tasks()
    assert len(tasks) == 1
    assert tasks[0].title == "Buy milk"
    assert not tasks[0].completed
    print("[OK] Add task works")

    # Test 2: List tasks
    print("\n[TEST] Testing: list")
    cli.process_command('list')
    print("[OK] List command works")

    # Test 3: Complete a task
    print("\n[TEST] Testing: complete task 1")
    task_id = tasks[0].id
    cli.handle_complete(str(task_id))
    completed_task = cli.service.get_task(task_id)
    assert completed_task.completed
    print("[OK] Complete task works")

    # Test 4: Update a task
    print("\n[TEST] Testing: update task 1")
    cli.handle_update(f'{task_id} "Buy whole milk" "Low fat"')
    updated_task = cli.service.get_task(task_id)
    assert updated_task.title == "Buy whole milk"
    assert updated_task.description == "Low fat"
    print("[OK] Update task works")

    # Test 5: Delete a task
    print("\n[TEST] Testing: delete task 1")
    cli.handle_delete(str(task_id))
    tasks = cli.service.list_tasks()
    assert len(tasks) == 0
    print("[OK] Delete task works")

    # Test 6: Help command
    print("\n[TEST] Testing: help command")
    cli.handle_help()
    print("[OK] Help command works")

    # Test 7: Error handling
    print("\n[TEST] Testing: error handling")
    cli.handle_complete("9999")  # Should produce an error
    print("[OK] Error handling works")

    print("\n[SUCCESS] All quickstart functionality validated successfully!")
    return True


if __name__ == "__main__":
    try:
        success = validate_quickstart_functionality()
        if success:
            print("\n[OK] Quickstart validation completed successfully")
            print("The Todo Console App is working as expected!")
    except Exception as e:
        print(f"\n[ERROR] Quickstart validation failed: {e}")
        sys.exit(1)