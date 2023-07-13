#!/usr/bin/python3
"""Minimum Operations"""


def minOperations(n):
    """
    Calculate the minimum number of operations to obtain n 'H' characters in the file.

    Args:
        n (int): The desired number of 'H' characters.

    Returns:
        int: The minimum number of operations required.
    """
    if n <= 1:
        return 0

    operations = 0
    factor = 2

    while factor <= n:
        if n % factor == 0:
            operations += factor
            n //= factor
        else:
            factor += 1

    return operations
