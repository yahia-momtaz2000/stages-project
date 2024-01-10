import random

firstNumber = random.randint(1, 100)
secondNumber = random.randint(1, 100)
print(str(firstNumber) + ' + ' + str(secondNumber) + ' = ')
result = int(input())

if result == firstNumber + secondNumber:
    print('Correct answer')
else:
    print('Wrong answer')
