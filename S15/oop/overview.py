class Temperature:
    def __init__(self, fahrenheit):
        if type(fahrenheit) not in [float, int]:
            raise ValueError
        self.fahrenheit = fahrenheit

    @property
    def celsius(self):
        return (self.fahrenheit - 32) * (5 / 9)

    @celsius.setter
    def celsius(self, value):
        self.fahrenheit = (value * (9 / 5)) + 32


try:
    t1 = Temperature("a")
    print(t1.fahrenheit)
    print(t1.celsius)

    t1.celsius = 100
    print(t1.fahrenheit)
    print(t1.celsius)

    t1.fahrenheit = 100
    print(t1.fahrenheit)
    print(t1.celsius)
except ValueError:
    print("unsupported type for temperature")