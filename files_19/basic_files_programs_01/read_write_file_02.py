# Read from input file and write to output file
def copy_file(input_file, output_file):
    try:
        # Open the input file in read mode
        with open(input_file, 'r') as file:
            content = file.read()

        # Open or create the output file in write mode and write the content
        with open(output_file, 'w') as file:
            file.write(content)

        print(f"Content from '{input_file}' has been copied to '{output_file}' successfully.")

    except FileNotFoundError:
        print("File not found. Please provide valid file names.")


# Example usage:
input_filename = 'C:\\MY_FILES\\read_data.txt'  # Replace 'input.txt' with the name of your input file
output_filename = 'C:\\MY_FILES\\write_data.txt'  # Replace 'output.txt' with the name of your output file

copy_file(input_filename, output_filename)