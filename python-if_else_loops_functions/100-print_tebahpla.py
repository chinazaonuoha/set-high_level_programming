#!/bin/env python3

"""Print the alphabet in reverse order. alternating lowercase and uppercase
(z in lowercase and Y in uppercase) , not followed by a new line."""


def print_tebahpla():
    """Print the alphabet in reverse order."""
    for i in range(122, 96, -1):
        print("{}".format(chr(i if i % 2 == 0 else i - 32)), end="")


if __name__ == "__main__":
    print_tebahpla()
