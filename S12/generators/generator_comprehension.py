def whatever():
    for i in range(1000000):
        yield i ** 2


res = (i ** 2 for i in range(1000000))

print(res)
print(res.__sizeof__())
