""" Project Euler problem #21. """

import math as mt


def problem():
    """ Solve the problem.

    For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44,
    55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4,
    71 and 142; so d(284) = 220.

    Evaluate the sum of all the amicable numbers under 10000.

    Answer: 31626

    """
    def gen_amicable(_max):
        for n in range(2, _max):
            aa = sum(factors(n)[:-1])
            if aa == n:
                continue

            if sum(factors(aa)[:-1]) == n:
                yield n

    return sum(gen_amicable(10000))


def factors(num):
    """ Get all factors for number. """
    f1 = []
    f2 = []
    for dd in range(1, int(mt.sqrt(num)) + 1):
        if num % dd == 0:
            f1.append(dd)
            if dd != num / dd:
                f2.insert(0, num / dd)
    return f1 + f2


if __name__ == '__main__':
    print problem()
