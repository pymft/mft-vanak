def loop(n):
    lst = list(range(n))
    for i in lst:
        yield i+1


gen = loop(1000)
print(gen.__sizeof__())
for i in gen:
    print(i)
