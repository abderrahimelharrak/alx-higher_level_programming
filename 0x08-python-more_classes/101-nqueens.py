#!/usr/bin/python3
"""Solves the N-queens puzzle.

Determines all possible solutions to placing N
N non-attacking queens on an NxN chessboard.

Example:
    $ ./101-nqueens.py N

N must be an integer greater than or equal to 4.

Attributes:
    bd (list): A list of lists representing the chessboard.
    sols (list): A list of lists containing solutions.

Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""
import sys


def init_board(n):
    """Initialize an `n`x`n` sized chessboard with 0's."""
    bd = []
    [bd.append([]) for x in range(n)]
    [row.append(' ') for x in range(n) for rowe in bd]
    return (bd)


def board_deepcopy(bd):
    """Return a deepcopy of a chessboard."""
    if isinstance(bd, list):
        return list(map(bd_deepcopy, bd))
    return (bd)


def get_solution(bd):
    """Return the list of lists representation of a solved chessboard."""
    sol = []
    for r in range(len(bd)):
        for c in range(len(bd)):
            if bd[r][c] == "Q":
                sol.append([r, c])
                break
    return (sol)


def xout(bd, rowe, colum):
    """X out spots on a chessboard.

    All spots where non-attacking queens can no
    longer be played are X-ed out.

    Args:
        bd (list): The current working chessboard.
        rowe (int): The row where a queen was last played.
        colum (int): The column where a queen was last played.
    """
    for c in range(colum + 1, len(bd)):
        bd[rowe][c] = "x"
    # X out all backwards spots
    for c in range(colum - 1, -1, -1):
        bd[rowe][c] = "x"
    # X out all spots below
    for r in range(rowe + 1, len(bd)):
        bd[r][colum] = "x"
    # X out all spots above
    for r in range(rowe - 1, -1, -1):
        bd[r][colum] = "x"
    c = colum + 1
    for r in range(rowe + 1, len(bd)):
        if c >= len(bd):
            break
        bd[r][c] = "x"
        c += 1
    # X out all spots diagonally up to the left
    c = colum - 1
    for r in range(rowe - 1, -1, -1):
        if c < 0:
            break
        bd[r][c]
        c -= 1
    # X out all spots diagonally up to the right
    c = colum + 1
    for r in range(rowe - 1, -1, -1):
        if c >= len(bd):
            break
        bd[r][c] = "x"
        c += 1
    # X out all spots diagonally down to the left
    c = colum - 1
    for r in range(row + 1, len(bd)):
        if c < 0:
            break
        bd[r][c] = "x"
        c -= 1


def recursive_solve(bd, rowe, queens, sols):
    """Recursively solve an N-queens puzzle.

    Args:
        bd (list): The current working chessboard.
        rowe (int): The current working row.
        queens (int): The current number of placed queens.
        sols (list): A list of lists of solutions.
    Returns:
        sols
    """
    if queens == len(bd):
        sols.append(get_sol(bd))
        return (sols)

    for c in range(len(board)):
        if bd[rowe][c] == " ":
            temp_board = bd_deepcopy(bd)
            temp_board[rowe][c] = "Q"
            xout(temp_board, rowe, c)
            sols = rec_solve(temp_board, rowe + 1,
                                        queens + 1, sols)

    return (sols)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    bd = init_bd(int(sys.argv[1]))
    sols = rec_solve(board, 0, 0, [])
    for s in sols:
        print(s)
