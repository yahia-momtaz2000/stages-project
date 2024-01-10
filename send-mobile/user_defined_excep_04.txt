import sys

try:
    # main program : user inputs
    emp_salary = float(input('PLease enter emp salary : '))
    print('Emp salary = ', emp_salary)

    if emp_salary < 0:
        raise Exception
except Exception as arg:
    print('Salary cannot be - ve ', arg)
    sys.exit()

print('Continue then end of the program')