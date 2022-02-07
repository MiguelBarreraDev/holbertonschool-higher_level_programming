#!/usr/bin/python3
""" Use the module for to instance of Rectangle

    Class:
        Rectangle
"""


from models.base import Base


class Rectangle(Base):
    """ Rectangle class definition to instance objects with attributes
        related to mathematical operations

        Instances:
            Members:
                __width(int): Width of the object
                __height(int): Height of the object
                __x(int): Coordinates on the horizontal axis
                __y(int): Coordinates on the vertical axis
                id(int): Unique indentifier of the instance

            Methods:
                Special:
                    __init__, __str__

                Adding:
                    width, heiht, x, y, area, diplay, to_dictionary
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        """ Constructor method to initialize fields at istantiate time """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """ Getter method to access a private variable(__width) """
        return self.__width

    @width.setter
    def width(self, value):
        """ Setter method to add or modify a private variable(__height)
            Args:
                value(int): New value fot the __width member
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height to a value"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Retrieves the x"""
        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x to a value"""
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Retrieves the y"""
        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y to a value"""
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Return area of the rectangle"""
        return self.__width * self.__height

    def display(self):
        """ Draw the object in console """
        print("\n" * self.y, end="")
        print("\n".join(
            [" "*self.x + "".join(
                ["#" for e in range(self.width)]
            ) for i in range(self.height)]))

    def __str__(self):
        """ Represent the objetc members in string format """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        )

    def update(self, *args, **kwargs):
        """ Modify the value of current members
            Args:
                args(list or iterable): Argument list without keyword
                Kwargs(dict): Argument list with keyword
        """
        if args is not None and len(args) != 0:
            members = zip(
                ["id", "width", "height", "x", "y"],  # keys
                list(args)  # values
            )
            for key, value in members:
                setattr(self, key, value)
        else:
            for attr in kwargs:
                if hasattr(self, attr):
                    setattr(self, attr, kwargs[attr])

    def to_dictionary(self):
        """ Get a dict(key/value) object with the members of the instance """
        return dict(zip(
            ["id", "width", "height", "x", "y"],
            [self.id, self.width, self.height, self.x, self.y]
        ))
