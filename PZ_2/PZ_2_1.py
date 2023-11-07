# вывод номера для недели для k-го дня года
while True:  # обработка исключений
    try:
        k = int(input('Введите число K от 1-365:'))
        if k <= 0 or k > 365:
            continue
        break
    except ValueError:
        print('Вы ввели не число')
jan_1_weekday = 4
weekday_number = (jan_1_weekday + (k - 1)) % 7  # вычисление номера для недели для k-го дня гола
print("Номер дня недели для", k, "-го дня года:", weekday_number)