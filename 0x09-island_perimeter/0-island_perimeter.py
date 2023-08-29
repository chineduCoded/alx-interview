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

    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 1:
                perimeter += dfs(i, j, grid, visited)
                break

    return perimeter

def dfs(row, col, grid, visited):
    """
     Depth-First Search (DFS) function to calculate
     the perimeter contribution of a land cell.
     """
    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] == 0:
        return 1

    if visited[row][col]:
        return 0

    visited[row][col] = True
    neighbors = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    cell_perimeter = 0

    for dr, dc in neighbors:
        cell_perimeter += dfs(row + dr, col + dc, grid, visited)

    return cell_perimeter
