# Shell_with_Python

## Tutorial Project: Custom Shell powered by Python
This repository contains a simple shell implementation in Python.  
The project is designed to teach system programming and working with the CLI.

## DEV logs:

### 08.03.2025 18:05 - Created project, added `main.py`
- Waiting for user input.

### 08.03.2025 18:10 - Added the `exit` command

### 08.03.2025 18:20 - Added the `echo` command

### 08.03.2025 18:35 - Refactored code
**Key changes:**  
- **Command Dictionary:** Added a dictionary (`commands`) to map command names to their corresponding functions (lambdas).  
  This makes it easy to add new commands without modifying the main logic.  
- **Simplified Command Handling:** Each command is associated with a lambda function that executes the desired behavior.  

### 08.03.2025 19:00 - Updated the `exit` command
- The `exit` command now accepts an optional argument for the exit code.
- If an argument is passed (e.g., `exit 0`), the program exits with that code.
- If no argument is passed (e.g., just `exit`), the program exits with the default code `0`.

### 08.03.2025 19:15 - Added the `type` command
- The `type` command checks whether a command is built-in or unrecognized.
- If the command is a built-in (such as `echo` or `exit`), a message like:  
  ```shell
  echo is a shell builtin
