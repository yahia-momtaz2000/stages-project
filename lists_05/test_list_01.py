"""
Python Lists are just like dynamically sized arrays,
declared in other languages (vector in C++ and ArrayList in Java).
In simple language, a list is a collection of things,
enclosed in [ ] and separated by commas.
"""
# Creating a List of numbers
numbers_list = [15, 16, 20, 3, 15, 20]
print('----------- printing numbers list -----------')
print('numbers list = '+str(numbers_list))

# Creating a List of strings
strings_list = ['python', 'java','oracle']
print('----------- printing string list -----------')
print(strings_list)

# Creating a mixed List of numbers, strings
mixed_list = ['ahmed', 'omar', 15, 6000.44,'cairo']
print('----------- printing mixed list -----------')
print(mixed_list)

# accessing element from the list using index
print('------- # accessing element from the list using index -----')
print(strings_list)
print(strings_list[0])
print(strings_list[1])
print(strings_list[2])

# Changing elements of the list
print('------------- # Changing elements of the list --------------')
print(strings_list)
strings_list[0] = 'Python programming'
print(strings_list)


# --------------- functions of List ----------------
print('---------------- # - functions of List ---------------- -------------------')
# append new elements to the last of the list
print('-------------- append function # append new elements to the last of the list  -------------------')
print(strings_list)
strings_list.append('testing')
list2 = ['asp', 'laravel','node js']
strings_list.append(list2)
print(strings_list)

# ---------------- # extend -------------------------
print('# ---------------- # extend : to add a list to end of a list -------------------------')
print(strings_list)
list3 = ['mongo', 'react','angular']
strings_list.extend(list3)
print(strings_list)

# -------------------- insert -----------------------
print('# -------------------- insert -----------------------')
print(strings_list)
strings_list.insert(0, 'basic programming')
strings_list.insert(0, list3)
print(strings_list)

# get the size of a list
print('------------- # get the size of a list -------------')
print(strings_list)
print(len(strings_list))

# remove() function : Remove method in List will only remove
# the first occurrence of the searched element.
print('------------------ # remove items from the list  -------------')
print(strings_list)
strings_list.remove('mongo')
strings_list.remove('react')
strings_list.remove('angular')
print(strings_list)

# pop() : can also be used to remove and return an
# element from the list, but by default it
# removes only the last element of the list,
# to remove an element from a specific position of the List,
# the index of the element is passed as an argument to the pop() method.
print('--------------- pop() -----------------')
print(strings_list)
removed_item = strings_list.pop()
print(removed_item)
removed_item = strings_list.pop(0)
print(removed_item)
print(strings_list)

# reversing a list
print('----------------- # reversing a list ----------------------')
print(strings_list)
backup_list = strings_list.copy()
strings_list.reverse()
print(backup_list)
print(strings_list)

# sorting a list
print('--------------- # sorting a list ------------------')
print(numbers_list)
numbers_list.sort()
print(numbers_list)
numbers_list.sort(reverse=True)
print(numbers_list)

print(strings_list)
strings_list.sort()
print(strings_list)

# max , min
print('--------------- max()   min() sum() -------------')
print(numbers_list)
print(max(numbers_list))
print(min(numbers_list))
print(sum(numbers_list))

# slicing list
print('--------------------- slicing list -----------------------')
numbers_list = [16, 5, 20, 13, 2, 14, 30, 20, 70, 20]
print(numbers_list[0]) # the first index : 16
print(numbers_list[-1]) # the last index : 20
print(numbers_list[0:5])  # from index 0 to 4 : [16, 5, 20, 13, 2]
print(numbers_list[:5])  # from index 0 to 4 : [16, 5, 20, 13, 2]
print(numbers_list[:-1]) # from the index 0 to the index before the last [16, 5, 20, 13, 2, 14, 30, 20, 70]
print(numbers_list[6:])  # from index 6 to end : [30, 20, 70, 20]]
print(numbers_list[-4:])  # from index -4 to end : [30, 20, 70, 20]
print(numbers_list[0:8:2]) # from index 0 to 7 - step 2 : [16, 20, 2, 30]
print(numbers_list[:]) # from 0 to end - same copy : [16, 5, 20, 13, 2, 14, 30, 20, 70, 20]
print(numbers_list[::-1]) # from 0 to end - step - 1 = print string in reverse order : [20, 70, 20, 30, 14, 2, 13, 20, 5, 16]

#------------------------ nested list ------------------------
print('------------------------ nested list ------------------------')
my_nested_list = [[101,'ahmed','Cairo'],[102, 'mostafa','Alex']]
print(my_nested_list)
print(my_nested_list[0][1]) # ahmed
print(my_nested_list[1][1]) # mostafa
