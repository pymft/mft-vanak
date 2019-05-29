a = 10
b = [0, 1, 2, 3, 4, 5]

try:
    num = a / b[4]
    print(num)
except ZeroDivisionError:
    print("you're not allowed to divide a number by zero!")
except IndexError:
    print("INDEX ERR")
finally:
    print("you will see me, it's inevitable!")
print("you're gonna see me, too")
