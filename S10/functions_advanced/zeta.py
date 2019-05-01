import math


def zeta(s, limit=1000):
    res = 0
    for i in range(1, limit+1):
        res += 1 / (i ** s)
    return res


val = zeta(2)


pi_approximate = math.sqrt(val * 6)
print(pi_approximate)
print(math.pi)
err = 100 * (math.pi - pi_approximate) / math.pi
print(err)
