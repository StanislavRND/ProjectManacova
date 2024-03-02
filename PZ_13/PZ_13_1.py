# Сгенерировать матрицу, в которой элементы больше 10 заменяются на 0.
import random

rows = 5
cols = 5

matrix = [[random.randint(1, 15) for _ in range(cols)] for _ in range(rows)]

print('Исходная матрица: ')
for row in matrix:
    print(row)

modified_matrix = [[0 if el > 10 else el for el in row] for row in matrix]

print('\nМодифицированная матрица: ')
for row in modified_matrix:
    print(row)