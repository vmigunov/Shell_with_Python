# Shell_with_Python

Tutorial Project: Custom Shell powered with Python.
This repository contains a simple shell implementation in Python. 
The project is designed to teach system programming and working with the CLI.

## DEV logs:
08.03.2025 18:05 **Created project, added main.py. Just waiting to user input**  
08.03.2025 18:10 **Added command "help" handler**  
08.03.2025 18:20 **Added command "echo" handler**  
08.03.2025 18:35 **Refactoring.** 
**Key changes:**  
**Command Dictionary:** Added a dictionary (commands) to map command names to their corresponding functions (lambdas). This makes it easy to add new commands without modifying the main logic.  
**Simplified Command Handling:** Each command is associated with a lambda function that executes the desired behavior.  

08.03.2025 19:00 **Changed command exit:**  
- The exit command now accepts an optional argument, the exit code.
- If an argument is passed (e.g. exit 0), the program will exit with that code.  
- If no argument is passed (e.g. just exit), the program will exit with the default code 0.  

