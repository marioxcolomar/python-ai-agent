import os
import subprocess

from google.genai import types

schema_run_python_file = types.FunctionDeclaration(
    name="run_python_file",
    description="Execute a python file",
    parameters=types.Schema(
        required=["working_directory", "file_path"],
        type=types.Type.OBJECT,
        properties={
            "working_directory": types.Schema(
                type=types.Type.STRING,
                description="The working the directory where file path is a child of",
            ),
            "file_path": types.Schema(
                type=types.Type.STRING,
                description="Path to the file we can to get the content from",
            ),
            "args": types.Schema(
                type=types.Type.STRING,
                description="Arguments to be added when running the command",
            ),
        },
    ),
)


def run_python_file(working_directory, file_path, args=None):
    try:
        path = os.path.abspath(working_directory)
        target_file = os.path.normpath(os.path.join(path, file_path))

        valid_target = os.path.commonpath([path, target_file]) == path
        if not valid_target:
            return f'Error: Cannot execute "{file_path}" as it is outside the permitted working directory'

        if not os.path.isfile(target_file):
            return f'Error: "{file_path}" does not exist or is not a regular file'

        if not file_path.endswith(".py"):
            return f'Error: "{file_path}" is not a Python file'

        command = ["python", target_file]

        if args:
            command.extend(args)

        res = subprocess.run(command, capture_output=True, text=True, timeout=30)
        print(f"response: {res.returncode}")
        if res.returncode != 0:
            return f"Process exited with code {res.returncode}"

        if res.stderr == "" and res.stdout == "":
            print(f"err: {res.stderr}, out: {res.stdout}")
            return "No output produced"

        if res.stdout:
            return f"STDOUT: {res.stdout}"

        if res.stderr:
            return f"STDERR: {res.stderr}"

    except Exception as e:
        return f"Error: executing Python file: {e}"
