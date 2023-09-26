#!/usr/bin/python3
"""Define a class Square."""

class Square:
    """Represent a square."""
    def __init__(selfe, size=0, position=(0, 0)):
        """Initialisation a new square.

        Args:
            size (int): The size of the  square.
            position (int, int): The position of  new square.
        """
        selfe.size = size
        selfe.position = position

    @property
    def size(selfe):
        """set and get the current size of the square."""
        return (selfe.__size)

    @size.setter
    def size(selfe, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        selfe.__size = value

    @property
    def position(selfe):
        """set and get the current position of the square."""
        return (selfe.__position)

    @position.setter
    def position(selfe, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(number, int) for number in value) or
                not all(number >= 0 for number in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        selfe.__position = value

    def area(selfe):
        """the current area of the square."""
        return (selfe.__size * selfe.__size)

    def my_print(selfe):
        """the square with the # character."""
        if selfe.__size == 0:
            print("")
            return

        [print("") for x in range(0, selfe.__position[1])]
        for x in range(0, selfe.__size):
            [print(" ", end="") for y in range(0, selfe.__position[0])]
            [print("#", end="") for z in range(0, selfe.__size)]
            print("")
