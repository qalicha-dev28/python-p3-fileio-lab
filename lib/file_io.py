# lib/file_io.py

def write_file(file_name, file_content):
    """
    Writes content to a .txt file with the given file name.
    
    Args:
        file_name (str): The name/path of the file (without .txt extension)
        file_content (str): The content to write to the file
    """
    full_file_name = f"{file_name}.txt"
    with open(full_file_name, 'w') as file:
        file.write(file_content)

def append_file(file_name, append_content):
    """
    Appends content to an existing .txt file with the given file name.
    
    Args:
        file_name (str): The name/path of the file (without .txt extension)
        append_content (str): The content to append to the file
    """
    full_file_name = f"{file_name}.txt"
    with open(full_file_name, 'a') as file:
        file.write(append_content)

def read_file(file_name):
    """
    Reads and returns the content of a .txt file with the given file name.
    
    Args:
        file_name (str): The name/path of the file (without .txt extension)
    
    Returns:
        str: The content of the file
    """
    full_file_name = f"{file_name}.txt"
    with open(full_file_name, 'r') as file:
        return file.read()