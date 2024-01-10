# Task: Read a CSV file and extract specific columns to a new CSV file.
import csv

def extract_columns(file_name, columns_to_extract, output_file):
    try:
        with open(file_name, 'r', newline='') as in_file, open(output_file, 'w', newline='') as out_file:
            reader = csv.DictReader(in_file)
            writer = csv.DictWriter(out_file, fieldnames=columns_to_extract)
            writer.writeheader()
            for row in reader:
                selected_data = {col: row[col] for col in columns_to_extract}
                writer.writerow(selected_data)
        print(f"Selected columns written to '{output_file}' successfully.")
    except (FileNotFoundError, KeyError):
        print("Error: Unable to extract columns.")

# Example usage:
input_file = 'C:\\MY_FILES\\people1.csv'
output_file = 'C:\\MY_FILES\\people_cols_extracted.csv'
columns_needed = ['Name', 'Age']  # Columns to extract
extract_columns(input_file, columns_needed, output_file)