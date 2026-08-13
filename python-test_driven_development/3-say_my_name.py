"""
This module contains a function that prints a formatted
string with the given first and last name.
The function takes two parameters: first_name and last_name.
It raises a TypeError if either parameter is not a string.
If last_name is not provided, it defaults to an empty string.
If first_name is an empty string, it raises a ValueError.
The function returns a string in the format
"My name is <first_name> <last_name>".
"""


def say_my_name(first_name, last_name=""):
    """Prints a formatted full name."""
    if not isinstance(first_name, str) or (
        last_name and not isinstance(last_name, str)
    ):
        raise TypeError("first_name and last_name must be strings")

    if not first_name:
        raise ValueError("first_name cannot be empty")

    if last_name:
        return f"My name is {first_name} {last_name}"
    return f"My name is {first_name}"
