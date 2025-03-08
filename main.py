import sys
import os
import subprocess


def main():
    # Display the command prompt
    sys.stdout.write("$ ")

    # List of supported builtin commands
    builtin_commands = {
        "exit": lambda args: sys.exit(
            int(args[0]) if args else 0
        ),  # Exit with optional code
        "echo": lambda args: print(" ".join(args)),  # Echo command with arguments
        "type": lambda args: type_command(args),  # Type command to check command type
    }

    def type_command(args):
        """Function to handle the 'type' command"""

        if not args:
            print("type: missing argument")
            return
        command = args[0]

        # Check if the command is a builtin
        if command in builtin_commands:
            print(f"{command} is a shell builtin")
            return

        # Search for the command in the PATH directories
        executable_path = find_executable(command)
        if executable_path:
            print(f"{command} is {executable_path}")
        else:
            print(f"{command}: not found")

    def find_executable(command):
        """Function to find an executable in PATH"""

        path_directories = os.getenv("PATH", "").split(os.pathsep)
        for directory in path_directories:
            executable_path = os.path.join(directory, command)
            if os.path.isfile(executable_path) and os.access(executable_path, os.X_OK):
                return executable_path
        return None

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
        # If the command is not a builtin, search for it in PATH
        executable_path = find_executable(command)
        if executable_path:
            try:
                # Run the external program with arguments
                subprocess.run([command] + args)
            except Exception as e:
                print(f"Error: {e}")
        else:
            print(f"{command}: command not found")

    # Recursively call main to keep the terminal running
    main()


if __name__ == "__main__":
    main()
