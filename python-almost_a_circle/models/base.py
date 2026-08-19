#!/usr/bin/python3
"""
Module containing the Base class, serving as the root manager
for all ID attributes across the project.
"""
import os

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
        """Writes the JSON string representation
        of a list of objects to a file.

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

    @staticmethod
    def from_json_string(json_string):
        """Returns the list of the JSON string representation json_string.

        Args:
            json_string (str): A string representing a list of dictionaries.

        Returns:
            list: The list represented by json_string, or an empty list if 
            json_string is None or empty.
        """
        import json

        if json_string is None or json_string == "":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set.

        Args:
            cls (class): The class to instantiate.
            **dictionary (dict): Key/value pairs of attributes to set.

        Returns:
            An instance of cls with the attributes set.
        """
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            dummy = None

        if dummy:
            dummy.update(**dictionary)
            return dummy
        return None

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances read from a JSON file.

        Args:
            cls (class): The class to instantiate instances for.

        Returns:
            list: A list of instantiated objects, or an empty list if the file doesn't exist.
        """
        filename = cls.__name__ + ".json"
        if not os.path.exists(filename):
            return []
        with open(filename, "r") as f:
            json_string = f.read()
        list_dicts = cls.from_json_string(json_string)
        return [cls.create(**d) for d in list_dicts]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes instances to a CSV file.

        Args:
            cls (class): The class of the objects being saved.
            list_objs (list): List of instances to save.
        """
        filename = cls.__name__ + ".csv"
        import csv

        with open(filename, "w", newline="") as f:
            if list_objs is None or not list_objs:
                f.write("")
                return
            if cls.__name__ == "Rectangle":
                fieldnames = ["id", "width", "height", "x", "y"]
            elif cls.__name__ == "Square":
                fieldnames = ["id", "size", "x", "y"]
            else:
                return
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            for obj in list_objs:
                writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes instances from a CSV file.

        Args:
            cls (class): The class to instantiate instances for.

        Returns:
            list: A list of instantiated objects, or an empty list if the file doesn't exist.
        """
        filename = cls.__name__ + ".csv"
        import csv
        import os
        if not os.path.exists(filename):
            return []
        list_objs = []
        with open(filename, "r", newline="") as f:
            if cls.__name__ == "Rectangle":
                fieldnames = ["id", "width", "height", "x", "y"]
            elif cls.__name__ == "Square":
                fieldnames = ["id", "size", "x", "y"]
            else:
                return []
            reader = csv.DictReader(f, fieldnames=fieldnames)
            for row in reader:
                d = {k: int(v) for k, v in row.items()}
                list_objs.append(cls.create(**d))
        return list_objs
