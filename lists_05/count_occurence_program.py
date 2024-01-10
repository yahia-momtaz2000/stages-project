# Python4 : Count occurrence of a number in a list
lst=[ 1, 6, 3, 6, 3, 6 ]
num = 6
counter = 0
for item in lst:
    if item == num:
        counter = counter + 1

print('number appear in the list time : '+str(counter))