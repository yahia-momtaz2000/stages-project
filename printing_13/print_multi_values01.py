# printing multi values
for i in range(1, 10):
    print(i, end=' ')

print('\nPrinting Multi values')
first_number = 7
second_number = 9
result = first_number + second_number
print('--------- using normal printing with multi parameters --------------')
print(first_number, second_number, result, sep=', ' )
print('The Value of Adding', first_number, 'and', second_number,' = ', result)
print('----------- print with format function ------------')
print('The value of Adding {} and {} = {}'.format(first_number, second_number, result))

print('The valueof pi is: %1.5f' %3.141592)
print('The valueof pi is: {0:1.5f}'.format(3.141592))

print('------------------- F String method --------------------')
# https://www.geeksforgeeks.org/python-string-format-method/
# Learn Python in Arabic #017 - Strings Formatting Old Way
# https://www.youtube.com/watch?v=m_OUIywn_XE&list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs&index=17
# Learn Python in Arabic #018 - Strings Formatting New Ways
# https://www.youtube.com/watch?v=nn4qN90A7X4&list=PLDoPjvoNmBAyE_gei5d18qkfIe-Z8mocs&index=18