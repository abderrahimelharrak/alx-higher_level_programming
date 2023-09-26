#!/usr/bin/python3
"""Define a class Square."""
class Square:
    """Represent a square."""
    def __init__(selfe, size=0):
    @property
    def size(selfe):
        return (selfe.__size)

    @size.setter
    def size(selfe, valeur):
        if not isinstance(valeur, int):
            raise TypeError("size must be an integer")
        elif valeur < 0:
            raise ValueError("size must be >= 0")
        selfe.__size = valeur

    def area(selfe):
        return (selfe.__size * selfe.__size)
