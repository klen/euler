""" Project Euler problem #15. """

import math as mt


def problem():
    """ Solve the problem.

    How many such lattice paths are there through a 20*20 grid?.

    http://mathworld.wolfram.com/BinomialCoefficient.html

    Answer: 137846528820

    """
    a = 20
    b = 20

    def binomial_coefficient(n, k):
        return mt.factorial(n) / (mt.factorial(n - k) * mt.factorial(k))

    return binomial_coefficient(a + b, a)


if __name__ == '__main__':
    print problem()
