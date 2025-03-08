import sys


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

    # Function to handle the 'type' command
    def type_command(args):
        if not args:
            print("type: missing argument")
            return
        command = args[0]
        if command in builtin_commands:
            print(f"{command} is a shell builtin")
        else:
            print(f"{command}: not found")

    user_input = input().strip()

    # Split the input into command and arguments
    parts = user_input.split()
    command = parts[0] if parts else ""  # Command is the first word
    args = parts[1:] if len(parts) > 1 else []  # Arguments are the rest

    if command in builtin_commands:
        try:
            builtin_commands[command](args)
        except (ValueError, IndexError) as e:
            print(f"Error: {e}")
    else:
        print(f"{command}: command not found")

    # Recursively call main to keep the terminal running
    main()


if __name__ == "__main__":
    main()
