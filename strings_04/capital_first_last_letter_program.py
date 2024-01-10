# Write a Python program to capitalize the first and last letters of each word in a given string.

str1 = "python exercises practice solution"
str1 = result = str1.title() # capitalize the first letter
result = ""
for word in str1.split():
    # word[:-1] : from the beginning to the letter before the last
    # word[-1] : the last letter
    result += word[:-1] + word[-1].upper() + " "
print( result[:-1] )
