"""
This module contains a function to print a
square of a given size using the '#' character.
"""


def print_square(size=0):
    """Prints a square of a given size using the '#' character.

    Args:
        size (int): The size of the square to be printed.

    Raises:
        TypeError: If size is not an integer.
        ValueError: If size is less than 0.
    """
    if size is None:
        raise TypeError(
            "print_square() missing 1 required positional argument: 'size'"
            )
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print('#' * size)
