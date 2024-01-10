# Create a function to check for a number found in a list or not - return its index or -1
def check_number_found(my_list, number):
    if number in my_list:
        return my_list.index(number)
    else:
        return -1

# calling
numbers_list = [14, 5, 2, 6, 8, 20]
a = 1
index = check_number_found(numbers_list, a)
print(index)