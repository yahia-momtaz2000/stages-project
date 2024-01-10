# Calculate the emp monthly net salary, annual salary
# based on his gross salary
# tax will be 10% if the gross salary >= 5000; otherwise no tax

emp_id = 101
emp_name = 'yahia momtaz'  # string
emp_gross_salary = 7000.23

if emp_gross_salary >= 5000:
    tax = 10
else:
    tax = 0

print(tax)
emp_monthly_net_salary = emp_gross_salary - (emp_gross_salary * tax / 100)
print('Monthly net salary = '+str(emp_monthly_net_salary))
annual_net_salary = emp_monthly_net_salary * 12
print('Annual net salary '+str(annual_net_salary))
