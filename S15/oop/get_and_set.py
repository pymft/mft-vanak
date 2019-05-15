# https://stackoverflow.com/questions/3798835/understanding-get-and-set-and-python-descriptors
class Celsius:
    def __get__(self, instance, owner):
        return (instance.fahrenheit - 32) * (5 / 9)

    def __set__(self, instance, value):
        instance.fahrenheit = (value * (9 / 5)) + 32


class Temperature:
    celsius = Celsius()

    def __init__(self, fahrenheit):
        self.fahrenheit = fahrenheit


t1 = Temperature(32)

print(t1.fahrenheit,  t1.celsius)
t1.celsius = 100
print(t1.fahrenheit,  t1.celsius)
t1.fahrenheit = 100
print(t1.fahrenheit,  t1.celsius)

