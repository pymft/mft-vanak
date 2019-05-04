lst = [1, 2, 3, 4, 5, 6, 7, 8, 1, 2, 2,1 ,1 ,100, 1 ]
# f = lambda x: x % 2 == 0

out = [i ** 2 for i in lst if i % 2 == 0]
# out = [i for i in lst if i > 4]

print(out)