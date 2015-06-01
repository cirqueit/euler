def is_palindrome(n):
    s = str(n)
    for i in range(len(s)/2):
        if s[i] != s[-(i+1)]:
            return False
    return True

max = 0
min_biggest = 0
for a, b in [(x, y) for x in range(1000, 100, -1) for y in range(1000, 100, -1)]:
    if 1 or a > min_biggest and b > min_biggest:
        if is_palindrome(a*b):
            if a*b > max:
                if a > b:
                    min_biggest = b
                else: 
                    min_biggest = a
                max = a*b
print max
