"""
1. Подсчитать, сколько было выделено памяти под переменные в ранее
разработанных программах в рамках первых трех уроков. Проанализировать
результат и определить программы с наиболее эффективным использованием памяти.
Примечание: Для анализа возьмите любые 1-3 ваших программы или несколько
вариантов кода для одной и той же задачи. Результаты анализа вставьте в виде
комментариев к коду. Также укажите в комментариях версию Python
и разрядность вашей ОС.
"""
import sys
import collections
from memory_profiler import profile

profit = collections.Counter()
@profile
def simple_func(*args, **kwargs):

    q = 4

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
    return profit


quantity = int(input('Введите кол-во предприятий  '))
simple_func(quantity)

print(sys.getrefcount(profit))
print(sys.getrefcount(quantity))
print(sys.platform)



# Line #    Mem usage    Increment   Line Contents
# ================================================
#     15     13.4 MiB     13.4 MiB   @profile
#     16                             def simple_func(*args, **kwargs):
#     17
#     18     13.4 MiB      0.0 MiB       q = 4
#     19
#     20     13.4 MiB      0.0 MiB       av_profit = 0
#     21
#     22     13.4 MiB      0.0 MiB       for n in range(1, quantity + 1):
#     23     13.4 MiB      0.0 MiB           a = 0
#     24     13.4 MiB      0.0 MiB           for m in range(1, q + 1):
#     25     13.4 MiB      0.0 MiB               s_profit = int(input(f'Введите прибыль для {m} квартала {n} компании '))
#     26     13.4 MiB      0.0 MiB               profit[n] += s_profit
#     27     13.4 MiB      0.0 MiB           print(profit)
#     28     13.4 MiB      0.0 MiB           av_profit = av_profit + profit[n]
#     29     13.4 MiB      0.0 MiB       a = av_profit / quantity
#     30     13.4 MiB      0.0 MiB       print(f'Средняя прибьль {a}')
#     31     13.4 MiB      0.0 MiB       for x in range(1, quantity + 1):
#     32     13.4 MiB      0.0 MiB           if profit[x] > a:
#     33                                         print(f'Средняя прибыль компании {x} равна {profit[x]}, это выше среднего')
#     34                                     else:
#     35     13.4 MiB      0.0 MiB               print(f'Средняя прибыль компании {x} равна {profit[x]}, это ниже среднего')
#     36     13.4 MiB      0.0 MiB       return profit
#
#
# 2
# 295
# win32