import math


def is_prime(n):
    if n % 2 == 0:
        return False
    else:
        i = 3
        max = math.floor(math.sqrt(n))

        while i <= max:
            if n % i == 0:
                return False
            i += 2
        return True

def gen_prime():
    p = 3
    while 1:
        if is_prime(p):
            yield p
        p += 2

i = 1
g = gen_prime()

while i < 10001:
    n = g.next()
    i += 1

print n
