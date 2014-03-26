""" Project Euler problem #9. """


def problem():
    """ Solve the problem.

    There exists exactly one Pythagorean triplet for which a + b + c = 1000.
    Find the product abc..

    Answer: 31875000

    """
    for a in range(1, 380):
        for b in range(a):
            if a + b + (a**2 + b**2)**0.5 == 1000:
                return int(a * b * (a**2 + b**2)**0.5)


if __name__ == '__main__':
    print problem()
