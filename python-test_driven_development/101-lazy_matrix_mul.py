"""
Module for lazy matrix multiplication using NumPy.
"""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices by using the module NumPy.

    Args:
        m_a (list of lists of int/float): The first matrix.
        m_b (list of lists of int/float): The second matrix.

    Returns:
        numpy.ndarray: The resulting matrix product.

    Raises:
        TypeError: If m_a or m_b is not a list, not a list of lists,
                   or contains non-int/float elements.
        ValueError: If m_a or m_b is empty (e.g., [] or [[]]),
                    or if the matrices cannot be multiplied due to
                    incompatible inner dimensions.
    """
    if not isinstance(m_a, list) or not isinstance(m_b, list):
        raise TypeError("m_a must be a list and m_b must be a list")
    if len(m_a) == 0 or m_a == [[]]:
        raise ValueError("m_a can't be empty")
    if len(m_b) == 0 or m_b == [[]]:
        raise ValueError("m_b can't be empty")
    for row in m_a:
        if not isinstance(row, list):
            raise TypeError("m_a must be a list of lists")
        if len(row) == 0:
            raise ValueError("m_a can't contain empty rows")
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError("m_a should contain only integers or floats")
    for row in m_b:
        if not isinstance(row, list):
            raise TypeError("m_b must be a list of lists")
        if len(row) == 0:
            raise ValueError("m_b can't contain empty rows")
        for elem in row:
            if not isinstance(elem, (int, float)):
                raise TypeError("m_b should contain only integers or floats")
    row_len_a = len(m_a[0])
    for row in m_a:
        if len(row) != row_len_a:
            raise ValueError("m_a rows must be of the same size")
    row_len_b = len(m_b[0])
    for row in m_b:
        if len(row) != row_len_b:
            raise ValueError("m_b rows must be of the same size")
    np_a = np.array(m_a)
    np_b = np.array(m_b)

    if np_a.shape[1] != np_b.shape[0]:
        raise ValueError("m_a and m_b can't be multiplied")
    return np.matmul(np_a, np_b)
