pos = (0, 0)
goal = (2, 2)

def next(current):
    possible = []
    x0, xy = current
    x, y = goal

    if x0 + 1 < x:
        possible.append((x0+1, y0))
    if y0 + 1 < y:
        possible.append((x0, y0+1))

    return possible



    

    


