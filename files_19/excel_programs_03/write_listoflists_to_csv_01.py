# Write data to a CSV file.
import csv

people_list = [
    ['Name', 'Age', 'City'],
    ['Adham', 25, 'Assuit'],
    ['Esam', 30, 'Cairo'],
    ['Shady', 28, 'Mansoura']
]
with open('C:\\MY_FILES\\people.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    print(type(writer)) # csv
    # writer.writerows(people_list)
    for row in people_list:
        writer.writerow(row)







