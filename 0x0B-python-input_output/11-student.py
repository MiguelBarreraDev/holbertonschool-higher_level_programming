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

    def to_json(self, attrs=None):
        if attrs is None:
            return self.__dict__
        my_dict = {}
        for key in self.__dict__.keys():
            if key in attrs:
                my_dict[key] = self.__dict__[key]
        return my_dict

    def reload_from_json(self, json):
        for key in json.keys():
            setattr(self, key, json[key])
