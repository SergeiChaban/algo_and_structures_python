"""
1. Проанализировать скорость и сложность одного любого алгоритма,
разработанных в рамках домашнего задания первых трех уроков.
Примечание: попробуйте написать несколько реализаций алгоритма и сравнить их.
"""

import time
from datetime import datetime
from random import random
# import timeit
# start = time.time()
start = datetime.now()
# M = 4
# N = 4
# a = []
# for i in range(N):
#     b = []
#     s = 0
#
#     for j in range(M):
#         n = int(random() * 100)
#         b.append(n)
#     a.append(b)
#
# for i in a:
#     print(f'{i}')
#
# mx = -1
# for j in range(M):
#     mn = 100
#     for i in range(N):
#         if a[i][j] < mn:
#             mn = a[i][j]
#     if mn > mx:
#         mx = mn
# # time.sleep(3)
# print("Максимальный среди минимальных: ", mx)



#
def rec(x):
    if x > 0:
        print(x % 10, end='')
        rec(x//10)


x = int(input('Введите число'))
rec(x)

# stop = time.time()
# print(stop - start)

# t1 = Timer('rec', 'from__main__import rec')
# print('rec', t1.timeit(number=100), 'milliseconds')

stop = datetime.now()
total = stop - start
print(str(total))