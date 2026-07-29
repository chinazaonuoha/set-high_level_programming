#!/usr/env python3

def islower(c):
    if not c:
        return False
    if len(c) != 1:
        return False
    return 'a' <= c <= 'z'
