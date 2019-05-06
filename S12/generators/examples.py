def fib():
    a, b = 1, 1
    yield a
    yield b
    while True:
        a, b = b, a + b
        yield b


lst = []

for i in fib():
    lst.append(i)
    size = lst.__sizeof__()
    size_mb = size//1024
    print(size_mb, "kB")

    if size_mb > 1000:
        break


