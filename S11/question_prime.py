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


members = 1000
lower_limit = 100000
upper_limit = 999999

data = [random.randint(lower_limit, upper_limit) for _ in range(members)]

# new approach
t1 = time.time()
primes = [i for i in data if is_prime_new(i)]
t2 = time.time()
print("Elapsed Time : ", t2 - t1, "seconds")


# check all the numbers in the range of 2 to n-1
t1 = time.time()
primes = [i for i in data if is_prime(i)]
t2 = time.time()
print("Elapsed Time : ", t2 - t1, "seconds")


# primes = filter(is_prime, data)

# print(primes)
