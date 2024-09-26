#!/usr/bin/python3
"""
Island Perimeter Module
"""


def island_perimeter(grid):
    """
    Returns the perimeter of the island described in grid.

    Args:
        grid (list of list of int): The grid representing the island.

    Returns:
        int: The perimeter of the island.
    """
    perimeter = 0
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:  # If the cell is land
                # Check all four sides of the cell
                if i == 0 or grid[i - 1][j] == 0:  # Check above
                    perimeter += 1
                if i == rows - 1 or grid[i + 1][j] == 0:  # Check below
                    perimeter += 1
                if j == 0 or grid[i][j - 1] == 0:  # Check left
                    perimeter += 1
                if j == cols - 1 or grid[i][j + 1] == 0:  # Check right
                    perimeter += 1

    return perimeter
