"""
- Dictionary in Python is a collection of keys values, used to store
 data values like a map, which, unlike other data types
 which hold only a single value as an element.

- Dictionary are mutable [ can be changed ]

- Dictionary holds key:value pair. Key-Value is provided in the dictionary to make it more optimized.

- Dictionaries in Python are a well designed version of a very common
data structure called a hash map.

"""
# Creating Dictionary
print('----------- creating dictionary -----------')
week_days_dict = {1: 'Sat', 2: 'Sun', 3: 'Mon',
                  4 : 'Tue', 5:'Wed', 6:'Thr', 7:'Fri'}

order_status = {1: 'Pending', 2: 'Shipping', 3: 'Cancelled', 4:'Received'}

gender_type = {'M': 'Male', 'F':'Female'}

# dictionary vs lists
print('--------- dictionary vs lists -------------')
shopping_list = ['milk, eggs, butter, bread']
shopping_prices_dict = {'milk': 30.0, 'eggs': 120.0, 'butter': 60.0, 'bread': 10.0}

# adding or modifying element to dict
print('----------- adding or modifying element to dict ---------------')
shopping_prices_dict['Tea'] = 45.5
shopping_prices_dict['milk'] = 39.0
print(shopping_prices_dict)

# access value based on a key in a dictionary
print('--------------- access value based on a key in a dictionary -----------------')
tea_price = shopping_prices_dict['Tea']
print(tea_price)

# Removing Items from a Dictionary
print('---------- Removing Items from a Dictionary --------')
shopping_prices_dict.pop('bread')
print(shopping_prices_dict)

# access all dict keys and all dict values
print('----------------  access all dict keys and all dict values ----------------')
print(shopping_prices_dict)
keys_list = shopping_prices_dict.keys()
values_list = shopping_prices_dict.values()
keys_values_list = shopping_prices_dict.items()
print(keys_list)
print(values_list)
print(keys_values_list)



# Merge 2 lists into a single Dictionary with key values
print('--------------- Merge 2 lists into a single Dictionary with key values ------')
emp_ids_list = [101, 102, 103]
emp_names_list = ['Ahmed', 'Omar', 'Sarah']
people_dict = {}
for i in range(len(emp_ids_list)):
    people_dict [emp_ids_list[i] ] = emp_names_list[i]

print(people_dict)

# List of Dictionaries
print('----------- List of Dictionaries ------------')
# create a list of dictionary with student
# id as key and name as value
data_list = [{7058: 'sravan', 7059: 'jyothika',
         7072: 'harsha', 7075: 'deepika'}]
# display the list
print(data_list)
# display the first index of the list which is the whole dict
print(data_list[0])

# display data of key 7058
print(data_list[0][7058])

# adding another dict to the list
data_list.append({7011: 'Hamad', 7012: 'Franshika'})
print(data_list[1][7011])

# update the value of dict of index 1 in the list with the key 7011
data_list[1][7011] = 'Ibraham'
print(data_list)


#----------------- Loops on a dictionary ----------------------
print('------- Loops on a dictionary -------')
for item_key in shopping_prices_dict:
    print(item_key)
    print(shopping_prices_dict[item_key])
    print('---')

print('_________________')
for item_key, item_value in shopping_prices_dict.items():
    print(item_key)
    print(item_value)
    print('---')
#----------------- example library ------------------
print('------------- example library ------------')
book_dict = {"pages": "277", "name": "Gone Girl", "year": 2007}

print(book_dict)
# Adding Elements To a Dictionary
print('-------  Adding Elements To a Dictionary -----')
book_dict['Author'] = 'Well Max'
print(book_dict)

# Accessing Elements inside a Dictionary
print('---- # Accessing Elements inside a Dictionary ----')
print(book_dict['name'])


# Changing Elements inside a Dictionary
print('---  Changing Elements inside a Dictionary -----')
book_dict['year'] = 2010
print(book_dict)

# Using Loop to print keys and values
print('------ Using Loop to print keys and values ------')
for k, v in book_dict.items():
    print(k, v)

# Removing Items from a Dictionary
print('---- Removing Items from a Dictionary ----')
book_dict.pop('name')
print(book_dict)

"""
example :
Write a Program to combine two different dictionaries. 
While combining, if you find the same keys, 
you can add the values of these same keys. Output the new dictionary
"""
print('------  Combine two different dictionaries and plus same keys -------')
dict1 = {'a': 100, 'b': 150, 'c': 100}
dict2 = {'a': 50, 'c': 100, 'd': 150}

for key in dict2:
    if key in dict1:
        dict1[key] = dict1[key] + dict2[key]
    else:
        dict1[key] = dict2[key]
print(dict1)


# Converting a List of Tuples to a Dictionary
print('----------- Converting a List of Tuples to a Dictionary --------------')
colors_list = [('red', 223), ('blue', 201), ('green', 210)]


colors_dict = dict(colors_list)
print(colors_dict)

# join multi tuples into 1 dictionary
print('--------- join multi tuples into 1 dictionary ---------')
person_1_tuples = (101, 'Ahmed Esam', 5000.0, 'Cairo', '0127454104')
person_2_tuples = (102, 'Mohamed Omar', 6000.0, 'Alex', '01147041564')
person_3_tuples = (103, 'Ibrahim Hesham', 7000.0, 'Portsaid', '01032659878')

persons_dict = {
        'person 1': person_1_tuples,
        'person 2': person_2_tuples,
        'person 3': person_3_tuples
}
print(persons_dict)

# concate dictionaries
print('--------- concate dictiocary----------')
gender_dict = {'M': 'Male', 'F':'Female'}
shopping_prices_dict = {'milk': 30.0, 'eggs': 120.0, 'butter': 60.0, 'bread': 10.0}
new_dict = {}
new_dict.update(gender_dict)
new_dict.update(shopping_prices_dict)
print(new_dict)


print('----------------------------')
print(shopping_prices_dict)
keys_list = shopping_prices_dict.keys() # return list of keys
values_list = shopping_prices_dict.values() # return list of values
keys_values_list = shopping_prices_dict.items() # return list of tuples contain keys & values
print(keys_list)
print(type(keys_list))
print(values_list)
print(type(values_list))
print(keys_values_list)
print(type(keys_values_list))


print('------------------')
dict1 = {101 : 'Ahmed', 102 :'Ola', 103:'Omar'}
dict2 = {101 : 'Ibrahim', 105 :'Sayed', 106:'Fathy'}
dict1.update(dict2)
print(dict1)