# В квадратной матрице все элементы, не лежащие на главной диагонали увеличить в
# 2 раза.
import random

def modify_matrix(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(n):
            if i != j:
                matrix[i][j] *= 2
    return matrix

rows = 3
cols = 3

matrix = [[random.randint(1, 20) for _ in range(cols)] for _ in range(rows)]

print('Исходная матрица: ')
for row in matrix:
    print(row)

modified_matrix = modify_matrix(matrix)

print('Модифицированная матрица: ')
for row in modified_matrix:
    print(row)