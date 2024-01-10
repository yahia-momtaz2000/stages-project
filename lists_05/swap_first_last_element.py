# Given a list, write a Python program to swap first and last element of the list.

newList = [12, 35, 9, 56, 24]
size = len(newList)
# Swapping
temp = newList[0]
newList[0] = newList[size - 1]
newList[size - 1] = temp
print(newList)

#------------------ another solution --------------
print('#------------------ another solution --------------')
newList = [12, 35, 9, 56, 24]
print(newList)
first = newList.pop(0)
last = newList.pop(-1)

newList.insert(0, last)
newList.append(first)
print(newList)

