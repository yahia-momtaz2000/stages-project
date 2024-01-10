# Task: Merge multiple CSV files into a single CSV file.

import csv

def merge_csv_files(output_file, *input_files):
    try:
        with open(output_file, 'w', newline='') as out_file:
            writer = csv.writer(out_file)
            for file_name in input_files:
                with open(file_name, 'r', newline='') as in_file:
                    reader = csv.reader(in_file)
                    for row in reader:
                        writer.writerow(row)
        print(f"Merged CSV files into '{output_file}' successfully.")
    except FileNotFoundError:
        print("One or more input files not found.")

# Example usage:
output_file = 'C:\\MY_FILES\\people.csv'
file1 = 'C:\\MY_FILES\\people1.csv'
file2 = 'C:\\MY_FILES\\people2.csv'
merge_csv_files(output_file, file1, file2)