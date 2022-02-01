#!/usr/bin/python3
"""Use module for get attributes and methods of an object

    function:
        lookup
"""
def add_attribute(obj, name, value):
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, name, value)
