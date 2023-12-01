# Описать функцию Minmax(X, Y), записывающую в переменную X минимальное из
# значений X и Y, а в переменную Y — максимальное из этих значений (X и Y —
# вещественные параметры, являющиеся одновременно входными и выходными).
# Используя четыре вызова этой функции, найти минимальное и максимальное из
# данных чисел A, B, C, D.
def Minmax(X, Y):
    if X > Y:
        return Y, X
    else:
        return X, Y


A = float(input("Введите число A: "))
B = float(input("Введите число B: "))
C = float(input("Введите число C: "))
D = float(input("Введите число D: "))

min_AB, max_AB = Minmax(A, B)
min_CD, max_CD = Minmax(C, D)
min_all, max_all = Minmax(min_AB, min_CD), Minmax(max_AB, max_CD)

print(f"Минимальное число: {min_all[0]}, Максимальное число: {max_all[1]}")



