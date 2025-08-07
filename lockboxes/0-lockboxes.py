#!/usr/bin/python3
"""Function is starting"""


def canUnlockAll(boxes):
    """
    Inside of Function
    """
    n = len(boxes)
    opened = set()
    stack = [0]

    while stack:
        current = stack.pop()
        if current not in opened:
            opened.add(current)
            for key in boxes[current]:
                if key < n:
                    stack.append(key)

    return len(opened) == n
