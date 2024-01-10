# Swap commas and dots in a String
str1 = 'He is Ahmed, Ahmed lives in cairo, Ahmed plays football.'
print(str1)
str1 = str1.replace(', ', '* ')
str1 = str1.replace('.', ', ')
str1 = str1.replace('*', '.')
print(str1)

