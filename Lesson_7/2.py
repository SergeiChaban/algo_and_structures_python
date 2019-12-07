"""
2. Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
заданный случайными числами на промежутке [0; 50). Выведите на экран исходный
и отсортированный массивы.
"""

from random import random

m = []

for a in range(10):
    rand_m = int(random() * 50)
    m.append(rand_m)
print(f'Исходный массив {m}')


def merge_sort(m):
    if len(m) < 2:
        return
    else:
        center = len(m)//2
        right = m[center:]
        left = m[:center]
        print(f'm0 = {m}')
        print(f'right0 = {right}')
        print(f'left0 = {left}')

    merge_sort(right)
    merge_sort(left)

    r_v = l_v = s_v = 0
    while len(left) > l_v and len(right) > r_v:
        if left[l_v] < right[r_v]:
            m[s_v] = left[l_v]
            l_v += 1
            print(f'left1 = {m}')
        else:
            m[s_v] = right[r_v]
            r_v += 1
            print(f'right1 = {m}')
        s_v += 1
    while l_v < len(left):
        m[s_v] = left[l_v]
        l_v += 1
        s_v += 1
        print(f'left2 = {m}')
    while r_v < len(right):
        m[s_v] = right[r_v]
        r_v += 1
        s_v += 1
        print(f'right2 = {m}')
    return m


merge_sort(m)
print(m)


