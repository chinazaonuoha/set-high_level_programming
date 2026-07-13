#!/usr/bin/python3

def magic_calculation(a, b):
    """Performs a magic calculation based on the values of a and b."""
    if a < b:
        return a + b
    elif a == b:
        return a * b
    else:
        return a - b
