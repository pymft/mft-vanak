def fact(n):
    if n == 0:
        return 1
    return n * fact(n - 1)


def my_sum(a, b, z=1, t=1):
    return (a ** z + b ** z) ** t


res = my_sum(2, 3, z=2, t=3)
print(res)

res = my_sum(2, 3, t=2, z=3)
print(res)
