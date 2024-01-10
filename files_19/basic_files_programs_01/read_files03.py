file = open('C:\\MY_FILES\\read_data.txt', 'r')
print(type(file))
print('---- Read text from file -----')
print('---- 1st way : REad Content as string ----')
file_text = file.read()
print(file_text)
print(type(file_text))
file.close()


print('---- 2nd way : Loop over File Handler using for each ----')
file = open('C:\\MY_FILES\\read_data.txt', 'r')
for item in file:
    print(item)
    print(type(item))
file.close()


print('---- 3rd way : using with ----')

with open('C:\\MY_FILES\\read_data.txt', 'r') as file:
    data = file.read()
print(data)
print(type(data))