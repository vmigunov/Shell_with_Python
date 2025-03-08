import os
import subprocess


def type_command(args, builtin_commands):
    """Handle the 'type' command."""
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
    """Find an executable in the PATH directories."""
    path_directories = os.getenv("PATH", "").split(os.pathsep)
    for directory in path_directories:
        executable_path = os.path.join(directory, command)
        if os.path.isfile(executable_path) and os.access(executable_path, os.X_OK):
            return executable_path
    return None


def run_external_command(command, args):
    """Run an external command with arguments."""
    executable_path = find_executable(command)
    if executable_path:
        try:
            # Run the external program with arguments
            subprocess.run([command] + args)
        except Exception as e:
            print(f"Error: {e}")
    else:
        print(f"{command}: command not found")
