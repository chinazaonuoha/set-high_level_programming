#!/bin/env python3

"""Print the alphabet in reverse order. alternating lowercase and uppercase 
(z in lowercase and Y in uppercase) , not followed by a new line."""


def print_tebahpla():
    """Print the alphabet in reverse order."""
    for i in range(122, 96, -1):
        if i % 2 == 0:
            print(chr(i).lower(), end="")
        else:
            print(chr(i).upper(), end="")
    print()

if __name__ == "__main__":
    print_tebahpla()

