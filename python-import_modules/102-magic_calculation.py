#!/usr/bin/python3
"""Write the Python function def magic_calculation(a, b):
that does exactly the same as the following Python bytecode:"""


def magic_calculation(a, b):
    """Perform a magic calculation based on the values of a and b."""
    if a < b:
        return a + b
    elif a > b:
        return a - b
    else:
        return a * b
