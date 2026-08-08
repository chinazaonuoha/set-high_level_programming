"""
2-append_write.py
--------
Write a function that appends a string to a text
file (UTF8) and returns the number of characters added:

Prototype: def append_write(filename="", text=""):
You must use the with statement
You don't need to manage file permission exceptions.
Your function should create the file if doesn't exist.
Your function should overwrite the content of the file if it already exists.
You are not allowed to import any module

"""


def append_write(filename="", text=""):
    """Appends a string to a text file (UTF8) and returns
    the number of characters added."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
