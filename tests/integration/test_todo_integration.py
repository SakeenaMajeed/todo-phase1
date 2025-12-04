"""
Integration tests for the Todo Console App.

These tests validate complete user workflows by testing the interaction
between CLI, service, and model layers together.
"""

import io
import sys
import pytest
from unittest.mock import patch
from src.cli.todo_cli import TodoCLI


class TestTodoAppIntegration:
    """
    Test suite for complete user workflows in the Todo Console App.
    """

    def test_complete_user_workflow_add_list_complete_delete(self):
        """
        Test a complete user workflow: add task, list tasks, complete task, delete task.
        """
        cli = TodoCLI()

        # Step 1: Add a task
        with patch('builtins.input', side_effect=['add "Test task" "Test description"', 'exit']):
            with patch('sys.stdout', new_callable=io.StringIO) as fake_out:
                cli.process_command('add "Test task" "Test description"')
                
                # Verify task was added
                tasks = cli.service.list_tasks()
                assert len(tasks) == 1
                assert tasks[0].title == "Test task"
                assert tasks[0].description == "Test description"
                assert not tasks[0].completed  # Should be incomplete initially

        # Step 2: List tasks
        with patch('sys.stdout', new_callable=io.StringIO) as fake_out:
            cli.handle_list()
            output = fake_out.getvalue()
            
            # Verify list output contains our task
            assert "Test task" in output
            assert "[O]" in output  # Should show as incomplete
            assert "Test description" in output

        # Step 3: Complete the task
        task_id = tasks[0].id
        cli.handle_complete(str(task_id))
        
        # Verify task is now complete
        updated_task = cli.service.get_task(task_id)
        assert updated_task.completed

        # Step 4: Verify completion in list
        with patch('sys.stdout', new_callable=io.StringIO) as fake_out:
            cli.handle_list()
            output = fake_out.getvalue()
            
            # Verify task now shows as complete
            assert "[X]" in output  # Should show as complete

        # Step 5: Delete the task
        cli.handle_delete(str(task_id))
        
        # Verify task is deleted
        tasks = cli.service.list_tasks()
        assert len(tasks) == 0

    def test_add_multiple_tasks_and_manage(self):
        """
        Test adding multiple tasks and performing various operations on them.
        """
        cli = TodoCLI()

        # Add multiple tasks
        cli.process_command('add "First task" "Description for first task"')
        cli.process_command('add "Second task" "Description for second task"')
        cli.process_command('add "Third task"')

        # Verify all tasks exist
        tasks = cli.service.list_tasks()
        assert len(tasks) == 3

        # Complete the second task
        cli.handle_complete("2")
        completed_task = cli.service.get_task(2)
        assert completed_task.completed

        # Update the first task
        cli.handle_update('1 "Updated first task" "Updated description"')
        updated_task = cli.service.get_task(1)
        assert updated_task.title == "Updated first task"
        assert updated_task.description == "Updated description"

        # List all tasks to verify the state
        with patch('sys.stdout', new_callable=io.StringIO) as fake_out:
            cli.handle_list()
            output = fake_out.getvalue()
            
            # Verify updated content appears
            assert "Updated first task" in output
            assert "Updated description" in output
            assert "[X]" in output  # Second task should be complete
            assert "[O]" in output  # First and third tasks should be incomplete

    def test_error_handling_integration(self):
        """
        Test error handling across the application layers.
        """
        cli = TodoCLI()

        # Try to complete a non-existent task
        with patch('sys.stdout', new_callable=io.StringIO) as fake_out:
            cli.handle_complete("999")
            output = fake_out.getvalue()

            # Verify appropriate error message (from exception formatting)
            assert "TASK_NOT_FOUND" in output
            assert "999" in output

        # Try to update a non-existent task
        with patch('sys.stdout', new_callable=io.StringIO) as fake_out:
            cli.handle_update('999 "New title"')
            output = fake_out.getvalue()

            # Verify appropriate error message
            assert "TASK_NOT_FOUND" in output
            assert "999" in output

        # Try to delete a non-existent task
        with patch('sys.stdout', new_callable=io.StringIO) as fake_out:
            cli.handle_delete("999")
            output = fake_out.getvalue()

            # Verify appropriate error message
            assert "TASK_NOT_FOUND" in output
            assert "999" in output

    def test_command_parsing_integration(self):
        """
        Test that commands are properly parsed and handled end-to-end.
        """
        cli = TodoCLI()

        # Add a task with spaces in title and description
        cli.process_command('add "Task with spaces" "Description with multiple words"')

        # Verify task was added correctly
        tasks = cli.service.list_tasks()
        assert len(tasks) == 1
        task = tasks[0]
        assert task.title == "Task with spaces"
        assert task.description == "Description with multiple words"

        # Test handling of commands with various argument patterns
        cli.process_command('add "Another task"')
        tasks = cli.service.list_tasks()
        assert len(tasks) == 2

        # Verify that both tasks exist and are properly formatted
        titles = [task.title for task in tasks]
        assert "Task with spaces" in titles
        assert "Another task" in titles

    def test_help_and_exit_commands(self):
        """
        Test that help and exit commands work correctly.
        """
        cli = TodoCLI()

        # Test help command
        with patch('sys.stdout', new_callable=io.StringIO) as fake_out:
            cli.handle_help()
            output = fake_out.getvalue()
            
            # Verify help text contains expected commands
            assert "add" in output
            assert "list" in output
            assert "complete" in output
            assert "delete" in output
            assert "update" in output
            assert "help" in output
            assert "exit" in output

        # Test exit command
        original_running = cli.running
        cli.handle_exit()
        assert not cli.running
        cli.running = original_running  # Reset for other tests