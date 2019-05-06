def fib(n):
    a, b = 1, 1
    yield a
    yield b
    i = 2
    while i < n:
        a, b = b, a + b
        i += 1
        yield b

# for i in fib(10):




fib_gen_1 = fib(10)
fib_gen_2 = fib(10)

print(next(fib_gen_1))   # 1
print(next(fib_gen_1))   # 1
print(next(fib_gen_1))   # 2
print(next(fib_gen_1))   # 3
print(next(fib_gen_2))   # 1

print(list(fib_gen_1))
print(list(fib_gen_2))

