# 2. Write List Elements to a File

my_list = ['Luxor', 'Cairo', 'Alex', 'Cairo']

with open('C:\\MY_FILES\\write_data.txt', 'w') as file:
    for i in range(len(my_list)):
        if i == len(my_list) - 1:
            file.write(my_list[i])
        else:
            file.write(my_list[i] + '\n')
