# program to move file from dir to another
import os
import shutil

source_file = 'C:\\MY_FILES\\people_filterred.csv'
destination_file = 'C:\\MY_FILES\\new_folder\\people_filterred.csv'
shutil.move(source_file, destination_file)
