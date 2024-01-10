# list only csv files in a directory
import os

def list_csv_files(directory):
    try:
        csv_files = [file for file in os.listdir(directory) if file.lower().endswith('.csv')]
        return csv_files
    except Exception as e:
        return f"Error: {e}"

# Example usage:
directory_path = 'C:\\MY_FILES'
csv_files_list = list_csv_files(directory_path)
print("CSV Files:")
print(csv_files_list)