#!/usr/bin/python3
"""
This module defines the Rectangle class, which inherits from the Base class.
The Rectangle class represents a rectangle
shape with attributes for width, height,
and its position (x, y) on a 2D plane.
"""

from models.base import Base


class Rectangle(Base):
    """Represent a Rectangle model inheriting from Base."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a Rectangle instance."""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Width getter."""
        return self.__width

    @width.setter
    def width(self, value):
        """Width setter."""
        self.__width = value

    @property
    def height(self):
        """Height getter."""
        return self.__height

    @height.setter
    def height(self, value):
        """Height setter."""
        self.__height = value

    @property
    def x(self):
        """X coordinate getter."""
        return self.__x

    @x.setter
    def x(self, value):
        """X coordinate setter."""
        self.__x = value

    @property
    def y(self):
        """Y coordinate getter."""
        return self.__y

    @y.setter
    def y(self, value):
        """Y coordinate setter."""
        self.__y = value
