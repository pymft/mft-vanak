import time
import math
import random


def is_prime(n):
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


def is_prime_new(n):
    for i in range(2, int(math.sqrt(n))):
        if n % i == 0:
            return False
    return True

prime = 1398269

# new approach
t1 = time.time()
res = is_prime_new(prime)
t2 = time.time()
print("Elapsed Time : ", t2 - t1, "seconds", res)


# check all the numbers in the range of 2 to n-1
t1 = time.time()
res = is_prime(prime)
t2 = time.time()
print("Elapsed Time : ", t2 - t1, "seconds", res)


# primes = filter(is_prime, data)

# print(primes)
