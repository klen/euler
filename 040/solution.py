# coding: utf-8

""" Project Euler problem #40. """


def problem():
    u""" Solve the problem.

    An irrational decimal fraction is created by concatenating the positive
    integers:

    0.12345678910(1)112131415161718192021...

    It can be seen that the 12th digit of the fractional part is 1.

    If dn represents the nth digit of the fractional part, find the value of
    the following expression.

    d1 × d10 × d100 × d1000 × d10000 × d100000 × d1000000

    Answer: 210

    """
    stops = [1, 10, 100, 1000, 10000, 10**5, 10**6]
    length, x, prod = 0, 0, 1
    while stops:
        x += 1
        length += len(str(x))
        if length >= stops[0]:
            prod *= int(str(x)[stops[0] - length - 1])
            stops.pop(0)
    return prod


if __name__ == '__main__':
    print problem()
