class Person:
    def set_name(self, name):
        self.name = name

    def walk(self):
        print(self.name, "walks")


p1 = Person()
p3 = Person()
p2 = Person()

print(p1)
print(p2)
print(p3)

p1.set_name("Jack")
p2.set_name("John")
p3.set_name("James")

p1.walk()
p2.walk()
p3.walk()
