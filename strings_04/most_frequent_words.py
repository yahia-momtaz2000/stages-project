# Find the k most frequent words from data set in Python
"""
Import Counter class from collections module.
Split the string into list using split(), it will
return the lists of words.
Now pass the list to the instance of Counter class
The function 'most-common()' inside Counter will return
the list of most frequent words from list and its count.
"""
# Python program to find the k most frequent words
# from data set
from collections import Counter # Import Counter class from collections module

data_set = "Welcome to the world of Geeks " \
           "This portal has been created to provide well written well" \
           "thought and well explained solutions for selected questions " \
           "If you like Geeks for Geeks and would like to contribute " \
           "here is your chance You can write article and mail your article " \
           " to contribute at geeksforgeeks org See your article appearing on " \
           "the Geeks for Geeks main page and help thousands of other Geeks. " \
 \
# split() returns list of all the words in the string
split_it = data_set.split()

# Pass the split_it list to instance of Counter class.
counter_object = Counter(split_it)

# most_common() produces k frequently encountered
# input values and their respective counts.
most_occur = counter_object.most_common(4)
# most_occur : list of tuples
print(most_occur)