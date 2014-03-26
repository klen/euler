""" Project Euler problem #5. """

from fractions import gcd


def problem():
    """ Solve the problem.

    2520 is the smallest number that can be divided by each of the numbers
    from 1 to 10 without any remainder.

    What is the smallest positive number that is evenly divisible by all of
    the numbers from 1 to 20?

    Answer: 232792560

    """
    def _lowest_common_multi(a, b):
        return a * b // gcd(a, b)
    return reduce(_lowest_common_multi, range(1, 21))


if __name__ == '__main__':
    print problem()
