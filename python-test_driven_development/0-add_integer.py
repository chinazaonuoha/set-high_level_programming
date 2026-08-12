def add_integer(a, b=98):
    """Adds 2 integers.

    Args:
        a: The first integer or float.
        b: The second integer or float (default is 98).

    Returns:
        An integer: the addition of a and b.

    Raises:
        TypeError: If a or b is not an integer or float.
    """
    if not isinstance(a, (int, float)) or isinstance(a, bool):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)) or isinstance(b, bool):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
