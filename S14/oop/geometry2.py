import math


class Area:
    def __get__(self, instance, owner):
        if type(owner) == Circle:
            return math.pi * self.radius ** 2
        rad = math.radians(instance.angle)
        height = instance.b * math.sin(rad)
        return instance.a * height


class Perimeter:
    def __get__(self, instance, owner):
        return (instance.a + instance.b) * 2


# TO READ : abstract class
class Geometry:
    area = Area()
    perimeter = Perimeter()


class Circle(Geometry):
    def __init__(self, r):
        self.radius = r


class Parallelogram(Geometry):
    def __init__(self, a, b, angle):
        print("Parallelogram")
        self.a = a
        self.b = b
        self.angle = angle


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
# print(s.__dict__)
print(s.area, s.perimeter)
