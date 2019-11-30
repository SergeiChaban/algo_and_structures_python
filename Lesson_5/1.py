"""
1. Пользователь вводит данные о количестве предприятий, их наименования и
прибыль за 4 квартала (т.е. 4 отдельных числа) для каждого предприятия..
Программа должна определить среднюю прибыль (за год для всех предприятий) и
вывести наименования предприятий, чья прибыль выше среднего и отдельно
вывести наименования предприятий, чья прибыль ниже среднего.
"""

import collections

#
# profit = 0
# av_profit = 0
# sum_profit = 0
# a_p = []
#
# quantity = int(input('Введите количество предприятий '))
# for i in range(1, quantity + 1):
#     for n in range(1, 5):
#         profit = int(input(f'Укажите прибыль для {n}-го квартала {i}-го предприятия '))
#         sum_profit += profit
#     a_p.append(sum_profit)
#
#     print(sum_profit)
#     print(),
# av_profit = sum_profit / quantity
# print(av_profit, a_p)
#
# for i_d, val in enumerate(a_p):
#     if val >= av_profit:
#         print(f'Прибыль {i_d+1}-го предприятия выше среднего')
#     else:
#         print(f'Прибыль {i_d+1}-го предприятия ниже среднего')


profit = 0
av_profit = 0
sum_profit = 0
a_p = collections.Counter()

quantity = int(input('Введите количество предприятий '))
for i in range(1, quantity + 1):
    for n in range(1, 5):
        profit = int(input(f'Укажите прибыль для {n}-го квартала {i}-го предприятия '))
        sum_profit += profit
        a_p[i] += sum_profit
    # av_profit = sum_profit / quantity
    # av_profit = a_p / quantity
    print(sum_profit, sum_profit / quantity)
    print(),

print(sum_profit, av_profit, a_p)


for val in a_p:
    if val >= av_profit:
        print(f'Прибыль {val}-го предприятия выше среднего')
    else:
        print(f'Прибыль {val}-го предприятия ниже среднего')





# counter = collections.Counter()
# for word in ['spam', 'egg', 'spam', 'counter', 'counter', 'counter']:
#     counter[word] += 1
# print(counter)
# print(counter['counter'])
# print(counter['collections'])
