class ReadWrite:
    def read(file_path):
        file = open(file_path, 'r')
        print(f"Contents of {file_path}:\n\n{file.read()}")

    def append(file_path, file_write):
        file = open(file_path, "a")
        file.write(f"\n{file_write}")
        file = open(file_path, "r")
        print(f"{file_write} has been added to the {file_path}. It now reads as:\n\n{file.read()}")