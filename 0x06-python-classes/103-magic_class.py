#!/usr/bin/python3
"""Bytecode of the class"""
import math


class MagicClass:
    """Class MagicClass
    """
    def __init__(self, raidus=0):
        """ Constructor """
        self.__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self, radius):
        """Get area"""
        return (self.__radius ** 2) * math.pi

    def circunference(self, radius):
        """Get circunference"""
        return 2 * math.pi * self.__radius
