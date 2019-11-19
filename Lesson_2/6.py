"""
6.	В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток. После каждой
неудачной попытки должно сообщаться больше или меньше введенное пользователем
число, чем то, что загадано. Если за 10 попыток число не отгадано,
то вывести загаданное число.
"""
from random import random

left = 1
right = 100
numb = int(random() * (right - left + 1)) + left
attempt = 10
while attempt > 0:
    numb_of_user = int(input('Введите Ваше число'))
    if numb == numb_of_user:
        print('Вы угадали')
        break
    if numb_of_user < numb:
        sign = 'меньше'
    else:
        sign = 'больше'
    attempt = attempt - 1
    if attempt > 4 or attempt == 0:
        text = 'попыток'
    else:
        text = 'попытки'
    print(f'Ваша цифра {sign}, осталось {attempt} {text}')


print(f'Случайное целое число: {numb}')
