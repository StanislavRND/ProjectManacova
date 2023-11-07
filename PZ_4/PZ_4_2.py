# Определить имеется ли в записи числа N цифра 2
while True:  # обработка исключений на строку
    try:
        N = int(input("Введите число > 0: "))
        while N < 0:  # проверка на отрицательное число
            print('Ошибка! Введите число > 0')
            N = int(input("Введите число > 0: "))
        has_two = False  # переменная, которая хранит False для дальнейших действий с ней

        while N > 0:
            remainder = N % 10
            if remainder == 2:
                has_two = True
                break
            N //= 10

        print(has_two)
        break
    except ValueError:
        print("Ошибка! Вы ввели строку")



