x = [6, 8, 3, 2, 5]
y = [5, 2, 3, 1, 7]

# for i in range(len(x)):
#     print(x[i], y[i])

for i, j in zip(x, y):
    res = (i ** 2 + j ** 2) ** 0.5
    print(i, j, "--->", res)
