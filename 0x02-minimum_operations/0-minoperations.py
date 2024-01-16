#!/usr/bin/python3


def minOperations(n):
    """
        Calculates the minimum number of operations required to reduce
        a positive integer n to 1.
        An operation is defined as subtracting 1 or dividing by an integer
        divisor.

        Args:
            n: A positive integer.

        Returns:
            The minimum number of operations required to reduce n to 1.
    """

    if n <= 0:
        return 0
    elif n == 1:
        return 1

    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return i + minOperations(n // i)

    return n
