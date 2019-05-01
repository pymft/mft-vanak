def my_sum(*args, **kwargs):
    print(args)
    print(kwargs)
    return sum(args)


# args = (1, 2, 3, 4, 5, 6, 7,)
# kwargs = {"constant":1}
res = my_sum(1, 2, 3, 4, 5, 6, 7, constant=1, mode='whatever')
print(res)
