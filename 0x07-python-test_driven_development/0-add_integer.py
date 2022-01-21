#!/usr/bin/python3
""" Add two integers or floats

    Functions:
        add_integer(object, object) -> int
"""


def add_integer(a, b=98):
    """ Definition of function that adds two integers or floats

    Args:
        param1 (int or float): the first number
        param2 (int or float): the second number. Defaults to 98

    Returns:
        int: the sum of the numbers

    Examples:
    """
    result = int
    if not isinstance(a, (int, float)):
        raise TypeError('a must be an integer')
    if not isinstance(b, (int, float)):
        raise TypeError('b must be an integer')
    result = int(a) + int(b)

    return result
