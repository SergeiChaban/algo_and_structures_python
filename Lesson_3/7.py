"""
7.	В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными),
 так и различаться.
"""
from random import random
m = []
N = 20
f2 = 0

min_num = 100
count_min = 0
x2 = []

for a in range(N):
    rand_m = int(random() * 100)
    m.append(rand_m)
print(m)

for second_num in range(0, N):

    if min_num > m[second_num]:
        count_min += 1
        min_num = m[second_num]
        for i in range(1):
            x2.append(min_num)
        # x2 = second_num
        # f2 = count_min
print(x2[-1], x2[-2])