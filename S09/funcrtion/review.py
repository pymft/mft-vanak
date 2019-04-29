num = 0

# nonlocal global
def factorial(n):
    global num
    num = num + 1
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
    return fact


def combination(m, n):
    value = factorial(m) / (factorial(m-n) * factorial(n))
    return int(value)


def pascal_row(n):
    lst = []
    for i in range(n+1):
        tmp = combination(n, i)
        lst.append(tmp)
    return lst


def triangle(rows):
    lst = []
    for i in range(rows+1):
        lst.append(pascal_row(i))

    return lst


# def full_t
#
print(pascal_row(15))
# res = triangle(9)
print(num)
# print(res)
#
# print(res[4][1])