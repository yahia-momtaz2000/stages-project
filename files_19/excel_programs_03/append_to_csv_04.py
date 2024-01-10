# Append Data from list of lists to an Existing CSV File
import csv

new_data = [['Emad', 29, 'Luxor'], ['Marwa', 33, 'Cairo']]
#
# with open('C:\\MY_FILES\\people.csv', 'a', newline='') as file:
#     writer = csv.writer(file)
#     for row in new_data:
#         writer.writerow(row)

with open('C:\\MY_FILES\\people.csv', 'a', newline='') as file:
    w = csv.writer(file)
    for row in new_data:
        w.writerow(row)