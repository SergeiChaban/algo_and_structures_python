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
import memory_profiler
from functools import reduce
from guppy import hpy
import time


# h = hpy()
# profit = collections.Counter()
# @profile

# t1 = time.process_time()
# m1 = memory_profiler.memory_usage()
# def simple_func(*args, **kwargs):
#
#     q = 4
#
#     av_profit = 0
#
#     for n in range(1, quantity + 1):
#         a = 0
#         for m in range(1, q + 1):
#             s_profit = int(input(f'Введите прибыль для {m} квартала {n} компании '))
#             profit[n] += s_profit
#         print(profit)
#         av_profit = av_profit + profit[n]
#     a = av_profit / quantity
#     print(f'Средняя прибьль {a}')
#     for x in range(1, quantity + 1):
#         if profit[x] > a:
#             print(f'Средняя прибыль компании {x} равна {profit[x]}, это выше среднего')
#         else:
#             print(f'Средняя прибыль компании {x} равна {profit[x]}, это ниже среднего')
#     return profit
#
#
# quantity = int(input('Введите кол-во предприятий  '))
# simple_func(quantity)
#
# t2 = time.process_time()
# m2 = memory_profiler.memory_usage()
# time_diff = t2 - t1
# mem_diff = m2[0] - m1[0]
#
# print(f'{time_diff} sec and {mem_diff} Mb')
# print(sys.getrefcount(profit))
# print(sys.getrefcount(quantity))
# print(sys.platform)
# print(h.heap())

#
# Line #    Mem usage    Increment   Line Contents
# ================================================
#     19     13.5 MiB     13.5 MiB   @profile
#     20                             def simple_func(*args, **kwargs):
#     21
#     22     13.5 MiB      0.0 MiB       q = 4
#     23
#     24     13.5 MiB      0.0 MiB       av_profit = 0
#     25
#     26     13.5 MiB      0.0 MiB       for n in range(1, quantity + 1):
#     27     13.5 MiB      0.0 MiB           a = 0
#     28     13.5 MiB      0.0 MiB           for m in range(1, q + 1):
#     29     13.5 MiB      0.0 MiB               s_profit = int(input(f'Введите прибыль для {m} квартала {n} компании '))
#     30     13.5 MiB      0.0 MiB               profit[n] += s_profit
#     31     13.5 MiB      0.0 MiB           print(profit)
#     32     13.5 MiB      0.0 MiB           av_profit = av_profit + profit[n]
#     33     13.5 MiB      0.0 MiB       a = av_profit / quantity
#     34     13.5 MiB      0.0 MiB       print(f'Средняя прибьль {a}')
#     35     13.5 MiB      0.0 MiB       for x in range(1, quantity + 1):
#     36     13.5 MiB      0.0 MiB           if profit[x] > a:
#     37     13.5 MiB      0.0 MiB               print(f'Средняя прибыль компании {x} равна {profit[x]}, это выше среднего')
#     38                                     else:
#     39     13.5 MiB      0.0 MiB               print(f'Средняя прибыль компании {x} равна {profit[x]}, это ниже среднего')
#     40     13.5 MiB      0.0 MiB       return profit
#
#
# 2
# 298
# win32


# Стандартной памяти достаточно, стек в программе не задействован, обращения к heap не происходит. Оптимизицию делать
# не нужно

# guppy3
# 2
# 298
# Partition of a set of 57615 objects. Total size = 4015018 bytes.
#  Index  Count   %     Size   % Cumulative  % Kind (class / dict of class)
#      0  16685  29  1163214  29   1163214  29 str
#      1  14897  26   610952  15   1774166  44 tuple
#      2   7552  13   420930  10   2195096  55 bytes
#      3   3821   7   321940   8   2517036  63 types.CodeType
#      4   3743   6   269496   7   2786532  69 function
#      5    617   1   254392   6   3040924  76 type
#      6    617   1   187992   5   3228916  80 dict of type
#      7    146   0   139992   3   3368908  84 dict of module
#      8    480   1   114644   3   3483552  87 dict (no owner)
#      9   1213   2    53372   1   3536924  88 types.WrapperDescriptorType

# ожидаемо памяти больше всего потребовалось для строк и кортежей

# time and memory_usage = 0.015625 sec and 0.03515625 Mb
#===================================================================
# Пример 4.2 решето Эратосфена

t1 = time.process_time()
m1 = memory_profiler.memory_usage()
# h = hpy()
# @profile
def simple_func(*args, **kwargs):
    n = int(input("n="))

    for i in range(2, n + 1):
        for j in lst:
            if i % j == 0:
                break
        else:
            lst.append(i)
    return lst


lst = []
simple_func(lst)
# # print(h.heap())
#
#
# print(sys.getrefcount(lst))
# print(sys.platform)
t2 = time.process_time()
m2 = memory_profiler.memory_usage()
time_diff = t2 - t1
mem_diff = m2[0] - m1[0]
print(f'{time_diff} sec and {mem_diff} Mb')

# n=3
# Filename: C:/Users/Admin/PycharmProjects/algo_and_structures_python/Lesson_6/1.py
#
# Line #    Mem usage    Increment   Line Contents
# ================================================
#     85     13.5 MiB     13.5 MiB   @profile
#     86                             def simple_func(*args, **kwargs):
#     87     13.5 MiB      0.0 MiB       n = int(input("n="))
#     88
#     89     13.5 MiB      0.0 MiB       for i in range(2, n + 1):
#     90     13.5 MiB      0.0 MiB           for j in lst:
#     91     13.5 MiB      0.0 MiB               if i % j == 0:
#     92                                             break
#     93                                     else:
#     94     13.5 MiB      0.0 MiB               lst.append(i)
#     95     13.5 MiB      0.0 MiB       return lst
#
#
# 2
# win32
# Стандартной памяти достаточно, стек в программе не задействован, обращения к heap не происходит. Оптимизицию делать
# не нужно

# guppy3
# n=3
# Partition of a set of 57605 objects. Total size = 4013914 bytes.
#  Index  Count   %     Size   % Cumulative  % Kind (class / dict of class)
#      0  16675  29  1162506  29   1162506  29 str
#      1  14897  26   610880  15   1773386  44 tuple
#      2   7552  13   420702  10   2194088  55 bytes
#      3   3821   7   321940   8   2516028  63 types.CodeType
#      4   3743   6   269496   7   2785524  69 function
#      5    617   1   254392   6   3039916  76 type
#      6    617   1   187992   5   3227908  80 dict of type
#      7    146   0   139992   3   3367900  84 dict of module
#      8    480   1   114644   3   3482544  87 dict (no owner)
#      9   1213   2    53372   1   3535916  88 types.WrapperDescriptorType


# ожидаемо памяти больше всего потребовалось для строк и кортежей

# time and memory_usage = 0.0 sec and 0.01171875 Mb