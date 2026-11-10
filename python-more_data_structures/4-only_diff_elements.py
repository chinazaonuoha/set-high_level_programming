#!/usr/bin/python3

"""
Write a function that returns a set
of all elements present in only one set.
"""


def only_diff_elements(set_1, set_2):
    """
    Returns a set of all elements present in only one set.

    Args:
        set_1 (set): The first set.
        set_2 (set): The second set.

    Returns:
        set: A set containing elements present in only one set.
    """
    # Use the symmetric_difference method to
    # find elements present in only one set
    return set_1.symmetric_difference(set_2)
