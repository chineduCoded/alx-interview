#!/usr/bin/python3
"""
N Queens problem
"""
import sys


def is_safe(board, row, col, N):
    # Check if there is a queen in the same column on the above rows
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check if there is a queen in the upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check if there is a queen in the upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, N)):
        if board[i][j] == 1:
            return False

    return True


def solve_nqueens(board, row, N):
    if row == N:
        solution = []
        for i in range(N):
            for j in range(N):
                if board[i][j] == 1:
                    solution.append([i, j])
        return [solution]

    solutions = []
    for col in range(N):
        if is_safe(board, row, col, N):
            board[row][col] = 1
            solutions.extend(solve_nqueens(board, row + 1, N))
            board[row][col] = 0

    return solutions


def print_solutions(N):
    board = [[0 for _ in range(N)] for _ in range(N)]
    solutions = solve_nqueens(board, 0, N)
    for solution in solutions:
        print(solution)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    print_solutions(N)
