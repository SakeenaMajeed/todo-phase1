"""
TodoService for the Todo Console App.

This module implements the business logic for task operations following the clean
architecture pattern. It manages in-memory storage and provides methods for
adding, listing, updating, completing, and deleting tasks.
"""

from typing import List, Optional
from models.task import Task
from lib.exceptions import InvalidTaskError, TaskNotFoundError


class TodoService:
    """
    Service class managing all business operations for tasks.

    This service handles the core functionality of the todo app including:
    - Adding new tasks
    - Listing all tasks
    - Updating existing tasks
    - Marking tasks as complete/incomplete
    - Deleting tasks

    All operations are performed in-memory as specified in the requirements.
    """

    def __init__(self):
        """
        Initialize the TodoService with empty storage and ID counter.
        """
        self._tasks = {}  # Dictionary with task ID as key and Task object as value
        self._next_id = 1  # Counter for generating unique task IDs

    def _get_next_id(self) -> int:
        """
        Generate the next available task ID.

        Returns:
            The next available positive integer ID
        """
        next_id = self._next_id
        self._next_id += 1
        return next_id

    def add_task(self, title: str, description: Optional[str] = None) -> Task:
        """
        Add a new task to the system.

        Args:
            title: Required task title (non-empty)
            description: Optional task description

        Returns:
            The newly created Task object

        Raises:
            InvalidTaskError: If title is empty
        """
        try:
            new_id = self._get_next_id()
            task = Task(new_id, title, description, completed=False)
            self._tasks[new_id] = task
            return task
        except ValueError as e:
            raise InvalidTaskError(f"Failed to create task: {str(e)}")

    def list_tasks(self) -> List[Task]:
        """
        Get all tasks in the system.

        Returns:
            List of all Task objects, sorted by ID
        """
        return sorted(self._tasks.values(), key=lambda x: x.id)

    def get_task(self, task_id: int) -> Task:
        """
        Get a specific task by ID.

        Args:
            task_id: ID of the task to retrieve

        Returns:
            The Task object

        Raises:
            TaskNotFoundError: If task with given ID doesn't exist
        """
        if task_id not in self._tasks:
            raise TaskNotFoundError(task_id)
        return self._tasks[task_id]

    def update_task(self, task_id: int, title: Optional[str] = None, description: Optional[str] = None) -> Task:
        """
        Update an existing task.

        Args:
            task_id: ID of the task to update
            title: New title (if provided)
            description: New description (if provided)

        Returns:
            The updated Task object

        Raises:
            TaskNotFoundError: If task with given ID doesn't exist
            InvalidTaskError: If new title is empty
        """
        if task_id not in self._tasks:
            raise TaskNotFoundError(task_id)

        try:
            task = self._tasks[task_id]
            task.update(title, description)
            return task
        except ValueError as e:
            raise InvalidTaskError(f"Failed to update task: {str(e)}")

    def complete_task(self, task_id: int) -> Task:
        """
        Mark a task as completed.

        Args:
            task_id: ID of the task to complete

        Returns:
            The completed Task object

        Raises:
            TaskNotFoundError: If task with given ID doesn't exist
        """
        if task_id not in self._tasks:
            raise TaskNotFoundError(task_id)

        task = self._tasks[task_id]
        task.complete()
        return task

    def incomplete_task(self, task_id: int) -> Task:
        """
        Mark a task as incomplete.

        Args:
            task_id: ID of the task to mark as incomplete

        Returns:
            The Task object marked as incomplete

        Raises:
            TaskNotFoundError: If task with given ID doesn't exist
        """
        if task_id not in self._tasks:
            raise TaskNotFoundError(task_id)

        task = self._tasks[task_id]
        task.incomplete()
        return task

    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task.

        Args:
            task_id: ID of the task to delete

        Returns:
            True if task was deleted successfully, False if task didn't exist

        Raises:
            TaskNotFoundError: If task with given ID doesn't exist
        """
        if task_id not in self._tasks:
            raise TaskNotFoundError(task_id)

        del self._tasks[task_id]
        return True

    def get_task_count(self) -> int:
        """
        Get the total number of tasks.

        Returns:
            The number of tasks in the system
        """
        return len(self._tasks)