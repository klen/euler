# coding: utf-8

""" Project Euler problem #52. """


def problem():
    u""" Solve the problem.

    It can be seen that the number, 125874, and its double, 251748, contain
    exactly the same digits, but in a different order.

    Find the smallest positive integer, x, such that 2x, 3x, 4x, 5x, and 6x,
    contain the same digits.

    Answer: 142857

    """
    multipliers = range(2, 7)
    for num in xrange(10*5, 10**6):
        snum = str(num)
        if '2' not in snum or '5' not in snum:
            continue
        for m in multipliers:
            num2 = num * m
            if not sorted(snum) == sorted(str(num2)):
                break
        else:
            return num


if __name__ == '__main__':
    print problem()
