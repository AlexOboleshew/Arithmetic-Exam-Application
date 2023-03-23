import random


def save_result(name, score, task):
    with open('results.txt', 'a') as file:
        file.write(f'{name}: {score}/5 in level {task.level} ({task.task_description})')


def is_correct_dif(text):

    if text.isdigit() and int(text) in [1, 2]:
        return True
    else:
        print('Incorrect format.')
        return False


class Task:

    def __init__(self):
        self.task_description = 'simple operations with numbers 2-9'
        self.level = 1
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


class HardTask(Task):

    def __init__(self):
        super().__init__()
        self.task_description = 'integral squares 11-29'
        self.level = 2

    def make_task(self):
        number = random.randint(11, 29)
        self.answer = number ** 2
        self.task = f'{number}'


CHOOSE_DIF_LVL_MSG = 'Which level do you want? Enter a number:\n' \
                     '1 - simple operations with numbers 2-9\n' \
                      '2 - integral squares of 11-29'

print(CHOOSE_DIF_LVL_MSG)
while True:
    dif_lvl = input()
    if is_correct_dif(dif_lvl):
        break
    else:
        continue
dif_lvl = int(dif_lvl)
if dif_lvl == 1:
    new_task = Task()
else:
    new_task = HardTask()
correct_answ = 0
total_answ = 0

while total_answ < 5:
    new_task.make_task()
    new_task.print_task()
    while True:
        user_input = input()
        try:
            int(user_input)
            break
        except ValueError:
            print('Incorrect format.')
            continue

    if int(user_input) == new_task.answer:
        print('Right!')
        correct_answ += 1
        total_answ += 1
    else:
        total_answ += 1
        print('Wrong!')

print(f'Your mark is {correct_answ}/5. Would you like to save the result? Enter yes or no.')
if input() in ['yes', 'YES', 'y', 'Yes']:
    user_name = input('What is your name?\n')
    save_result(user_name, correct_answ, new_task)
    print('The results are saved in "results.txt".')
