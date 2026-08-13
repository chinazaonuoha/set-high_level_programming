"""
This module contains a function that divides all elements of a
matrix by a given divisor and returns a new matrix with the results
rounded to 2 decimal places. It also includes error
handling to ensure that the inputs are valid.
"""


def matrix_divided(matrix, div):
    """Divides all elements of a matrix by a number."""
    
    matrix_err = "matrix must be a matrix (list of lists) of integers/floats"
    row_err = "Each row of the matrix must have the same size"
    is_matrix_valid = (
        isinstance(matrix, list)
        and len(matrix) > 0
        and all(isinstance(row, list) for row in matrix)
    )
    if not is_matrix_valid:
        raise TypeError(matrix_err)
    first_row_len = len(matrix[0])
    if not all(len(row) == first_row_len for row in matrix):
        raise TypeError(row_err)
    are_elements_numbers = all(
        all(
            isinstance(num, (int, float)) and not isinstance(num, bool)
            for num in row
        )
        for row in matrix
    )
    if not are_elements_numbers:
        raise TypeError(matrix_err)
    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    return [[round(num / div, 2) for num in row] for row in matrix]