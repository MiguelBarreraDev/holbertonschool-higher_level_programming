#!/usr/bin/python3
"""Use this module to instantiate objects that refer to geometric figures

    Class:
        BaseGeometry
"""


BaseGeometry = __import__("7-base_geometry").BaseGeometry
""" Import module for inherits BaseGeometry class
"""


class Rectangle(BaseGeometry):
    """ Class definition
    """
    def __init__(self, width, height):
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height
