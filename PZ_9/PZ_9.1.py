# Сгенерировать словарь вида {0: 0, 1: 1, 2: 8, 3: 27, 4: 64, 5: 125, 6: 216},
# удалить из него первый и последний элементы. Отобразить исходный и
# получившийся словарь. Использовать for, range.
d = {i: i ** 3 for i in range(7)}
print('Исходный словарь:', d)

del d[0]
d.popitem()
print('Изменённый словарь', d)