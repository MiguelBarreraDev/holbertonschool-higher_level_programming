#!/usr/bin/python3
"""Use this module to instantiate objects that refer to geometric figures

    Class:
        BaseGeometry
"""
class BaseGeometry:
    """ Definition class
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name:str, value):
        if type(value) is not int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))
