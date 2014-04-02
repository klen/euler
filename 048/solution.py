# coding: utf-8

""" Project Euler problem #48. """


def problem():
    u""" Solve the problem.

    The series, 11 + 22 + 33 + ... + 1010 = 10405071317.

    Find the last ten digits of the series, 11 + 22 + 33 + ... + 10001000.

    Answer: 9110846700

    """
    result = long(0)
    for num in range(1, 1001):
        result += long(num) ** num

    print str(result)[-10:]


if __name__ == '__main__':
    print problem()
