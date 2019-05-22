class MyClass:
    instances = {}

    def __new__(cls, *args, **kwargs):
        # print("hello from __new__", cls, args, kwargs)
        name = args[0]
        if name in cls.instances:
            return cls.instances[name]
        return super().__new__(cls)

    def __init__(self, name):
        self.name = name
        self.instances.update({name: self})



m = MyClass("name-sample")
n = MyClass("name-sample")
# print(m, type(m))
print(id(m))
print(id(n))
