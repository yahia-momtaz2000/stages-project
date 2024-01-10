# Task: Read data from a CSV file and generate a bar chart.

import csv
import matplotlib.pyplot as plt

with open('C:\\MY_FILES\\people.csv', 'r') as file:
    reader = csv.reader(file)
    reader.__next__() # ignore the header
    x = []
    y = []
    for row in reader:
        print(type(row[0]))
        x.append(row[0]) #Names
        y.append(float(row[1])) # Ages
    plt.bar(x, y)
    plt.xlabel('Name')
    plt.ylabel('Age')
    plt.title('Bar Chart from CSV Data')
    plt.xticks(rotation=45)  # Rotate x-axis labels for readability
    plt.show()