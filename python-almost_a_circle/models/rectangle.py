#!/usr/bin/python3
"""Module for the Rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Represent a Rectangle class that inherits from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a Rectangle instance."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """Return the print and str representation of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        )

    @property
    def width(self):
        """Width getter."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is bool:
            raise TypeError("width must be an integer")
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Height getter."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is bool:
            raise TypeError("height must be an integer")
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """X getter."""
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Y getter."""
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return the area of the Rectangle instance."""
        return self.width * self.height

    def display(self):
        """Print the Rectangle instance using the '#' character."""
        result = ""
        for _ in range(self.y):
            result += "\n"
        for _ in range(self.height):
            result += " " * self.x + "#" * self.width + "\n"
        print(result, end="")
        return result

    def display(self):
        """Print in stdout the Rectangle instance with the character #,
        taking into account x and y offsets.
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)
