import os

def get_files_info(working_directory, directory="."):
    working_dir = os.path.abspath(working_directory)
    joined_dir = os.path.abspath(os.path.join(working_directory, directory))

    curr_dir_str = "current" if directory == "." else f"'{directory}'"

    res = ""
    res += f"Result for {curr_dir_str} directory:\n"

    if not joined_dir.startswith(working_dir):
        res += f'\tError: Cannot list "{directory}" as it is outside the permitted working directory'
        return res

    if not os.path.isdir(joined_dir):
        res += f'\tError: "{directory}" is not a directory'
        return res

    try: 
        files_info = []
        for filename in os.listdir(joined_dir):
            file_path = os.path.join(joined_dir, filename)
            file_size = 0
            is_dir = os.path.isdir(file_path)
            file_size = os.path.getsize(file_path)
            files_info.append(
                f'- {filename}: file_size= {file_size} bytes, is_dir={is_dir}'
            )
        return res + "\n".join(files_info)
    except Exception as e:
        return f"Error listing files: {e}"


