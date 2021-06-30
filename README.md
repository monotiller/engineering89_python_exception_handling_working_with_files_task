# Working with Files task
The main program can be found in `program.py` and the class files can be found in the `app` directory

## `program.py`
First we will import the classes we want to use from `app/`. We'll go more in detail as to the contents of those files later
```python
from app.checks import FileCheck
from app.read_write import ReadWrite
```
Then we're going to ask the user for the path of the file they want to check:
```python
user_path = str(input("Provide the path to the file you wish to check: "))
```
Then we're going to pass it to the check and read functions that will check if the file is present and then prints its content out to the screen:
```python
FileCheck.error_check(user_path)
ReadWrite.read(user_path)
```
Finally we're going to ask the user to add something to the file and then attempt to append it to the file:
```python
user_input = str(input("Add something to the file: "))
ReadWrite.append(user_path, user_input)
```
## `app/checks.py`
Here is the file that 