#  program to reverse a string
str = "i like this program very much"
print(str)
print(str[::-1])
words_list = str.split(' ')
reversed_list = []
for word in words_list:
    print(word)
    reversed_list.insert(0, word)

# convert the reversed list to string
rev_str = " ".join(reversed_list)
print("Reversed String:")
print(rev_str)