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

### 08.03.2025 19:30 Extended `type` command
- **Search for Executable Files in PATH:**
        We use the PATH environment variable to get a list of directories to search for executable files.  
        For each directory in PATH, we check if a file with the command name exists and is executable (using os.access(executable_path, os.X_OK)).  
- **Output for Executable Files:** 
        If an executable file is found, the program prints the full path to it in the format <command> is <path>.  
        If the command is not found in either the builtin commands or in PATH, the message <command>: not found is printed.  
- **Handling Missing Argument for type:**
    If the type command is called without arguments, the message type: missing argument is printed.   

### 08.03.2025 19:45 Added support for running external programs with arguments:   
- If the command is not a built-in, the program searches for an executable file in the directories specified in PATH.  
- If the file is found, it is launched using subprocess.run, and arguments are passed to it.  

**The find_executable function:** This function searches for an executable file in the directories in PATH and returns the full path to it if it is found.  
**Error handling:** If an error occurs when launching an external program, the program displays an error message.

### 08.03.2025 20:00 Added `type` command: to print current directory.  
Functions **type_command**, **find_executable** and **run_external_command** are moved to the module **shell_utils.py**  
These functions are responsible for processing the type command, searching for executable files and running external commands.  
