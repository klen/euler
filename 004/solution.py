""" Project Euler problem #4. """

import itertools as it


def problem():
    u""" Solve the problem.

    A palindromic number reads the same both ways. The largest palindrome made
    from the product of two 2-digit numbers is 9009 = 91 * 99.

    Find the largest palindrome made from the product of two 3-digit numbers.

    Answer: 906609

    """
    return max([
        x for x in [
            a * b for a, b in it.product(range(999, 900, -1), repeat=2)]
        if is_palindrome(x)
    ])


def is_palindrome(num):
    """ Check for number is palindrome. """
    num = str(num)
    return num == num[::-1]


if __name__ == '__main__':
    print problem()
