import os

from config import MAX_CHARS


def get_file_content(working_directory, file_path):
    try:
        path = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(path, file_path))

        if not os.path.isfile(target_file):
            return f"Error: File not found or is not a regular file: '{target_file}'"

        valid_target = os.path.commonpath([path, target_file]) == path
        if not valid_target:
            return f"Error: Cannot read '{file_path}' as it is outside the permitted working directory"

        with open(target_file, "r") as f:
            chunk = f.read(MAX_CHARS)

            if f.read(1):
                chunk += (
                    f"[...File '{target_file}' truncated at {MAX_CHARS} characters]"
                )

            return chunk

    except Exception as e:
        return f"Error: {e}"
