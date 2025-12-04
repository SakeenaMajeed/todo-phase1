"""
Unit tests for the Task model in the Todo Console App.

These tests validate the Task entity with its validation rules as specified 
in the data model.
"""

import pytest
from src.models.task import Task
from src.lib.exceptions import InvalidTaskError


class TestTaskModel:
    """
    Test suite for the Task model class.
    """
    
    def test_create_task_valid(self):
        """
        Test creating a valid task with all fields.
        """
        task = Task(1, "Valid Task", "A description", False)
        
        assert task.id == 1
        assert task.title == "Valid Task"
        assert task.description == "A description"
        assert not task.completed
    
    def test_create_task_minimal(self):
        """
        Test creating a task with only required fields.
        """
        task = Task(1, "Valid Task")
        
        assert task.id == 1
        assert task.title == "Valid Task"
        assert task.description == ""  # Default empty description
        assert not task.completed  # Default to incomplete
    
    def test_validate_id_positive_integer(self):
        """
        Test that task ID must be a positive integer.
        """
        # Valid ID
        task = Task(1, "Valid Task")
        assert task.id == 1
        
        # Invalid IDs should raise ValueError
        with pytest.raises(ValueError):
            Task(0, "Invalid ID Task")
        
        with pytest.raises(ValueError):
            Task(-1, "Invalid ID Task")
    
    def test_validate_title_non_empty(self):
        """
        Test that task title must be non-empty.
        """
        # Valid title
        task = Task(1, "Valid Title")
        assert task.title == "Valid Title"
        
        # Invalid titles should raise ValueError
        with pytest.raises(ValueError):
            Task(1, "")
        
        with pytest.raises(ValueError):
            Task(1, "   ")  # Only spaces should be treated as empty after stripping
    
    def test_update_task_title_and_description(self):
        """
        Test updating task title and description.
        """
        task = Task(1, "Original Title", "Original Description")
        
        # Update both title and description
        task.update("New Title", "New Description")
        
        assert task.title == "New Title"
        assert task.description == "New Description"
    
    def test_update_task_title_only(self):
        """
        Test updating only the title.
        """
        task = Task(1, "Original Title", "Original Description")
        
        # Update only the title
        task.update("New Title")
        
        assert task.title == "New Title"
        assert task.description == "Original Description"  # Should remain unchanged
    
    def test_update_task_description_only(self):
        """
        Test updating only the description.
        """
        task = Task(1, "Original Title", "Original Description")
        
        # Update only the description
        task.update(description="New Description")
        
        assert task.title == "Original Title"  # Should remain unchanged
        assert task.description == "New Description"
    
    def test_update_task_invalid_title(self):
        """
        Test that updating with an invalid title raises an exception.
        """
        task = Task(1, "Original Title", "Original Description")
        
        with pytest.raises(ValueError):
            task.update("")  # Empty title should fail
    
    def test_complete_and_incomplete_task(self):
        """
        Test marking tasks as complete and incomplete.
        """
        task = Task(1, "Test Task")
        
        # Initially incomplete
        assert not task.completed
        
        # Mark as complete
        task.complete()
        assert task.completed
        
        # Mark as incomplete again
        task.incomplete()
        assert not task.completed
    
    def test_task_repr(self):
        """
        Test the string representation of a task.
        """
        # Incomplete task
        task_incomplete = Task(1, "Test Task", completed=False)
        assert "O" in repr(task_incomplete)
        assert "1:" in repr(task_incomplete)
        assert "Test Task" in repr(task_incomplete)

        # Complete task
        task_complete = Task(2, "Test Task", completed=True)
        assert "X" in repr(task_complete)
        assert "2:" in repr(task_complete)
        assert "Test Task" in repr(task_complete)
    
    def test_task_equality(self):
        """
        Test equality comparison between tasks.
        """
        task1 = Task(1, "Title", "Description", False)
        task2 = Task(1, "Title", "Description", False)
        task3 = Task(2, "Title", "Description", False)
        
        # Same ID, title, description, and completion status should be equal
        assert task1 == task2
        
        # Different ID should not be equal
        assert task1 != task3
        
        # Different type should not be equal
        assert task1 != "not a task"