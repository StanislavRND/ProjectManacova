# В квадратной матрице все элементы, не лежащие на главной диагонали увеличить в
# 2 раза.
import random

rows = 3
cols = 3

matrix = [[random.randint(1, 20) for _ in range(cols)] for _ in range(rows)]

modified_matrix = [[el * 2 if i != j else el for i, el in enumerate(row)] for j, row in enumerate(matrix)]

print('Исходная матрица: ')
for row in matrix:
    print(row)


print('Модифицированная матрица: ')
for row in modified_matrix:
    print(row)