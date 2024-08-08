#!/usr/bin/python3
"""
This function calculates the minimum number of operations required
to achieve exactly `n` 'H' characters in a text file. You start
with one 'H' and can perform two operations: "Copy All" and "Paste".
"""


def minOperations(n):
    """
    Calculates the minimum number of operations needed to achieve exactly 'n'.
    in a text file, starting with one 'H' and using only the operations.

    Parameters:
    n (int): The target number of 'H' characters to achieve.

    Returns:
    int: The minimum number of operations needed.
    """

    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while n > 1:
        while n % factor == 0:
            operations += factor
            n //= factor
        factor += 1

    return operations
