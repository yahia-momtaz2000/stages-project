# Task: Convert a List of dictionaries into a CSV file.

import csv

data_dict_list = [
    {'Name': 'Emad', 'Age': 25},
    {'Name': 'Marwa', 'Age': 30},
    {'Name': 'Asmaa', 'Age': 28}
]
# with open('C:\\MY_FILES\\people_by_dict.csv', 'w', newline='') as file:
#     writer = csv.DictWriter(file, fieldnames=data_dict[0].keys())
#     writer.writeheader()
#     writer.writerows(data_dict)

with open('C:\\MY_FILES\\people_by_dict.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=data_dict_list[0].keys())
    writer.writeheader()
    for line in data_dict_list:
        writer.writerow(line)