#!/usr/bin/python3
"""Module containing lazy_matrix_mul function using NumPy."""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices using NumPy.

    Args:
        m_a (list of lists of int/float): First matrix.
        m_b (list of lists of int/float): Second matrix.

    Returns:
        ndarray: Resulting matrix product.

    Raises:
        TypeError: If m_a/m_b are not lists, list of lists,
        or contain non-numbers.
        ValueError: If m_a/m_b are empty or cannot be multiplied.
    """
    # 1. Validate m_a and m_b are lists
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # 2. Validate m_a and m_b are lists of lists
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # 3. Validate m_a and m_b are not empty
    if m_a == [] or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if m_b == [] or m_b == [[]]:
        raise ValueError("m_b can't be empty")

    # 4. Validate numeric types (ints or floats)
    for row in m_a:
        for val in row:
            if not isinstance(val, (int, float)) or isinstance(val, bool):
                raise TypeError("m_a should contain only integers or floats")

    for row in m_b:
        for val in row:
            if not isinstance(val, (int, float)) or isinstance(val, bool):
                raise TypeError("m_b should contain only integers or floats")

    # 5. Validate rectangular shapes
    first_row_len_a = len(m_a[0])
    if not all(len(row) == first_row_len_a for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    first_row_len_b = len(m_b[0])
    if not all(len(row) == first_row_len_b for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    # 6. Delegate matrix multiplication and dimension alignment check to NumPy
    try:
        return np.matmul(m_a, m_b)
    except ValueError:
        raise ValueError("m_a and m_b can't be multiplied")
