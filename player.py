import mat

def firstDigit(n):
    digits = (int)(math.log10(n))

    n = (int)(n/pow(10, digits))

    return n

def player(n, p):
    number = n**p

    first = firstDigit(number)
    # num = str(number)

    length_of = (int)(math.log10(number)) + 1

    last = number%10

    print(first, length_of, last)

    # print([num[0],len(num),num[-1]])

player(5,2)