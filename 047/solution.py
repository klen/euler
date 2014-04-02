# coding: utf-8

""" Project Euler problem #47. """

import math as mt


def problem():
    u""" Solve the problem.

    The first two consecutive numbers to have two distinct prime factors are:

    14 = 2 × 7
    15 = 3 × 5

    The first three consecutive numbers to have three distinct prime factors
    are:

    644 = 2² × 7 × 23
    645 = 3 × 5 × 43
    646 = 2 × 17 × 19.

    Find the first four consecutive integers to have four distinct prime
    factors. What is the first of these numbers?

    Answer: 134043

    """
    for num in range(647, 150000, 4):
        if len(set(prime_factors(num))) == 4:
            if len(set(prime_factors(num + 1))) == 4:
                if len(set(prime_factors(num + 2))) == 4:
                    if len(set(prime_factors(num + 3))) == 4:
                        return num


def prime_factors(num):
    """ Get all prime factors for number. """
    while num % 2 == 0:
        yield 2
        num //= 2

    f, limit = 3, mt.sqrt(num + 1)
    while f <= limit:
        while num % f == 0:
            yield f
            num //= f
            limit = mt.sqrt(num + f)
        f += 2

    yield num


if __name__ == '__main__':
    print problem()
