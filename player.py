import math

def first_digit(n, p):
    if p == 0:
        return 1
    if n == 0:
        return 0
    value = p*(math.log10(n))
    frac, whole = math.modf(value)
    return int(str(10**frac)[:1])

def len_digit(n, p):
    if n == 0:
        return 1
    return int(p*(math.log10(n))+1)

def last_digit(n1, n2):
    if n2 == 0:
        return 1
    if n1 == 0:
        return 0

    cycle = [n1 % 10]
    while True:
        nxt = (cycle[-1] * n1) % 10
        if nxt == cycle[0]:
            break
        cycle.append(nxt)
    return cycle[(n2 - 1) % len(cycle)]

def player(n, p):


    print(last_digit(n,p))
    print(len_digit(n,p))
    print(first_digit(n,p))

    # number = n**p

    # first = firstDigit(number)
    # # num = str(number)

    # length_of = (int)(math.log10(number)) + 1

    # last = number%10

    # print(first, length_of, last)


    # number = test['n']**test['p']
    # digits = (int)(math.log10(number))

    # n = (int)(n/pow(10, number))
player(0,0)
