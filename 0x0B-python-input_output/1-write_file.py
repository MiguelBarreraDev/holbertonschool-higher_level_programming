#!/usr/bin/python3
""" Use the module for write in a file

    Funtions:
        write_file
"""


def write_file(filename="", text=""):
    """ Function definition
        Args:
            filename(str): file path to wirte
            text(str): Content to write in the open file
    """
    try:
        with open(filename, "x", encoding="UTF-8") as file:
            file
    except FileExistsError:
        with open(filename, "w", encoding="UTF-8") as file:
            file.write(text)
    return len(text)
