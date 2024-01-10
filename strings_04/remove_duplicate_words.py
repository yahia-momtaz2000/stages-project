# -remove-duplicates-words-given-sentence/
sentence = "Python is great great great Php is also good"
words_list = sentence.split(" ")
final_list = []
for item in words_list:
    if item not in final_list:
        final_list.append(item)
# convert from list to string
final_str = " ".join(final_list)
print(final_str)

