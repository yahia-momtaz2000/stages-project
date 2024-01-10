# The task is to generate another list,
# which contains only the duplicate elements
lis = [1, 2, 1, 2, 3, 4, 5, 1, 1, 2, 5, 6, 7, 8, 9, 9]

uniqueList = []
duplicateList = []

for item in lis:
    if item not in uniqueList:
        uniqueList.append(item)
    elif item not in duplicateList:
        duplicateList.append(item)
print(uniqueList)
print(duplicateList)