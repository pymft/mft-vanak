class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def calc_length(self):
        return (self.x ** 2 + self.y **2)**0.5

    def __repr__(self):
        return "VECTOR ({} , {})".format(self.x, self.y)

    def __add__(self, other):
        x_new = self.x + other.x
        y_new = self.y + other.y
        return Vector(x_new, y_new)




v1 = Vector(10, 30)

Vector.calc_length(v1)
v1.calc_length()

v1.calc_length()
v2 = Vector(20, 20)

v3 = v1 + v2
v1.__add__(v2)
Vector.__add__(v1, v2)

print(v1, v2, v3)

# print(Vector.__dict__)
# print(set(dir(v1))-set(dir(object)))
# print(set(dir(Vector))-set(dir(object)))
# Vector.calc_length()
# Vector.__dict__['calc_length']
# print(v1.x)
# print(Vector.__dict__)
# print(Vector.__dict__['calc_length'])
# Vector.calc_length(v1)

