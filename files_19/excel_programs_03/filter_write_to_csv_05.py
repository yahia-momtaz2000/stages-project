# Task: Read a CSV file, filter rows based on a condition, and write the filtered data to a new file.

import csv
input_file = 'C:\\MY_FILES\\people.csv'
output_file = 'C:\\MY_FILES\\people_filterred.csv'

# with open(input_file, 'r') as read_from_file, open(output_file, 'w', newline='') as write_to_file:
#     reader = csv.reader(read_from_file)
#     writer = csv.writer(write_to_file)
#     writer.writerow(['Name', 'Age', 'City'])
#     for row in reader:
#         if row[2] == 'Cairo':
#             writer.writerow(row)

with open(input_file, 'r') as read_from_file, open(output_file, 'w', newline='') as write_to_file:
    reader = csv.reader(read_from_file)
    writer = csv.writer(write_to_file)
    writer.writerow(['Name', 'Age','City'])
    for row in reader:
        if row[2] == 'Cairo':
            row[1] = row[1] + 'edited'
            writer.writerow(row)