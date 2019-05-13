class Rectangle:
    name = "rectangle"     # class Variable

    def __init__(self, w, h):
        self.width = w            # instance variable
        self.height = h

    @property
    def area(self):     # instance method
        return self.width * self.height

    @area.setter
    def area(self, value):
        ratio2 = value / self.area
        ratio = ratio2 ** 0.5
        self.width = self.width * ratio
        self.height = self.height * ratio




r1 = Rectangle(1, 2)

r1.width = 4
print(r1.area)
r1.area = 32
print(Rectangle.__dict__)



# print(r1.name, r2.name, Rectangle.name)
# r1.name = "RECTANGLE"
# print(r1.name, r2.name, Rectangle.name)
# Rectangle.name = "Rect"
# print(r1.name, r2.name, Rectangle.name)
#

# print(Rectangle.name, '|', Rectangle.__dict__.keys())
# print(r1.name, '|', r1.width, r1.height, r1, r1.__dict__)
# r1.area = 40
# r1.name = "RECTANGLE"
# print(r1.name, '|', r1.width, r1.height, r1, r1.__dict__)

