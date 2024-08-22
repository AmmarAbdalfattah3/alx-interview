#!/usr/bin/python3
"""This module determines if a given data
set represents a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Determine if a given data set represents a valid UTF-8 encoding.

    :param data: List of integers representing bytes of data
    :return: True if data is a valid UTF-8 encoding, else False
    """
    num_bytes = 0  # Number of continuation bytes expected

    # Masks for identifying the types of bytes
    first_byte_masks = [
            0b11111111, 0b11111110,
            0b11111100, 0b11111000,
            0b11110000
            ]
    continuation_mask = 0b11000000
    continuation_check = 0b10000000

    for byte in data:
        # Mask the byte to get only the least significant 8 bits
        byte = byte & 0xFF

        if num_bytes == 0:
            # Determine how many bytes in the UTF-8 character
            for i, mask in enumerate(first_byte_masks):
                if (byte & mask) == (mask ^ (1 << (7 - i))):
                    num_bytes = i
                    break
            else:
                # If no match, it's a 1-byte character
                if (byte & continuation_check) != 0:
                    return False
        else:
            # This must be a continuation byte
            if (byte & continuation_mask) != continuation_check:
                return False
            num_bytes -= 1

    # Ensure we've processed all bytes correctly
    return num_bytes == 0
