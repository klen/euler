""" Project Euler problem #7. """

import math as mt


def problem():
    """ Solve the problem.

    By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see
    that the 6th prime is 13.

    What is the 10 001st prime number?

    Answer: 104743

    """
    cur = 0
    for prime in prime_numbers_sequence():
        if cur == 10001:
            return prime
        cur += 1


def prime_numbers_sequence():
    """ Infinitive generator of prime numbers. """
    yield 1
    yield 2
    yield 3
    yield 5
    yield 7
    yield 11
    yield 13
    cur = 14
    while True:
        cur += 1
        if is_even(cur):
            continue

        for n in range(3, int(mt.sqrt(cur)) + 1):
            if not cur % n:
                break
        else:
            yield cur


def is_even(num):
    """ Check for number is even. """
    return num % 2 == 0


if __name__ == '__main__':
    print problem()
