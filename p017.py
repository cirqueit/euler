l_ones = ['', 'one', 'two', 'three', 'four',
          'five', 'six', 'seven', 'eight', 'nine']

l_teens = ['', 'eleven', 'twelve', 'thirteen', 'fourteen',
           'fifteen', 'sixteen', 'seventeen', 'eighteen', 'nineteen']

l_tens = ['', 'ten', 'twenty', 'thirty', 'forty',
          'fifty', 'sixty', 'seventy', 'eighty', 'ninety']


def hundreds(n):
    n = (n % 1000) / 100

    if n < 100:
        return 0

    return len('hundred' + 'and') + ones(n)

def ones(n):
    n = n % 10
    return len(l_ones[n])

def teens(n):
    return len(l_teen[(n % 100)-10])

def tens(n):
    n = (n % 100) / 10
    return len(l_tens[n])

def alpha_length(n):
    h = hundreds(n)
    t = tens(n)
    o = ones(n)

    l = h + t + o

    if (n % 100) == 0:
        l = l - 3

    if (n % 100) > 10 and (n % 100) < 20:
        l = l - t - o + teens(n)

    return l

print alpha_length(10)
