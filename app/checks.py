class FileCheck:
    def error_check(file_path): # Passing variable `file_path` in to the function from `user_path`
        try:
            file = open(file_path) # Opening the file the user has defined
            print("File found") # Print a success message
        except FileNotFoundError as errmsg: # If above has the error `FileNotFoundError` then do the following as an `errmsg`
            print(f"File not found: {errmsg}\nThe program will now quit") # Prints a more readable error message
            exit() # Force quits since `program.py` would just continue on to the next part and cause another error