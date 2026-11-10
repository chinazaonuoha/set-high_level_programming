#!/usr/bin/python3

"""
Write a function that deletes keys with a
specific value in a dictionary.
"""


def complex_delete(a_dictionary, value):
    a_dictionary = {k: v for k, v in a_dictionary.items() if v != value}
    return a_dictionary
