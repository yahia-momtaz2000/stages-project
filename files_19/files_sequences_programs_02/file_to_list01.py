# 1. Read File and Create a List of Lines
lines_list = []
with open('C:\\MY_FILES\\read_data.txt', 'r') as file:
    lines = file.readlines()
    for line in lines:
        # remove spaces, tabs, new lines
        lines_list.append(line.strip())
print(lines_list)