#!/usr/bin/python3
"""Use this module to instantiate classes that inherit from int

    Class:
        MyInt
"""


class MyInt(int):
    """ Class definition
    """
    def __init__(self, value: int):
        self.value = value

    def __eq__(self, other):
        return self.value != other

    def __ne__(self, other):
        return self.value == other
