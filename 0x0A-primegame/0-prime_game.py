#!/usr/bin/python3

"""
    Prime Game - Maria and Ben are playing a game. In this game,
    they take turns choosing prime numbers from a list.
    The player who chooses a number with the most multiples wins the round.
"""


def isWinner(x, nums):
    """
        Determines the winner of the game.

        Parameters:
            x (int): The number of rounds played.
            nums (list): The list of numbers to choose from.

        Returns:
            str: The name of the winner or None if there's an error.
    """

    if x <= 0 or nums is None:
        return None
    if x != len(nums):
        return None

    ben = 0
    maria = 0

    a = [1 for x in range(sorted(nums)[-1] + 1)]
    a[0], a[1] = 0, 0
    for i in range(2, len(a)):
        rm_multiples(a, i)

    for i in nums:
        if sum(a[0:i + 1]) % 2 == 0:
            ben += 1
        else:
            maria += 1
    if ben > maria:
        return "Ben"
    if maria > ben:
        return "Maria"
    return None


def rm_multiples(ls, x):
    """
        Removes multiples of a given number from a list.

        Parameters:
            ls (list): The list of numbers.
            x (int): The number to remove multiples of.
    """
    for i in range(2, len(ls)):
        try:
            ls[i * x] = 0
        except (ValueError, IndexError):
            break
