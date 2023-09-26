#!/usr/bin/python3

"""Define a class that make a Square."""

class Square:
    """Representation of  a square."""

    def __init__(selfe, size):
        """Initialisation square.

        Args:
            size (int): The size of the new square.
        """
        selfe.size = size

    @property
    def size(selfe):
        """set and sget the current size of square."""
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

    def my_print(selfe):
        """the square with the # character."""
        for x in range(0, selfe.__size):
            [print("#", end="") for y in range(selfe.__size)]
            print("")
        if selfe.__size == 0:
            print("")
