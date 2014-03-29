# coding: utf-8

""" Project Euler problem #37. """

import math as mt
import re


def problem():
    """ Solve the problem.

    The number 3797 has an interesting property. Being prime itself, it is
    possible to continuously remove digits from left to right, and remain prime
    at each stage: 3797, 797, 97, and 7. Similarly we can work from right to
    left: 3797, 379, 37, and 3.

    Find the sum of the only eleven primes that are both truncatable from left
    to right and right to left.

    NOTE: 2, 3, 5, and 7 are not considered to be truncatable primes.

    Answer: 748317

    """
    bless_prime_re = re.compile(r'^[1379]+$')

    _sum = 0
    for prime in primes_xrange(10**6):
        sprime = str(prime)
        if not bless_prime_re.match(sprime) and prime > 300 or prime < 10:
            continue
        for n in range(len(sprime) - 1, 0, -1):
            if not is_prime(int(sprime[n:])) or not is_prime(int(sprime[:n])):
                break
        else:
            _sum += prime

    return _sum


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
    if is_even(num) and num != 2 or num == 1:
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
