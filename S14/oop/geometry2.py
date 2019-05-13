import math


class Parallelogram:
    def __init__(self, a, b, angle):
        print("Parallelogram")
        self.a = a
        self.b = b
        self.angle = angle

    def calc_area(self):
        rad = math.radians(self.angle)
        height = self.b * math.sin(rad)
        return self.a * height

    def calc_perimeter(self):
        return (self.a + self.b) * 2


class Rectangle(Parallelogram):
    def __init__(self, w, h):
        print("Rectangle")
        super().__init__(w, h, 90)


class Diamond(Parallelogram):
    def __init__(self, a, angle):
        print("Diamond")
        super().__init__(a, a, angle)


class Square(Rectangle):
    def __init__(self, a):
        print("Square")
        super().__init__(a, a)


s = Square(10)
print(s.__dict__)
print(s.calc_area())

