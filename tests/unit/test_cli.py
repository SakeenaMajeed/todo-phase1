"""
Unit tests for the TodoCLI in the Todo Console App.

These tests validate the CLI interface functionality, ensuring that user commands
are properly parsed and handled according to the specification.
"""

import io
import sys
import pytest
from unittest.mock import Mock, patch
from src.cli.todo_cli import TodoCLI
from src.models.task import Task


class TestTodoCLI:
    """
    Test suite for the TodoCLI class.
    """

    def test_handle_add_with_title_only(self):
        """
        Test CLI handling of add command with title only.
        """
        cli = TodoCLI()
        cli.service.add_task = Mock(return_value=Task(1, "Test Task"))

        # Capture printed output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        cli.handle_add('"Test Task"')

        # Restore stdout
        sys.stdout = sys.__stdout__

        # Verify output
        output = captured_output.getvalue().strip()
        assert "Task added with ID: 1" in output

        # Verify service method was called
        cli.service.add_task.assert_called_once_with("Test Task", None)

    def test_handle_add_with_title_and_description(self):
        """
        Test CLI handling of add command with title and description.
        """
        cli = TodoCLI()
        cli.service.add_task = Mock(return_value=Task(1, "Test Task", "Test Description"))

        # Capture printed output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        cli.handle_add('"Test Task" "Test Description"')

        # Restore stdout
        sys.stdout = sys.__stdout__

        # Verify output
        output = captured_output.getvalue().strip()
        assert "Task added with ID: 1" in output

        # Verify service method was called
        cli.service.add_task.assert_called_once_with("Test Task", "Test Description")

    def test_handle_add_missing_title_shows_error(self):
        """
        Test CLI handling of add command with missing title.
        """
        cli = TodoCLI()
        cli.service.add_task = Mock()

        # Capture printed output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        cli.handle_add("")

        # Restore stdout
        sys.stdout = sys.__stdout__

        # Verify error message
        output = captured_output.getvalue().strip()
        assert "[ERROR] Missing task title" in output

        # Verify service method was not called
        cli.service.add_task.assert_not_called()

    def test_handle_list_with_tasks(self):
        """
        Test CLI handling of list command with existing tasks.
        """
        cli = TodoCLI()
        mock_tasks = [
            Task(1, "Task 1", completed=False),
            Task(2, "Task 2", "Description", completed=True)
        ]
        cli.service.list_tasks = Mock(return_value=mock_tasks)

        # Capture printed output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        cli.handle_list()

        # Restore stdout
        sys.stdout = sys.__stdout__

        # Verify output includes task information
        output = captured_output.getvalue()
        assert "Task List:" in output
        assert "[O] 1: Task 1" in output  # Incomplete task
        assert "[X] 2: Task 2" in output  # Complete task
        assert "Description: Description" in output

        # Verify service method was called
        cli.service.list_tasks.assert_called_once()

    def test_handle_list_empty(self):
        """
        Test CLI handling of list command with no tasks.
        """
        cli = TodoCLI()
        cli.service.list_tasks = Mock(return_value=[])

        # Capture printed output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        cli.handle_list()

        # Restore stdout
        sys.stdout = sys.__stdout__

        # Verify empty list message
        output = captured_output.getvalue().strip()
        assert "No tasks in the list." in output

        # Verify service method was called
        cli.service.list_tasks.assert_called_once()

    def test_handle_complete_task(self):
        """
        Test CLI handling of complete command.
        """
        cli = TodoCLI()
        task = Task(1, "Test Task")
        task.complete()  # Mark as complete to simulate return
        cli.service.complete_task = Mock(return_value=task)

        # Capture printed output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        cli.handle_complete("1")

        # Restore stdout
        sys.stdout = sys.__stdout__

        # Verify output
        output = captured_output.getvalue().strip()
        assert "Task 1 marked as complete" in output

        # Verify service method was called
        cli.service.complete_task.assert_called_once_with(1)

    def test_handle_complete_task_invalid_id_shows_error(self):
        """
        Test CLI handling of complete command with invalid ID.
        """
        cli = TodoCLI()
        cli.service.complete_task = Mock()

        # Capture printed output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        cli.handle_complete("abc")

        # Restore stdout
        sys.stdout = sys.__stdout__

        # Verify error message
        output = captured_output.getvalue().strip()
        assert "[ERROR] Invalid task ID" in output

        # Verify service method was not called
        cli.service.complete_task.assert_not_called()

    def test_handle_complete_task_missing_id_shows_error(self):
        """
        Test CLI handling of complete command without ID.
        """
        cli = TodoCLI()
        cli.service.complete_task = Mock()

        # Capture printed output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        cli.handle_complete("")

        # Restore stdout
        sys.stdout = sys.__stdout__

        # Verify error message
        output = captured_output.getvalue().strip()
        assert "[ERROR] Missing task ID" in output

        # Verify service method was not called
        cli.service.complete_task.assert_not_called()

    def test_handle_delete_task(self):
        """
        Test CLI handling of delete command.
        """
        cli = TodoCLI()
        cli.service.delete_task = Mock(return_value=True)

        # Capture printed output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        cli.handle_delete("1")

        # Restore stdout
        sys.stdout = sys.__stdout__

        # Verify output
        output = captured_output.getvalue().strip()
        assert "Task 1 deleted successfully" in output

        # Verify service method was called
        cli.service.delete_task.assert_called_once_with(1)

    def test_handle_delete_task_invalid_id_shows_error(self):
        """
        Test CLI handling of delete command with invalid ID.
        """
        cli = TodoCLI()
        cli.service.delete_task = Mock()

        # Capture printed output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        cli.handle_delete("abc")

        # Restore stdout
        sys.stdout = sys.__stdout__

        # Verify error message
        output = captured_output.getvalue().strip()
        assert "[ERROR] Invalid task ID" in output

        # Verify service method was not called
        cli.service.delete_task.assert_not_called()

    def test_handle_delete_task_missing_id_shows_error(self):
        """
        Test CLI handling of delete command without ID.
        """
        cli = TodoCLI()
        cli.service.delete_task = Mock()

        # Capture printed output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        cli.handle_delete("")

        # Restore stdout
        sys.stdout = sys.__stdout__

        # Verify error message
        output = captured_output.getvalue().strip()
        assert "[ERROR] Missing task ID" in output

        # Verify service method was not called
        cli.service.delete_task.assert_not_called()

    def test_handle_update_task(self):
        """
        Test CLI handling of update command with new title.
        """
        cli = TodoCLI()
        task = Task(1, "Updated title")
        cli.service.update_task = Mock(return_value=task)

        # Capture printed output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        cli.handle_update('1 "Updated title"')

        # Restore stdout
        sys.stdout = sys.__stdout__

        # Verify output
        output = captured_output.getvalue().strip()
        assert "Task 1 updated successfully" in output

        # Verify service method was called
        cli.service.update_task.assert_called_once_with(1, "Updated title", None)

    def test_handle_update_task_with_description(self):
        """
        Test CLI handling of update command with new title and description.
        """
        cli = TodoCLI()
        task = Task(1, "Updated title", "Updated description")
        cli.service.update_task = Mock(return_value=task)

        # Capture printed output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        cli.handle_update('1 "Updated title" "Updated description"')

        # Restore stdout
        sys.stdout = sys.__stdout__

        # Verify output
        output = captured_output.getvalue().strip()
        assert "Task 1 updated successfully" in output

        # Verify service method was called
        cli.service.update_task.assert_called_once_with(1, "Updated title", "Updated description")

    def test_handle_update_task_invalid_id_shows_error(self):
        """
        Test CLI handling of update command with invalid ID.
        """
        cli = TodoCLI()
        cli.service.update_task = Mock()

        # Capture printed output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        cli.handle_update("abc")

        # Restore stdout
        sys.stdout = sys.__stdout__

        # Verify error message
        output = captured_output.getvalue().strip()
        assert "[ERROR] Invalid task ID" in output

        # Verify service method was not called
        cli.service.update_task.assert_not_called()

    def test_handle_update_task_missing_args_shows_error(self):
        """
        Test CLI handling of update command without proper arguments.
        """
        cli = TodoCLI()
        cli.service.update_task = Mock()

        # Capture printed output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        cli.handle_update("1")

        # Restore stdout
        sys.stdout = sys.__stdout__

        # Verify error message
        output = captured_output.getvalue().strip()
        assert "[ERROR] Missing new title" in output

        # Verify service method was not called
        cli.service.update_task.assert_not_called()

    def test_handle_unknown_command_shows_error(self):
        """
        Test CLI handling of unknown commands.
        """
        cli = TodoCLI()

        # Capture printed output
        captured_output = io.StringIO()
        sys.stdout = captured_output

        cli.handle_unknown_command("unknown_cmd")

        # Restore stdout
        sys.stdout = sys.__stdout__

        # Verify error message
        output = captured_output.getvalue().strip()
        assert "[ERROR] Unknown command 'unknown_cmd'" in output

    def test_process_command_add(self):
        """
        Test processing add command through main command processor.
        """
        cli = TodoCLI()
        cli.handle_add = Mock()

        cli.process_command("add Test Task")

        cli.handle_add.assert_called_once_with("Test Task")

    def test_process_command_list(self):
        """
        Test processing list command through main command processor.
        """
        cli = TodoCLI()
        cli.handle_list = Mock()

        cli.process_command("list")

        cli.handle_list.assert_called_once()

    def test_process_command_complete(self):
        """
        Test processing complete command through main command processor.
        """
        cli = TodoCLI()
        cli.handle_complete = Mock()

        cli.process_command("complete 1")

        cli.handle_complete.assert_called_once_with("1")

    def test_process_command_delete(self):
        """
        Test processing delete command through main command processor.
        """
        cli = TodoCLI()
        cli.handle_delete = Mock()

        cli.process_command("delete 1")

        cli.handle_delete.assert_called_once_with("1")

    def test_process_command_update(self):
        """
        Test processing update command through main command processor.
        """
        cli = TodoCLI()
        cli.handle_update = Mock()

        cli.process_command("update 1 New Title")

        cli.handle_update.assert_called_once_with("1 New Title")

    def test_process_command_help(self):
        """
        Test processing help command through main command processor.
        """
        cli = TodoCLI()
        cli.handle_help = Mock()

        cli.process_command("help")

        cli.handle_help.assert_called_once()

    def test_process_command_exit(self):
        """
        Test processing exit command through main command processor.
        """
        cli = TodoCLI()
        cli.handle_exit = Mock()

        cli.process_command("exit")

        cli.handle_exit.assert_called_once()

    def test_process_command_unknown(self):
        """
        Test processing unknown command through main command processor.
        """
        cli = TodoCLI()
        cli.handle_unknown_command = Mock()

        cli.process_command("invalid_command")

        cli.handle_unknown_command.assert_called_once_with("invalid_command")

    def test_process_empty_command(self):
        """
        Test processing empty command - should do nothing.
        """
        cli = TodoCLI()

        # Mock all handlers to ensure none are called
        cli.handle_add = Mock()
        cli.handle_list = Mock()
        cli.handle_complete = Mock()
        cli.handle_delete = Mock()
        cli.handle_update = Mock()
        cli.handle_help = Mock()
        cli.handle_exit = Mock()
        cli.handle_unknown_command = Mock()

        cli.process_command("")

        # Verify no handlers were called
        cli.handle_add.assert_not_called()
        cli.handle_list.assert_not_called()
        cli.handle_complete.assert_not_called()
        cli.handle_delete.assert_not_called()
        cli.handle_update.assert_not_called()
        cli.handle_help.assert_not_called()
        cli.handle_exit.assert_not_called()
        cli.handle_unknown_command.assert_not_called()