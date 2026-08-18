from models.base import Base

"""
This module defines the Rectangle class, which inherits from the Base class.
The Rectangle class represents a rectangle shape with attributes for width, height,
and its position (x, y) on a 2D plane. It provides methods to calculate the area,
Display the rectangle using ASCII characters,
and update its attributes. The class also includes
validation for the attributes to ensure they are of the correct type and value.
"""
class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y

    # --- Width ---
    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.__width = value

    # --- Height ---
    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    # --- X ---
    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value

    # --- Y ---
    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value
