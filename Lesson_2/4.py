"""
4.	Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""
y = 0.75
x = (-2.25)
m = 1
n = int(input('Введите количество элементов в ряду'))


def n_row(m, y, x, n):

    while n > 0:

        print(m)

        # меняем шаг ряда (-1,5 и 0,75)
        y = x + y

        # строим ряд
        m = m + y

        # меняем знак на противоположенный
        x = x * (-1)

        # счетчик
        n = n - 1


n_row(m, y, x, n)