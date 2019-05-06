height = float(input("Height (m) : "))
mass = float(input("Mass (kg) : "))

bmi = mass / height ** 2

if bmi < 18.5:
    print("Underweight")
elif bmi < 25:
    print("Normal")
elif bmi < 30:
    print("Over-weight")
else:
    print("Obese")


