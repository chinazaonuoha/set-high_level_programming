"""
Write the Python class MagicClass that does exactly
the same as the following Python bytecode:
"""


class MagicClass:
    """A class that represents a magic number."""

    def __init__(self, radius=0):
        """Initialize the magic class with an optional radius."""
        self.__radius = 0
        self.__radius = radius

    def area(self):
        """Calculate and return the area based on the radius."""
        from math import pi
        return pi * (self.__radius ** 2)

    def circumference(self):
        """Calculate and return the circumference based on the radius."""
        from math import pi
        return 2 * pi * self.__radius

    @property
    def radius(self):
        """Retrieve the radius of the magic class."""
        return self.__radius

    @radius.setter
    def radius(self, value):
        """Set the radius of the magic class with validation."""
        if not isinstance(value, (int, float)) or isinstance(value, bool):
            raise TypeError("radius must be a number")
        self.__radius = value
