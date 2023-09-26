#!/usr/bin/python3
"""Define a class that make a Square."""

class Square:
    """Represent a square."""

    def __init__(selfe, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        selfe.__size = size
