class FileCheck:
    def error_check(file_path):
        try:
            file = open(file_path)
            print("File found")
        except FileNotFoundError as errmsg:
            print(f"File not found: {errmsg}")
        finally:
            print("Thank you for visiting! See you again!")