pow = 1000
print reduce(lambda x, y: x + int(y), list(str(2**pow)), 0)
