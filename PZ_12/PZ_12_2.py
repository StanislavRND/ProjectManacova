# Составить генератор (yield), который преобразует все буквенные символы в
# заглавные.
from string import ascii_lowercase

def uppercase_gen(text):
    for char in text:
        if char in ascii_lowercase:
            yield char.upper()
        else:
            yield char

string = 'I love learning programming, I enjoy it'
uppercase_text = ''.join(uppercase_gen(string))
print(uppercase_text)

# def uppercase_gen(text):
#     return (char.upper() if char in ascii_lowercase else char for char in text)
#
# string = 'I love learning programming, I enjoy it'
# uppercase_text = ''.join(uppercase_gen(string))
# print(uppercase_text) 

