#            <----function--->  <-iterator->
res = filter(lambda x: x < 100, range(10900))
print(list(res))

f = lambda x: x < 100
rng = range(10900)

res = filter(f, rng)
