"""
Custom exceptions for the Todo Console App.

This module defines application-specific exceptions that follow the constitution
requirement for clear error handling with category, issue description, and resolution.
"""


class InvalidTaskError(Exception):
    """
    Raised when a task operation is invalid.

    Args:
        message (str): Description of the error
        resolution (str): Suggested resolution for the error
    """
    def __init__(self, message: str, resolution: str = "Check the input and try again"):
        self.message = message
        self.resolution = resolution
        super().__init__(f"[INVALID_TASK] {message} - {resolution}")


class TaskNotFoundError(Exception):
    """
    Raised when a task with a specified ID does not exist.

    Args:
        task_id (int): The ID of the task that was not found
        resolution (str): Suggested resolution for the error
    """
    def __init__(self, task_id: int, resolution: str = "Verify task ID exists before operation"):
        self.task_id = task_id
        self.message = f"Task with ID {task_id} does not exist"
        self.resolution = resolution
        error_message = f"[TASK_NOT_FOUND] {self.message} - {self.resolution}"
        super().__init__(error_message)