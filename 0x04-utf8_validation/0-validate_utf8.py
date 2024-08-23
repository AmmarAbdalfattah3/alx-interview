#!/usr/bin/python3
"""
Module to validate UTF-8 encoding in a list of integers.
"""


def validUTF8(data):
    """
    Check if a list of integers represents a valid UTF-8 encoding.

    Args:
        data (list of int): A list of integers representing bytes.

    Returns:
        bool: True if the list represents a valid
        UTF-8 encoding, False otherwise.
    """

    def count_leading_ones(byte):
        """
        Count the number of leading 1s in the byte to
        determine the expected number
        of bytes for this character.

        Args:
            byte (int): The byte to check.

        Returns:
            int: The number of leading 1s minus 1,
            or -1 if the byte is invalid.
        """
        if byte >> 7 == 0:
            return 0
        elif byte >> 5 == 0b110:
            return 1
        elif byte >> 4 == 0b1110:
            return 2
        elif byte >> 3 == 0b11110:
            return 3
        return -1  # Invalid starting byte

    n = len(data)
    i = 0
    while i < n:
        # Check for invalid byte values
        if data[i] < 0 or data[i] > 255:
            return False

        # Count how many bytes should follow this one
        num_bytes = count_leading_ones(data[i])
        if num_bytes == -1:
            return False

        # Check if the following bytes are valid continuation bytes
        for j in range(1, num_bytes + 1):
            if i + j >= n or (data[i + j] >> 6 != 0b10):
                return False

        # Move to the next character
        i += num_bytes + 1

    return True
