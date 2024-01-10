# Write a Python program to count Uppercase, Lowercase, special characters and numeric values in a given string.



upper_ctr, lower_ctr, number_ctr, special_ctr = 0, 0, 0, 0
str1 = "@W3Resource.Com"
for i in range(len(str1)):
    print(str1[i])
    if str1[i] >= 'A' and str1[i] <= 'Z':
        upper_ctr += 1
    elif str1[i] >= 'a' and str1[i] <= 'z':
        lower_ctr += 1
    elif str1[i] >= '0' and str1[i] <= '9':
        number_ctr += 1
    else:
        special_ctr += 1

print("Original Substrings:" + str1)
print('\nUpper case characters: ' + str(upper_ctr))
print('Lower case characters: '+ str(lower_ctr))
print('Number case: '+ str(number_ctr))
print('Special case characters: '+str(special_ctr))