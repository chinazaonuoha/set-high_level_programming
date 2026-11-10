#!/usr/bin/python3

"""
Write a function
that prints a dictionary by ordered keys.
"""


def print_sorted_dictionary(a_dictionary):
    """
    Prints a dictionary by ordered keys.

    Args:
        a_dictionary (dict): The input dictionary.
    """
    # Sort the keys of the dictionary
    for key in sorted(a_dictionary.keys()):
        # Print each key-value pair in the format "key: value"
        print("{}: {}".format(key, a_dictionary[key]))
