#!/usr/bin/python3
""" You can create instances of objects related to geometric figures

    Class:
        Rectangule
"""


class Rectangle:
    """ Define the contructor method -  Rectangle class
    """
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise Exception("width must be an integer")
        if value < 0:
            raise Exception("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise Exception("height must be an integer")
        if value < 0:
            raise Exception("height must be >= 0")
        self.__height = value