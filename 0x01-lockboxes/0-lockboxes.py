#!/usr/bin/python3
"""
    Determines whether all boxes can be unlocked using the available keys.
"""


def canUnlockAll(boxes):
    """
        Args:
        boxes: A list of lists, where each inner list represents
        the keys contained in a box.

        Returns:
        True if all boxes can be unlocked, False otherwise.
    """

    n = len(boxes)

    opened = [False] * n

    opened[0] = True

    keys = [key for key in boxes[0] if key < n]

    while keys:
        new_keys = []

        for key in keys:
            if not opened[key]:
                opened[key] = True
                for new_key in boxes[key]:
                    if new_key < n and not opened[new_key]:
                        new_keys.append(new_key)
        keys = new_keys
    return all(opened)
