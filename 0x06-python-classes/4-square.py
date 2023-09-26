#!/usr/bin/python3
"""Define a class Square."""
class Square:
    """Represent a square."""
    def __init__(selfe, size=0):
    @property
    def size(selfe):
        return (selfe.__size)

    @size.setter
    def size(selfe, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        selfe.__size = value

    def area(selfe):
        return (selfe.__size * selfe.__size)
