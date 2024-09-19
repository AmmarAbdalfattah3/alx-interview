#!/usr/bin/python3
"""
Solution for the "Change comes from within" project.
"""


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

    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1


if __name__ == '__main__':
    print(makeChange([1, 2, 25], 37))
    print(makeChange([1256, 54, 48, 16, 102], 1453))
