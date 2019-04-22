n = 0
limit = 10
while n < 10:
    n = n + 1
    pattern = "*" * (2*n+1)
    print(pattern.center(2 * limit + 1))


