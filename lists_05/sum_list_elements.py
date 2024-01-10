# get the sum between elements in a list
numbers_list = [15, 16, 20, 3, 15, 20]
sum_items = 0
for item in numbers_list:
    sum_items = sum_items + item

print('sum = '+str(sum_items))
average = sum_items / len(numbers_list)
print('average = '+str(average))
print(sum(numbers_list))