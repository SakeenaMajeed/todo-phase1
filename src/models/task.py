"""
Task entity model for the Todo Console App.

This module defines the Task class with required fields, validation rules,
and methods for updating properties as specified in the data model.
"""

from typing import Optional


class Task:
    """
    Represents a todo item with ID, title, optional description, and completion status.
    
    Attributes:
        id (int): Unique identifier for the task (positive integer)
        title (str): Required string representing the task name (non-empty)
        description (Optional[str]): Optional string providing additional details
        completed (bool): Boolean flag indicating completion status
    """
    
    def __init__(self, task_id: int, title: str, description: Optional[str] = None, completed: bool = False):
        """
        Initialize a Task instance.
        
        Args:
            task_id: Unique identifier for the task (positive integer)
            title: Required task title (non-empty string)
            description: Optional task description
            completed: Completion status (default: False)
            
        Raises:
            ValueError: If task_id is not a positive integer or title is empty
        """
        self.id = self._validate_id(task_id)
        self.title = self._validate_title(title)
        self.description = description if description is not None else ""
        self.completed = completed
    
    @staticmethod
    def _validate_id(task_id: int) -> int:
        """
        Validate that the task ID is a positive integer.
        
        Args:
            task_id: The ID to validate
            
        Returns:
            The validated ID
            
        Raises:
            ValueError: If ID is not a positive integer
        """
        if not isinstance(task_id, int) or task_id <= 0:
            error_msg = f"Task ID must be a positive integer, got {task_id}"
            raise ValueError(error_msg)
        return task_id
    
    @staticmethod
    def _validate_title(title: str) -> str:
        """
        Validate that the title is a non-empty string.
        
        Args:
            title: The title to validate
            
        Returns:
            The validated title
            
        Raises:
            ValueError: If title is empty
        """
        if not isinstance(title, str) or not title.strip():
            raise ValueError("Task title cannot be empty")
        return title.strip()
    
    def update(self, title: Optional[str] = None, description: Optional[str] = None) -> None:
        """
        Update task properties.
        
        Args:
            title: New title (if provided)
            description: New description (if provided)
            
        Raises:
            ValueError: If title is provided but is empty
        """
        if title is not None:
            self.title = self._validate_title(title)
        
        if description is not None:
            self.description = description
    
    def complete(self) -> None:
        """Mark the task as completed."""
        self.completed = True
    
    def incomplete(self) -> None:
        """Mark the task as incomplete."""
        self.completed = False
    
    def __repr__(self) -> str:
        """
        Return string representation of the task.

        Returns:
            A string representation of the task
        """
        status = "X" if self.completed else "O"
        return f"[{status}] {self.id}: {self.title}"
    
    def __eq__(self, other) -> bool:
        """
        Compare two Task objects for equality.
        
        Args:
            other: Another Task object to compare with
            
        Returns:
            True if the tasks are equal, False otherwise
        """
        if not isinstance(other, Task):
            return False
        return (self.id == other.id and self.title == other.title and
                self.description == other.description and self.completed == other.completed)