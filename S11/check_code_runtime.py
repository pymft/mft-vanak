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


def is_prime_3(n):
    """
    Miller-Rabin primality test.

    A return value of False means n is certainly not prime. A return value of
    True means n is very likely a prime.
    """
    if n != int(n):
        return False
    n = int(n)
    # Miller-Rabin test for prime
    if n == 0 or n == 1 or n == 4 or n == 6 or n == 8 or n == 9:
        return False

    if n == 2 or n == 3 or n == 5 or n == 7:
        return True
    s = 0
    d = n - 1
    while d % 2 == 0:
        d >>= 1
        s += 1
    assert (2 ** s * d == n - 1)

    def trial_composite(a):
        if pow(a, d, n) == 1:
            return False
        for i in range(s):
            if pow(a, 2 ** i * d, n) == n - 1:
                return False
        return True

    for i in range(8):  # number of trials
        a = random.randrange(2, n)
        if trial_composite(a):
            return False

    return True

prime =  85053461164796801949539541639542805770666392330682673302530819774105141531698707146930307290253537320447270457

# miller approach
t1 = time.time()
res = is_prime_3(prime)
t2 = time.time()
print("Elapsed Time : ", t2 - t1, "seconds", res)


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
