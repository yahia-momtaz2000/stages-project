# gloal scope
def add_numbers(a, b, c):
    global my_variable
    my_variable = 55
    z = a + b + c
    return z


result = add_numbers(2, 5, 2)
print(result)
print(my_variable)
