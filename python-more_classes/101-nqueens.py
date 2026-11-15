"""
The N queens puzzle is the challenge of placing N
non-attacking queens on an N×N chessboard.
Write a program that solves the N queens problem.

Usage: nqueens N
If the user called the program with the wrong number
of arguments, print Usage: nqueens N, followed by a new
line, and exit with the status 1
where N must be an integer greater or equal to 4
If N is not an integer, print N must be a number,
followed by a new line, and exit with the status 1
If N is smaller than 4, print N must be at least 4,
followed by a new line, and exit with the status 1
The program should print every possible solution to the problem
One solution per line
Format: see example
You don't have to print the solutions in a specific order
You are only allowed to import the sys module
"""


class NQueens:
    """A class that solves the N queens problem."""

    def __init__(self, n):
        """Initialize a new NQueens instance."""
        self.n = n
        self.solutions = []

    def solve(self):
        """Solve the N queens problem."""
        self._solve_recursive([], 0)

    def _solve_recursive(self, queens, row):
        """Recursively place queens on the board."""
        if row == self.n:
            self.solutions.append(queens)
            return

        for col in range(self.n):
            if self._is_safe(queens, row, col):
                self._solve_recursive(queens + [col], row + 1)

    def _is_safe(self, queens, row, col):
        """Check if it's safe to place a queen at (row, col)."""
        for r in range(row):
            c = queens[r]
            if c == col or abs(c - col) == abs(r - row):
                return False
        return True

    def print_solutions(self):
        """Print all the solutions found."""
        for solution in self.solutions:
            print([[i, solution[i]] for i in range(self.n)])
