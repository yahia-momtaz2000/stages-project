# Make Uppercase Half String
str1 = 'ArabRepublicOfEgypt'
# printing original string
print("The original string is : " + str1)

half_idx = len(str1) // 2

final_str = str1[:half_idx].lower() + str1[half_idx:].upper()

# printing result
print("The resultant string : " + final_str)