"""
0-read_file.py
--------
Write a function that reads a text file (UTF8) and prints it to stdout:

Prototype: def read_file(filename=""):
You must use the with statement
You don't need to manage file permission or file doesn't exist exceptions.
You are not allowed to import any module
"""

def read_file(filename=""):
    """Reads a text file (UTF8) and prints it to stdout."""
    with open(filename, encoding="utf-8") as f:
        print(f.read(), end="")
