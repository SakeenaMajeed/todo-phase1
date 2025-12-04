# Data Model: Todo Console App

## Task Entity

### Fields
- **id** (int): Unique identifier for the task, auto-generated starting from 1
- **title** (str): Required string representing the task name, minimum length 1 character
- **description** (str): Optional string providing additional details about the task, can be empty or None
- **completed** (bool): Boolean flag indicating whether the task is completed (True) or incomplete (False), defaults to False

### Validation Rules
- Title must be provided and not empty (length > 0)
- ID must be unique within the application session
- ID must be a positive integer

### State Transitions
- A task starts with `completed = False`
- A task can transition to `completed = True` when marked as complete
- A task can transition back to `completed = False` from `completed = True`
- A task is removed from storage when deleted

## Relationships
- No relationships needed as this is a single entity application