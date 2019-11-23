# 4.	Определить, какое число в массиве встречается чаще всего.
from random import random

m = []
n = []
N = 20
f = 0

for a in range(N):
    rand_m = int(random() * 5)
    m.append(rand_m)
print(m)

j = 0
for first_num in range(j+1, N):
    m_max = 0
    for second_num in range(j, N-1):
        if first_num != second_num and m[first_num] == m[second_num]:
            m_max += 1
            if m_max > f:
                n = m[first_num]
                f = m_max


if f > 0:
    print('Число:', n, '; повторов:', f+1)
else:
    print('Нет повторов')
