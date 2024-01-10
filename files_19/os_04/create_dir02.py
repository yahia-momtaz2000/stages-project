# Task: Create a new directory if it does not exist.
import os

if not os.path.exists('C:\\MY_FILES\\new_folder'):
    os.makedirs('C:\\MY_FILES\\new_folder')
