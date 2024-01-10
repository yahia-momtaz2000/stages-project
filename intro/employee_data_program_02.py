employee_id = 101               # int
employee_name = 'Ahmed Eissa'   # string
employee_salary = 7000.55       # float
employee_email = 'ahmed.eissa@gmail.com'    # string
employee_address = 'Cairo - Nasr city'      # string

print(employee_name + ' lives at '+employee_address)
print(employee_name +' takes salary  '+str(employee_salary)) # convert to string
print(employee_name +' with id '+str(employee_id) )  # convert to string

# employee salary with no decimal > Convert to int
no_decimal_salary = int(employee_salary)  # convert to int
print(employee_name + ' takes salary = '+ str(no_decimal_salary) )  # convert to string