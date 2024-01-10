"""
Tuple is a collection of Python objects much like a list.
The sequence of values stored in a tuple can be of any type,
and they are indexed by integers.
to define a tuple by closing the sequence of values in parentheses.
- Tuple is a collection which is ordered and unchangeable. Allows duplicate members
- Tuples are heterogeneous data structures (i.e., their entries have different meanings)
- Lists are for looping, tuples are for structures
- Tuples are like records and struct in C++
#
Six main benefits

1- Tuples are immutable
2- They can be used as keys in a dictionary
3- Function Return Values of type Tuple
4- They're more idiomatic for some purposes, e.g. an ordered pair of coordinates
5- Slight performance improvement
6- Unpacking on tuples
"""
# Creating a Tuple
print('------------ Creating a tuple ----------------')
person_tuple = (101, 'Ahmed Esam', 5000.0, 'Cairo', '0127454104')
print(person_tuple)
print(type(person_tuple))

print('----------- Accessing a tuple -----------')
# Accessing a tuple
print(type(person_tuple[0]))
print(type(person_tuple[1]))
print('person name : '+person_tuple[1])


# concat tuple
print('---------- Concat tuple -----------------')
person_job_tuple = ('python developer', 'senior')
# this will not edit the tuple : will create a new one
person_tuple = person_tuple + person_job_tuple
print(person_tuple)


print('---------- Casting : convert from tuple to list ------------------')
# ---------- convert from tuple to list ------------------'
new_list = list(person_tuple)
print(new_list)


print('-------------- Casting : convert from list to tuple ---------------')
# ---------- convert from list to tuple ------------------'
my_list = [10, 20, 30]
my_tuple = tuple(my_list)
print(my_tuple)


print('---------- slicing a tuple -----------------')
# slicing a tuple


print('------------ methods for a tuple -------------------')
# index('Cairo'), count('Cairo'), len(), max(), min(), sum(), sorted(),
print(person_tuple.index('Cairo'))
print(person_tuple.count('Cairo')) # count occurence


# unpacking tuple
print('------------- unpacking tuple -----------------')
print(person_tuple)
person_id, person_name, person_salary, person_address, person_mobile, \
            person_job, job_position = person_tuple
print(person_name+' lives in '+person_address)


# list of Tuples
print('------------ List of Tuples ------------------')
rejected_ips = [
    ('192.168.0.15', 33, 60),
    ('192.168.0.22', 34, 60),
    ('192.168.0.1', 34, 60),
    ('192.168.0.2', 34, 60),
    ('192.168.0.8', 34, 60),
    ('192.168.0.11', 34, 60)
]

print(rejected_ips)
# loop over a tuple
print('------------ loop over a tuple ---------------')
for person_value in person_tuple:
    print(person_value)

# loop over a tuple
print('------------ loop over a tuple using index -----------')
for i in range(len(person_tuple)):
    print(person_tuple[i])