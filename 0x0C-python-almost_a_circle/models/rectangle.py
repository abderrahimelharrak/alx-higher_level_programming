#!/usr/bin/python3
"""Defining a rectangle class."""
from models.base import Base


class Rectangle(Base):
    """Representing a rectangle."""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        """
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def height(self):
        """get or set the height of the Rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value
    
    @property
    def width(self):
        """get or set the width of the Rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
    
    @property
    def y(self):
        """Get or set the y coordinate of the Rectangle."""
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    @property
    def x(self):
        """Get or set the x coordinate of the Rectangle."""
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    def area(self):
        """Returning the area of the Rectangle."""
        return self.width * self.height

    def display(self):
        """Printing the Rectangle using the `#` character."""
        if self.width == 0 or self.height == 0:
            print("")
            return

        [print("") for Y in range(self.y)]
        for H in range(self.height):
            [print(" ", end="") for X in range(self.x)]
            [print("#", end="") for W in range(self.width)]
            print("")

    def update(self, *args, **kwargs):
        """Updating the Rectangle.

        Args:
            *args (ints): New attribute values.
                - 1st argument represents id attribute
                - 2nd argument represents width attribute
                - 3rd argument represent height attribute
                - 4th argument represents x attribute
                - 5th argument represents y attribute
            **kwargs (dict): New key/value pairs of attributes.
        """
        if args and len(args) != 0:
            A = 0
            for arge in args:
                if A == 0:
                    if arge is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = arge
                elif A == 1:
                    self.width = arge
                elif A == 2:
                    self.height = arge
                elif A == 3:
                    self.x = arge
                elif A == 4:
                    self.y = arge
                A += 1

        elif kwargs and len(kwargs) != 0:
            for K, V in kwargs.items():
                if K == "id":
                    if V is None:
                        self.__init__(self.width, self.height, self.x, self.y)
                    else:
                        self.id = V
                elif K == "width":
                    self.width = V
                elif K == "height":
                    self.height = V
                elif K == "x":
                    self.x = V
                elif K == "y":
                    self.y = V

    def to_dictionary(self):
        """Returning the dictionary representation of a Rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }

    def __str__(self):
        """Returning the print() and str() representation of the Rectangle."""
        return "[Rectangle] ({}) {}/{} - {}/{}".format(self.id,
                                                       self.x, self.y,
                                                       self.width, self.height)
