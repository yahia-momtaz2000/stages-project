# Task: Copy a file from one location to another.
import os
import shutil

source_file = 'C:\\MY_FILES\\people.csv'
destination_file = 'C:\\MY_FILES\\new_folder\\people2.csv'
shutil.copyfile(source_file, destination_file)