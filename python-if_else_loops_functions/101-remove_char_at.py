#!/usr/bin/env python3

"""Write a function that creates a copy of the string,
removing the character at the position n
(not the Python way, the "C array index")."""


def remove_char_at(str, n):
    """Remove the character at the position n."""
    if n < 0 or n >= len(str):
        return str
    return str[:n] + str[n + 1:]
