"""
Write a function that writes an Object
to a text file, using a JSON representation:

Prototype: def save_to_json_file(my_obj, filename):
You must use the with statement
You don't need to manage exceptions if the object can't be serialized.
You don't need to manage file permission exceptions.

"""


def save_to_json_file(my_obj, filename):
    """Writes an Object to a text file, using a JSON representation."""
    import json
    with open(filename, 'w') as f:
        json.dump(my_obj, f)
