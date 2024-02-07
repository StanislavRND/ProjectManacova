# Из предложенного текстового файла (text18-31.txt) вывести на экран его содержимое,
# количество символов, принадлежащих к группе букв. Сформировать новый файл, в
# который поместить строку наименьшей длины.

with open('text30.txt', 'r', encoding='utf-16') as file:
    content = file.read()
    punctuation_count = sum(content.count(char) for char in ('!', ',', '-', ':', '.'))

    print(content + '\n')
    print(f'Количество знаков препинания: {punctuation_count}' )

author = 'Лермонтов'
name = 'Бородино'

with open('file_stix.txt', 'w', encoding='utf-16') as file.stix:
    file.stix.write(f'{content}\n\nАвтор: {author}\nПроизведение: {name}')

