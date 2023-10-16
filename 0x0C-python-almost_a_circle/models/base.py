#!/usr/bin/python3

"""Defining a base model class"""
import json
import csv
import turtle


class Base:
    """Base model

    This Representing the base for all other classes in the project

    Private Class Attributes:
        __nb_object (int): Number of instantiated Bases.
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initializing a new Base.

        Args:
            id (int): The id of the new Base.
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def save_to_file(cls, list_objs):
        """Writing the JSON serialization of a list of objects to a file.

        Args:
            list_objs (list): List of inherited Base instances.
        """
        file_name = cls.__name__ + ".json"
        with open(file_name, "w") as json_file:
            if list_objs is None:
                json_file.write("[]")
            else:
                lt_dicts = [O.to_dictionary() for O in list_objs]
                json_file.write(Base.to_json_string(lt_dicts))

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returning the JSON serialization of a list of dicts.

        Args:
            list_dictionaries (list): List of dictionarie
        """
        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(jsons_tring):
        """Returning the deserialization of a JSON string.

        Args:
            json_string (str): A JSON str representation of a list of dicts.
        Returns:
            Success
        """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def load_from_file(cls):
        """Returning a list of classes instantiated from a file of JSON strings.

        Returns:
            Success
        """
        file_name = str(cls.__name__) + ".json"
        try:
            with open(file_name, "r") as json_file:
                lt_dicts = Base.from_json_string(json_file.read())
                return [cls.create(**D) for D in lt_dicts]
        except IOError:
            return []
    @classmethod
    def create(cls, **dictionary):
        """Returning a class instantied from a dictionary of attributes.

        Args:
            **dictionary (dict): Value or key pairs of attributes to initialize.
        """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                nouveau = cls(1, 1)
            else:
                nouveau = cls(1)
            nouveau.update(**dictionary)
            return nouveau

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Writing the CSV serialization of a list of objects to a file.

        Args:
            list_objs (list): A list of inherited Base instances.
        """
        file_name = cls.__name__ + ".csv"
        with open(file_name, "w", newline="") as csv_file:
            if list_objs is None or list_objs == []:
                csv_file.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    field_names = ["id", "width", "height", "x", "y"]
                else:
                    field_names = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csv_file, field_names=field_names)
                for objs in list_objs:
                    writer.writerow(objs.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Returning a list of classes instantiated from a CSV file.

        Reads from `<cls.__name__>.csv`.

        Returns:
            Success
        """
        file_name = cls.__name__ + ".csv"
        try:
            with open(file_name, "r", newline="") as csv_file:
                if cls.__name__ == "Rectangle":
                    field_names = ["id", "width", "height", "x", "y"]
                else:
                    field_names = ["id", "size", "x", "y"]
                lt_dicts = csv.DictReader(csv_file, field_names=field_names)
                lt_dicts = [dict([K, int(V)] for K, V in D.items())
                              for D in list_dicts]
                return [cls.create(**D) for D in lt_dicts]
        except IOError:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Drawing Rectangles and Squares using the turtle module.

        Args:
            list_rectangles (list): A list of Rectangle objects to draw.
            list_squares (list): A list of Square objects to draw.
        """
        turte = turtle.Turtle()
        turte.screen.bgcolor("#c3312d")
        turte.pensize(3)
        turte.shape("turtle")

        turte.color("#f38fcf")
        for recte in list_rectangles:
            turte.showturtle()
            turte.up()
            turte.goto(recte.x, recte.y)
            turte.down()
            for x in range(2):
                turte.forward(recte.width)
                turte.left(90)
                turte.forward(recte.height)
                turte.left(90)
            turte.hideturtle()

        turte.color("#b9e3df")
        for sqe in list_squares:
            turte.showturtle()
            turte.up()
            turte.goto(sqe.x, sqe.y)
            turte.down()
            for x in range(2):
                turte.forward(sqe.width)
                turte.left(90)
                turte.forward(sqe.height)
                turte.left(90)
            turte.hideturtle()

        turtle.exitonclick()
