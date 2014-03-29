# coding: utf-8

""" Project Euler problem #33. """

import operator as op


def problem():
    """ Solve the problem.

    The fraction 49/98 is a curious fraction, as an inexperienced mathematician
    in attempting to simplify it may incorrectly believe that 49/98 = 4/8,
    which is correct, is obtained by cancelling the 9s.

    We shall consider fractions like, 30/50 = 3/5, to be trivial examples.

    There are exactly four non-trivial examples of this type of fraction, less
    than one in value, and containing two digits in the numerator and
    denominator.

    If the product of these four fractions is given in its lowest common terms,
    find the value of the denominator.

    Answer:

    """
    return reduce(op.mul, (
        float(a * 10 + b) / (c * 10 + a)
        for a in range(1, 10)
        for b in range(1, 10)
        for c in range(1, b)
        if (a * 10 + b) * c == (c * 10 + a) * b))


if __name__ == '__main__':
    print problem()
