# Дан целочисленный список размера N. Увеличить все четные числа, содержащиеся
# в списке, на исходное значение первого четного числа. Если четные числа в списке
# отсутствуют, то оставить список без изменений.
def increase_number(lst):
    first_num = None
    for i in range(len(lst)):
        if lst[i] % 2 == 0:
            if first_num is None:
                first_num = lst[i]
            else:
                lst[i] += first_num
    return lst
arr = [1, 4, 6, 9, 14]
print(f'Исходный массив {arr}')
print(increase_number(arr))
