i#!/usr/bin/python3
"""Defining a file-appending function."""


def append_write(filename="", text=""):
    """Appending a string to the end of a UTF8 text file.

    Args:
        filename (str): The name of the file to append to.
        text (str): The string to append to the file.
    Returns:
        Success
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
