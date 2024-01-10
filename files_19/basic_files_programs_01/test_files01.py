# Working of open() Function in Python in read mode
file = open('C:\\MY_FILES\\read_data.txt', 'r')
print('---- Read text from file -----')
print('---- 1st way : ----')
"""
file_text = file.read()
print(file_text)
"""

print('---- 2nd way : ----')
# for item in file:
#     print(item)

print('---- 3rd way : using with ----')
"""
with open('C:\\MY_FILES\\read_data.txt', 'r') as file:
    data = file.read()
print(data)
"""

print('---- 4th way : using with , readlines ----')
with open('C:\\MY_FILES\\read_data.txt', 'r') as file:
    data = file.readlines()
    print(type(data))
    print(data)
    for line in data:
        word = line.split()
        print(word)

# ++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++
# ++++++++++++++++++++++++++++++++
# Writing to A file
"""
print('---- Writing to A file -----')
print('--- 1st way -----')
file = open('C:\\MY_FILES\\write_data.txt', 'w')
file.write('Python is Simple\n')
file.write('Python is OOP\n\n')
file.write('Python was full of libraries')
file.close()
"""
"""
print('--- 2nd way using else write or append | auto close file-----')
with open('C:\\MY_FILES\\write_data.txt', 'a') as f:  # append mode
    f.write('\nJava is Simple\n')
    f.write('Java is OOP\n\n')
    f.write('Java was full of libraries')
"""
print('---- write using writeLines -----')
countries_list = ['Cairo\n', 'Alex\n', 'Assuit\n']

with open('C:\\MY_FILES\\write_data.txt', 'a') as f:
    f.write('\nFirst statement\n')
    # f.writelines(countries_list) # we can use this instead of Loop
    for country in countries_list:
        f.write(country+'\n')
