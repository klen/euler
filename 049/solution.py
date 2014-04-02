# coding: utf-8

""" Project Euler problem #49. """


def problem():
    u""" Solve the problem.

    The arithmetic sequence, 1487, 4817, 8147, in which each of the terms
    increases by 3330, is unusual in two ways: (i) each of the three terms are
    prime, and, (ii) each of the 4-digit numbers are permutations of one
    another.

    There are no arithmetic sequences made up of three 1-, 2-, or 3-digit
    primes, exhibiting this property, but there is one other 4-digit increasing
    sequence.

    What 12-digit number do you form by concatenating the three terms in this
    sequence?

    Answer: 296962999629

    """
    primes = set(primes_xrange(1488, 9999))
    for p1 in primes:
        p2, p3 = p1 + 3330, p1 + 6660
        if p2 in primes and p3 in primes:
            if sorted(str(p1)) == sorted(str(p2)) == sorted(str(p3)):
                return "%d%d%d" % (p1, p2, p3)


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
