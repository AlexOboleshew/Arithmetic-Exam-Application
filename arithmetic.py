import random

a = random.randint(2, 9)
b = random.randint(2, 9)
operations = '+-*'
operation = random.choice(operations)
if operation == '+':
    result = a + b
elif operation == '-':
    result = a - b
else:
    result = a * b
print(f'{a} {operation} {b}')
user_input = int(input())
if user_input == result:
    print('Right!')
else:
    print('Wrong!')
