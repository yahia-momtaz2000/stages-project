# Read csv and convert into dictionary
# Task: Read a CSV file and convert its contents to a list of dictionaries.

import csv

# with open('C:\\MY_FILES\\people.csv', 'r') as file:
#     reader = csv.DictReader(file)
#     data_list = []
#     for row in reader:
#         data_list.append(row)
#
# print(data_list)

with open('C:\\MY_FILES\\people.csv', 'r') as file:
    reader = csv.DictReader(file)
    print(reader.__next__())
    print(reader.__next__())
    print(reader.__next__())
    data_list = []
    for row in reader:
        data_list.append(row)
# print(data_list)