#!/usr/bin/python3

"""
Write a function that
replaces or adds key/value in a dictionary.
"""


def update_dictionary(a_dictionary, key, value):
    """
    Replaces or adds key/value in a dictionary.

    Args:
        a_dictionary (dict): The input dictionary.
        key: The key to be replaced or added.
        value: The value to be associated with the key.

    Returns:
        dict: The updated dictionary.
    """
    # Update the dictionary with the new key-value pair
    a_dictionary[key] = value
    return a_dictionary
