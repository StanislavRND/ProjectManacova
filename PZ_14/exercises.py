import re

with open('exircises.txt', encoding='utf-8') as f:
    lines = f.read()


print('Найдите все натуральные числа (возможно, окружённые буквами)')
print(re.findall(r'\d+', lines))

print('Найдите все «слова», написанные капсом (то есть строго заглавными), возможно внутри настоящих слов (аааБББввв)')
print(re.findall(r'[A-Z-А-ЯЁ+]', lines))