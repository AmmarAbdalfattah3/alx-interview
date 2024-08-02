#!/usr/bin/python3
"""
This script writes a method that determines if all the boxes can be opened.
"""


from collections import deque


def canUnlockAll(boxes):
    """
    Determine if all boxes can be unlocked starting from the first box.

    Parameters:
    boxes (list of lists): A list where each sublist represents a box.

    Returns:
    bool: True if all boxes can be unlocked, otherwise False.

    Example:
    >>> canUnlockAll([[1], [2], [3], [4], []])
    True

    >>> canUnlockAll([[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]])
    True

    >>> canUnlockAll([[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]])
    False
    """
    # Number of boxes
    n = len(boxes)

    # Initialize a queue for BFS and a set to track visited boxes
    queue = deque([0])
    visited = set([0])

    while queue:
        current_box = queue.popleft()

        # Access keys in the current box
        for key in boxes[current_box]:
            if key < n and key not in visited:
                visited.add(key)
                queue.append(key)

    # Check if we visited all boxes
    return len(visited) == n
