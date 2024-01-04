Pascal’s Triangle Function
This repository contains a Python function pascal_triangle(n) that generates Pascal’s Triangle up to n levels.

Function Signature

def pascal_triangle(n: int) -> List[List[int]]:

Parameters
n (int): The number of levels of Pascal’s Triangle to generate.
Returns
If n <= 0, the function returns an empty list [].
Otherwise, the function returns a list of lists of integers representing the Pascal’s Triangle of n.
Assumptions
The function assumes that n will always be an integer.
Example
print(pascal_triangle(5))

Output:

[
 [1],
 [1, 1],
 [1, 2, 1],
 [1, 3, 3, 1],
 [1, 4, 6, 4, 1]
]

How to Run
You can run the function in a Python environment or script by importing it and calling pascal_triangle(n) with your desired n value.
