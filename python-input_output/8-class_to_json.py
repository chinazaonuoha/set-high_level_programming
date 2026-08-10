"""
This module contains a function that converts a class object to a dictionary
for JSON serialization.
"""


def class_to_json(obj):
    """Returns the dictionary description with
    a simple data structure
    for JSON serialization of an object.
    """
    return obj.__dict__
