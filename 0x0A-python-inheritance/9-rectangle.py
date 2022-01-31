#!/usr/bin/python3
"""Use this module to instantiate objects that refer to geometric figures

    Class:
        BaseGeometry
"""


class BaseGeometry:
    """ Definition class
    """
    def integer_validator(self, name: str, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """ Class definition
    """
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
        self.area()

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return ("[Rectangle] {}/{}".format(self.__width, self.__height))
