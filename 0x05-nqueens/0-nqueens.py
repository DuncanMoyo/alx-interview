#!/usr/bin/python3
""" N queens """
import sys


def validate_input():
    """Validates command-line arguments."""
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        exit(1)

    if not sys.argv[1].isdigit():
        print("N must be a number")
        exit(1)

    b_size = int(sys.argv[1])
    if b_size < 4:
        print("N must be at least 4")
        exit(1)
    return b_size


def find_possible_queen_positions(b_size, c_r=0, r_place=[], p_s=[], n_s=[]):
    """Recursively finds possible queen positions."""
    if c_r < b_size:
        for column in range(b_size):
            if (
                column not in r_place
                and c_r + column not in p_s
                and c_r - column not in n_s
            ):
                yield from find_possible_queen_positions(
                    b_size,
                    c_r + 1,
                    r_place + [column],
                    p_s + [c_r + column],
                    n_s + [c_r - column],
                )
    else:
        yield r_place


def solve_n_queens(b_size):
    """Prints solutions for the N-Queens problem."""
    solution_counter = 0
    for solution in find_possible_queen_positions(b_size):
        solution_coordinates = []
        for row, column in enumerate(solution):
            solution_coordinates.append([row, column])
        print(f"{solution_coordinates}")
        solution_counter += 1


if __name__ == "__main__":
    b_size = validate_input()
    solve_n_queens(b_size)
