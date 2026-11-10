#!/usr/bin/python3

"""
Write a function that returns a list
with all values multiplied by a number without using any loops.
"""


def multiply_list_map(my_list=[], number=0):
    """
    Returns a list with all values multiplied by a number.

    Args:
        my_list (list): The input list of numbers.
        number (int or float): The number
        to multiply each value by.

    Returns:
        list: A new list with values multiplied
        by the specified number.
    """
    # Use the map function to multiply each
    # value in the list by the specified number
    return list(map(lambda x: x * number, my_list))
