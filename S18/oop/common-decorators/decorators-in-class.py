import math

class Length:
    def __get__(self, instance, owner):
        return math.sqrt(instance.x ** 2 + instance.y ** 2)

    def __set__(self, instance, value):
        ratio = value / instance.length
        instance.x = instance.x * ratio
        instance.y = instance.y * ratio


class Vector:
    length = Length()

    def __init__(self, x, y):
        self.x, self.y = x, y



v1 = Vector(3, 4)
print(v1.length)
v1.length = 100
