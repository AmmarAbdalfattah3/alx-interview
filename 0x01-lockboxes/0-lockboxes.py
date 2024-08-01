#!/usr/bin/env python3
"""
This module writes a type-annotated function add that takes a float a and
a float b as arguments and returns their sum as a float.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked given a list of boxes.

    Args:
        boxes (List[List[int]]): A list where each sublist represents a box.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    """

    # Number of boxes
    n = len(boxes)

    # To keep track of unlocked boxes
    unlocked = set()
    # To keep track of boxes to explore
    to_explore = [0]

    while to_explore:
        # Get the next box to explore
        current_box = to_explore.pop()

        # If this box is already unlocked, skip it
        if current_box in unlocked:
            continue

        # Mark the current box as unlocked
        unlocked.add(current_box)

        # Get the list of keys from the current box
        keys = boxes[current_box]

        # Add new boxes to explore if they haven't been unlocked yet
        for key in keys:
            if key < n and key not in unlocked:
                to_explore.append(key)

    # Check if all boxes are unlocked
    return len(unlocked) == n
