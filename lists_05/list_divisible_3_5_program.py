# print only numbers from the list that are divisible by 3 and 5
numbers_list = [15, 30, 20, 45, 16, 20]

for item in numbers_list:
    if item % 3 == 0 and item % 5 == 0:
        print(item)