from math import floor, sqrt

def num_divisors(n):
    max = floor(sqrt(n))
    i = 1
    divisors = 0
    while i < max:
        if n % i == 0:
            divisors += 2
        i += 1
    if n % max == 0:
        divisors += 1

    return divisors

def gen_triangle():
    tri = 1
    i = 1
    while True:
        yield tri
        i += 1
        tri += i

g = gen_triangle()

while True:
    tri = g.next()
    if num_divisors(tri) > 500:
        break

print tri
