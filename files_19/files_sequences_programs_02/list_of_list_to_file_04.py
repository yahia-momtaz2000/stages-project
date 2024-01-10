
# Write List of Lists to a File
def write_list_of_lists_to_file(filename, list_of_lists):
    try:
        with open(filename, 'w') as file:
            for inner_list in list_of_lists:
                file.write(' '.join(map(str, inner_list)) + '\n')
        print(f"List of lists written to '{filename}' successfully.")
    except IOError:
        print(f"Unable to write to file '{filename}'.")

# Example usage:
output_file = 'C:\\MY_FILES\\write_data.txt'
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
write_list_of_lists_to_file(output_file, list_of_lists)