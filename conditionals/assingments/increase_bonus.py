# increase bonus based on salary
emp_salary = 7000
if emp_salary < 5000:
    bonus = 4000
else:
    bonus = 2000

emp_salary = emp_salary + bonus
print(f'bonus = {bonus}')
print(f'After bonus, salary = {emp_salary}')