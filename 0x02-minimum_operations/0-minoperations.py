#!/usr/bin/python3
""" Module for minimum_operations"""


def minimum_operations(target_chars):
    """
        minimum_operations
        Calculates the minimum number of operations needed to result in exactly
        target_chars 'H' characters
    """
    """
        The minimum number of operations should be at least 2:
        (Copy All => Paste)
    """
    if (target_chars < 2):
        return 0
    total_operations, divisor = 0, 2
    while divisor <= target_chars:
        """If target_chars is divisible by divisor"""
        if target_chars % divisor == 0:
            """
                The number of times target_chars is divisible by divisor
                equals the total operations
            """
            total_operations += divisor
            """Update target_chars to the quotient"""
            target_chars = target_chars / divisor
            """
                Decrease divisor to find remaining smaller values
                that divide target_chars evenly
            """
            divisor -= 1
        """ Increase divisor until it divides target_chars evenly"""
        divisor += 1
    return total_operations
