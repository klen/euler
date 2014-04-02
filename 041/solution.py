# coding: utf-8

""" Project Euler problem #41. """

import math as mt


def problem():
    u""" Solve the problem.

    We shall say that an n-digit number is pandigital if it makes use of all
    the digits 1 to n exactly once. For example, 2143 is a 4-digit pandigital
    and is also prime.

    What is the largest n-digit pandigital prime that exists?

    Solution: any integer divisible by 3 or 9 when sum of digits is divisible
    by 3 or 9. So it's mean we could check only range (4321, 7654321), because
    1+2+3+4+5+6+7+8=36

    Answer: 7652413

    """
    for x in xrange(7654321, 4321, -2):
        if is_pandigital(x) and is_prime(x):
            return x


def is_pandigital(*args):
    """ Check numbers is pandigital through 9. """
    return '123456789'.startswith(
        ''.join(sorted(x for arg in args for x in str(arg))))


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
