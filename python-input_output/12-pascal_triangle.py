"""
This module contains a function to generate Pascal's
triangle up to a given number of rows.
The function `pascal_triangle(n)` takes an integer `n`
as input and returns a list of lists representing
Pascal's triangle with `n` rows.
"""


def pascal_triangle(n):
    """Generate Pascal's triangle up to `n` rows."""
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)
    return triangle
