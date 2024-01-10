"""
Primary conditions for password validation:
Minimum 8 characters.
At least one alphabet should be of Lower Case [a-z]
At least one alphabet should be of Upper Case [A-Z]
At least 1 number or digit between [0-9].
At least 1 character from [ _ or @ or $ ].
"""
count_lower, count_upper, count_special, count_digits = 0, 0, 0, 0
str = "sr@m@_f0rtu9e$._2023"
if (len(str) >= 8):
    for letter in str:
        # counting lowercase alphabets
        if letter.islower():
            count_lower += 1
            # counting uppercase alphabets
        elif letter.isupper():
            count_upper += 1
            # counting digits
        elif letter.isdigit():
            count_digits += 1
            # counting the mentioned special characters
        elif not letter.isalnum():
            count_special += 1
if (count_lower >= 1 and
        count_upper >= 1 and
        count_special >= 1 and
        count_digits >= 1):
    print("Valid Password")
else:
    print("Invalid Password")