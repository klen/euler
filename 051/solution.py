# coding: utf-8

""" Project Euler problem #51. """

import math as mt


def problem():
    u""" Solve the problem.

    By replacing the 1st digit of the 2-digit number *3, it turns out that six
    of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

    By replacing the 3rd and 4th digits of 56**3 with the same digit, this
    5-digit number is the first example having seven primes among the ten
    generated numbers, yielding the family: 56003, 56113, 56333, 56443, 56663,
    56773, and 56993. Consequently 56003, being the first member of this
    family, is the smallest prime with this property.

    Find the smallest prime which, by replacing part of the number (not
    necessarily adjacent digits) with the same digit, is part of an eight prime
    value family.

    Answer: 121313

    """
    # First prime number>2 ends only with (1, 3, 5, 7, 9). Last digit cannot be
    # replaced.
    # Number of digits that need to be replaced are 3.

    masks = (
        "{1}{2}{0}{0}{0}{3}",
        "{1}{0}{2}{0}{0}{3}",
        "{1}{0}{0}{2}{0}{3}",
        "{1}{0}{0}{0}{2}{3}",
        "{0}{1}{2}{0}{0}{3}",
        "{0}{1}{0}{2}{0}{3}",
        "{0}{1}{0}{0}{2}{3}",
        "{0}{0}{1}{2}{0}{3}",
        "{0}{0}{1}{0}{2}{3}",
        "{0}{0}{0}{1}{2}{3}",
    )

    for num in range(101, 1000, 2):

        if not num % 5:
            continue

        for mask in masks:
            family = []
            for repeat in range(0, 10):
                number = int(mask.format(repeat, *str(num)))
                if len(str(number)) == 6 and is_prime(number):
                    family.append(number)
            if len(family) >= 8:
                return family[0]


def is_prime(num):
    """ Check number is prime. """
    if is_even(num) and num != 2 or num == 1:
        return False

    for dd in range(3, int(mt.sqrt(num)) + 1):
        if num % dd == 0:
            return False

    return True


def is_even(num):
    """ Check for number is even. """
    return num % 2 == 0


if __name__ == '__main__':
    print problem()
