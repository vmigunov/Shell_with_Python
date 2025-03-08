import sys


def main():
    while True:
        sys.stdwrite("$ ")
        commands = ["exit"]

        command = input().strip()

        if command in commands:
            if command == "exit":
                sys.exit(0)
        else:
            print(f"{command}: command not found")


if __name__ == "__main__":
    main()
