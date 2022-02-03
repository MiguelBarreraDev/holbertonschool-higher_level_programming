#!/usr/bin/python3
""" Use the module for to instance of Rectangle

    Class:
        Rectangle
"""


from .base import Base


class Rectangle(Base):
    """ Class definition
    """
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        return self.__width * self.__height

    def display(self):
        print("\n" * self.y, end="")
        print("\n".join(
            [" "*self.x + "".join(
                ["#" for e in range(self.width)]
            ) for i in range(self.height)]))

    def __str__(self):
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.width, self.height
        )

    def update(self, *args, **kwargs):
        if args is not None and len(args) != 0:
            for i in range(len(args)):
                setattr(self, (list(self.__dict__.keys()))[i], args[i])
        else:
            for attr in kwargs:
                setattr(self, attr, kwargs[attr])

    def to_dictionary(self):
        return dict(zip(
            ["id", "width", "height", "x", "y"],
            [self.id, self.width, self.height, self.x, self.y]
        ))
