# Средствами языка Python сформировать два текстовых файла (.txt), содержащих по одной
# последовательности из целых положительных и отрицательных чисел. Сформировать
# новый текстовый файл (.txt) следующего вида, предварительно выполнив требуемую
# обработку элементов:

from random import random
from random import randint

num_1 = [randint(-10, 10) for _ in range(10)]
num_2 = [randint(-10, 10) for _ in range(10)]

for i in num_1:
    open('file_1.txt', 'a').write(str(i) + '\n')

for i in num_2:
    open('file_2.txt', 'a').write(str(i) + '\n')

num = num_1 + num_2
min_el = min(num_1)
max_el = max(num_2)

with open('file_3.txt', 'w', encoding='utf-8') as f:
    f.write(f'Элементы: {" ".join(map(str, num))} \n')
    f.write(f'Всего элементов: {len(num)} \n')
    f.write(f'Индекс min элемента: {num_1.index(min_el)} \n')
    f.write(f'Индекс max элемента: {len(num_2) - num_2[::-1].index(max_el) - 1} \n')
    f.write('Элементы кратные 4: ')
    for i in set(num):
       if (i % 4 == 0):
           f.write(str(i) + ' ')




