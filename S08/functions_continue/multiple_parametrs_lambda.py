distance = lambda p: (p[0] ** 2 + p[1] ** 2) ** 0.5

point = (3, 4)
res_1 = distance(point)

new_point = (12, 5)
res_2 = distance(new_point)

print(res_1, res_2)


