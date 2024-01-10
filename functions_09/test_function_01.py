print('it is my main program')


def add_numbers(a, b):
    result = a + b
    return result

def subt_numbers(a, b):
    result = a - b
    return result

def mult_numbers(a, b):
    result = a * b
    return result

def div_numbers(a, b):
    result = a / b
    return result


# call functions
add_result = add_numbers(5, 7)
print('Add result : ', add_result)
print('Add result : ', add_numbers(5, 7))

subt_result = subt_numbers(5, 7)
print('Add result : ', subt_result)
print('subt result : ', subt_numbers(5, 7))