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
            id (int, optional): Explicit identifier.
            If None, an auto-incremented
            integer is assigned based on __nb_objects.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Converts a list of dictionaries to a JSON string.

        Args:
            list_dictionaries (list): List of dictionaries to convert.

        Returns:
            str: JSON string representation of the list.
            If list_dictionaries is None or empty, returns "[]".
        """
        import json
        if not list_dictionaries:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON string representation of a list of objects to a file.

        Args:
            cls (class): The class of the objects being saved.
            list_objs (list): List of instances to save.
        """
        filename = cls.__name__ + ".json"
        list_dicts = []
        if list_objs is not None:
            list_dicts = [obj.to_dictionary() for obj in list_objs]
        json_string = cls.to_json_string(list_dicts)
        with open(filename, "w") as f:
            f.write(json_string)

