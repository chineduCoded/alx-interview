#!/usr/bin.python3
"""
0-lockboxes.py
"""


def canUnlockAll(boxes):
    '''
    Determines if all the boxes can be opened or not.

    Args:
        boxes (list): A list of lists representing the boxes and their corresponding keys.

    Returns:
        bool: True if all boxes can be opened, False otherwise.
    '''

    length = len(boxes)
    opened_boxes = set()
    opened_boxes.add(0)
    keys = set(boxes[0])

    while keys:
        key = keys.pop()
        if key < length and key not in opened_boxes:
            opened_boxes.add(key)
            keys.update(boxes[key])

    return len(opened_boxes) == length
