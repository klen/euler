""" Project Euler problem #14. """


def problem():
    """ Solve the problem.

    Which starting number, under one million, produces the longest Collatz
    sequence?.

    Answer: 837799

    """
    @cached
    def cs_lengths(num):
        if num == 1:
            return 1

        return 1 + cs_lengths(num / 2 if is_even(num) else 3 * num + 1)

    _max, num, x = 0, 0, 1
    while x <= 10**6:
        ll = cs_lengths(x)
        if ll > _max:
            _max, num = ll, x
        x += 1

    return num


def cached(func):
    """ Cache function execution. """
    cache = dict()

    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper


def is_even(num):
    """ Check for number is even. """
    return num % 2 == 0


if __name__ == '__main__':
    print problem()
