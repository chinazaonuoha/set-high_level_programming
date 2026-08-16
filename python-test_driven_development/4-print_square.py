"""
This module contains a function to print a
square of a given size using the '#' character.
"""


def print_square(size):
    """Prints a square of a given size using the '#' character.

    Args:
        size (int): The size of the square to be printed.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than or equal to 0.
    """
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size <= 0:
        raise ValueError("size must be greater than 0")

    for _ in range(size):
        print('#' * size)
