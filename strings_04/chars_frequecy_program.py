# find the frequencies of all the characters in
# that string and return a dictionary with key
# as the character and its value as its frequency in the given string
# initializing string
test_str = "GeeksforGeeks"

# using naive method to get count
# of each element in string
all_freq = {}

for i in test_str:
    if i in all_freq:
        all_freq[i] += 1
    else:
        all_freq[i] = 1

# printing result
print("Count of all characters in GeeksforGeeks is :\n "
      + str(all_freq))