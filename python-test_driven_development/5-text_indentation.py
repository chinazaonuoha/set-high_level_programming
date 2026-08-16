#!/usr/bin/python3
"""This module contains a function that prints text with 2 new lines
after specific punctuation marks: ., ? and :
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :.

    Args:
        text (str): The text to be printed.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    # Flag to skip spaces right after punctuation/newlines
    skip_space = True
    for char in text:
        if skip_space and char == ' ':
            continue
        skip_space = False
        print(char, end="")
        if char in ".?:":
            print("\n\n", end="")
            skip_space = True
