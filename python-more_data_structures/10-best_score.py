#!/usr/bin/python3

"""
Write a function that returns a key with the biggest integer value.
"""


def best_score(a_dictionary):
    """
    Returns a key with the biggest integer value.

    Args:
        a_dictionary (dict): The input dictionary.

    Returns:
        The key with the biggest integer
        value, or None if the dictionary is empty.
    """
    # Check if the dictionary is empty
    if not a_dictionary:
        return None

    # Find the key with the maximum value using max() and a lambda function
    return max(a_dictionary, key=lambda k: a_dictionary[k])
