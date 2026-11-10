#!/usr/bin/python3

"""
Write a function
that returns a set of common elements in two sets.
"""

def common_elements(set_1, set_2):
    """
    Returns a set of common elements in two sets.

    Args:
        set_1 (set): The first set.
        set_2 (set): The second set.

    Returns:
        set: A set containing common elements.
    """
    # Use the intersection method to find common elements
    return set_1.intersection(set_2)
