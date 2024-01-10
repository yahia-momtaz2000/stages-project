import math

# using print function and its parameters
emp_id = 100
emp_name = 'Ahmed Omar'
emp_salary = 85955.758921

print('-----  printing with concatenation in 1 parameter ---')
print('Emp whose id = '+str(emp_id)+', his name is '+emp_name +
      '\n\ttakes salary = '+str(emp_salary))

print('----  Printing using multi parameters not concatenation -----')
print('Emp whose id = ', emp_id, ', his name is '+emp_name,', takes salary = ', emp_salary)

print('----- Printing using sep between values -----')
print(14, 12, 'ahmed', 'omar', 500, sep=' - ')

print('------ Printing using end parameter ---------')
my_list = [15, 20, 40, 44, 30, 60 ]
for item in my_list:
      print(item, end=' ')

print('\n------ Printing using placeHolders %s   %d    %f -------')
print('Emp whose id is %d, his name is %s, takes salary =%.2f' %(emp_id, emp_name, emp_salary))

print('--------------- Printing using placeholders using format function and format money ------------')
print('Emp whose id is {:d}, his name is {:s}, takes salary = {:,.2f}'.format(emp_id, emp_name, emp_salary))

print('------ using F-String function ---------')
print(f'Emp whose id is {emp_id:d}, his name is {emp_name:s}, takes salary = {emp_salary:,.2f}')


print(f'emp salary = {emp_salary}')
# print('Emp salary using placeholder = %.2f' %(emp_salary))  # cannot directly put , separator
# print('Emp salary using format = {:,.2f}'.format(emp_salary))
# print(f'Emp salary using f-string = {emp_salary:,.2f}')
print('----- Numbers Functions --------')
emp_salary = 85955.758921
print(f'Emp salary using round = {round(emp_salary, 2)}')
print(f'Emp salary using trunc = {math.trunc(emp_salary)}')
print(f'Emp salary using ceil = {math.ceil(emp_salary)}')
print(f'Emp salary using floor = {math.floor(emp_salary)}')