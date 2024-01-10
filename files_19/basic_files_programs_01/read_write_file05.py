# Open the input file in read mode
with open('C:\\MY_FILES\\read_data.txt', 'r') as file:
    content = file.read()

# Open or create the output file in write mode and write the content
with open('C:\\MY_FILES\\write_data.txt', 'w') as file:
    file.write(content)