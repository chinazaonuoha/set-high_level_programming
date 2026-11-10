#!/usr/bin/python3

"""
Write a function that deletes keys with a
specific value in a dictionary.
"""


def complex_delete(a_dictionary, value):
    lambda_delete = lambda d, v: {k: v for k, v in d.items() if v != value}
    return lambda_delete(a_dictionary, value)
