"""
8.	Посчитать, сколько раз встречается определенная цифра в введенной
 последовательности чисел. Количество вводимых чисел и цифра,
 которую необходимо посчитать, задаются вводом с клавиатуры.
"""
import random

x = int(input('Количество вводимых чисел'))
y = int(input('Цифра, количество которых нужно подсчитать'))
numb = round(random.random(), x)

for i in range(x):
    numb = numb * 10
numb = int(numb)
print(numb)

def rec(numb, x):
    z = 0
    while x > 0:
        numb1 = numb % 10
        if numb1 == y:
            z += 1
        rec(numb // 10, x - 1)
    print(z)


rec(numb, x)
