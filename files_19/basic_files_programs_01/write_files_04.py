print('---- Writing to A file -----')
print('--- 1st way -----')
file = open('C:\\MY_FILES\\write_data.txt', 'w')
file.write('Let''s Learn Python\n')
file.write('Python is Simple\n\n')
file.write('Python is full of libraries')
file.close()


print('2nd way : +++++++++++++++++++++++++++++++++')
with open('C:\\MY_FILES\\write_data.txt', 'a') as f:  # append mode
    f.write('\nLet''s Learn Python\n')
    f.write('Python is Simple\n\n')
    f.write('Python is full of libraries')