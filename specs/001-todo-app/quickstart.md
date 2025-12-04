# Quickstart: Todo Console App

## Running the Application

The Todo Console App is a Python application that runs directly from the command line:

```bash
python -m src.cli.todo_cli
```

## Available Commands

Once the application is running, you can use the following commands:

### Add a Task
```
add "Task title" ["Optional description"]
```
- Creates a new task with the provided title and optional description
- Task will be assigned a unique ID and marked as incomplete
- Example: `add "Buy groceries" "Milk, bread, eggs"`

### List Tasks
```
list
```
- Displays all tasks with their ID, status (completed/incomplete), title, and description
- Example: `list`

### Complete a Task
```
complete <task_id>
```
- Marks the task with the given ID as completed
- Example: `complete 1`

### Update a Task
```
update <task_id> "New title" ["New description"]
```
- Updates the title and/or description of a task
- Example: `update 1 "Updated task title" "New description"`

### Delete a Task
```
delete <task_id>
```
- Removes the task with the given ID from the list
- Example: `delete 1`

### Show Help
```
help
```
- Displays this help message with all available commands
- Example: `help`

### Exit the Application
```
exit
```
- Quits the application
- Example: `exit`

## Examples

### Adding and Completing a Task
1. `add "Buy milk"`
2. `list` (shows the new task with ID 1)
3. `complete 1` (marks task 1 as complete)

### Viewing All Commands
- `help` (displays all available commands)

## Error Handling

The application will display clear error messages if:
- You enter an invalid command
- You provide an invalid task ID
- You try to operate on a task that doesn't exist
- You provide insufficient arguments to a command