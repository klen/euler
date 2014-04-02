# coding: utf-8

""" Project Euler problem #42. """

import os.path as op


def problem():
    u""" Solve the problem.

    The nth term of the sequence of triangle numbers is given by, tn = ½n(n+1);
    so the first ten triangle numbers are:

    1, 3, 6, 10, 15, 21, 28, 36, 45, 55, ...

    By converting each letter in a word to a number corresponding to its
    alphabetical position and adding these values we form a word value.
    For example, the word value for SKY is 19 + 11 + 25 = 55 = t10. If the word
    value is a triangle number then we shall call the word a triangle word.

    Using words.txt, a 16K text file containing nearly two-thousand common
    English words, how many are triangle words?

    Answer:

    """
    path = op.join(op.dirname(__file__), 'words.txt')
    with open(path, 'r') as ff:
        words = [n.strip('"') for n in ff.read().split(',')]
    triangle_nums = [triangle_num(x) for x in range(20)]
    return len([
        w for w in [sum(ord(c) - 64 for c in word) for word in words]
        if w in triangle_nums])


def triangle_num(n):
    """ Return nth triangle number. """
    return n * (n + 1) / 2


if __name__ == '__main__':
    print problem()
