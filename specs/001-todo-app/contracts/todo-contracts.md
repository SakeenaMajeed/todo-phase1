# Internal API Contracts: Todo Console App

## Task Model Contract

### Task Class Interface
```python
class Task:
    def __init__(self, id: int, title: str, description: str = None, completed: bool = False):
        """
        Creates a new task.
        
        Args:
            id: Unique identifier for the task (positive integer)
            title: Required task title (non-empty string)
            description: Optional task description
            completed: Completion status (default: False)
        """
    
    def update(self, title: str = None, description: str = None) -> None:
        """
        Update task properties.
        
        Args:
            title: New title (if provided)
            description: New description (if provided)
        """
    
    def complete(self) -> None:
        """Mark the task as completed."""
    
    def incomplete(self) -> None:
        """Mark the task as incomplete."""
```

## Todo Service Contract

### TodoService Class Interface
```python
class TodoService:
    def add_task(self, title: str, description: str = None) -> Task:
        """
        Add a new task.
        
        Args:
            title: Task title (required, non-empty)
            description: Task description (optional)
            
        Returns:
            The newly created Task object
            
        Raises:
            InvalidTaskError: If title is empty
        """
    
    def list_tasks(self) -> List[Task]:
        """
        Get all tasks.
        
        Returns:
            List of all Task objects
        """
    
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
    
    def update_task(self, task_id: int, title: str = None, description: str = None) -> Task:
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
    
    def delete_task(self, task_id: int) -> bool:
        """
        Delete a task.
        
        Args:
            task_id: ID of the task to delete
            
        Returns:
            True if task was deleted, False if not found
            
        Raises:
            TaskNotFoundError: If task with given ID doesn't exist
        """
```

## CLI Interface Contract

### CLI Command Format
- Commands are case-sensitive strings
- Arguments are enclosed in quotes if containing spaces
- Task IDs are positive integers

### Command Contracts
```
add <title> [description]
- Add a task with the given title and optional description
- Returns: "Task added with ID: <id>"

list
- List all tasks in the system
- Returns: Formatted list of tasks with ID, status, title, and description

complete <task_id>
- Mark the task with given ID as complete
- Returns: "Task <id> marked as complete" or error message

update <task_id> <title> [description]
- Update the task with given ID
- Returns: "Task <id> updated successfully" or error message

delete <task_id>
- Delete the task with given ID
- Returns: "Task <id> deleted successfully" or error message

help
- Show available commands
- Returns: List of available commands with explanations

exit
- Exit the application
- Returns: Exits with goodbye message
```

## Error Contract
All errors return a message in the format:
```
[ERROR_CATEGORY] Error: <specific issue description> - <suggested resolution>
```