""" Project Euler problem #12. """

import math as mt


def problem():
    """ Solve the problem.

    What is the value of the first triangle number to have over five hundred
    divisors?

    Answer: 76576500

    """
    x = 0
    while True:
        x += 1
        half, odd = (x/2, x + 1) if x % 2 == 0 else ((x + 1)/2, x)
        if len(factors(half)) * len(factors(odd)) >= 500:
            return half * odd


def factors(num):
    """ Get all factors for number. """
    f1 = []
    f2 = []
    for dd in range(1, int(mt.sqrt(num)) + 1):
        if num % dd == 0:
            f1.append(dd)
            if dd != num / dd:
                f2.insert(0, num / dd)
    return f1 + f2


if __name__ == '__main__':
    print problem()
