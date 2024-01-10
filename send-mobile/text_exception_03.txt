try:
    # main program : get inputs from the user
    first_no = int( input('Enter your first no : ') )
    second_no = int( input('Enter your second no : ') )
    result = first_no / second_no
    print('Result = ', result)

    open('c:\\my_files\\egypt.txt')
except ValueError as arg:
    print('Only numbers are valid ', arg)
except ZeroDivisionError as arg:
    print('Divisbile By Zero ', arg)
# except Exception as arg:
#     print('Error happen - please call administrator')
finally:
    print('This is the finally statement - always run')

print('End of the program')