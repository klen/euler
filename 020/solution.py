""" Project Euler problem #20. """

import math as mt


def problem():
    """ Solve the problem.

    Find the sum of the digits in the number 100!

    Answer: 648

    """
    num = mt.factorial(100)
    return sum(map(int, str(num)))


if __name__ == '__main__':
    print problem()
