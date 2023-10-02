#!/usr/bin/python3
"""a function that defines a Rectangle class."""


class Rectangle:
    """Representation of a rectangle."""

    def __init__(self, width=0, height=0):
        """Initializing a new Rectangle.

        Args:
            width (int): The width of the  rectangle.
            height (int): The height of the  rectangle.
        """
        self.width = width
        self.height = height


    @property
    def height(self):
        """set or get the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @property
    def width(self):
        """set or get the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        """a function that Return the area of the Rectangle."""
        return (self.__width * self.__height)

    def perimeter(self):
        """a function that Return the perimeter of the Rectangle."""
        if self.__width == 0 or self.__height == 0:
            return (0)
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self):
        """Return the printable representation of the Rectangle.

        Represents the rectangle with the # character.
        """
        if self.__width == 0 or self.__height == 0:
            return ("")

        recte = []
        for x in range(self.__height):
            [recte.append('#') for y in range(self.__width)]
            if x != self.__height - 1:
                recte.append("\n")
        return ("".join(recte))
