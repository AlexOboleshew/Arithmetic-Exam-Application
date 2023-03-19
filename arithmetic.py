import random


def is_correct_format(text):
    try:
        int(text)
        return True
    except ValueError:
        print('Incorrect format.')
        return False


class Task:

    def __init__(self):
        self.answer = None
        self.task = None

    def make_task(self):
        a = random.randint(2, 9)
        b = random.randint(2, 9)
        operations = '+-*'
        operation = random.choice(operations)
        if operation == '+':
            self.answer = a + b
        elif operation == '-':
            self.answer = a - b
        else:
            self.answer = a * b
        self.task = f'{a} {operation} {b}'

    def print_task(self):
        print(self.task)


new_task = Task()
correct_answ = 0
total_answ = 0
while total_answ < 5:
    new_task.make_task()
    new_task.print_task()
    while True:
        user_input = input()
        if is_correct_format(user_input):
            break
        else:
            continue
    if int(user_input) == new_task.answer:
        print('Right!')
        correct_answ += 1
        total_answ += 1
    else:
        total_answ += 1
        print('Wrong!')
print(f'Your mark is {correct_answ}/5.')
