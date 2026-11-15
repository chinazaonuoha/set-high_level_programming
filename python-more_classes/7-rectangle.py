"""
Write a class Rectangle that defines a rectangle by:
(based on 6-rectangle.py)

Private instance attribute: width:
property def width(self): to retrieve it
property setter def width(self, value): to set it:
width must be an integer, otherwise raise a
TypeError exception with the message width must be an integer
if width is less than 0, raise a ValueError
exception with the message width must be >= 0
Private instance attribute: height:
property def height(self): to retrieve it
property setter def height(self, value): to set it:
height must be an integer, otherwise raise a
TypeError exception with the message height must be an integer
if height is less than 0, raise a ValueError
exception with the message height must be >= 0
Public class attribute number_of_instances:
Initialized to 0
Incremented during each new instance instantiation
Decremented during each instance deletion
Public class attribute print_symbol:
Initialized to #
Used as symbol for string representation
Can be any type
Instantiation with optional width and height:
def __init__(self, width=0, height=0):
Public instance method: def area(self): that
returns the rectangle area
Public instance method: def perimeter(self):
that returns the rectangle perimeter:
if width or height is equal to 0, perimeter has to be equal to 0
print() and str() should print the rectangle
with the character(s) stored in print_symbol:
if width or height is equal to 0, return an empty string
repr() should return a string representation
of the rectangle to be able to recreate a
new instance by using eval()
Print the message Bye rectangle... (...
being 3 dots not ellipsis) when an instance of
Rectangle is deleted
You are not allowed to import any module
"""


class Rectangle:
    """A class that defines a rectangle."""

    number_of_instances = 0  # Public class attribute
    print_symbol = "#"  # Public class attribute

    def __init__(self, width=0, height=0):
        """Initialize the rectangle with optional width and height."""
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1  # Increment instance count

    @property
    def width(self):
        """Retrieve the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle with validation."""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieve the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """Set the height of the rectangle with validation."""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
