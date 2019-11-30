"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
"""
import cProfile


pr = cProfile.Profile()

# Решето

n = int(input("n="))
pr.enable()
lst = []
for i in range(2, n+1):
    for j in lst:
        if i % j == 0:
            break
    else:
        lst.append(i)

pr.disable()
pr.print_stats()

# без решета
n = int(input("n="))
pr.enable()
s = [x for x in range(2, n+1) if x not in [i for sub in [list(range(2 * j, n+1, j)) for j in range(2, n // 2)]
                                           for i in sub]]

pr.disable()
pr.print_stats()

# без решета

# n=1000
# 2 function calls in 0.062 seconds
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.062    0.062    0.613    0.613 2.py:28(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# n=10000
# 2 function calls in 9.614 seconds
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    9.614    9.614   83.762   83.762 2.py:29(<listcomp>)
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# c решетом

# n=1000
# 169 function calls in 0.000 seconds
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#       168    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# n=10000
# 1230 function calls in 0.000 seconds
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1229    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# 1.Результат работы алгоритма с решетом показывает лучшие результаты как на малых (1000), так и на больших (10000)
# значениях за счет оптимизации в начале расчета (for i in range(2, n+1)
# 2. Алгоритм основанный на генераторах проигрывает по скорости р.Эратосфена за счет вдвое большей сложности
#
#
#

