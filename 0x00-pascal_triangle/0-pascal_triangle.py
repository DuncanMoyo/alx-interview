#!/usr/bin/python3
"""
    This script uses the pascal_triangle function
    to generate and print Pascal's Triangle.
"""


def pascal_triangle(n):
    """
        Print the triangle
        This function takes a list of lists of integers
        (representing Pascal's Triangle)
        and prints it in a human-readable format.
    """
    if n <= 0:
        return []
    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        last_row = triangle[-1]
        row += [sum(pair) for pair in zip(last_row, last_row[1:])]
        row.append(1)
        triangle.append(row)
    return triangle
