# copy only files with names contains people word (in upper or in lower ) to another directory
import os
import shutil


def copy_files_with_people_in_name(source_dir, destination_dir):
    try:
        # Create the destination directory if it doesn't exist
        if not os.path.exists(destination_dir):
            os.makedirs(destination_dir)

        # List files in the source directory
        files_to_copy = os.listdir(source_dir)

        # Copy files with 'people' in their names (case insensitive)
        for file_name in files_to_copy:
            if 'people' in file_name.lower():
                source_file_path = os.path.join(source_dir, file_name)
                if os.path.isfile(source_file_path):
                    shutil.copy(source_file_path, destination_dir)

        return f"Files with 'people' in their names copied from '{source_dir}' to '{destination_dir}' successfully."
    except Exception as e:
        return f"Error: {e}"


# Example usage:
source_directory = 'C:\\MY_FILES'
destination_directory = 'C:\\MY_FILES\\new_folder'
result = copy_files_with_people_in_name(source_directory, destination_directory)
print(result)
