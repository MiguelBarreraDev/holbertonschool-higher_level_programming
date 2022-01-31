#!/usr/bin/python3
"""Use module for declarate a class that inherits from list

    Class:
        MyList
"""
class MyList(list):
    """ Class definition
    """
    def print_sorted(self):
        print(sorted(self))
