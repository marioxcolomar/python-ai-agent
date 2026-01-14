import os


def write_file(working_directory, file_path, content):
    try:
        path = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(path, file_path))

        if os.path.isdir(target_file):
            return f"Error: Cannot write to '{file_path}' as it is a directory"

        valid_target = os.path.commonpath([path, target_file]) == path
        if not valid_target:
            return f"Error: Cannot write to '{file_path}' as it is outside the permitted working directory"

        # Check all paths exist
        os.makedirs(working_directory, exist_ok=True)

        with open(target_file, "w") as f:
            f.write(content)
            return f"Successfully wrote to '{file_path} ({len(content)} characters written)"

    except Exception as e:
        return f"Error: {e}"
