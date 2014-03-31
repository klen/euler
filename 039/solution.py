# coding: utf-8

""" Project Euler problem #39. """

import operator as op
from collections import defaultdict


def problem():
    u""" Solve the problem.

    If p is the perimeter of a right angle triangle with integral length sides,
    {a,b,c}, there are exactly three solutions for p = 120.

    {20,48,52}, {24,45,51}, {30,40,50}

    For which value of p <= 1000, is the number of solutions maximised?

    Answer: 840

    """
    solutions = defaultdict(int)
    for p in range(2, 1002, 2):
        for a in range(2, p / 2):
            if not p * (p - 2 * a) % (2 * (p - a)):
                solutions[p] += 1

    return max(solutions.items(), key=op.itemgetter(1))[0]


if __name__ == '__main__':
    print problem()
