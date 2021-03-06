""" Project Euler problem #22. """

import os.path as op


def problem():
    """ Solve the problem.

    Using names.txt, a 46K text file containing over five-thousand first names,
    begin by sorting it into alphabetical order. Then working out the
    alphabetical value for each name, multiply this value by its alphabetical
    position in the list to obtain a name score.

    For example, when the list is sorted into alphabetical order, COLIN, which
    is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So,
    COLIN would obtain a score of 938 * 53 = 49714.

    What is the total of all the name scores in the file?

    Answer: 871198282

    """
    path = op.join(op.dirname(__file__), 'names.txt')
    with open(path, 'r') as ff:
        names = [n.strip('"') for n in ff.read().split(',')]
        names = sorted(names)

    return sum(
        sum((ord(c) - 64) for c in name) * pos
        for pos, name in enumerate(names, 1))


if __name__ == '__main__':
    print problem()
