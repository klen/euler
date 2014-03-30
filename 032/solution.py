# coding: utf-8

""" Project Euler problem #X. """

import itertools as it


def problem():
    u""" Solve the problem.

    We shall say that an n-digit number is pandigital if it makes use of all
    the digits 1 to n exactly once; for example, the 5-digit number, 15234, is
    1 through 5 pandigital.

    The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing
    multiplicand, multiplier, and product is 1 through 9 pandigital.

    Find the sum of all products whose multiplicand/multiplier/product identity
    can be written as a 1 through 9 pandigital.

    Answer: 45228

    """
    digits = '123456789'
    products = set()

    for size in (1, 2):
        for multiplicand in it.permutations(digits, size):
            dd = [d for d in digits if d not in multiplicand]
            for multiplier in it.permutations(dd, 5 - size):
                m1 = int(''.join(multiplicand))
                m2 = int(''.join(multiplier))
                product = m1 * m2
                if is_pandigital(m1, m2, product):
                    products.add(product)

    return sum(products)


def is_pandigital(*args):
    """ Check numbers is pandigital through 9. """
    return ''.join(sorted(x for arg in args for x in str(arg))) == '123456789'


if __name__ == '__main__':
    print problem()
