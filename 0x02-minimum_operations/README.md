# Minimum Operations

## Description

In a text file, there is a single character 'H'. Your text editor can execute only two operations in this file: Copy All and Paste. This project contains a Python method that calculates the fewest number of operations needed to result in exactly `n` 'H' characters in the file.

## Prototype

```python
def minOperations(n: int) -> int:

This function returns an integer which is the minimum number of operations to reach n characters. If n is impossible to achieve, it returns 0.

Example
For n = 9, the sequence of operations is:

H => Copy All => Paste => HH => Paste =>HHH => Copy All => Paste => HHHHHH => Paste => HHHHHHHHH

The number of operations is 6.

Usage:
```
	minOperations = __import__('0-minoperations').minOperations

n = 4
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))

n = 12
print("Min # of operations to reach {} char: {}".format(n, minOperations(n)))
```

Output
Min number of operations to reach 4 characters: 4
Min number of operations to reach 12 characters: 7
