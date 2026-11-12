"""
Write a class Square that defines a
square by: (based on 0-square.py)

Private instance attribute: size
Instantiation with size (no type/value verification)
"""


class Square:
    """A class that defines a square."""

    def __init__(self, size):
        """Initialize the square with a given size."""
        self.__size = size
