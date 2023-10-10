#!/usr/bin/python3
"""Defining a text file insertion function."""


def append_after(filename="", search_string="", new_string=""):
    """Inserting text after each line containing a given string in a file.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): The string to insert.
    """
    texte = ""
    with open(filename) as re:
        for linee in re:
            texte += linee
            if search_string in linee:
                texte += new_string
    with open(filename, "w") as wr:
        wr.write(text)
