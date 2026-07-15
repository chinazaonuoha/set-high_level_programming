#!/usr/bin/python3
def print_alphabet():
    """Print the alphabet in lowercase."""
    for letter in range(97, 123):
        print(f"{chr(letter)}", end="")
    print()


print_alphabet()
