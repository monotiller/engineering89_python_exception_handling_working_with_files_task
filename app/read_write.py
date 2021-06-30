from app.checks import FileCheck # Importing FileCheck to handle errors better

class ReadWrite:
    def read(file_path): # Passing variable `file_path` in to the function from `user_path`
        file = open(file_path, 'r') # Opening the file the user has defined in read mode and attributing it to a variable valled `file`
        print(f"Contents of {file_path}:\n\n{file.read()}") # Printing out the contents of the file that was opened

    def append(file_path, file_write): # Passing both the `file_path` from before and the `file_write` which is defined as `user_input in `program.py`
        file = open(file_path, "a") # Opening the file the user has defined in append mode ready for items to be added to the file
        file.write(f"\n{file_write}") # Passes in what the user had typed in and appends it to the file
        file = open(file_path, "r") # Opening the file the user has defined in read mode and attributing it to a variable valled `file`
        print(f"{file_write} has been added to the {file_path}. It now reads as:\n\n{file.read()}") # Printing out the contents of the file that was opened