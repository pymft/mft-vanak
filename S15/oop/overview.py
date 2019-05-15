class Temperature:
    def __init__(self, fahrenheit):
        self.fahrenheit = fahrenheit

    @property
    def celsius(self):
        return (self.fahrenheit - 32) * (5 / 9)

    @celsius.setter
    def celsius(self, value):
        self.fahrenheit = (value * (9 / 5)) + 32


t1 = Temperature(32)
print(t1.fahrenheit)
print(t1.celsius)

t1.celsius = 100
print(t1.fahrenheit)
print(t1.celsius)

t1.fahrenheit = 100
print(t1.fahrenheit)
print(t1.celsius)