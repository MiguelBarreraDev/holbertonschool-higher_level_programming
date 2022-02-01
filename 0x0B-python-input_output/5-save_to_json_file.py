#!/usr/bin/python3
""" Use the module for save object to a file

    Functions:
        save_to_json_file
"""


import json
""" Import module for to use dumps method
"""


def save_to_json_file(my_obj, filename):
    """ Function definition
        Args:
            my_obj(obj): Convert to JSON for save
            filename(str): File path
    """
    with open(filename, "w") as file:
        file.write(json.dumps(my_obj))
