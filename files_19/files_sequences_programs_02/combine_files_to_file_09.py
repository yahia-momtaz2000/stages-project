# Combine Content from Multiple Files into One File
def combine_files_into_one(output_file, *input_files):
    try:
        with open(output_file, 'w') as output:
            for file_name in input_files:
                with open(file_name, 'r') as file:
                    output.write(file.read())
        print(f"Content from {', '.join(input_files)} combined into '{output_file}' successfully.")
    except FileNotFoundError as e:
        print(f"Error: {e}")

# Example usage:
output_file = 'C:\\MY_FILES\\write_data.txt'
file1 = 'C:\\MY_FILES\\read_data.txt'
file2 = 'C:\\MY_FILES\\read_data_numbers.txt'
combine_files_into_one(output_file, file1, file2)