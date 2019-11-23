#5.	В массиве найти максимальный отрицательный элемент.
# Вывести на экран его значение и позицию (индекс) в массиве.

from random import random
a = []
N = 10
for i in range(N):
    n = int(random()*10) - 5
    a.append(n)
print(a)

i = 0
x = 0
max_min = N
while i < N + 2:
    if a[i] < 0 and abs(a[i]) < abs(max_min):
        max_min = a[i]
        x = i
        N -= 1
    else:
        i += 1
print(max_min, x)

