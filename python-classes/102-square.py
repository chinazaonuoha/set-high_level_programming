"""
Write a class Square that defines a
square by: (based on 4-square.py)

Private instance attribute: size:
property def size(self): to retrieve it
property setter def size(self, value): to set it:
size must be a number (float or integer),
otherwise raise a TypeError exception with
the message size must be a number
if size is less than 0, raise a ValueError
exception with the message size must be >= 0
Instantiation with size: def __init__(self, size=0):
Public instance method: def area(self): that
returns the current square area
Square instance can answer to
comparators: ==, !=, >, >=, < and <= based
on the square area
You are not allowed to import any module
"""


class Square:
    """A class that defines a square with size."""

    def __init__(self, size=0):
        """Initialize the square with an optional size."""
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation."""
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise TypeError("size must be a number")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the current square area."""
        return self.__size ** 2

    def __eq__(self, other):
        """Check if two squares are equal based on their area."""
        if isinstance(other, Square):
            return self.area() == other.area()
        return NotImplemented

    def __ne__(self, other):
        """Check if two squares are not equal based on their area."""
        if isinstance(other, Square):
            return self.area() != other.area()
        return NotImplemented

    def __gt__(self, other):
        """Check if this square is greater than another based on their area."""
        if isinstance(other, Square):
            return self.area() > other.area()
        return NotImplemented

    def __ge__(self, other):
        """Check if this square is greater than
        or equal to another based on their area."""
        if isinstance(other, Square):
            return self.area() >= other.area()
        return NotImplemented

    def __lt__(self, other):
        """Check if this square is less than another based on their area."""
        if isinstance(other, Square):
            return self.area() < other.area()
        return NotImplemented

    def __le__(self, other):
        """Check if this square is less than
        or equal to another based on their area."""
        if isinstance(other, Square):
            return self.area() <= other.area()
        return NotImplemented

    def area(self):
        """Return the current square area."""
        return self.__size ** 2
