import time

upper_limit = 100000001


#print("range size: ", rng.__sizeof__())
t1 = time.time()
rng = range(1, upper_limit)
t2 = time.time()

print("Elapsed Time : ", t2 - t1, "seconds")

#print("list  size: ", lst.__sizeof__())
t1 = time.time()
lst = list(range(1, upper_limit))
t2 = time.time()
print("Elapsed Time : ", t2 - t1, "seconds")
