# Remove all duplicates from a given string in Python
string="geeksforgeeks"
p=""
for char in string:
    if char not in p:
        p=p+char
print(p)
k=list("geeksforgeeks")