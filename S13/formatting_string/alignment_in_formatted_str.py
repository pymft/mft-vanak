import random


data = []
for i in range(7,16):
    data.append([i, i**2, random.random(), random.randint(1, 10000)])

print(data)
for row in data:
    i, x, rand1, rand2 = row
    line = "{i:<5}|{x:>5}|{rand2:^10}|{rand1:^20.4f}|".format(i=i, x=x, rand1=rand1, rand2=rand2)
    print(line)