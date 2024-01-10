# Sort words of sentence in ascending order

# Splitting the Sentence into words
sentence = "to learn programming refer geeksforgeeks"
print(sentence)
words = sentence.split(" ")
print(type(words))

# Sorting the words list in asc
words.sort()

# Making new Sentence by
# joining the sorted words
new_sentence = " ".join(words)

# Print the sortedSentence
print(new_sentence)