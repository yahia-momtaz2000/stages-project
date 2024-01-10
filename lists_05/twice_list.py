# Multiply each element of the list by 2 and store them again in the list
lst=[ 1, 6, 3, 6, 3, 6 ]
print(lst)

for i in range(len(lst)):
    lst[i] = lst[i] * 2

print(lst)
