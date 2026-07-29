#!/usr/env python3


def uppercase(text):
    ASCII_LOWER_A = 97
    ASCII_LOWER_Z = 122
    ASCII_CASE_OFFSET = 32
    result = ""
    for c in text:
        is_lowercase = (
            ASCII_LOWER_A <= ord(c) <= ASCII_LOWER_Z
        )
        transformed_char = (
            chr(ord(c) - ASCII_CASE_OFFSET)
            if is_lowercase
            else c
        )
        result += transformed_char
    print("{}".format(result))
