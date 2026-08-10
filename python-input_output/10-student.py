#!/usr/bin/python3
"""Defines a Student class with dictionary serialization."""


class Student:
    """Defines a student by first_name, last_name, and age."""

    def __init__(self, first_name, last_name, age):
        """Initializes a Student instance
        with first name, last name, and age."""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dictionary representation of the Student instance.

        If attrs is a list of strings, only attribute names contained in this
        list are retrieved. Otherwise, all public attributes are retrieved.
        """
        keys = attrs if isinstance(attrs, list) else [
            attr for attr in dir(self)
            if not attr.startswith("__") and not callable(getattr(self, attr))
        ]
        return {key: getattr(self, key) for key in keys if hasattr(self, key)}
