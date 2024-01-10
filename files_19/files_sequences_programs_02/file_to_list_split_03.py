# 3. Read File, Split Content, and Create a List of Words

with open('C:\\MY_FILES\\read_data.txt', 'r') as file:
    content = file.read()
    words_list = content.split()
    print(words_list)