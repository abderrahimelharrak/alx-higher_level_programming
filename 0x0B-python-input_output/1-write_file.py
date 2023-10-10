#!/usr/bin/python3
"""Defining a file-writing function."""


def write_file(filename="", text=""):
    """Writig a string to a UTF8 text file.

    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.
    Returns:
        Success
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
