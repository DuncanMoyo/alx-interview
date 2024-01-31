#!/usr/bin/python3
""" UTF-8 Validation """


def validUTF8(data):
    """
    Determine if a given data set represents a valid UTF-8 encoding.

    A character in UTF-8 can be 1 to 4 bytes long.
    The data set can contain multiple characters.
    Each integer represents 1 byte of data, therefore you only need to handle
    the 8 least significant bits of each integer.

    Parameters:
    data (list of int): The data set to be checked.

    Returns:
    bool: True if data is a valid UTF-8 encoding, else False.
    """

    # Initialize the count of bytes left to process in the current character
    count = 0

    # Process each byte in the data
    for num in data:
        if count == 0:
            # If this is the start of a new character, determine how many bytes
            # it includes based on the number of leading 1s in the current byte
            if (num >> 5) == 0b110:
                count = 1
            elif (num >> 4) == 0b1110:
                count = 2
            elif (num >> 3) == 0b11110:
                count = 3
            elif (num >> 7):
                # If the byte starts with 1, it's not a valid 1-byte character
                return False
        else:
            # If not the first byte of a character, it must start with 10
            if (num >> 6) != 0b10:
                return False
            # Decrease the count of bytes left
            count -= 1

    # If all characters have been fully processed, the data is valid
    return count == 0
