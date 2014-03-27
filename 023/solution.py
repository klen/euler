""" Project Euler problem #23. """

import math as mt


def problem():
    """ Solve the problem.

    A perfect number is a number for which the sum of its proper divisors is
    exactly equal to the number. For example, the sum of the proper divisors of
    28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect
    number.

    A number n is called deficient if the sum of its proper divisors is less
    than n and it is called abundant if this sum exceeds n.

    As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest
    number that can be written as the sum of two abundant numbers is 24. By
    mathematical analysis, it can be shown that all integers greater than 28123
    can be written as the sum of two abundant numbers. However, this upper
    limit cannot be reduced any further by analysis even though it is known
    that the greatest number that cannot be expressed as the sum of two
    abundant numbers is less than this limit.

    Find the sum of all the positive integers which cannot be written as the
    sum of two abundant numbers.

    Answer: 4179871

    """
    limit = 28123

    def abundant_nums_sequence():
        for num in range(12, limit):
            if sum(divisors(num)) - num > num:
                yield num

    anums = list(abundant_nums_sequence())

    losers = set()
    for a in anums:
        for b in anums:
            if (a + b) > limit:
                break
            if a + b in losers:
                continue
            losers.add(a + b)

    return sum(n for n in range(1, limit + 1) if n not in losers)


def divisors(num):
    """ Get all divisors for number. """
    store = []
    for dd in range(1, int(mt.sqrt(num)) + 1):
        if num % dd == 0:
            yield dd
            if dd != num / dd:
                store.insert(0, num / dd)
    for dd in store:
        yield dd


if __name__ == '__main__':
    print problem()
