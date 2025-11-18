from abc import ABC, abstractmethod

class Shape(ABC): 
    def __init__(self, name, x):
        self.name = name
        self.x = x

    @abstractmethod
    def calculate_area(self):
        pass
    
    @abstractmethod
    def calculate_perimeter(self):
        pass
    
    def __info__(self):
        return f'Фигура: {self.name}'


class Square(Shape):
    def calculate_area(self):
       return self.x**2
    def calculate_perimeter(self):
        print(4*self.x)
    def __len__(self):
        self.calculate_perimeter()
    def __str__(self):
        print(f'Квадрат со стороной {self.x} см')
    def __eq__(self, other):
        return self.calculate_area() == other.calculate_area()

class Circle(Shape):
    def calculate_area(self):
        return 3.14*self.x**2
    def calculate_perimeter(self):
        print( 2*3.14*self.x)
    def __str__(self):
        print(f'Окружность со стороной {self.x} см')
    def __len__(self):
        self.calculate_perimeter()
    def __eq__(self, other):
        return self.calculate_area() == other.calculate_area()


class GeometryCalculator():
    @staticmethod
    def validate_positive(number):
        return number > 0
    @staticmethod
    def calculate_diagonal(length, width):
        return (length**2 + width**2)**0.5
    @staticmethod
    def is_larger(shape1, shape2):
        if shape1 > shape2: return 'Фигура 1 > Фигура 2'
        elif shape1 < shape2: return 'Фигура 2 > Фигура 1'
        else: return 'Фигуры равны'

a = Square('квадрат', 5)
b = Circle('круг', 5)
print(a.__eq__(b))

print(GeometryCalculator.validate_positive(-1))
print(GeometryCalculator.calculate_diagonal(3, 4))
print(GeometryCalculator.is_larger(a.calculate_area(), b.calculate_area()))