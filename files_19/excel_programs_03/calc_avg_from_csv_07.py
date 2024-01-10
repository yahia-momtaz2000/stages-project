# Task: Read a CSV file and calculate the average value from a specific column.
import csv
def calculate_average(file_name, column_index):
    try:
        with open(file_name, 'r', newline='') as file:
            reader = csv.reader(file)
            next(reader)  # Skip header if present
            values = [float(row[column_index]) for row in reader]
            avg = sum(values) / len(values)
            return avg
    except (FileNotFoundError, IndexError, ValueError, ZeroDivisionError):
        print("Error: Unable to calculate average.")

# Example usage:
input_file = 'C:\\MY_FILES\\people.csv'
column_index_to_avg = 1  # Column index for values (e.g., 1 for column 2)
result = calculate_average(input_file, column_index_to_avg)
print(f"Average from column {column_index_to_avg}: {result}")