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
    num_bytes_to_process = 0

    # Masks to identify the significant bits of the byte
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for byte in data:
        # Keep only the 8 least significant bits of the byte
        byte = byte & 0xFF

        if num_bytes_to_process == 0:
            # Determine the number of bytes in the UTF-8 character
            if (byte & mask1) == 0:
                # 1-byte character (starts with 0xxxxxxx)
                continue
            elif (byte & (mask1 >> 1)) == mask1:
                # 2-byte character (starts with 110xxxxx)
                num_bytes_to_process = 1
            elif (byte & (mask1 >> 2)) == mask1:
                # 3-byte character (starts with 1110xxxx)
                num_bytes_to_process = 2
            elif (byte & (mask1 >> 3)) == mask1:
                # 4-byte character (starts with 11110xxx)
                num_bytes_to_process = 3
            else:
                # Invalid byte (does not match any valid UTF-8 header)
                return False
        else:
            # The byte must be a continuation byte (starts with 10xxxxxx)
            if not (byte & mask1 and not (byte & mask2)):
                return False
            num_bytes_to_process -= 1

    # If num_bytes_to_process is not zero, we have an incomplete character
    return num_bytes_to_process == 0
