def matrix_mul(m_a, m_b):
    """Multiplies two matrices after validating their format and dimensions."""
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

    # 11. Validate compatibility (Cols of m_a == Rows of m_b)
    cols_a = len(m_a[0])
    rows_b = len(m_b)
    if cols_a != rows_b:
        raise ValueError("m_a and m_b can't be multiplied")

    # Matrix multiplication
    rows_a = len(m_a)
    cols_b = len(m_b[0])

    result = []
    for i in range(rows_a):
        new_row = []
        for j in range(cols_b):
            cell_value = sum(m_a[i][k] * m_b[k][j] for k in range(cols_a))
            new_row.append(cell_value)
        result.append(new_row)

    return result
