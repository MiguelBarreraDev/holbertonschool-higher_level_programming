#!/usr/bin/python3
""" Use this module for intance object of Student class

    Class:
        Student
"""


class Student:
    """ Class definition
    """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
