"""
6.	В одномерном массиве найти сумму элементов, находящихся
между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""
from random import random
m = []
n = []
N = 20
f = 0
f2 = 0
max_num = 0
min_num = 100
count_max = 0
count_min = 0
x1 = 0
x2 = 0
s_arr = 0
i = 0

for a in range(N):
    rand_m = int(random() * 100)
    m.append(rand_m)
print(m)

for second_num in range(0, N):
    if m[second_num] > max_num:
        count_max += 1
        if count_max > f:
            max_num = m[second_num]
            x1 = second_num
            f = count_max


    if min_num > m[second_num]:
        count_min += 1
        min_num = m[second_num]
        x2 = second_num
        f2 = count_min

if x1 > x2:
    x1, x2 = x2, x1

for i in range(x1 + 1, x2):
    s_arr += m[i]

print(max_num, min_num, s_arr)
