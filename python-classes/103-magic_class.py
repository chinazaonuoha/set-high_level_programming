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
