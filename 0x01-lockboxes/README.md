# Locked Boxes Problem

## Problem Statement

You have `n` number of locked boxes in front of you. Each box is numbered sequentially from `0` to `n - 1` and each box may contain keys to the other boxes.

The goal is to write a method that determines if all the boxes can be opened.

## Method Prototype

```python
def canUnlockAll(boxes):
```

Parameters
boxes is a list of lists. Each list represents a box and contains zero or more keys.

Rules
A key with the same number as a box opens that box.
You can assume all keys will be positive integers.
There can be keys that do not have boxes.
The first box boxes[0] is unlocked.
Return
Return True if all boxes can be opened, else return False.

```boxes = [[1], [2], [3], []]
print(canUnlockAll(boxes))  # returns True

boxes = [[1, 3], [3, 0, 1], [2], [0]]
print(canUnlockAll(boxes))  # returns False

boxes = [[1, 4, 5], [2], [0, 3, 1], [5], [1], []]
print(canUnlockAll(boxes))  # returns True
```
