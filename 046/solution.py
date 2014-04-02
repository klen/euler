# coding: utf-8

""" Project Euler problem #46. """

import itertools as it


def problem():
    u""" Solve the problem.

    It was proposed by Christian Goldbach that every odd composite number can
    be written as the sum of a prime and twice a square.

    9 = 7 + 2×12
    15 = 7 + 2×22
    21 = 3 + 2×32
    25 = 7 + 2×32
    27 = 19 + 2×22
    33 = 31 + 2×12

    It turns out that the conjecture was false.

    What is the smallest odd composite that cannot be written as the sum of a
    prime and twice a square?

    Answer: 5777

    """
    primes = list(primes_xrange(6962))
    numbers = set(n for n in range(9, 6962, 2) if n not in primes)
    squares = set(n**2*2 for n in range(1, 60))
    sums = set(sum(c) for c in it.product(primes, squares))
    return min(numbers.difference(sums))


def primes_xrange(stop):
    """ Get prime numbers below passed stop value. """
    primes = [True] * stop
    primes[0], primes[1] = [False, False]
    for idx, value in enumerate(primes):
        if value is True:
            primes[idx*2::idx] = [False] * ((stop - 1)/idx - 1)
            yield idx


if __name__ == '__main__':
    print problem()
