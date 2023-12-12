# Дана строка, состоящая из русских слов, набранных заглавными буквами и
# разделенных пробелами (одним или несколькими). Найти количество слов, которые
# начинаются и заканчиваются одной и той же буквой.

def count_str(str):
    words = str.split()
    count = 0
    for word in words:
        if word[0].upper() == word[-1].upper() :
            count += 1
    return count

str = input('Введите строку\n')
result = count_str(str)
print(f'Результат: {result}')