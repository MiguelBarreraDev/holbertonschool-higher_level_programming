#!/usr/bin/python3
"""Use module for validate the type of a object

    function:
        lookup
"""


def inherits_from(obj, a_class):
    """ function definition
    """
    v = True \
        if isinstance(obj, a_class) and type(obj) is not a_class \
        else False
    return v
