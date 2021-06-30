from app.checks import FileCheck # Imports the function that checks if a file is present
from app.read_write import ReadWrite # Imports the functions that are able to read from and write to a file

user_path = str(input("Provide the path to the file you wish to check: ")) # Asks the user the path to the file and assigns it to a variable
FileCheck.error_check(user_path) # Passes the user's path to the `checks.py` file to check if the file is there
ReadWrite.read(user_path) # Passes the user's path to the `read_write.py` file to print the content of the file

user_input = str(input("Add something to the file: ")) # Asks the user to add something to the file and saves it to a variable
ReadWrite.append(user_path, user_input) # Passes the user's path to the `read_write.py` file to append the user's input to the file