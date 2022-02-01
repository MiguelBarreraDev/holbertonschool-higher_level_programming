#!/usr/bin/python3
"""Use the module for read of a file

    Function:
        filename
"""


def read_file(filename=""):
    """ Function definition

        Args:
            filename(str): Path of the file to read
    """
    with open(filename, "r", encoding="UTF-8") as text:
        print(text.read(), end="")
