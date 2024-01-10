# One of the string operations can be
# computing the intersection of two strings i.e,
# output the common values that appear in both the strings.
# initializing strings
test_str1 = 'GeeksforGeeks'
test_str2 = 'Codefreaks'

# using naive method to
# get string intersection
res = ""
for i in test_str1:
    if i in test_str2 and not i in res:
        res += i

# printing intersection
print("String intersection is : " + res)