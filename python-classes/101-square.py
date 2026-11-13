#!/usr/bin/python3
"""
Write a class Square that defines a square by: (based on 6-square.py)

Private instance attribute: size:
property def size(self): to retrieve it
property setter def size(self, value): to set it:
size must be an integer, otherwise raise a
TypeError exception with the message
size must be an integer
if size is less than 0, raise a ValueError
exception with the message size must be >= 0
Private instance attribute: position:
property def position(self): to retrieve it
property setter def position(self, value): to set it:
position must be a tuple of 2 positive integers,
otherwise raise a TypeError exception with the
message position must be a tuple of 2 positive integer
Instantiation with optional size and optional
position: def __init__(self, size=0, position=(0, 0)):
Public instance method: def area(self): that
returns the current square area
Public instance method: def my_print(self):
that prints in stdout the square with the character #:
if size is equal to 0, print an empty line
position should be use by using space
Printing a Square instance should have
the same behavior as my_print()
You are not allowed to import any module"
"""


class Square:
    """A class that defines a square with size and position."""

    def __init__(self, size=0, position=(0, 0)):
        """Initialize the square with an optional size and position."""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Retrieve the position of the square."""
        return self.__position

    @position.setter
    def position(self, value):
        """Set the position of the square with validation."""
        if (not isinstance(value, tuple) or len(value) != 2 or
                not all(isinstance(num, int) and not isinstance(num, bool)
                        and num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character # considering position."""
        if self.__size == 0:
            print("")
            return

        for _ in range(self.__position[1]):
            print("")
        for _ in range(self.__size):
            print(" " * self.__position[0] + "#" * self.__size)

    def __str__(self):
        """Define the print() representation of a Square."""
        if self.__size == 0:
            return ""

        lines = ["" for _ in range(self.__position[1])]
        for _ in range(self.__size):
            lines.append(" " * self.__position[0] + "#" * self.__size)
        return "\n".join(lines)
