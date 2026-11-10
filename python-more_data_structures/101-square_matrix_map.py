#!/usr/bin/python3

"""
Write a function that computes the square value of all integers of a matrix using map
"""


def square_matrix_map(matrix=[]):
    """
    Computes the square value of all integers in a matrix using map.

    Args:
        matrix (list of list of int): The input matrix.

    Returns:
        list of list of int: The matrix with squared values.
    """
    return list(map(lambda row: list(map(lambda x: x ** 2, row)), matrix))
