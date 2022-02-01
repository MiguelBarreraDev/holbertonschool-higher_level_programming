#!/usr/bin/python3
""" Use the module for represented a JSON in an object

    Function:
        from_json_string
"""


import json
""" Import json module for to use the loads method for converto json to object
"""


def from_json_string(my_str):
    """ Function definition
        Args:
            my_str(str): convert to object
    """
    return json.loads(my_str)
