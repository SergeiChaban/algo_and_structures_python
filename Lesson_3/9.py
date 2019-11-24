# 9.	Найти максимальный элемент среди минимальных элементов столбцов матрицы.
from random import random
M = 4
N = 4
a = []
for i in range(N):
    b = []
    s = 0

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
print("Максимальный среди минимальных: ", mx)