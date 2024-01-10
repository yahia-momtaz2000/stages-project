# 6. Append List of Strings to an Existing File

words_list = ['Hello', 'World', 'Python']

with open('C:\\MY_FILES\\write_data.txt', 'a') as file:
    file.write('\n')
    for i in range(len(words_list)):
        if i == len(words_list) - 1:
            file.write(words_list[i])
        else:
            file.write(words_list[i] + '\n')