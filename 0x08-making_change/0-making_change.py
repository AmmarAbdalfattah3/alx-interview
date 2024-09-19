#!/usr/bin/python3
"""
Optimized solution for the "Change comes from within" project using BFS.
"""


from collections import deque


def makeChange(coins, total):
    """
    Determine the fewest number of coins needed to meet a given amount total.

    Args:
    coins (list): List of coin denominations available.
    total (int): The total amount of money to be made using the coins.

    Returns:
    int: Fewest number of coins needed to make up the total.
         Return -1 if it's not possible to make the total.
    """
    if total <= 0:
        return 0

    queue = deque([(0, 0)])
    visited = set([0])

    while queue:
        current_sum, num_coins = queue.popleft()

        for coin in coins:
            new_sum = current_sum + coin

            if new_sum == total:
                return num_coins + 1
            if new_sum < total and new_sum not in visited:
                queue.append((new_sum, num_coins + 1))
                visited.add(new_sum)

    return -1


if __name__ == '__main__':
    print(makeChange([1, 2, 25], 37))
    print(makeChange([1256, 54, 48, 16, 102], 1453))
