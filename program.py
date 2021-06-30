from app.checks import FileCheck
from app.read_write import ReadWrite

user_path = str(input("Provide the path to the file you wish to check: "))
FileCheck.error_check(user_path)
ReadWrite.read(user_path)

user_input = str(input("Add something to the list: "))
ReadWrite.append(user_path, user_input)