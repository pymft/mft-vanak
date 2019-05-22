class KeepHistory:
    instances = []

    def __init__(self, name):
        self.name = name
        self.instances.append(self)

    @classmethod
    def count_instances(cls):
        return len(cls.instances)

    @staticmethod
    def say_hello():
        return "hello"


a = KeepHistory("a")
b = KeepHistory("b")
c = KeepHistory("c")
print(a.count_instances())
print(b.count_instances())
print(KeepHistory.count_instances())