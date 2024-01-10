# Write a Python program that accepts a comma-separated sequence of words as input
# and prints the distinct words in sorted form (alphanumerically)

items = input("Input comma separated sequence of words")
# example : red,black,red,green,yellow,red
words = [word for word in items.split(",")]
print(type(words))
print(",".join(sorted(list(set(words)))))