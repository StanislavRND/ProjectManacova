# Составить функцию, которая выполнит суммирования числового ряда
def sum_num():
    while True:
        try:
            start = int(input("Введите начальное число: "))
            end = int(input("Введите конечное число: "))

            total_sum = 0
            for number in range(start, end + 1):
                total_sum += number
            print(total_sum)
            break
        except ValueError:
            print('Ошибка! Введите число')

sum_num()


