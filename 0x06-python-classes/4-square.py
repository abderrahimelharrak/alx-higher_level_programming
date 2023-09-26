#!/usr/bin/python3
"""Define a class Square."""

class Square:
    """Represent a square."""

    def __init__(selfe, size=0):
        """Initialisation a new square.

        Args:
            size (int): The size of the square.
        """
        selfe.size = size

    @property
    def size(self):
        """set and get the current size of the square."""
        return (selfe.__size)

    @size.setter
    def size(selfe, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        selfe.__size = value

    def area(selfe):
        """the current area of the square."""
        return (selfe.__size * selfe.__size)
