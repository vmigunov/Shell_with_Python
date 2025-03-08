import sys


def main():
    # Display the command prompt
    sys.stdout.write("$ ")

    # List of supported commands
    commands = {
        "exit": lambda args: sys.exit(
            int(args[0]) if args else 0
        ),  # Exit with optional code
        "echo": lambda args: print(" ".join(args)),  # Echo command with arguments
    }

    user_input = input().strip()

    # Split the input into command and arguments
    parts = user_input.split()
    command = parts[0] if parts else ""  # Command is the first word
    args = parts[1:] if len(parts) > 1 else []  # Arguments are the rest

    if command in commands:
        try:
            commands[command](args)
        except (ValueError, IndexError) as e:
            print(f"Error: {e}")
    else:
        print(f"{command}: command not found")

    # Recursively call main to keep the terminal running
    main()


if __name__ == "__main__":
    main()
