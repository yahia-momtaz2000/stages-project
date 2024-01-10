student_name = 'Ahmed Omar'
print(student_name)
print(type(student_name))
# ------------------------
print('---------- slicing string ---------------')
print(student_name[0]) # the first letter : A
print(student_name[-1]) # the last letter : r
print(student_name[0:5])  # from index 0 to 4 : Ahmed
print(student_name[:5])  # from index 0 to 4 : Ahmed
print(student_name[:-1]) # from the index 0 to the letter before the last
print(student_name[6:])  # from index 6 to end : Omar
print(student_name[-4:])  # from index -4 to end : Omar
print(student_name[0:8:2]) # from index 0 to 7 - step 2 : Amd0
print(student_name[:]) # from 0 to end - same copy : Ahmed Omar
print(student_name[::-1]) # from 0 to end - step - 1 = print string in reverse order : ramO demhA
# length of a string
print('----------- length of the variable -------------')
print(len(student_name))

# String methods
# upper() lower()
print('--------- upper() lower() ----------')
upper_student_name = student_name.upper()
lower_student_name = student_name.lower()
print(student_name)
print(upper_student_name)
print(lower_student_name)
print(student_name.upper())
print(student_name.lower())

# startWith()
# endWith()
print('-------- startWith() endWith() -------')
student_mobile = '01147041564'
if student_mobile.startswith('012'):
    print('Orange phone')
elif student_mobile.startswith('011'):
    print('Etisalat phone')
elif student_mobile.startswith('010'):
    print('Vodafone phone')
else:
    print('Invalid phone')
# ------------------------
file_path = 'C:\my_files\learn_python.pdf'
if file_path.endswith('PDF'):
    print('it is a book')
else:
    print('it is not a book')

# isalpha() - return true if all the characters in the string is alpha with no spaces
print('----------- isalpha()-----------')
student_name = 'Ahmed'
print(student_name.isalpha())
print(student_mobile.isalpha())

# isDigit() : Returns “True” if all characters in the string are digits
print('------------- isDigit() -----------')
print(student_mobile.isdigit())

# isalnum() method returns True if all the characters are alphanumeric, meaning alphabet letter (a-z) and numbers (0-9).
print('---------- isalnum -----------')
txt = "Company12"
print( txt.isalnum() )

# isupper() -- returns true if all characters are upper
# islower() -- returns true if all characters are lower
print('---------- isupper()   is lower() --------------')
print(upper_student_name)
print(upper_student_name.isupper())
print(upper_student_name.islower())

# index() : Returns the position of the first occurrence of substring in a string
print('-------------- index() --------------')
student_name = 'Ahmad Omar'
print(student_name.index('a'))
print(student_name.lower().index('a'))

# capitalize() : Return a word ( first word ) with its first character capitalized.
print('-------------- capitalize ----------------')
print(student_name)
print(student_name.capitalize())

# title() : convert the first character in each word to uppercase and the remaining characters to lowercase in the
print('-------------- title() ------------------')
student_name = student_name.lower()
print(student_name)
print(student_name.title())

# strip() : like ( trim ) It returns a copy of the string with both leading and
# trailing white spaces removed or custom parameter removed
print('-------- strip() -----------')
student_address = '    addr :  Cairo    '
student_address = student_address.strip('addr :')
print(student_address)
print(student_address)


# replace() : Python returns a copy of the string where occurrences of a substring are replaced with another substring.
print('----------- replace() -------------')
student_information = 'He is Ahmed, Ahmed lives in cairo, Ahmed plays football'
print(student_information)
student_information = student_information.replace('Ahmed','Esam')
print(student_information)

# count() -- returns the number of occurrences of a substring in the given string.
print('----------- count() -------------')
print(student_information.count('Esam'))


# swapcase
print('------------ swapcase ----------------')
stud_info = student_information.swapcase()
print(stud_info)

# find() - Return the lowest indexing a sub string.
# rfind() - find the highest index.
print('-------------- find() -----------------')
student_information = student_information.swapcase()
print(student_information)
print(student_information.index('eSAM'))
print(student_information.find('eSsAM'))
print(student_information.rfind('eSAM'))

# join() -- used to join elements of the sequence separated by a string separator.
print('--------------- join() --------------------')
str = 'hello'
print('$'.join('hello'))
str = '12345'
print('-'.join(str))
my_list = ['ahmed','omar','farouk']
# convert list to string
names = ','.join(my_list)
print(names)


# split() Return a list of the words of the string, If the optional second argument sep is absent or None
print('---------------- split() -------------------')
words = student_information.split(' ')
print(type(words))
print(words)

# loop over the string
print('----------- loop over the string --------------')
print(student_name)
for i in student_name:
    print(i)

# create random strings : Return a random character from a string:
print('----------- random choice ------------')
import random

x = "WELCOME"
print(random.choice(x))

print('------------ del() ------------')
# del the variable
#del student_name