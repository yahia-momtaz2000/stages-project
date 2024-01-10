### Chaining comparison operators in Python
x = 15
print( 10 < x < 13) # Output: False
#-------------------------------
z = 30
print(z + 20 > 20 <= 20) # Output: True
#-------------------------------
x = 10
result = 5 < x < 15
print(result)  # Output: True
#-------------------------------
y = 20
result = 10 < y <= 20
print(result)  # Output: True
#-------------------------------
z = 25
result = 20 == z < 30
print(result)  # Output: False
#-------------------------------
a = 7
result = 5 <= a != 10
print(result)  # Output: True
#-------------------------------
b = 3
result = 1 < b < 5 < 10
print(result)  # Output: True