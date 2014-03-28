# coding: utf-8

""" Project Euler problem #31. """


def problem():
    u""" Solve the problem.

    In England the currency is made up of pound, £, and pence, p, and there are
    eight coins in general circulation:

    1p, 2p, 5p, 10p, 20p, 50p, £1 (100p) and £2 (200p).
    It is possible to make £2 in the following way:

    1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
    How many different ways can £2 be made using any number of coins?

    Answer: 73682

    """
    goal = 200
    coins = 1, 2, 5, 10, 20, 50, 100, 200
    ways = [1] + [0] * goal

    for coin in coins:
        for idx in range(coin, goal + 1):
            ways[idx] += ways[idx - coin]

    return ways[-1]

    # Alternative (bruteforce solution)
    # return sum(
    # 1
    # for c200 in range(goal, -1, -200)
    # for c100 in range(c200, -1, -100)
    # for c50 in range(c100, -1, -50)
    # for c20 in range(c50, -1, -20)
    # for c10 in range(c20, -1, -10)
    # for c5 in range(c10, -1, -5)
    # for _ in range(c5, -1, -2)
    # )


if __name__ == '__main__':
    print problem()
