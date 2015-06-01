sum = lambda x, y: x + y
square = lambda x: x**2

print reduce(sum, range(1, 101), 0)**2 - reduce(sum, map(square, range(1, 101)), 0)
