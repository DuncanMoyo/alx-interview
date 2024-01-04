#!/usr/bin/python3
"""
    0-main
    This script uses the pascal_triangle function 
    to generate and print Pascal's Triangle.
"""

""" Import the pascal_triangle function from the 0-pascal_triangle module """
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle

def print_triangle(triangle):
    """
        Print the triangle
        This function takes a list of lists of integers
        (representing Pascal's Triangle)
        and prints it in a human-readable format.
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    """ Generate Pascal's Triangle with 5 levels and print it """
    print_triangle(pascal_triangle(5))

