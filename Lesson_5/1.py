"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""

import collections

q = 4
profit = collections.Counter()
quantity = int(input('Введите кол-во предприятий  '))
av_profit = 0

for n in range(1, quantity + 1):
    a = 0
    for m in range(1, q + 1):
        s_profit = int(input(f'Введите прибыль для {m} квартала {n} компании '))
        profit[n] += s_profit
    print(profit)
    av_profit = av_profit + profit[n]
a = av_profit / quantity
print(f'Средняя прибьль {a}')
for x in range(1, quantity + 1):
    if profit[x] > a:
        print(f'Средняя прибыль компании {x} равна {profit[x]}, это выше среднего')
    else:
        print(f'Средняя прибыль компании {x} равна {profit[x]}, это ниже среднего')
