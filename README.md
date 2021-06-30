# Working with Files task
The main program can be found in `program.py` and the class files can be found in the `app` directory

## `program.py`
```python
from app.checks import FileCheck
from app.read_write import ReadWrite

user_path = str(input("Provide the path to the file you wish to check: "))
FileCheck.error_check(user_path)
ReadWrite.read(user_path)

user_input = str(input("Add something to the list: "))
ReadWrite.append(user_path, user_input)
```