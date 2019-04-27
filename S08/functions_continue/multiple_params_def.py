def distance(p):
    dist_2 = p[0] ** 2 + p[1] ** 2
    res = dist_2 ** 0.5
    return res


def distance_new(x, y):
    dist_2 = x ** 2 + y ** 2
    res = dist_2 ** 0.5
    return res


res_1 = distance_new(3, 4)
print(res_1)

res_2 = distance_new(12, 5 )
print(res_2)
