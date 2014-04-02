# coding: utf-8

""" Project Euler problem #X. """

import itertools as it


def problem():
    u""" Solve the problem.

    The number, 1406357289, is a 0 to 9 pandigital number because it is made up
    of each of the digits 0 to 9 in some order, but it also has a rather
    interesting sub-string divisibility property.

    Let d1 be the 1st digit, d2 be the 2nd digit, and so on. In this way,
    we note the following:

    d2*d3*d4=406 is divisible by 2
    d3*d4*d5=063 is divisible by 3
    d4*d5*d6=635 is divisible by 5
    d5*d6*d7=357 is divisible by 7
    d6*d7*d8=572 is divisible by 11
    d7*d8*d9=728 is divisible by 13
    d8*d9*d10=289 is divisible by 17

    Find the sum of all 0 to 9 pandigital numbers with this property.

    Answer: 16695334890

    """
    primes = list(enumerate((2, 3, 5, 7, 11, 13, 17), 1))
    _sum = 0
    for pandigital in it.permutations('0123456789', 10):
        if any(int(''.join(pandigital[num:num + 3])) % prime
               for num, prime in primes):
            continue
        _sum += int(''.join(pandigital))
    return _sum


def is_pandigital(*args):
    """ Check numbers is pandigital through 9. """
    return '123456789'.startswith(
        ''.join(sorted(x for arg in args for x in str(arg))))


if __name__ == '__main__':
    print problem()
