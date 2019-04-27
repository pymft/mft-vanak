distance = lambda p: (p[0] ** 2 + p[1] ** 2) ** 0.5
distance_new = lambda x, y: (x ** 2 + y ** 2) ** 0.5


res_1 = distance_new(3, 4)

res_2 = distance_new(12, 5)

print(res_1, res_2)


