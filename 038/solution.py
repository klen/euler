# coding: utf-8

""" Project Euler problem #X. """


def problem():
    u""" Solve the problem.

    Take the number 192 and multiply it by each of 1, 2, and 3:

    192 × 1 = 192
    192 × 2 = 384
    192 × 3 = 576
    By concatenating each product we get the 1 to 9 pandigital, 192384576.
    We will call 192384576 the concatenated product of 192 and (1,2,3)

    The same can be achieved by starting with 9 and multiplying by 1, 2, 3, 4,
    and 5, giving the pandigital, 918273645, which is the concatenated product
    of 9 and (1,2,3,4,5).

    What is the largest 1 to 9 pandigital 9-digit number that can be formed as
    the concatenated product of an integer with (1,2, ... , n) where n > 1?

    Answer: 932718654

    """
    return sorted(
        "%d%d" % (n, n * 2)
        for n in range(9123, 9876) if is_pandigital(n, n * 2))[-1]


def is_pandigital(*args):
    """ Check numbers is pandigital through 9. """
    return ''.join(sorted(x for arg in args for x in str(arg))) == '123456789'


if __name__ == '__main__':
    print problem()
