# for i in range(10):
#     if i in (3, 5):
#         continue
#     print(i)

# for i in range(10):
#     if i == 3:
#         break
#     print(i)
#
#
#
# i = 0
# while (i < 4):
#     print(i, "Hello World")
#
#
# nl=[]
# for x in range(1500, 2701):
#     if (x%7==0) and (x%5==0):
#         nl.append(str(x))
# print (','.join(nl))

#
# list1 = [5,10,15,20]
# list2 = ['Tomatoes','Potatoes','Carrots','Cucumbers']
#
#
# for x in list1:
#     for y in list2:
#         print(x,y)



# n = 4
# for i in range(0, n):
#     print(i)

#
# n = 4
# for i in range(n):
#     print(i)

#
# n = 8
# for i in range(0, n, 2):
#     print(i)


# for i in range(1, 4):
#     for j in range(1, 4):
#         print(i, j)

#
# colors_list = ["red", "yellow", "green"]
# for i in range(len(colors_list) ):
#     print(i, colors_list[i] )

#
# colors_list = ["red", "yellow", "green"]
# for item in colors_list:
#     print( item )

#
# person_tuple = (101, 'Ahmed', 6000, 'Cairo')
# for i in range(len(person_tuple ) ):
#     print(i, person_tuple [i] )

#
# person_tuple = (101, 'Ahmed', 6000, 'Cairo')
# for item in person_tuple:
#     print( item )
#
# shopping_prices_dict = {'milk': 30.0, 'eggs': 120.0, 'butter': 60.0}
# for item_key in shopping_prices_dict:
#     print(item_key, shopping_prices_dict[item_key])

# shopping_prices_dict = {'milk': 30.0, 'eggs': 120.0, 'butter': 60.0}
# for item_key, item_value in shopping_prices_dict.items():
#     print(item_key, item_value)

# student_name = 'ahmad omar'
# for letter in student_name:
#     print(letter)
M = 1
sum_odd = 0
while M <= 10:
    if M % 2 == 0:
        pass
    else:
        sum_odd = sum_odd + M
    M = M + 1

print(sum_odd)
