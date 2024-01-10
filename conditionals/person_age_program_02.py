personName = input('Enter your name : ')
personAge = int(input('Enter your age : '))

if personAge > 16:
    print('You are a man')
elif personAge >= 11:
    print('You are a boy')
else:
    print('You are a child')
