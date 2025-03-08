import sys


def main():

    sys.stdwrite("$ ")
    commands = ["exit", "echo"]

    user_input = input().strip()

    # Splitting command and args
    parts = user_input.split(maxsplit=1)
    command = parts[0]

    if command in commands:
        if command == "exit":
            sys.exit(0)
        elif command == "echo":
            if len(parts) > 1:
                # Print args
                print(parts[1])
            else:
                print()
    else:
        print(f"{command}: command not found")

    # Recursively call main to keep the terminal running
    main()


if __name__ == "__main__":
    main()
