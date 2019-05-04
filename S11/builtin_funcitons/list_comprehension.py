lst = [1, 2, 3, 4, 5, 6, 7]

f = lambda x: x ** 2

out = [f(i) for i in lst]

print(out)


out = map(f, lst)
out2 = map(f, out)

print(list(out))
