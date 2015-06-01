def fib_gen(max):
    i = 0
    a = 1
    b = 2

    while a < max:
        yield a
        b = a + b
        a = b - a
        i += 1

print reduce(lambda x, y: x + y, filter(lambda x: not (x % 2), fib_gen(4e6)))
