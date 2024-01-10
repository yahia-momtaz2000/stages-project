# example : Variable length keyword argument
# *args in Python (Non-Keyword Arguments)
def sum_numbers(*args):
    sum = 0
    for item in args:
        sum = sum + item
    return sum


print(sum_numbers(4, 5, 2, 1, 20))