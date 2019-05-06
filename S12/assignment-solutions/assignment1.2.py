units = input("use (SI) units? (y/n) ")

if units == 'n':
    ratio = 730
    height = float(input("Height (in) : "))
    mass = float(input("Mass (lbs) : "))
else:
    ratio = 730
    height = float(input("Height (m) : "))
    mass = float(input("Mass (kg) : "))

bmi = mass / height ** 2
bmi *= ratio

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Over-weight")
else:
    print("Obese")
