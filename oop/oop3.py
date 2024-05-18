class Comment:
    def __init__(self, text):
        self.text = text

    @staticmethod
    def merge_comments(first, second):
        return f'{first} {second}'

my_comments = Comment('My coment')

a_1 = Comment.merge_comments('Привет,', 'студент')
a_2 = Comment.merge_comments('Great', 'OK')
print(a_1)
print(a_2)

# Атрибуты класса

class Comm:
    count = 0  # Атрибут (с ним можно взаимодействовать, но он не является частью(?) класса)
    def __init__(self, text):  # Метод
        self.text = text  # Атрибут (он прикреплен к классу и является его частью, с ним также можно взаимодействовать)

    def upcount(self):  # Метод
        self.count += 1

my_comm = Comm('My comm')
"""my_comm.upcount()
print(my_comm.count)
print(my_comm.__dict__)"""

my_comm.count = 17
print(my_comm.count)  # Изменилось значение только в экземпляре
print(Comm.count)  # В классе значение не изменилось
print(my_comm.__dict__)
print(Comm.__dict__)