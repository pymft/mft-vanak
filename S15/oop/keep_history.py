class MyClass:
    instances = []

    def __init__(self, name):
        self.name = name
        self.instances.append(self)
        if len(self.is_duplicated()) > 1:
            print(name, "is duplicated ")

    def is_duplicated(self):
        return [o for o in self.instances if o.name == self.name]

    @classmethod
    def count(cls):
        print(len(cls.instances))


a = MyClass("a")
b = MyClass("b")
c = MyClass("c")
MyClass("c")

MyClass.is_duplicated(a)
a.is_duplicated()

a.count()
MyClass.count()

