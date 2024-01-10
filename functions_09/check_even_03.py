# Create a function to check a number if it is even number:
def check_even(a):
    if a % 2 == 0:
        return True
    else:
        return False

# call
number = 8
is_even = check_even(number)
print(is_even)

if is_even == True:
    print('it is even number')
else:
    print('it is odd number')
