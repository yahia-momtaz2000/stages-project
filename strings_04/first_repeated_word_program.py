# find the first repeated word in a string in Python using Dictionary
"""
Input : "Ravi had been saying that he had been there"
Output : had

Input : "Ravi had been saying that"
Output : No Repetition

Input : "he had had he"
Output : he
"""
word_freq = {} # dictionary
input_string = "Ravi had been saying that he had been there"

words = input_string.split()
for word in words:
    if word not in word_freq:
        word_freq[word] = 1
    else:
        word_freq[word] += 1
        break

if word_freq[word] > 1:
   print(word)
else:
   print('No Repetition')
