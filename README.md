# Shell_with_Python

Tutorial Project: Custom Shell powered with Python.
This repository contains a simple shell implementation in Python. 
The project is designed to teach system programming and working with the CLI.

## DEV logs:
08.03.2025 18:05 **Created project, added main.py. Just waiting to user input**  
08.03.2025 18:10 **Added command "exit"**  
08.03.2025 18:20 **Added command "echo"**  
08.03.2025 18:35 **Refactoring.** 
**Key changes:**  
**Command Dictionary:** Added a dictionary (commands) to map command names to their corresponding functions (lambdas). This makes it easy to add new commands without modifying the main logic.  
**Simplified Command Handling:** Each command is associated with a lambda function that executes the desired behavior.  

08.03.2025 19:00 **Changed command exit:**  
- The exit command now accepts an optional argument, the exit code.
- If an argument is passed (e.g. exit 0), the program will exit with that code.  
- If no argument is passed (e.g. just exit), the program will exit with the default code 0.  

08.03.2025 19:15 **Added command "type":**
- The type command checks whether the command is a builtin or not recognized.  
- If the command is a builtin (such as echo or exit), a message like echo is a shell builtin is printed.  
- If the command is not recognized, a message like invalid_command: not found is printed.  

08.03.2025 19:30 **Extended command "type":**  
- **Search for Executable Files in PATH:**
        We use the PATH environment variable to get a list of directories to search for executable files.  
        For each directory in PATH, we check if a file with the command name exists and is executable (using os.access(executable_path, os.X_OK)).  
- **Output for Executable Files:** 
        If an executable file is found, the program prints the full path to it in the format <command> is <path>.  
        If the command is not found in either the builtin commands or in PATH, the message <command>: not found is printed.  
- **Handling Missing Argument for type:**
    If the type command is called without arguments, the message type: missing argument is printed.   

08.03.2025 19:45 **Added support for running external programs with arguments:**  
- If the command is not a built-in, the program searches for an executable file in the directories specified in PATH.  
- If the file is found, it is launched using subprocess.run, and arguments are passed to it.  

**The find_executable function:** This function searches for an executable file in the directories in PATH and returns the full path to it if it is found.  
**Error handling:** If an error occurs when launching an external program, the program displays an error message.

08.03.2025 20:00 **Added command "pwd":** to print current directory
Functions **type_command**, **find_executable** and **run_external_command** moved to the module **shell_utils.py**  
These functions are responsible for processing the type command, searching for executable files and running external commands.  
