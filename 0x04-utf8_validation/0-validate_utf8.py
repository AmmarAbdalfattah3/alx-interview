#!/usr/bin/python3
"""This module determines if a given data
set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    :param data: List of integers representing bytes of data
    :return: True if data is a valid UTF-8 encoding, else False
    """
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks for checking the most significant bits of a byte
    mask1 = 1 << 7  # 10000000 in binary
    mask2 = 1 << 6  # 01000000 in binary

    for byte in data:
        # Extract only the 8 least significant bits of the byte
        byte = byte & 0xFF

        if num_bytes == 0:
            # Determine the number of bytes in the UTF-8 character
            if byte & mask1 == 0:
                # 1-byte character (ASCII)
                continue
            elif byte & (mask1 >> 1) == mask1:
                # 2-byte character
                num_bytes = 1
            elif byte & (mask1 >> 2) == mask1:
                # 3-byte character
                num_bytes = 2
            elif byte & (mask1 >> 3) == mask1:
                # 4-byte character
                num_bytes = 3
            else:
                # Invalid UTF-8 character
                return False
        else:
            # Check that this byte is a valid continuation byte (10xxxxxx)
            if byte & mask1 == mask1 and byte & mask2 == 0:
                num_bytes -= 1
            else:
                return False

    return num_bytes == 0
