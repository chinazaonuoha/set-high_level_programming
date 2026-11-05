#!/usr/bin/python3
"""Write a program that prints the alphabet in
uppercase, followed by a new line."""


def print_alphabet():
    """Prints the alphabet in uppercase."""
    for letter in range(65, 91):
        print(chr(letter), end="")
    print()  # Print a new line at the end
