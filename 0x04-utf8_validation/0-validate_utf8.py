#!/usr/bin/python3
"""
Module to validate if a given list of integers
represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Validate if the given list of integers
    represents a valid UTF-8 encoding.

    Args:
        data (list of int): List where each
        integer is a byte (0-255).

    Returns:
        bool: True if data is valid UTF-8
        encoding, otherwise False.
    """
    num_bytes = 0

    for byte in data:
        # Check if the byte is within the valid range
        if byte < 0 or byte > 255:
            return False

        # Determine the number of bytes expected
        if num_bytes == 0:
            if (byte >> 7) == 0b0:
                num_bytes = 0
            elif (byte >> 5) == 0b110:
                num_bytes = 1
            elif (byte >> 4) == 0b1110:
                num_bytes = 2
            elif (byte >> 3) == 0b11110:
                num_bytes = 3
            else:
                return False
        else:
            # Check if it's a valid continuation byte
            if (byte >> 6) != 0b10:
                return False
            num_bytes -= 1

    return num_bytes == 0
