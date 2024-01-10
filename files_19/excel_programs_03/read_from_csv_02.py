# Task: Read a CSV file and display its contents.
import csv

with open('C:\\MY_FILES\\people.csv', 'r') as file:
    reader = csv.reader(file) # csv reader
    for row in reader:
        print(row)

print('--------------------')
with open('C:\\MY_FILES\\people.csv', 'r') as file:
    reader = csv.reader(file)
    # print(reader.__next__())

    for row in reader:
        print(row)