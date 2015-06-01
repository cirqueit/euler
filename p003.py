import math

def is_prime(n):
    if not (n % 2):
        return False
    else:
        x = 3
        max = int(math.floor(math.sqrt(n)))
        while x <= max:
            if not (n % x):
                return False
            x += 2
        return True


def prime_gen():
    n = 3
    while 1:
        while not is_prime(n):
            n += 1
        yield n
        n += 1


def prime_factors(n):
    g = prime_gen()
    p = 2
    factors = []

    max = int(math.floor(math.sqrt(n)))
    while p <= max:
        if not (n % p):
            factors.append(p)
        p = g.next()
    return factors


print prime_factors(600851475143)
