""" Project Euler problem #3. """


def problem():
    """ Solve the problem.

    What is the largest prime factor of the number 600851475143 ?

    Answer: 6857

    """
    return max(prime_factors(600851475143))


def prime_factors(num):
    """ Get all prime factors for number. """
    dd = 2
    while num > 1:
        while num % dd == 0:
            yield dd
            num /= dd
        dd = dd + 1


if __name__ == '__main__':
    print problem()
