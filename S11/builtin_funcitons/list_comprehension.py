lst = [1, 2, 3, 4, 5, 6, 7]
f = lambda x: x ** 2
#
# out = [f(1), f(2), f(3), f(4), f(5), f(6), f(7)]
#
#
out = []
for i in lst:
    out.append(i ** 2)

out = [i ** 2 for i in lst]

out = [f(i) for i in lst]

print(out)


out = map(f, lst)
out2 = map(f, out)

print(list(out))
