# https://www.geeksforgeeks.org/precision-handling-python/
rounded = round(825620.657541235875, 2)

print('{:,.2f}'.format(rounded))

formatted = "{:.3f}".format(825620.657541235875)
print(formatted)

import math

a = 3.7536
print("The integral value of number is : ", end="")
print(math.trunc(a))
print(a)
print(int(a))

# using ceil() to print number after ceiling
a = 3.2536
print(a)
print("The smallest integer greater than number is : ", end="")
print(math.ceil(a))

# using floor() to print number after flooring
a = 3.7536
print(a)
print("The greatest integer smaller than number is : ", end="")
print(math.floor(a))

a = 3.4536








print("The value of number till 2 decimal place(using %) is : ", end="")
print('%.2f' % a)

# using format() to print value till 3 decimal places
print("The value of number till 3 decimal place(using format()) is : ", end="")
print("{0:.3f}".format(a))

# using round() to print value till 2 decimal places
print("The value of number till 2 decimal place(using round()) is : ", end="")
print(round(a, 2))

# using f-string to print value till 2 decimal places
print("The value of number till 2 decimal place(using f-string) is : ", end="")
a= 825620.657541235875
print(f"{a:,.2f}")


