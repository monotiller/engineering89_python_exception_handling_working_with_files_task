from app.checks import FileCheck
from app.read_write import ReadWrite

user_file = str(input("Provide the path to the file you wish to check: "))
FileCheck.error_check(user_file)

# TODO: Create a write and read function so that we can read from the file
# with open(file, "r") as file