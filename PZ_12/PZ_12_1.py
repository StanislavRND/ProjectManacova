# Даны средние значения температур за каждый месяц в году. Найти минимальное
# и максимальное значения температур за год. Вывести значения температур по временам
# года.
tempe = {'Январь': -23, 'Февраль': -15, 'Март': 4, 'Апрель': 13, 'Май': 18,
         'Июнь': 25, 'Июль': 29, 'Август': 28, 'Сентябрь': 18,
         'Октябрь': 12, 'Ноябрь': 5, 'Декабрь': -14}

min_el = min(tempe.values())
max_el = max(tempe.values())
print(f'Минимальная температура: {min_el}\nМаксимальная температура: {max_el}\n')

for key in tempe:
    print(f'{key}: {tempe[key]}')