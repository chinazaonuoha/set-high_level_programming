#!/usr/bin/python3
"""Module for the Square class."""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Represent a Square class that inherits from Rectangle."""

    def __init__(self, size, x=0, y=0, id=None):
        """Initialize a new Square."""
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Return the print string representation of the Square."""
        return f"[Square] ({self.id}) {self.x}/{self.y} - {self.width}"

    @property
    def size(self):
        """Get the size of the square."""
        return self.width

    @size.setter
    def size(self, value):
        """Set the size of the square."""
        self.width = value
        self.height = value

    def area(self):
        """Return the area of the Square instance."""
        return self.size ** 2

    def display(self):
        """Print in stdout the Square instance with the character #,
        taking into account x and y offsets, and return the string.
        """
        result = ""
        for _ in range(self.y):
            result += "\n"
        for _ in range(self.size):
            result += " " * self.x + "#" * self.size + "\n"
        print(result, end="")
        return result

    def update(self, *args, **kwargs):
        """Update attributes using positional (*args)
        or keyword (**kwargs) arguments."""
        if args and len(args) > 0:
            attributes = ["id", "size", "x", "y"]
            for i, arg in enumerate(args):
                if i < len(attributes):
                    setattr(self, attributes[i], arg)
        elif kwargs:
            for key, value in kwargs.items():
                if hasattr(self, key):
                    setattr(self, key, value)
