# coding: utf-8

""" Project Euler problem #34. """

import math as mt


def problem():
    u""" Solve the problem.

    145 is a curious number, as 1! + 4! + 5! = 1 + 24 + 120 = 145.

    Find the sum of all numbers which are equal to the sum of the factorial of
    their digits.

    Note: as 1! = 1 and 2! = 2 are not sums they are not included.

    Answer: 40730

    """
    factorials = dict((str(n), mt.factorial(n)) for n in range(10))
    return sum(
        x for x in range(3, factorials['9'])
        if sum(factorials[n] for n in str(x)) == x
    )


if __name__ == '__main__':
    print problem()
