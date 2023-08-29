#!/usr/bin/python3
"""
Island Perimeter
"""


def island_perimeter(grid):
    """
    Calculate the perimeter of the island described in the given grid.
    """
    if not grid:
        return 0

    rows, cols = len(grid), len(grid[0])
    visited = [[False] * cols for _ in range(rows)]
    perimeter = 0

    def dfs(row, col):
        if row < 0 or row >= rows or col < 0 or col >= cols or grid[row][col] == 0:
            return 1

        if visited[row][col]:
            return 0

        visited[row][col] = True
        neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        cell_perimeter = 0

        for dr, dc in neighbors:
            cell_perimeter += dfs(row + dr, col + dc)

        return cell_perimeter

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += dfs(i, j)
                break

    return perimeter
