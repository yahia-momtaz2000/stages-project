# 8. Read File, Convert to Upper Case, and Write Content to Another File
with open('C:\\MY_FILES\\read_data.txt', 'r') as file:
    content = file.read().upper()
with open('C:\\MY_FILES\\write_data.txt', 'w') as file:
    file.write(content)