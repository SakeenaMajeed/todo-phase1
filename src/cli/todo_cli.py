
"""
CLI interface for the Todo Console App.

This module provides the command-line interface that handles user input/output
and command parsing according to the constitution's requirements for a usable
console user experience.
"""

from typing import Optional
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from services.todo_service import TodoService


class TodoCLI:
    """
    Command-line interface for interacting with the TodoService.

    This class handles user commands like add, list, complete, delete, update, and help.
    It parses user input and delegates to the TodoService for business logic.
    """

    def __init__(self):
        """
        Initialize the CLI with a TodoService instance.
        """
        self.service = TodoService()
        self.running = True

    def run(self):
        """
        Run the main CLI loop, processing user commands until exit.
        """
        print("Welcome to the Todo Console App!")
        print("Type 'help' for available commands or 'exit' to quit.")

        while self.running:
            try:
                user_input = input("\n> ").strip()
                self.process_command(user_input)
            except KeyboardInterrupt:
                print("\nReceived interrupt signal. Exiting...")
                break
            except EOFError:
                print("\nEnd of input. Exiting...")
                break

    def process_command(self, user_input: str):
        """
        Process a single command from the user.

        Args:
            user_input: The raw command string from the user
        """
        if not user_input:
            return

        parts = user_input.split(" ", 1)
        command = parts[0].lower()
        args = parts[1] if len(parts) > 1 else ""

        if command == "add":
            self.handle_add(args)
        elif command == "list":
            self.handle_list()
        elif command == "complete":
            self.handle_complete(args)
        elif command == "incomplete":
            self.handle_incomplete(args)
        elif command == "delete":
            self.handle_delete(args)
        elif command == "update":
            self.handle_update(args)
        elif command == "help":
            self.handle_help()
        elif command == "exit":
            self.handle_exit()
        else:
            self.handle_unknown_command(command)

    def handle_add(self, args: str):
        """
        Handle the 'add' command to create a new task.

        Args:
            args: The arguments following the 'add' command
        """
        # Parse arguments: expecting "title" ["description"]
        if not args:
            print("[ERROR] Missing task title - Please provide a title for the task")
            return

        try:
            # Handle quoted arguments
            title, description = self._parse_title_and_description(args)
            task = self.service.add_task(title, description)
            print(f"Task added with ID: {task.id}")
        except Exception as e:
            self._handle_error(e)

    def handle_list(self):
        """
        Handle the 'list' command to display all tasks.
        """
        try:
            tasks = self.service.list_tasks()

            if not tasks:
                print("No tasks in the list.")
                return

            print("\nTask List:")
            for task in tasks:
                status = "X" if task.completed else "O"
                print(f"[{status}] {task.id}: {task.title}")
                if task.description:
                    print(f"     Description: {task.description}")
        except Exception as e:
            self._handle_error(e)

    def handle_complete(self, args: str):
        """
        Handle the 'complete' command to mark a task as complete.

        Args:
            args: The arguments following the 'complete' command (task ID)
        """
        if not args:
            print("[ERROR] Missing task ID - Please provide task ID to complete")
            return

        try:
            task_id = int(args.strip())
            task = self.service.complete_task(task_id)
            print(f"Task {task.id} marked as complete")
        except ValueError:
            print("[ERROR] Invalid task ID - Please provide a valid integer ID")
        except Exception as e:
            self._handle_error(e)

    def handle_incomplete(self, args: str):
        """
        Handle the 'incomplete' command to mark a task as incomplete.

        Args:
            args: The arguments following the 'incomplete' command (task ID)
        """
        if not args:
            print("[ERROR] Missing task ID - Please provide task ID to mark as incomplete")
            return

        try:
            task_id = int(args.strip())
            task = self.service.incomplete_task(task_id)
            print(f"Task {task.id} marked as incomplete")
        except ValueError:
            print("[ERROR] Invalid task ID - Please provide a valid integer ID")
        except Exception as e:
            self._handle_error(e)

    def handle_delete(self, args: str):
        """
        Handle the 'delete' command to remove a task.

        Args:
            args: The arguments following the 'delete' command (task ID)
        """
        if not args:
            print("[ERROR] Missing task ID - Please provide task ID to delete")
            return

        try:
            task_id = int(args.strip())
            self.service.delete_task(task_id)
            print(f"Task {task_id} deleted successfully")
        except ValueError:
            print("[ERROR] Invalid task ID - Please provide a valid integer ID")
        except Exception as e:
            self._handle_error(e)

    def handle_update(self, args: str):
        """
        Handle the 'update' command to modify a task's details.

        Args:
            args: The arguments following the 'update' command (task ID, title, description)
        """
        if not args:
            print("[ERROR] Missing arguments - Please provide task ID and new title")
            return

        try:
            # Parse: task_id "new_title" ["new_description"]
            parts = args.split(" ", 1)
            task_id = int(parts[0])
            remaining_args = parts[1] if len(parts) > 1 else ""

            if not remaining_args:
                print("[ERROR] Missing new title - Please provide new title for the task")
                return

            new_title, new_description = self._parse_title_and_description(remaining_args)

            task = self.service.update_task(task_id, new_title, new_description)
            print(f"Task {task.id} updated successfully")
        except ValueError:
            print("[ERROR] Invalid task ID - Please provide a valid integer ID")
        except Exception as e:
            self._handle_error(e)

    def handle_help(self):
        """
        Handle the 'help' command to display available commands.
        """
        help_text = """
Available Commands:
  add "title" ["description"]  - Add a new task
  list                       - List all tasks
  complete <id>              - Mark task as complete
  incomplete <id>            - Mark task as incomplete
  delete <id>                - Delete a task
  update <id> "title" ["desc"] - Update a task
  help                       - Show this help message
  exit                       - Exit the application
        """
        print(help_text)

    def handle_exit(self):
        """
        Handle the 'exit' command to terminate the application.
        """
        print("Goodbye!")
        self.running = False

    def handle_unknown_command(self, command: str):
        """
        Handle unknown commands with an error message.

        Args:
            command: The unrecognized command
        """
        print(f"[ERROR] Unknown command '{command}' - Type 'help' for commands")

    def _parse_title_and_description(self, args: str) -> tuple[str, Optional[str]]:
        """
        Parse title and optional description from command arguments.

        Args:
            args: The arguments to parse

        Returns:
            A tuple of (title, description) where description can be None
        """
        # Simple case: no quotes
        if not ('"' in args or "'" in args):
            parts = args.split(" ", 1)
            title = parts[0]
            description = parts[1] if len(parts) > 1 else None
            return title, description

        # Handle quoted arguments
        parts = []
        current_part = ""
        in_quotes = False
        quote_char = None

        i = 0
        while i < len(args):
            char = args[i]

            if not in_quotes and (char == '"' or char == "'"):
                in_quotes = True
                quote_char = char
            elif in_quotes and char == quote_char:
                in_quotes = False
                quote_char = None
            elif not in_quotes and char == ' ' and current_part:
                parts.append(current_part)
                current_part = ""
            else:
                current_part += char

            i += 1

        # Add the last part if it exists
        if current_part:
            parts.append(current_part)

        title = parts[0] if len(parts) > 0 else ""
        description = parts[1] if len(parts) > 1 else None

        return title, description

    def _handle_error(self, error: Exception):
        """
        Handle exceptions according to the constitution's error message requirements.

        Args:
            error: The exception to handle
        """
        # Print the error with the expected format from constitution
        error_msg = str(error)
        print(error_msg)


def main():
    """
    Main function to run the CLI application.
    """
    cli = TodoCLI()
    cli.run()


if __name__ == "__main__":
    main()