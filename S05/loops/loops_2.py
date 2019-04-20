
i = 0
limit = 10
numbers = []

while i < limit:
    numbers.append(i)
    # numbers = numbers + [i]
    i = i + 1
    print(id(numbers), numbers)

print("sum ==", sum(numbers))

