import os

from google.genai import types

schema_write_file = types.FunctionDeclaration(
    name="write_file",
    description="Write or overwrite a file",
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
            "content": types.Schema(
                type=types.Type.STRING,
                description="Content to write to file",
            ),
        },
    ),
)


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
