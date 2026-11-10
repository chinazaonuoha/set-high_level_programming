#!/usr/bin/env python3

"""
Write a function that replaces all occurrences
of an element by another in a new list.
"""


def search_replace(my_list, search, replace):
    """
    Replaces all occurrences of an element by another in a new list.

    Args:
        my_list (list): The original list.
        search: The element to be replaced.
        replace: The element to replace with.

    Returns:
        list: A new list with the specified replacements.
    """
    # Create a new list to hold the modified values
    new_list = []

    # Iterate through each element in the original list
    [
        new_list.append(replace)
        if item == search
        else new_list.append(item)
        for item in my_list
    ]
    return new_list
