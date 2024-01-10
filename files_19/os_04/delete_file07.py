# Task: Delete a file if it exists.
import os
from send2trash import send2trash


file_to_delete = 'C:\\MY_FILES\\new_folder\\people_filterred.csv'
if os.path.exists(file_to_delete):
    # os.remove(file_path) # delete without recyclebin
    send2trash(file_to_delete)  # put in recyclebin