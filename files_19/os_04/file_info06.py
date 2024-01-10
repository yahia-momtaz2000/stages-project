# Task: Retrieve information about a file.
import os
from datetime import datetime


def get_file_info(file_path):
    try:
        modification_time = os.path.getmtime(file_path)
        mod_time_formatted = datetime.fromtimestamp(modification_time).strftime('%d-%m-%Y %H:%M:%S')
        info = {
            'File Name': os.path.basename(file_path),
            'Size (bytes)': os.path.getsize(file_path),
            'Last Modified': mod_time_formatted
        }
        return info
    except FileNotFoundError:
        return f"File '{file_path}' not found."

# Example usage:
file_to_check = 'C:\\MY_FILES\\new_folder\\people_filterred.csv'
file_info = get_file_info(file_to_check)
print(file_info)