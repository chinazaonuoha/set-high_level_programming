#!/usr/bin/python3
"""Module containing lazy_matrix_mul function using NumPy."""

import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Multiplies two matrices using NumPy.

    Args:
        m_a (list): First matrix.
        m_b (list): Second matrix.

    Returns:
        ndarray: Resulting matrix product.

    Raises:
        TypeError: If m_a or m_b are not lists or contain invalid types.
        ValueError: If matrix shapes cannot be multiplied.
    """
    return np.matmul(m_a, m_b)
