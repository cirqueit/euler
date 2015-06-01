mul3or5 = lambda x: not (x % 3) or not (x % 5)
ans =  reduce(lambda x, y: x + y, filter(mul3or5, range(1000)), 0)
print ans

