#!/usr/bin/python3
""" Use the module for create an object from a JSON file

    Function:
        load_from_json_file
"""


import json
""" Import json module for to use loads method
"""


def load_from_json_file(filename):
    """ Function definition
        Args:
            filename(str): File path
    """
    with open(filename, "r") as file:
        return json.loads(file.read())
