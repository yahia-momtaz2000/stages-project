# Python: Takes a list of words and returns the length of the longest one

words_list = (["PHP", "Exercises", "Backend"])
word_len = []
for n in words_list:
    word_len.append((len(n), n))
word_len.sort()
print("\nLongest word: ",word_len[-1][0])
print("Length of the longest word: ",word_len[-1][1])