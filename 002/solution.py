""" Project Euler problem #2. """


def problem():
    """ Solve the problem.

    By considering the terms in the Fibonacci sequence whose values do not
    exceed four million, find the sum of the even-valued terms.

    Answer: 4613732

    """
    return sum([x for x in fib_sequence(4000000) if not x % 2])


def fib_sequence(_max):
    """ Get Fibonacci sequence. """
    p, c = 1, 2
    yield p
    while c <= _max:
        yield c
        p, c = c, p + c


if __name__ == '__main__':
    print problem()
