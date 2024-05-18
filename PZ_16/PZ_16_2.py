# Создайте базовый класс "Фигура" со свойствами "ширина" и "высота". От этого
# класса унаследуйте классы "Прямоугольник" и "Квадрат". Для класса "Квадрат"
# переопределите методы, связанные с вычислением площади и периметра.

class Figure:
    def __init__(self, weight, height):
        self.weight = weight
        self.height = height

    def area(self):
        return self.weight * self.height

    def perimeter(self):
        return 2 * (self.weight + self.height)


class Rectangle(Figure):
    pass


class Square(Figure):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side

    def perimeter(self):
        return self.side * 4


rect = Rectangle(5, 10)
print(f'Площадь прямоугольника - {rect.area()}\nПериметр прямоугольника - {rect.perimeter()}\n')

square = Square(5)
print(f'Площадь квадрата - {square.area()}\nПериметр квадрата - {square.perimeter()}')