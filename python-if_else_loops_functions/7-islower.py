#!/usr/env python3

def islower(c):
    if not c:
        raise ValueError("Input string cannot be empty")
    if len(c) != 1:
        raise ValueError("Input must be a single character")
    return 'a' <= c <= 'z'
