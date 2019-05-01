def my_range(*args):
    if len(args) == 3:
        start, stop, step = args
    elif len(args) == 2:
        start, stop = args
        step = 1
    elif len(args) == 1:
        start, stop, step = 0, args[0], 1
    else:
        return None

    lst = []
    while start < stop:
        lst.append(start)
        start += step

    return lst


print(my_range(8))  # [0, 1, 2, 3, 4, 5, 6, 7]
print(my_range(5, 8))  # [5, 6, 7]
print(my_range(3, 8, 2))  # [3, 5, 7]

print(my_range())  # None
