class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        x_new = self.x + other.x
        y_new = self.y + other.y
        return Vector(x_new, y_new)

    def __mul__(self, other):
        if isinstance(other, (int, float)):
            x_new = self.x * other
            y_new = self.y * other
            return Vector(x_new, y_new)

    def __repr__(self):
        return "\033[31;2m({x}, {y})\033[0m".format(x=self.x, y=self.y)

    def __str__(self):
        return "({x}, {y})".format(x=self.x, y=self.y)

    def __getitem__(self, item):
        if item == 0:
            return self.x
        elif item == 1:
            return self.y

    def __setitem__(self, item, value):
        if item == 0:
            self.x = value
        elif item == 1:
            self.y = value


v1 = Vector(2, 3)
v2 = Vector(6, 2)

v1[1] = 100
print(v1[0], v1[1])

# v3 = v1 * 10.2
# print(v3)
