#!/usr/bin/python3
""" Use the module for get dictionary description for JSON serialization
    of an object
"""


def class_to_json(obj):
    """ Function definition
        Args:
            obj(object): object to get dict

    """
    return obj.__dict__
