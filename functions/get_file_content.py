import os 

from config import MAX_CHARS

def get_file_content(working_directory, file_path):
    working_dir = os.path.abspath(working_directory)
    abs_file_path = os.path.abspath(os.path.join(working_directory, file_path))

    if not abs_file_path.startswith(working_dir):
        res = f'Error: Cannot read "{file_path}" as it is outside the permitted working directory'
        return res
    if not os.path.isfile(abs_file_path):
        return f'Error: File not found or is not a regular file: "{file_path}"'

    try: 
        with open(abs_file_path, "r") as f:
            file_content_string = f.read(MAX_CHARS)
            if os.path.getsize(abs_file_path) > MAX_CHARS:
                file_content_string += f'[...File "{file_path}" truncated at 1000 characters]'
        return file_content_string
    except Exception as e:
        return f'Error reading file "{file_path}": {e}'


