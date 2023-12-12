# Дан целочисленный список размера N. Увеличить все четные числа, содержащиеся
# в списке, на исходное значение первого четного числа. Если четные числа в списке
# отсутствуют, то оставить список без изменений.
import random


def increase_number(lst):
    first_num = None
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            if first_num is None:
                first_num = lst[i]
            lst[i] += first_num
    return lst

N = 5
arr = [random.randint(0, 100) for i in range(N)]
print(f'Исходный массив {arr}')
print(increase_number(arr))
