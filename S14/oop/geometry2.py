class Rectangle:
    def __init__(self, w, h):
        self.width = w
        self.height = h

    def calc_area(self):
        print("rect")
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, a):
        # Rectangle.__init__(self, a, a)
        super().__init__(a, a)


    def calc_area(self):
        print("square")
        return super().calc_area()



s = Square(10)
print(s.__dict__)
print(s.calc_area())

