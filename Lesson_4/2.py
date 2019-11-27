"""
2. Написать два алгоритма нахождения i-го по счёту простого числа.
Без использования «Решета Эратосфена»;
Используя алгоритм «Решето Эратосфена»
"""
import cProfile


pr = cProfile.Profile()

# Решето

n = int(input("n="))
# pr.enable()
# lst = []
# for i in range(2, n+1):
#     for j in lst:
#         if i % j == 0:
#             break
#     else:
#         lst.append(i)
# # print(lst)
# pr.disable()
# pr.print_stats()
#
# без решета
pr.enable()
s = [x for x in range(2, n+1) if x not in [i for sub in [list(range(2 * j, n+1, j)) for j in range(2, n // 2)]
                                           for i in sub]]
# print(*s)
pr.disable()
pr.print_stats()