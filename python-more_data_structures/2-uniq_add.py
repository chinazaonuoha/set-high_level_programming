#!/usr/bin/python3

"""
Write a function that adds all unique integers
in a list (only once for each integer).
"""


def uniq_add(my_list=[]):
    """
    Adds all unique integers in a list.

    Args:
        my_list (list): The list of integers.

    Returns:
        int: The sum of unique integers.
    """
    # Use a set to store unique integers
    unique_integers = set(my_list)

    # Return the sum of unique integers
    return sum(unique_integers)
