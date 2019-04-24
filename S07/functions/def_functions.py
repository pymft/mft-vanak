# f = lambda y: y ** 2



def f(y):
    res = y ** 2
    return res

def fact(n):
    s = 1
    for i in range(1, n+1):
        s *= i
    return s

print(fact(10))

res = fact(10) / (fact(10-3)*fact(3))
print(res)
