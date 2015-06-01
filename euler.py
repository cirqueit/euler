import copy 


def my_reduce(func, col, init=0):
    if not col:
        return init
    return my_reduce(func, col[1:], func(init, col[0]))


def my_filter(func, col, init=[]):
    if not col:
        return init
    if func(col[0]):
        init.append(col[0])

    return my_filter(func, col[1:], init)


def my_reduce_tco(func, col, init=0):
    i = 0 
    while i < len(col):
        init = func(init, col[i])
        i += 1

    return init


def my_filter_tco(func, col, init=[]):
    i = 0 
    while i < len(col):
        if func(col[i]):
            init.append(col[i])
        i += 1

    return init

def my_map_using_reduce(func, col, init=[]):
    def h(x, y):
        x.append(func(y))
        return x

    return my_reduce_tco(h, col, [])

def my_filter_using_reduce(func, col, init=[]):
    def h(x, y):
        if func(y):
            x.append(y)
        return x

    return my_reduce_tco(h, col, [])


if __name__ == "__main__":

    print my_reduce(lambda x, y: x + y, range(4), 0)
    print my_filter(lambda x: x % 3 == 0, range(4))
    print my_reduce_tco(lambda x, y: x + y, range(4), 0)
    print my_filter_tco(lambda x: x % 3 == 0, range(4))

    print my_map_using_reduce(lambda x: x * 3, range(4))
    print my_filter_using_reduce(lambda x: x % 3 == 0, range(4))
