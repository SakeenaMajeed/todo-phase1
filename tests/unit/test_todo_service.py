"""
Unit tests for the TodoService in the Todo Console App.

These tests validate the core functionality of adding, listing, and validating tasks
as specified in the feature requirements.
"""

import pytest
from src.services.todo_service import TodoService
from src.models.task import Task
from src.lib.exceptions import InvalidTaskError, TaskNotFoundError


class TestTodoService:
    """
    Test suite for the TodoService class.
    """
    
    def test_add_task_with_title(self):
        """
        Test adding a task with only a title.
        
        Scenario: Given I'm on the main menu of the todo app, 
        When I enter the add task command with a title, 
        Then a new task with that title should appear in my todo list with a unique ID and 'incomplete' status
        """
        service = TodoService()
        
        # Add a task with only a title
        task = service.add_task("Buy groceries")
        
        # Verify the task was created correctly
        assert task.id == 1  # First task should get ID 1
        assert task.title == "Buy groceries"
        assert task.description == ""  # Default empty description
        assert not task.completed  # Default to incomplete
        
        # Verify the task is in the service
        tasks = service.list_tasks()
        assert len(tasks) == 1
        assert tasks[0] == task
    
    def test_add_task_with_title_and_description(self):
        """
        Test adding a task with both title and description.
        
        Scenario: Given I'm on the main menu, 
        When I enter the add task command with a title and description, 
        Then a new task with that title and description should appear in my todo list with a unique ID and 'incomplete' status
        """
        service = TodoService()
        
        # Add a task with title and description
        task = service.add_task("Buy groceries", "Milk, bread, eggs")
        
        # Verify the task was created correctly
        assert task.id == 1  # First task should get ID 1
        assert task.title == "Buy groceries"
        assert task.description == "Milk, bread, eggs"
        assert not task.completed  # Default to incomplete
        
        # Verify the task is in the service
        tasks = service.list_tasks()
        assert len(tasks) == 1
        assert tasks[0] == task
    
    def test_add_task_with_empty_title_should_fail(self):
        """
        Test that adding a task with an empty title raises an exception.
        
        Scenario: Given I'm on the main menu, 
        When I enter the add task command with an empty title, 
        Then I should see an error message indicating the title is required
        """
        service = TodoService()
        
        # Attempt to add a task with an empty title
        with pytest.raises(InvalidTaskError) as exc_info:
            service.add_task("")
        
        # Verify the exception message
        assert "title cannot be empty" in str(exc_info.value).lower()
    
    def test_add_multiple_tasks_unique_ids(self):
        """
        Test that multiple tasks get unique IDs.
        """
        service = TodoService()
        
        # Add two tasks
        task1 = service.add_task("First task")
        task2 = service.add_task("Second task")
        
        # Verify they have different IDs
        assert task1.id == 1
        assert task2.id == 2
        assert task1.id != task2.id
    
    def test_list_tasks_empty_list(self):
        """
        Test listing tasks when the list is empty.
        
        Scenario: Given I have no tasks in my list, 
        When I enter the list command, 
        Then I should see a message indicating the list is empty
        """
        service = TodoService()
        
        # List tasks when none exist
        tasks = service.list_tasks()
        
        # Verify the list is empty
        assert len(tasks) == 0
    
    def test_list_tasks_multiple_tasks(self):
        """
        Test listing multiple tasks.
        
        Scenario: Given I have multiple tasks in my list, 
        When I enter the list command, 
        Then all tasks should be displayed with their ID, status (complete/incomplete), and title
        """
        service = TodoService()
        
        # Add multiple tasks
        service.add_task("Task 1", "Description 1")
        service.add_task("Task 2", "Description 2")
        
        # List all tasks
        tasks = service.list_tasks()
        
        # Verify both tasks are returned
        assert len(tasks) == 2
        assert tasks[0].title == "Task 1"
        assert tasks[1].title == "Task 2"
        # Verify they are sorted by ID
        assert tasks[0].id == 1
        assert tasks[1].id == 2

    def test_complete_incomplete_task(self):
        """
        Test completing an incomplete task.

        Scenario: Given I have an incomplete task in my list,
        When I enter the complete task command with the task ID,
        Then the task's status should change to 'complete'
        """
        service = TodoService()

        # Add an incomplete task
        task = service.add_task("Test task")
        assert not task.completed  # Initially incomplete

        # Complete the task
        completed_task = service.complete_task(task.id)

        # Verify the task is now complete
        assert completed_task.completed
        assert service.get_task(task.id).completed  # Verify in storage too

    def test_complete_already_completed_task(self):
        """
        Test completing an already completed task.

        Scenario: Given I have a completed task in my list,
        When I enter the complete task command with that task's ID,
        Then the task should remain marked as 'complete'
        """
        service = TodoService()

        # Add and complete a task
        task = service.add_task("Test task")
        service.complete_task(task.id)
        assert task.completed  # Already complete

        # Try to complete it again
        completed_task = service.complete_task(task.id)

        # Verify the task remains complete
        assert completed_task.completed

    def test_complete_nonexistent_task_should_fail(self):
        """
        Test that completing a non-existent task raises an exception.

        Scenario: Given I have tasks in my list,
        When I enter the complete task command with a non-existent task ID,
        Then I should see an error message indicating the task doesn't exist
        """
        service = TodoService()

        # Add one task
        service.add_task("Test task")

        # Try to complete a non-existent task
        with pytest.raises(TaskNotFoundError) as exc_info:
            service.complete_task(999)  # Non-existent ID

        # Verify the exception message
        assert "999" in str(exc_info.value)

    def test_delete_existing_task(self):
        """
        Test deleting an existing task.

        Scenario: Given I have a task in my list,
        When I enter the delete task command with the task ID,
        Then the task should be removed from my list
        """
        service = TodoService()

        # Add a task
        task = service.add_task("Test task")
        assert len(service.list_tasks()) == 1  # Task exists

        # Delete the task
        result = service.delete_task(task.id)

        # Verify the task is deleted
        assert result is True  # Deletion successful
        assert len(service.list_tasks()) == 0  # No tasks left

    def test_delete_nonexistent_task_should_fail(self):
        """
        Test that deleting a non-existent task raises an exception.

        Scenario: Given I have tasks in my list,
        When I enter the delete task command with a non-existent task ID,
        Then I should see an error message indicating the task doesn't exist
        """
        service = TodoService()

        # Add one task
        service.add_task("Test task")

        # Try to delete a non-existent task
        with pytest.raises(TaskNotFoundError) as exc_info:
            service.delete_task(999)  # Non-existent ID

        # Verify the exception message
        assert "999" in str(exc_info.value)

    def test_delete_from_empty_list_should_fail(self):
        """
        Test that deleting from an empty list raises an exception.

        Scenario: Given I have no tasks in my list,
        When I enter the delete task command,
        Then I should see an error message indicating there are no tasks to delete
        """
        service = TodoService()

        # Try to delete from an empty list
        with pytest.raises(TaskNotFoundError) as exc_info:
            service.delete_task(1)  # No tasks exist

        # Verify the exception message
        assert "1" in str(exc_info.value)

    def test_update_task_title(self):
        """
        Test updating task title.

        Scenario: Given I have a task in my list,
        When I enter the update task command with the task ID and new title,
        Then the task's title should be updated
        """
        service = TodoService()

        # Add a task
        task = service.add_task("Old title", "Description")
        assert task.title == "Old title"

        # Update the task title
        updated_task = service.update_task(task.id, "New title")

        # Verify the title was updated
        assert updated_task.title == "New title"
        assert updated_task.description == "Description"  # Description should remain unchanged

    def test_update_task_description(self):
        """
        Test updating task description.

        Scenario: Given I have a task in my list,
        When I enter the update task command with the task ID and new description,
        Then the task's description should be updated
        """
        service = TodoService()

        # Add a task
        task = service.add_task("Title", "Old description")
        assert task.description == "Old description"

        # Update the task description
        updated_task = service.update_task(task.id, description="New description")

        # Verify the description was updated
        assert updated_task.description == "New description"
        assert updated_task.title == "Title"  # Title should remain unchanged

    def test_update_nonexistent_task_should_fail(self):
        """
        Test that updating a non-existent task raises an exception.

        Scenario: Given I have tasks in my list,
        When I enter the update task command with a non-existent task ID,
        Then I should see an error message indicating the task doesn't exist
        """
        service = TodoService()

        # Add one task
        service.add_task("Test task")

        # Try to update a non-existent task
        with pytest.raises(TaskNotFoundError) as exc_info:
            service.update_task(999, "New title")  # Non-existent ID

        # Verify the exception message
        assert "999" in str(exc_info.value)