#!/usr/bin/env python3

"""
Write a function that computes the square value of all integers of a matrix.

Prototype: def square_matrix_simple(matrix=[]):
matrix is a 2 dimensional array
Returns a new matrix:
Same size as matrix
Each value should be the square of the value of the input
Initial matrix should not be modified
You are not allowed to import any module
You are allowed to use regular loops, map, etc
"""


def square_matrix_simple(matrix=[]):
    """
    Computes the square value of all integers of a matrix.

    Args:
        matrix (list): A 2-dimensional array.

    Returns:
        list: A new matrix with squared values.
    """
    # Create a new matrix to hold the squared values
    squared_matrix = []

    # Iterate through each row in the input matrix
    for row in matrix:
        # Use list comprehension to square each element in the row
        squared_row = [x ** 2 for x in row]
        # Append the squared row to the new matrix
        squared_matrix.append(squared_row)

    return squared_matrix
