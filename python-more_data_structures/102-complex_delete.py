#!/usr/bin/python3

"""
Write a function that deletes keys with a
specific value in a dictionary.
"""


def complex_delete(a_dictionary, value):
    """
    Deletes keys with a specific value in a dictionary.

    Args:
        a_dictionary (dict): The input dictionary.
        value: The value to be deleted.

    Returns:
        dict: The updated dictionary with keys removed.
    """
    if not isinstance(a_dictionary, dict):
        return {}

    # Create a new dictionary without the keys that have the specified value
    updated_dict = {key: val for key, val in a_dictionary.items() if val != value}

    return updated_dict
