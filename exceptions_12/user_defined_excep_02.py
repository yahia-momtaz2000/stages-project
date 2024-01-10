
try:
    emp_salary = input('Enter Employee Salary : ')
    emp_salary = float(emp_salary)

    if emp_salary < 0:
        raise Exception
except Exception as arg:
    print('Invalid Salary : Cannot be -ve')

print('End of The program')