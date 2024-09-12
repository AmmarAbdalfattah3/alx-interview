#!/usr/bin/python3
"""
Rotate a 2D matrix by 90 degrees clockwise
"""


def rotate_2d_matrix(matrix):
    """
    Rotates the input matrix 90 degrees clockwise in-place.

    Args:
        matrix (list of list of int): A 2D matrix to rotate.

    Returns:
        None: The matrix is modified in-place.
    """
    n = len(matrix)
    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()
