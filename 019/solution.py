""" Project Euler problem #19. """

import datetime as dt


def problem():
    """ Solve the problem.

    How many Sundays fell on the first of the month during the twentieth
    century (1 Jan 1901 to 31 Dec 2000)?

    Answer: 171

    """
    seek = dt.datetime(1901, 1, 6)
    end = dt.datetime(2000, 12, 31)
    _sum = 0
    while seek <= end:
        seek += dt.timedelta(days=7)
        _sum += int(seek.day == 1)

    return _sum


if __name__ == '__main__':
    print problem()
