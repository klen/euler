""" Project Euler problem #25. """


def problem():
    """ Solve the problem.

    What is the first term in the Fibonacci sequence to contain 1000 digits?

    Answer: 4782

    """
    def fib():
        p, c = 1, 1
        yield p
        while True:
            yield c
            p, c = c, p + c

    counter = 0
    for num in fib():
        counter += 1
        if len(str(num)) >= 1000:
            return counter


if __name__ == '__main__':
    print problem()
