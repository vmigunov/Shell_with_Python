import sys
import os
from shell_utils import type_command, run_external_command, change_directory


def main():
    # Display the command prompt
    sys.stdout.write("$ ")

    # List of supported builtin commands
    builtin_commands = {
        "exit": lambda args: sys.exit(
            int(args[0]) if args else 0
        ),  # Exit with optional code
        "echo": lambda args: print(" ".join(args)),  # Echo command with arguments
        "type": lambda args: type_command(
            args, builtin_commands
        ),  # Type command to check command type
        "pwd": lambda args: print(
            os.getcwd()
        ),  # Pwd command to print current directory
        "cd": lambda args: change_directory(args),  # cd command to change directory
    }

    # Wait for user input
    user_input = input().strip()

    # Split the input into command and arguments
    parts = user_input.split()
    command = parts[0] if parts else ""  # Command is the first word
    args = parts[1:] if len(parts) > 1 else []  # Arguments are the rest

    # Check if the command is supported
    if command in builtin_commands:
        try:
            # Execute the corresponding command with arguments
            builtin_commands[command](args)
        except (ValueError, IndexError) as e:
            # Handle invalid exit codes or other errors
            print(f"Error: {e}")
    else:
        # If the command is not a builtin, run it as an external command
        run_external_command(command, args)

    # Recursively call main to keep the terminal running
    main()


if __name__ == "__main__":
    main()
