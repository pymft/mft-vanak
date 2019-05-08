import time
import math
import random


def timer(f):
    def inner(*args):
        t1 = time.time()
        res = f(*args)
        t2 = time.time()
        print("Elapsed time = ", t2 - t1, "seconds")
        return res
    return inner


@timer
def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


@timer
def is_prime_new(n):
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True



num = 1398269
print(is_prime_new(num))
print(is_prime(num))
