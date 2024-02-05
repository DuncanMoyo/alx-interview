N-Queens Problem
The N-Queens problem involves placing N chess queens on an N×N chessboard such that no two queens threaten each other (i.e., they don’t share the same row, column, or diagonal).

Problem Description
The goal is to find all possible solutions to the N-Queens problem.
Each solution represents a valid arrangement of queens on the board.
Solutions exist for all natural numbers other than N=2 and N=3.

Algorithm Used
We employ the backtracking algorithm to solve the N-Queens problem.
Backtracking explores all possible placements and backtracks when needed.
The algorithm ensures that no two queens attack each other.

How to Use
Clone this repository to your local machine.
Compile and run the provided N-Queens solver program.
Specify the value of N as a command-line argument.
The program will print all valid solutions.

```
$ ./nqueens.py 4
[[0, 1], [1, 3], [2, 0], [3, 2]]
[[0, 2], [1, 0], [2, 3], [3, 1]]

$ ./nqueens.py 6
[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]
[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]
[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]
[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]
```
