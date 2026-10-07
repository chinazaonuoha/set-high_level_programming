#!/usr/bin/python3
"""Module containing lazy_matrix_mul function using NumPy."""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices using NumPy after custom validation.

    Args:
        m_a (list of lists of int/float): First matrix.
        m_b (list of lists of int/float): Second matrix.

    Returns:
        ndarray: Resulting matrix product as a NumPy array.

    Raises:
        TypeError: For invalid types, non-list-of-lists, or non-numbers.
        ValueError: For empty matrices or incompatible dimensions.
    """
    # 1. Validate m_a is a list
    if not isinstance(m_a, list):
        raise TypeError("m_a must be a list")

    # 2. Validate m_b is a list
    if not isinstance(m_b, list):
        raise TypeError("m_b must be a list")

    # 3. Validate m_a is a list of lists
    if not all(isinstance(row, list) for row in m_a):
        raise TypeError("m_a must be a list of lists")

    # 4. Validate m_b is a list of lists
    if not all(isinstance(row, list) for row in m_b):
        raise TypeError("m_b must be a list of lists")

    # 5. Validate m_a is not empty
    if (
        m_a == [] or m_a == [[]] or any(len(row) == 0 for row in m_a)
    ):
        raise ValueError("m_a can't be empty")

    # 6. Validate m_b is not empty
    if (
        m_b == [] or m_b == [[]] or any(len(row) == 0 for row in m_b)
    ):
        raise ValueError("m_b can't be empty")

    # 7. Validate m_a contains only integers or floats
    for row in m_a:
        for element in row:
            if (
                not isinstance(element, (int, float))
                or isinstance(element, bool)
            ):
                raise TypeError("m_a should contain only integers or floats")

    # 8. Validate m_b contains only integers or floats
    for row in m_b:
        for element in row:
            if (
                not isinstance(element, (int, float))
                or isinstance(element, bool)
            ):
                raise TypeError("m_b should contain only integers or floats")

    # 9. Validate m_a is rectangular
    first_row_len_a = len(m_a[0])
    if not all(len(row) == first_row_len_a for row in m_a):
        raise TypeError("each row of m_a must be of the same size")

    # 10. Validate m_b is rectangular
    first_row_len_b = len(m_b[0])
    if not all(len(row) == first_row_len_b for row in m_b):
        raise TypeError("each row of m_b must be of the same size")

    # 11. Validate dimension compatibility for multiplication
    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")

    # Perform matrix multiplication via NumPy
    return np.matmul(m_a, m_b)
