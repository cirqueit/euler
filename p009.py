def pythagorean_triplet():
    for a in range(1, 1000):
        for b in range(a, 1000):
            for c in range(b, 1000):
                if a + b + c == 1000:
                    if a**2 + b**2 == c**2:
                         return a, b, c
    return None

a, b, c = pythagorean_triplet()
print a*b*c
