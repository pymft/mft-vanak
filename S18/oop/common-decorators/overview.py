class MyClass:
    instances = []

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.instances.append(self)

    def say_hello(self):
        return "hello"


mc1 = MyClass(1, 2)
mc2 = MyClass(1234, 2342)
mc3 = MyClass(121, 234)
print(mc1.instances)


# mc = MyClass(10, 20)
# # mc = MyClass.__new__()
# # mc.__init__(10, 20)
# mc.say_hello()
