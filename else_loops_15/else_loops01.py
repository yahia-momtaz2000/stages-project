"""
The else block in a loop is executed when the loop
completes its iterations without any break statements being encountered.
"""
"""
The else block in a loop is not executed if the loop is 
terminated prematurely using break. 
This behavior provides a way to execute code only if the 
loop completes all its iterations without any early exits.
"""
for i in range(5):
    if i == 10:
        print("Encountered 3, breaking loop")
        break
else:
    print("Loop completed without encountering a break statement")
print('--------------------------------')
# using while loop
i = 0
while i < 6:
    if i == 10:
        print("Encountered 3, breaking loop")
        break
    i = i + 1
else:
    print("Loop completed without encountering a break statement")
print('--------------------------------')
"""
Common Use Cases: The else block in loops is often used in
scenarios where you're searching for an element or condition
and want to execute some code if the search is successful or
unsuccessful without the need for an additional flag 
variable to track the search status.
"""
# List of numbers
numbers = [10, 20, 35, 40, 50]

# Number to search for in the list
search_number = 35
# Loop through the list to search for the number
for num in numbers:
    if num == search_number:
        print("Number found in the list at index ", numbers.index(num))
        break
else:
    print("Number not found in the list")
