# create a function to return sum of even numbers from a list
def get_sum_even(my_list):
    sum_even = 0
    for item in my_list:
        if item % 2 == 0:
            sum_even = sum_even + item
    return sum_even

# call
numbers_list = [14, 5, 2, 6, 8,20]
print(get_sum_even(numbers_list))