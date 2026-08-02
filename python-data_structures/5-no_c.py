#!/usr/bin/python3

def no_c(my_string: str = None) -> str:
    if not my_string:
        return ""
    return "".join(char for char in my_string if char not in ('c', 'C'))
