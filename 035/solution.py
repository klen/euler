# coding: utf-8

""" Project Euler problem #35. """

import math as mt
import re


def problem():
    """ Solve the problem.

    The number, 197, is called a circular prime because all rotations of the
    digits: 197, 971, and 719, are themselves prime.

    There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37,
    71, 73, 79, and 97.

    How many circular primes are there below one million?

    Answer: 55

    """
    cprime_re = re.compile(r'^[1379]+$')

    def cprimes_xrange(stop):
        for prime in primes_xrange(stop):
            sprime = str(prime)

            if len(sprime) == 1:
                yield prime
                continue

            if not cprime_re.match(sprime):
                continue

            for _ in range(0, len(sprime)):
                if not is_prime(int(sprime)):
                    break
                sprime = sprime[1:] + sprime[0]

            else:
                yield prime

    return len(list(cprimes_xrange(10**6)))


def primes_xrange(stop):
    """ Get prime numbers below passed stop value. """
    primes = [True] * stop
    primes[0], primes[1] = [False, False]
    for idx, value in enumerate(primes):
        if value is True:
            primes[idx*2::idx] = [False] * ((stop - 1)/idx - 1)
            yield idx


def is_prime(num):
    """ Check number is prime. """
    if is_even(num) and num != 2:
        return False

    for dd in range(3, int(mt.sqrt(num)) + 1):
        if num % dd == 0:
            return False

    return True


def is_even(num):
    """ Check for number is even. """
    return num % 2 == 0


if __name__ == '__main__':
    print problem()
