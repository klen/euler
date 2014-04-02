# coding: utf-8

""" Project Euler problem #50. """

import itertools as it


def problem():
    u""" Solve the problem.

    The prime 41, can be written as the sum of six consecutive primes:

    41 = 2 + 3 + 5 + 7 + 11 + 13

    This is the longest sum of consecutive primes that adds to a prime below
    one-hundred.

    The longest sum of consecutive primes below one-thousand that adds to a
    prime, contains 21 terms, and is equal to 953.

    Which prime, below one-million, can be written as the sum of the most
    consecutive primes?

    Answer: 997651

    """
    limit = 10**6
    primes = list(primes_xrange(limit))
    sums = [0]
    while sums[-1] < limit:
        sums.append(sums[-1] + primes[len(sums) - 1])
    return max(
        set(a - b for b, a in it.combinations(sums[:-1], 2)) & set(primes))


def primes_xrange(a, b=0):
    """ Get prime numbers below passed stop value. """
    stop, start = (a, b) if not b else (b, a)
    primes = [True] * stop
    primes[0], primes[1] = [False, False]
    for idx, value in enumerate(primes):
        if value is True:
            primes[idx*2::idx] = [False] * ((stop - 1)/idx - 1)
            if idx >= start:
                yield idx


if __name__ == '__main__':
    print problem()
