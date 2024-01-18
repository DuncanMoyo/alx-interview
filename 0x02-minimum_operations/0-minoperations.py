#!/usr/bin/python3

def minOperations(target_chars):
    """
        A function that calculates the fewest number of operations
        needed to give a result of exactly n H characters in a file
        args: target_chars: Number of characters to be displayed
        return:
               number of min operations
    """

    current_chars = 1
    copied_chars = 0
    operation_count = 0
    while current_chars < target_chars:
        remaining_chars = target_chars - current_chars
        if (remaining_chars % current_chars == 0):
            copied_chars = current_chars
            current_chars += copied_chars
            operation_count += 2
        else:
            current_chars += copied_chars
            operation_count += 1
    return operation_count
