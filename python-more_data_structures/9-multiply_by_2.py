#!/usr/bin/python3

"""
Write a function that returns a new dictionary with all values multiplied by 2
"""


def multiply_by_2(a_dictionary):
    """
    Returns a new dictionary with all values multiplied by 2.

    Args:
        a_dictionary (dict): The input dictionary.

    Returns:
        dict: A new dictionary with values multiplied by 2.
    """
    # Use a dictionary comprehension to create a new dictionary
    return {key: value * 2 for key, value in a_dictionary.items()}
