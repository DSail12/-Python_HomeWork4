# Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.
# Пример [1, 1, 2, 3, 3, 4, 5, 6, 6, 7] -> 2 4 5 7

import collections
cntr = collections.Counter([1, 1, 2, 3, 3, 4, 5, 6, 6, 7])
print(*filter(lambda x: cntr[x] == 1, cntr.keys()))