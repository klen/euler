# coding: utf-8

""" Project Euler problem #27. """


def problem():
    u""" Solve the problem.

    Considering quadratics of the form:

    n² + an + b, where |a| < 1000 and |b| < 1000

    where |n| is the modulus/absolute value of n
    e.g. |11| = 11 and |−4| = 4

    Find the product of the coefficients, a and b, for the quadratic expression
    that produces the maximum number of primes for consecutive values of n,
    starting with n = 0.

    Answer: -59231

    """
    # b should be prime
    bs = [n for b in primes_xrange(1000) for n in (b, -b)]
    # max prime number for task is 79 ** 2 + 1000 * 79 + 1000 = 86241
    primes = set(primes_xrange(79 ** 2 + 1000 * 79 + 1000))

    _max, product = 0, 0
    for a in range(-1000, 1000):
        for b in bs:
            n = 0
            while n**2 + a * n + b in primes:
                n += 1
            if n and n > _max:
                _max, product = n, a * b

    return product


def primes_xrange(stop):
    """ Get prime numbers below passed stop value. """
    primes = [True] * stop
    primes[0], primes[1] = [False, False]
    for idx, value in enumerate(primes):
        if value is True:
            primes[idx*2::idx] = [False] * ((stop - 1)/idx - 1)
            yield idx


if __name__ == '__main__':
    print problem()
