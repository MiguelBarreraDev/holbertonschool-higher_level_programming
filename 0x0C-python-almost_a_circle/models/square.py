#!/usr/bin/python3
""" Use the module for to instance of the Square class

    Class:
        Square
"""


from .rectangle import Rectangle


class Square(Rectangle):
    """ Square class definition to instance objects with attributes
        related to mathematical operations

        Instances:
            Campos:
                size(int): Width or height of the square
                x(int): Coordinates on the horizontal axis
                y(int): Coordinates on the vertical axis
                id(int): Unique identifier of the instance

            Methods:
                Special:
                    __init__, __str__

                Adding:
                    size, update, to_dictionary
    """
    def __init__(self, size, x=0, y=0, id=None) -> None:
        """ Constructor method to initialize fields at instantiate time """
        super().__init__(size, size, x, y, id)

    def __str__(self) -> str:
        """ Represent the object members in string format """
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width
        )

    @property
    def size(self) -> int:
        """ Getter method to get a private member """
        return self.width

    @size.setter
    def size(self, value) -> None:
        """ Setter method to add or modify a private member
            Args:
                value(int): New value for the width and height members
        """
        self.width = value
        self.height = value

    def update(self, *args, **kwargs) -> None:
        """ Modify the value of current members
            Args:
                args(list or iterable): Argument list without keyword
                kwargs(dict): Argument list with keyword
        """
        if args is not None and len(args) != 0:
            members = zip(
                ["id", "size", "x", "y"],  # keys
                list(args)  # values
            )
            for key, value in members:
                setattr(self, key, value)
        else:
            for attr in kwargs:
                if hasattr(self, attr):
                    setattr(self, attr, kwargs[attr])

    def to_dictionary(self) -> dict:
        """ Get a dict(key/value) object with the members of the instance"""
        return dict(
            zip(
                ["id", "size", "x", "y"],
                [self.id, self.size, self.x, self.y]
            )
        )
