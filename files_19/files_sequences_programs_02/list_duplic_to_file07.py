# 8. Remove Duplicates from a List and Write Unique Elements to a File
def remove_duplicates_write_file(filename, input_list):
    try:
        unique_list = list(set(input_list))
        with open(filename, 'w') as file:
            for item in unique_list:
                file.write(str(item) + '\n')
        print(f"Unique elements written to '{filename}' successfully.")
    except IOError:
        print(f"Unable to write to file '{filename}'.")

# Example usage:
output_file = 'C:\\MY_FILES\\write_data.txt'
my_list = [1, 2, 2, 3, 4, 4, 5]
remove_duplicates_write_file(output_file, my_list)