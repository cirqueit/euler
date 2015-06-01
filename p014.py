def is_even(n):
    return n % 2 == 0

def collatz(n, col=[]):
    col.append(n)

    if n == 1:
        return col

    if is_even(n):
        return collatz(n/2, col)
    else:
        return collatz(3*n+1, col)

def collatz_iterative(n):
    col = []

    while n != 1:
        col.append(n)
        if is_even(n):
            n = n/2
        else:
            n = 3*n+1
    col.append(n)
    return col

max = 0
# memo = [-1]
# for i in range(1, int(1e6)):
#     memo.append(-1)

for i in range(1, int(1e6)):
    # if memo[i] != -1:
    #     l = memo[i]
    # else:
    #     l = len(collatz_iterative(i))
    #     memo[i] = l

    l = len(collatz_iterative(i))
    if l > max:
        max = l
        print i

