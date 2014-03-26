""" Project Euler problem #16. """


def problem():
    """ Solve the problem.

    What is the sum of the digits of the number 2**1000?.

    The shift operator '<<' is used to shift each binary digit to the left,
    each shift being equivalent to a multiply by two.

    Answer: 1366

    """
    return sum(map(int, str(1 << 1000)))


if __name__ == '__main__':
    print problem()
