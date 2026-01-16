import os

from google.genai import types

from config import MAX_CHARS

schema_get_file_content = types.FunctionDeclaration(
    name="get_file_content",
    description="Get the content of a given file by their path",
    parameters=types.Schema(
        type=types.Type.OBJECT,
        required=["working_directory", "file_path"],
        properties={
            "working_directory": types.Schema(
                type=types.Type.STRING,
                description="The working the directory where file path is a child of",
            ),
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file we can to get the content from",
            ),
        },
    ),
)


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
