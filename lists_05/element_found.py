# Check if an element exists in a list in Python
lst=[ 1, 6, 3, 5, 3, 4 ]

num = 6
is_found = False
for i in range(len(lst)):
    if num == lst[i]:
        print(str(num) +' is found on index ='+str(i))
        is_found = True
        break;

if is_found == False:
    print('number is not found')
