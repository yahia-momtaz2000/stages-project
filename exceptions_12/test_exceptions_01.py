# intro to exceptions handling
import sys
# main program
first_no = input('Enter First No. : ')
second_no = input('Enter Second No. : ')
try:
    first_no = int(first_no)
    second_no = int(second_no)
    result = first_no / second_no
    print('Result = ', result)
    open('c:\\my_files\\employees.txt')
except ValueError as arg:
    print('enter only numbers ', arg)
    sys.exit()
except ZeroDivisionError as arg:
    print('cannot divide by Zero ', arg)
    sys.exit()
except Exception as arg:
    print('Error happened - Contact Administrator', arg)
    sys.exit()
finally:
    print('This statement is the finally - always execute')

print('End of The program')