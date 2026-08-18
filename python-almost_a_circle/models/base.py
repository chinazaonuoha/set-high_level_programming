#!/usr/bin/python3
"""
Module containing the Base class, serving as the root manager
for all ID attributes across the project.
"""


class Base:
    """A base class to manage 'id' attributes for future subclasses.

    Attributes:
        __nb_objects (int): Private class attribute tracking total instances.
        id (int): Public instance attribute uniquely identifying the object.
    """
    __nb_objects = 0

    def __init__(self, id=None):
        """Initializes a new Base instance.

        Args:
            id (int, optional): Explicit identifier. If None, an auto-incremented
            integer is assigned based on __nb_objects.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
