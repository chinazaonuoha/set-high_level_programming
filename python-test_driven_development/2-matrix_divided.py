#!/usr/bin/python3
"""
Module for matrix_divided method.
"""

def matrix_divided(matrix=None, div=None):
    """
    Divides all elements of a matrix by a given number.
    Handles missing arguments, inf divisors, and full validation.
    """
    matrix_err = "matrix must be a matrix (list of lists) of integers/floats"
    row_err = "Each row of the matrix must have the same size"
    div_type_err = "div must be a number"
    div_zero_err = "division by zero"
    if matrix is None:
        raise TypeError("matrix_divided() missing 1 required positional argument: 'matrix'")
    if div is None:
        raise TypeError("matrix_divided() missing 1 required positional argument: 'div'")
    if not isinstance(matrix, list):
        raise TypeError(matrix_err)
    row_len = None
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError(matrix_err)
        if row_len is None:
        
            row_len = len(row)
        elif len(row) != row_len:
            raise TypeError(row_err)
        for elem in row:
            if not isinstance(elem, (int, float)) or isinstance(elem, bool):
                raise TypeError(matrix_err)
    if not isinstance(div, (int, float)) or isinstance(div, bool):
        raise TypeError(div_type_err)
    if div == 0:
        raise ZeroDivisionError(div_zero_err)
    return [
        [0.0 if (elem / div) == 0 else round(elem / div, 2) for elem in row]
        for row in matrix
    ]
