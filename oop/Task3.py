class Person:
    count = 0

    def __init__(self, name):
        self.name = name
        Person.count += 1

    @staticmethod
    def total_people():
        return f'Создано {Person.count} экземпляров класса!'

p1 = Person('first')
p2 = Person('second')
p3 = Person('third')
p4 = Person('fird')
print(Person.total_people())