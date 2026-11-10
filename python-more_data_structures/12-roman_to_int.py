#!/usr/bin/python3


"""
Create a function def roman_to_int(roman_string):
that converts a Roman numeral to an integer.
"""


def roman_to_int(roman_string):
    """
    Converts a Roman numeral to an integer.

    Args:
        roman_string (str): The Roman numeral string.

    Returns:
        int: The integer representation of the Roman numeral.
    """
    if not isinstance(roman_string, str) or not roman_string:
        return 0

    # Define a mapping of Roman numerals to integers
    roman_numerals = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }

    total = 0
    prev_value = 0

    # Iterate through the Roman numeral string in reverse order
    for char in reversed(roman_string):
        value = roman_numerals.get(char, 0)

        # If the current value is less than the previous value, subtract it
        if value < prev_value:
            total -= value
        else:
            total += value

        prev_value = value

    return total
