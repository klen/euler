""" Project Euler problem #10. """

import math as mt


def problem():
    """ Solve the problem.

    The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
    Find the sum of all the primes below two million.

    Answer: 142913828922

    """
    return sum(prime_numbers(2000000))


def prime_numbers(_max):
    """ Get prime numbers below passed max. """
    a = [True] * _max
    for n in range(2, int(mt.sqrt(_max)) + 1):
        if not a[n]:
            continue
        for j in range(n ** 2, _max, n):
            a[j] = False
    return [n for n in range(2, _max) if a[n]]


if __name__ == '__main__':
    print problem()
