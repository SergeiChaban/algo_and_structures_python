"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""

import time as t
from random import random
import timeit
import cProfile
import sys

sys.setrecursionlimit(1000000)


def time_test(func):
    def wrapper(*args):
        start = t.time()*1000
        result = func(*args)
        time = t.time() * 1000 - start
        print(f'Время выполнения {time} миллисекунд')
        return result
    return wrapper


@time_test
def numb_count():
    M = 4
    N = 4
    a = []
    for i in range(N):
        b = []
        for j in range(M):
            n = int(random() * 100)
            b.append(n)
        a.append(b)

    for i in a:
        print(f'{i}')

    mx = -1
    for j in range(M):
        mn = 100
        for i in range(N):
            if a[i][j] < mn:
                mn = a[i][j]
        if mn > mx:
            mx = mn
    # time.sleep(3)
    print(f'{mx}')


numb_count()

# @time_test
# def rec(x):
#     if x > 0:
#         print(x % 10, end='')
#         rec(x//10)
#
#
# x = int(input('Введите число'))
# rec(x)

cProfile.run(numb_count)
cProfile.run(rec)
print(timeit.timeit('numb_count(34560**200)', number=1, setup='from__main__import numb_count'))
print(timeit.timeit('numb_count(34560**200)', number=1, setup='from__main__import rec'))




