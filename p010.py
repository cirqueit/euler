import math

def is_prime(n):
    if n % 2 == 0:
        return False
    else:
        max = math.floor(math.sqrt(n))
        i = 3
        while i <= max:
            if n % i == 0:
                return False
            i += 2
        return True

def gen_prime():
    p = 3
    while True:
        if is_prime(p):
            yield p
        p += 2

p = 2
sum = 0
g = gen_prime()
while p < 2e6:
    sum += p
    p = g.next()

print sum
