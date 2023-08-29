#!/usr/bin/python3
"""
Island Perimeter
"""
from typing import List


def island_perimeter(grid: List[List[int]]) -> int:
    """
    Calculate the perimeter of the island

    Args:
        grid -> (list[list[int]]): A 2D grid represneting the island

    Returns:
        int: The Perimeter of the island

    Contraints:
        - The grid is rectangular with width and height not exceeding 100.
        - The grid is completely surrounded by water.
        - There is only one island (or nothing).
        - The island doesn't have 'lakes' (water inside that isn't connected).
    """
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    perimeter = 0

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += dfs(i, j, grid, visited)
                break

    return perimeter


def dfs(row, col, grid, visited):
    """
    Depth-First Search Algorithm to calculate the perimeter

    Args:
        row (int): Row index of the current cell
        col (int): Column index of the current cell.
        grid (List[List[int]]): The 2D grid representing the island
        visited (List[List[bool]]): Matrix to track visited cells.

    Return:
        int: Perimeter contribution of the current cell.

    Note:
        This function is called recursively to explore neighboring cells.
    """
    rows, cols = len(grid), len(grid[0])
    if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0:
        return 1

    if visited[row][col]:
        return 0

    visited[row][col] = True
    neighbours = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    cell_perimeter = 0

    for dr, dc in neighbours:
        cell_perimeter += dfs(row + dr, col + dc, grid, visited)

    return cell_perimeter
