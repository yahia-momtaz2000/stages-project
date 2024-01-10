# Copy Multi files to another directory
import os
import shutil


def copy_files_to_directory(source_dir, destination_dir):
    try:
        # Create the destination directory if it doesn't exist
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)

        # List files in the source directory
        files_to_copy = os.listdir(source_dir)

        # Copy each file from source to destination
        for file_name in files_to_copy:
            source_file_path = os.path.join(source_dir, file_name)
            if os.path.isfile(source_file_path):
                shutil.copy(source_file_path, destination_dir)

        return f"Files copied from '{source_dir}' to '{destination_dir}' successfully."
    except Exception as e:
        return f"Error: {e}"


# Example usage:
source_directory = 'C:\\MY_FILES'
destination_directory = 'C:\\MY_FILES\\new_folder'
result = copy_files_to_directory(source_directory, destination_directory)
print(result)