""" Project Euler problem #6. """


def problem():
    """ Solve the problem.

    Find the difference between the sum of the squares of the first one hundred
    natural numbers and the square of the sum.

    Answer: 25164150

    """
    sum_of_squares = sum([n ** 2 for n in range(101)])
    square_of_sums = sum(range(101)) ** 2
    return square_of_sums - sum_of_squares


if __name__ == '__main__':
    print problem()
