#!/usr/bin/python3

"""
Write a function that deletes a key in a dictionary.
"""


def simple_delete(a_dictionary, key=""):
    """
    Deletes a key in a dictionary.

    Args:
        a_dictionary (dict): The input dictionary.
        key: The key to be deleted.

    Returns:
        dict: The updated dictionary after deletion.
    """
    # Check if the key exists in the dictionary
    if key in a_dictionary:
        # Delete the key from the dictionary
        del a_dictionary[key]
    return a_dictionary
