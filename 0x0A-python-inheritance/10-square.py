#!/usr/bin/python3
"""Use this module to instantiate objects that refer to geometric figures

    Class:
        BaseGeometry
"""


Rectangle = __import__("9-rectangle").Rectangle
""" Import module for inherit the Rectangle class
"""


class Square(Rectangle):
    """ Class definition
    """
    def __init__(self, size):
        super().integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
