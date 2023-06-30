#!/usr/bin/python3
"""
0-pascal_triangle
"""


def pascal_triangle(n):
    """
    Represent Pascal Triangle

    Attrs:
        n (int): number of column to be generated
    Return:
        list of lists of integers representing pascal triangle
    """
    if n <= 0:
        return []

    triangle = [[1]]
    prev_row = [1]

    for i in range(1, n):
        current_row = [1]

        for j in range(1, i):
            value = prev_row[j - 1] + prev_row[j]
            current_row.append(value)

        current_row.append(1)

        triangle.append(current_row)

        prev_row = current_row

    return triangle
