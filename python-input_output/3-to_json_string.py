"""
3-to_json_string.py
--------
Write a function that returns the JSON
representation of an object (string):

Prototype: def to_json_string(my_obj):
You don't need to manage exceptions if the object can't be serialized.

"""


def to_json_string(my_obj):
    """Returns the JSON representation of an object (string)."""
    import json
    return json.dumps(my_obj)
