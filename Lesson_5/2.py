"""
2. Написать программу сложения и умножения двух шестнадцатеричных чисел.
При этом каждое число представляется как массив, элементы которого это цифры
числа. Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и
[‘C’, ‘4’, ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’],
произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""

import collections
from functools import reduce

nums = collections.defaultdict(list)

for n in range(1, 3):
    d = input(f'Введите {n}-е шестнадцатеричное число')
    nums[n] = list(d)
print(nums)

sum = hex(sum([int(''.join(i), 16) for i in nums.values()]))
print(list(sum))

mult = reduce(lambda a, b: a * b, [int(''.join(i), 16) for i in nums.values()])
mult = hex(mult)
print(list(mult))


