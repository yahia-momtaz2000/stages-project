# delete all files in a directory
import os

def delete_all_files_in_directory(directory):
    try:
        # List all files in the directory
        files_to_delete = os.listdir(directory)

        # Delete each file in the directory
        for file_name in files_to_delete:
            file_path = os.path.join(directory, file_name)
            if os.path.isfile(file_path):
                os.remove(file_path)

        return f"All files in '{directory}' deleted successfully."
    except Exception as e:
        return f"Error: {e}"


# Example usage:
directory_to_clear = 'C:\\MY_FILES\\new_folder'
result = delete_all_files_in_directory(directory_to_clear)
print(result)