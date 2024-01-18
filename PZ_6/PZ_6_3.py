# Дан список размера N и целое число K (1 < K < N). Осуществить сдвиг элементов
# списка вправо на K позиций (при этом A1 перейдет в AK+1, A2 — в AK+2, ..AN-K — в
# AN, а исходное значение K последних элементов будет потеряно). Первые K
# элементов полученного списка положить равными 0.

import random

N = 5
my_list = [random.randint(1, 100) for _ in range(N)]
print("Исходный список:", my_list)

K = 2
if K >= N or K < 1:
    print("Ошибка: введено неверное число K")
else:
    new_list = [0] * K + my_list[:-K]
    print("Преобразованный список:", new_list)