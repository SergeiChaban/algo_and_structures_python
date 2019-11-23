#3.	В массиве случайных целых чисел поменять местами минимальный
# и максимальный элементы.
from random import random
m = []
n = []
N = 20
f = 0
f2 = 0
max_num = 0
min_num = 0
count_max = 0
count_min = 0
x1 = 0
x2 = 0

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
    if second_num > 0:
        if m[second_num] > min_num:
            count_min += 1
            if count_min > f2:
                min_num = m[second_num]
                x2 = second_num
                f2 = count_min

print(max_num, min_num)
# m[x1] = m[x2]
# print(m)
m[x2] = m[x1]
print(m)
