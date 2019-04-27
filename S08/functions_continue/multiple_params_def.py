def distance(p):
    dist_2 = p[0] ** 2 + p[1] ** 2
    res = dist_2 ** 0.5
    return res

point = (3, 4)
res_1 = distance((3, 4))
print(res_1)

new_point = (12, 5)
res_2 = distance(new_point)
print(res_2)
