import os


def get_files_info(working_directory, directory="."):
    try:
        path = os.path.abspath(working_directory)
        target_dir = os.path.normpath(os.path.join(path, directory))
        if not os.path.isdir(target_dir):
            return f"Error: '{target_dir}' is not a directory"
        valid_target = os.path.commonpath([path, target_dir]) == path
        if not valid_target:
            return f"Error: Cannot list '{directory}' as it is outside the permitted working directory"

        output = []
        for dir in os.listdir(target_dir):
            p = "/".join([target_dir, dir])
            size = os.path.getsize(p)
            is_dir = os.path.isdir(p)
            output.append(f"{dir}: file_size={size} bytes, is_dir={is_dir}\n")

        return "".join(output)

    except Exception as e:
        return f"Error: {e}"
