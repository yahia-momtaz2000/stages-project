# Ways to remove numeric digits from given string
# initialising string
str1 = "Geeks123for127geeks"

# printing initial ini_string
print("initial string : ", str1)

# using join and isalpha
# to remove numeric digits from string
str2 = "".join(x for x in str1 if x.isalpha())

# printing result
print("final string : ", str2)