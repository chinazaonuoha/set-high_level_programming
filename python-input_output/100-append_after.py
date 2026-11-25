#!/usr/bin/python3
"""Defines a function that inserts a line of text after a specific string."""


def append_after(filename="", search_string="", new_string=""):
    """Inserts new_string after each line containing search_string in filename."""
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    updated_lines = [
        line + new_string if search_string in line else line
        for line in lines
    ]

    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(updated_lines)
