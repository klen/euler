# coding: utf-8

""" Project Euler problem #36. """


def problem():
    u""" Solve the problem.

    The number, 197, is called a circular prime because all rotations of the
    digits: 197, 971, and 719, are themselves prime.

    There are thirteen such primes below 100: 2, 3, 5, 7, 11, 13, 17, 31, 37,
    71, 73, 79, and 97.

    How many circular primes are there below one million?

    Answer: 872187

    """
    _sum = 0
    for num in range(1, 10**6):
        if is_palindrome(num):
            bnum = str(bin(num))[2:]
            if bnum == bnum[::-1]:
                _sum += num

    return _sum


def is_palindrome(num):
    """ Check for number is palindrome. """
    num = str(num)
    return num == num[::-1]


if __name__ == '__main__':
    print problem()
